#running on python 3.5


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#1) naive cross sectional cascade
n0 = pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/n0.csv")

ret=round(n0.iloc[0,1]*100)
art=round(n0.iloc[0,0]*100)
sup=round(n0.iloc[0,2]*100)
link=100

#print(n0)
y = (link, art, ret, sup)
print(y)
N = len(y)
x = (0, 1, 2, 3)
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.ylim(0, 115)
plt.xlim(0, 4)
plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

for k in range(0, 101, 20):
    plt.plot(range(0, 5), [k] * len(range(0, 5)), "--", lw=0.5, color="black", alpha=0.3)

plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="off", left="off", right="off", labelleft="on")

ax.set_ylabel('% of patients linked to care', fontsize=16)
ax.set_xlabel(' ', fontsize=16)
#plt.bar(x, y, width=0.4, color="#3F5D7D")
plt.text(0, 110, "Cross sectional cascade", fontsize=17, ha="left")
plt.text(0, -7, "Linked", fontsize=16, ha="left")
plt.text(1, -7, "On ART", fontsize=16, ha="left")
plt.text(2, -7, "Retained", fontsize=16, ha="left")
plt.text(3.25, -7, "Suppressed", fontsize=16, ha="center")
plot1 = plt.bar(x, y, width=0.4, color="#3F5D7D")
plt.savefig("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/naivecascade.png", bbox_inches="tight")


#2: 90 90 90 targets
#hard coded these numbers (embarassing)
first90 = 90
plt.bar(1, 90, width=0.4, edgecolor="red", linestyle="dashed",fill=False)
plt.bar(2, 81, width=0.4, edgecolor="red", linestyle="dashed",fill=False)
plt.bar(3, 73, width=0.4, edgecolor="red", linestyle="dashed",fill=False)

ax.annotate(' ', xy=(1, 70), xytext=(0.45, 70),
            arrowprops=dict(facecolor='red', shrink=0.05, edgecolor='red'),
            )
plt.text(.75, 75, "90%", fontsize=16, ha="center", color='red')
plt.text(1.25, 93, "90%", fontsize=16, ha="center", color='red')
ax.annotate(' ', xy=(2, 70), xytext=(1.45, 70),
            arrowprops=dict(facecolor='red', shrink=0.05, edgecolor='red'),
            )
plt.text(1.75, 75, "90%", fontsize=16, ha="center", color='red')
plt.text(2.25, 83, "81%", fontsize=16, ha="center", color='red')
ax.annotate(' ', xy=(3, 70), xytext=(2.45, 70),
            arrowprops=dict(facecolor='red', shrink=0.05, edgecolor='red'),
            )
plt.text(2.75, 75, "90%", fontsize=16, ha="center", color='red')
plt.text(3.25, 75, "73%", fontsize=16, ha="center", color='red')

plt.savefig("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/naivecascade2.png", bbox_inches="tight")

#3: 90 90 90 progress

ax.annotate(' ', xy=(1, 30), xytext=(0.45, 30),
            arrowprops=dict(facecolor='steelblue', shrink=0.05, edgecolor='steelblue'),
            )
plt.text(.75, 35, "59%", fontsize=16, ha="center", color='steelblue')
plt.text(1.25, 63, "59%", fontsize=16, ha="center", color='steelblue')
ax.annotate(' ', xy=(2, 30), xytext=(1.45, 30),
            arrowprops=dict(facecolor='steelblue', shrink=0.05, edgecolor='steelblue'),
            )
plt.text(1.75, 35, "77%", fontsize=16, ha="center", color='steelblue')
plt.text(2.25, 49, "45%", fontsize=16, ha="center", color='steelblue')
ax.annotate(' ', xy=(3, 30), xytext=(2.45, 30),
            arrowprops=dict(facecolor='steelblue', shrink=0.05, edgecolor='steelblue'),
            )
plt.text(2.75, 35, "72%", fontsize=16, ha="center", color='steelblue')
plt.text(3.25, 37, "33%", fontsize=16, ha="center", color='steelblue')



plt.savefig("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/naivecascade3.png", bbox_inches="tight")


#4 assume viral loads are unsuppressed
n1 = pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/n1.csv")

ret=round(n1.iloc[0,1]*100)
art=round(n1.iloc[0,0]*100)
sup=round(n1.iloc[0,2]*100)
link=100

#print(n0)
y = (link, art, ret, sup)
print(y)
N = len(y)
x = (0, 1, 2, 3)
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.ylim(0, 115)
plt.xlim(0, 4)
plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

for k in range(0, 101, 20):
    plt.plot(range(0, 5), [k] * len(range(0, 5)), "--", lw=0.5, color="black", alpha=0.3)

plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="off", left="off", right="off", labelleft="on")

ax.set_ylabel('% of patients linked to care', fontsize=16)
ax.set_xlabel(' ', fontsize=16)
#plt.bar(x, y, width=0.4, color="#3F5D7D")
plt.text(0, 110, "Worst case cross sectional cascade", fontsize=17, ha="left")
plt.text(0, -7, "Linked", fontsize=16, ha="left")
plt.text(1, -7, "On ART", fontsize=16, ha="left")
plt.text(2, -7, "Retained", fontsize=16, ha="left")
plt.text(3.25, -7, "Suppressed", fontsize=16, ha="center")
ax.annotate(' ', xy=(3, 30), xytext=(2.45, 30),
            arrowprops=dict(facecolor='steelblue', shrink=0.05, edgecolor='steelblue'),
            )
plt.text(2.75, 35, "6%", fontsize=16, ha="center", color='steelblue')
plt.text(3.25, 7, "3%", fontsize=16, ha="center", color='steelblue')
plot1 = plt.bar(x, y, width=0.4, color="#3F5D7D")
plt.savefig("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/worstcascade.png", bbox_inches="tight")


#4 assume missing viral loads are suppressed
n2 = pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/n2.csv")

ret=round(n2.iloc[0,1]*100)
art=round(n2.iloc[0,0]*100)
sup=round(n2.iloc[0,2]*100)
link=100

#print(n0)
y = (link, art, ret, sup)
print(y)
N = len(y)
x = (0, 1, 2, 3)
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.ylim(0, 115)
plt.xlim(0, 4)
plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

for k in range(0, 101, 20):
    plt.plot(range(0, 5), [k] * len(range(0, 5)), "--", lw=0.5, color="black", alpha=0.3)

plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="off", left="off", right="off", labelleft="on")

ax.set_ylabel('% of patients linked to care', fontsize=16)
ax.set_xlabel(' ', fontsize=16)
#plt.bar(x, y, width=0.4, color="#3F5D7D")
plt.text(0, 110, "Best case cross sectional cascade", fontsize=17, ha="left")
plt.text(0, -7, "Linked", fontsize=16, ha="left")
plt.text(1, -7, "On ART", fontsize=16, ha="left")
plt.text(2, -7, "Retained", fontsize=16, ha="left")
plt.text(3.25, -7, "Suppressed", fontsize=16, ha="center")
ax.annotate(' ', xy=(3, 30), xytext=(2.45, 30),
            arrowprops=dict(facecolor='steelblue', shrink=0.05, edgecolor='steelblue'),
            )
plt.text(2.75, 35, "97%", fontsize=16, ha="center", color='steelblue')
plt.text(3.25, 49, "44%", fontsize=16, ha="center", color='steelblue')
plot1 = plt.bar(x, y, width=0.4, color="#3F5D7D")
plt.savefig("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/bestcascade.png", bbox_inches="tight")
