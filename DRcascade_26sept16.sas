%let source=Y:/Sync/DR; 
%let output=Y:/Dropbox/Research/drcascade/data;
%let cen='30may2016'd;
%include "Y:/Box Sync/resources/macros/quickci.sas";

data base; infile "&source./base.dat";
input  idpat 1-5 idsai 7-12 firsty 14-22 starty 24-32  site 34
male 36 age0 38-40 @42 nationality $25. @67 prov $30. @98 mun $30. 
sdss 130 cd40 132-136 cd40y 138-142 vl0 144-150 vl0y 152-157 art0y 159-164 
endy 166-170 deathy 172-177 @179 sai $30. haitian 211;
run;
proc sql; select count(distinct(idpat)) as totalinbase from base; run; quit;


data long; infile "&source./long.dat";
input  idpat 1-5 idseg 7-15 @17 saivisit $30. tb 49 syph 51 @53 reason $10. next_visity 65-70 visity 72-77 art 79 pregnant 81 cd4 83-87
cd4y 89-94 vl 96-102 vly 104-109 @111 exit $15. @127 transferto $30.  hepb 159  hepc 161;
run;

proc sql; select count(distinct(idpat)) as totalinlong from long; run; quit;

data all; merge base(in=inbase) long; by idpat; if inbase; run;
proc sql; select count(distinct(idpat)) as total from all; run; quit;

data all2; set all; by idpat visity;
if visity>'1jun2016'd then delete;
if first.idpat and visity=. then do; visity=starty; output; end;
else if first.idpat and visity ne . then do; output; visity=starty; cd4=cd40; vl=vl0; output; end;
else if not first.idpat then output;
format firsty starty visity cd4y vly cd40y vl0y next_visity deathy art0y endy  date9.;
run;
proc sql; select count(distinct(idpat)) as totalafter13 from all2; run; quit;

data slim; set all2;
if starty>='1aug2013'd and (art0y>='1aug2013'd|art0y=.)and (deathy=.|deathy>starty) and visity>=starty;
if art=. then art=0;
keep idpat visity next_visity cd40 age0 vl0 cd4 vl art art0y male age0 haitian starty deathy sai haitian vly;
run;
proc sql; select count(distinct(idpat)) as totalafter13 from slim; run; quit;

data fu; set slim; by idpat; retain everart 0 arty; 
if first.idpat then do; everart=0; arty=.; end;
if art=1 and everart=0 then do; everart=1; arty=visity; end;
else if art=1 and everart=1 then do; everart=everart; arty=arty; end;
run;


*plot 1: time to ART start;
data p1; set fu; by idpat; if last.idpat;
if arty ne . then do; art=1; t_art=(arty-starty)/30.43; end; *time in months;
if arty=. and deathy=. then do; art=0; t_art=(&cen-starty)/30.43; end;
if arty=. and deathy ne . then do; art=2; t_art=(deathy-starty)/30.43; end;
run;
data p1; set p1; if t_art<0 then t_art=0; run;
data ch; set p1; if t_art<0; run;
proc freq data=p1; tables art/missprint; run;
proc means data=p1; var t_art; run;
*plot 0: retention;
proc sort data=fu out=fu2; by idpat descending visity; run;

data last; set fu2; by idpat ; *retain lost; 
nexty=lag(visity); 
if first.idpat then do; nexty=.; end; 
format nexty date9.;
run;
proc sort data=last; by idpat visity; run;
data last; set last; by idpat visity;retain lost;
if first.idpat then lost=0;
if intck('month', visity, nexty, 'c')>6 and lost=0 then do;lasty=visity; lost=1; output;end;
if last.idpat and lost=0 then do; lasty=visity; output; end;
run;
data last; set last; 
nry=intnx('month', lasty, 6, 's'); 
/*if nry>=&cen then do; nry=&cen; lost=0; end;*/
/*else if nry<&cen then do; lost=1; end;*/
if nry<=&cen and (deathy=.| nry<deathy) then do; t_lost=(nry-starty)/30.43; lost=1; end;
else if .<deathy<=nry and deathy<=&cen then do; t_lost=(deathy-starty)/30.43; lost=2; end;
else if nry>&cen and (deathy=.| nry<deathy|deathy>&cen) then do; t_lost=(&cen-starty)/30.43; lost=0; end;
run;
proc freq data=last; tables lost; run;

data p0; set last; by idpat; format lasty nry date9.; keep starty nry idpat t_lost lost male age0 site cd40 vl0 arty lasty haitian;
run;

%quickci(data=p0, t=t_lost, j=lost, out=p01)

proc export data=p01
   outfile="&output/ret.csv"
   dbms=dlm;
   delimiter=',';
run;

%quickci(data=p1, t=t_art, j=art, out=p11); 
proc export data=p11
   outfile="&output/art.csv"
   dbms=dlm replace;
   delimiter=',';
run;

data p2; set fu;by idpat; if last.idpat; if .<deathy<starty then delete;
if deathy ne . then do; td=(deathy-starty)/30.43; dead=1; end;
if deathy>&cen or deathy=. then do; td=(&cen-starty)/30.43; dead=0; end;
run;
 
%quickci(data=p2, t=td, j=dead, out=p21); 
proc export data=p21
   outfile="&output/dead.csv"
   dbms=dlm replace;
   delimiter=',';
run;


*visit intervals;
proc sort data=fu out=fu2; by idpat descending visity; run;

data vis; set fu2; by idpat ; *retain lost; 
nexty=lag(visity); 
if first.idpat then do; nexty=.; end; 
format nexty date9.;
run; 

proc sort data=vis; by idpat visity; run;

data vis; set vis; interval=nexty-visity; planned=next_visity-visity; if interval=0 then delete; run;
proc means data=vis mean min max p5 p25 p50 p75 p95; var interval planned; run;


*how many vls;
proc sort data=fu; by idpat visity; run;
*time to virst viral load?;
data p3; set fu; by idpat visity; if .<vly<=visity; run;
data p2b; set p3; by idpat; if first.idpat; firstvly=visity; keep idpat firstvly; run;
data p2c; set fu; by idpat; if first.idpat; run;
data p2d; merge p2c p2b; by idpat; 
if .<firstvly<=&cen then do;  t_vl=(firstvly-starty)/30.43; hasvl=1; end;
else if .<deathy<=&cen then do; t_vl=(deathy-starty)/30.43; hasvl=2; end;
else if deathy = . or deathy>&cen then do; t_vl=(&cen-starty)/30.43; hasvl=0; end;
run;

proc freq data=p2d; tables hasvl; run;

%quickci(data=p2d, t=t_vl, j=hasvl, out=p31); 
proc export data=p31
   outfile="&output/vl.csv"
   dbms=dlm replace;
   delimiter=',';
run;

proc sort data=fu; by idpat visity; run;
*cross sectional cascade;
data csc; set fu; by idpat; if last.idpat; 
if visity>(&cen-180) and art=1 then ret=1; else  ret=0; *on ART and retained;
run;

data cscvl; set fu; 
	by idpat visity;
	where vl ne .; 
	if last.idpat then do; lastvl=vly; output; end; run;
data cscvl; set cscvl; keep idpat lastvl;
data csc2; merge cscvl csc; by idpat; 
if lastvl>&cen-180 then cvl=vl; else cvl=.; 
if .<cvl<=50 then sup=1; else if cvl>50 then sup=0; else if cvl=. then sup=.; 
if ret=0 then sup=0;
run;
proc freq data=csc2; tables ret sup ret*sup/missing; run;
proc freq data=csc; * where art=1; tables ret; run;
proc means data=csc noprint mean; var art; output out=a1 mean=art; run;
proc means data=csc noprint mean; var ret; output out=a2 mean=ret; run;
proc means data=csc2  mean;where ret=1; var sup; output out=a3 mean=supi; run;
data n0; merge a1 a2 a3; sup=supi*ret; keep art ret sup; run;
proc print data=n0; run;
proc export data=n0
   outfile="&output/n0.csv"
   dbms=dlm replace;
   delimiter=',';
run;
*worst case;
data csc3; set csc2; if ret=1 and sup=. then sup=0; run;
proc means data=csc3  mean;where ret=1; var sup; output out=a3 mean=supi; run;
data n1; merge a1 a2 a3; sup=supi*ret; keep art ret sup supi; run;
proc print data=n1; run;
proc export data=n1
   outfile="&output/n1.csv"
   dbms=dlm replace;
   delimiter=',';
run;
*best case;
data csc3; set csc2; if ret=1 and sup=. then sup=1; run;
proc means data=csc3  mean;where ret=1; var sup; output out=a3 mean=supi; run;
data n2; merge a1 a2 a3; sup=supi*ret; keep art ret sup supi; run;
proc print data=n2; run;
proc export data=n2
   outfile="&output/n2.csv"
   dbms=dlm replace;
   delimiter=',';
run;


*explore vl missingness; 
proc freq data=csc2  ;where ret=1; tables sup/missing; run;

*output naive cross sectional cascade as of june 2016;



*proportion with VL in first 6 months?;
*proportion with VL around 2 years?;

*bounds on VL;
*accounting for missing data analytically;
*show hypothetical double sampling data;
