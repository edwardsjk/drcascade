

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

p01= pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/ret.csv")
p01.ci1=(1-p01.ci1)*100
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)

def init():
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(0, 115)
    plt.xlim(0, 33)
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 101, 20):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('% Retained in care', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    plt.step(p01.t_lost[p01.t_lost<2],
            p01.ci1[p01.t_lost<2], lw=2.5, color="red")
    plt.text(2, 110, "Percentage of patients retained in care through 6 months", fontsize=17, ha="left")
    plt.text(0, -13, "Retention in care defined as time without a >= 6 month gap in care", fontsize=10)

def animate(i):
    ax.clear()
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(0, 115)
    plt.xlim(0, 33)
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 101, 20):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('% Retained in care', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    pl = plt.step(p01.t_lost[p01.t_lost<=i],
                  p01.ci1[p01.t_lost<=i], lw=2.5, color="red")
    months=i;
    lab =  plt.text(2, 110, "Percentage of patients retained in care through %s months" % months, fontsize=17, ha="left")
    fn =   plt.text(0, -13, "Retention in care defined as time without a >= 6 month gap in care", fontsize=10)
    return pl, lab, fn

from matplotlib import animation
ani = animation.FuncAnimation(fig, animate, frames=33, interval=1, blit=False)
ffmpeg_args = '-r 40'
ffmpeg_args = ' '.join([ffmpeg_args, '-c:v libx264']).strip()
ffmpeg_args = ' '.join([ffmpeg_args, '-pix_fmt yuv420p']).strip()
ani.save("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/retention.mp4", writer = 'ffmpeg', extra_args=ffmpeg_args.split(' '), fps=3)



###ART



p01= pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/art.csv")
p01.ci1=(p01.ci1)*100
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)

def init():
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(0, 115)
    plt.xlim(-1, 33)
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 101, 20):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('% Initiated on ART', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    plt.step(p01.t_art[p01.t_art<2],
            p01.ci1[p01.t_art<2], lw=2.5, color="green")
    plt.text(2, 110, "Percentage of patients initiated on ART", fontsize=17, ha="left")


def animate(i):
    ax.clear()
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(0, 115)
    plt.xlim(-1, 33)
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 101, 20):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('% Initiated on ART', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    pl = plt.step(p01.t_art[p01.t_art<=i],
                  p01.ci1[p01.t_art<=i], lw=2.5, color="green")
    months=i;
    lab =  plt.text(2, 110, "Percentage of patients initiated on ART through %s months" % months, fontsize=17, ha="left")
    return pl, lab

from matplotlib import animation
ani = animation.FuncAnimation(fig, animate, frames=33, interval=1, blit=False)
ffmpeg_args = '-r 40'
ffmpeg_args = ' '.join([ffmpeg_args, '-c:v libx264']).strip()
ffmpeg_args = ' '.join([ffmpeg_args, '-pix_fmt yuv420p']).strip()
ani.save("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/art.mp4", writer = 'ffmpeg', extra_args=ffmpeg_args.split(' '), fps=3)

#death


p01= pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/dead.csv")
p01.ci1=(p01.ci1)*100
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)

def init():
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(-1, 15)
    plt.xlim(-1, 33)
    plt.yticks(range(0, 11, 2), [str(x) + "%" for x in range(0, 11, 2)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 11, 2):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('Mortality, %', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    plt.step(p01.td[p01.td<2],
            p01.ci1[p01.td<2], lw=2.5, color="blue")
    plt.text(2, 13, "Mortality", fontsize=17, ha="left")


def animate(i):
    ax.clear()
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(-1, 15)
    plt.xlim(-1, 33)
    plt.yticks(range(0, 11, 2), [str(x) + "%" for x in range(0, 11, 2)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 11, 2):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('Mortality, %', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    pl = plt.step(p01.td[p01.td<=i],
                  p01.ci1[p01.td<=i], lw=2.5, color="blue")
    months=i+1
    mortlist = np.array(p01.loc[p01.td<=i+1, "ci1"])
    mort = mortlist[-1]
    lab =  plt.text(2, 13, 'Mortality through {:d} months = {:.2f} %'.format(months, mort), fontsize=17, ha="left")
    return pl, lab

from matplotlib import animation
ani = animation.FuncAnimation(fig, animate, frames=30, interval=1, blit=False)
ffmpeg_args = '-r 40'
ffmpeg_args = ' '.join([ffmpeg_args, '-c:v libx264']).strip()
ffmpeg_args = ' '.join([ffmpeg_args, '-pix_fmt yuv420p']).strip()
ani.save("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/dead.mp4", writer = 'ffmpeg', extra_args=ffmpeg_args.split(' '), fps=3)




p01= pd.read_csv("/Users/jkedwar/Dropbox/Research/drcascade/analysis/data/vl.csv")
p01.ci1=(p01.ci1)*100
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(111)

def init():
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(0, 115)
    plt.xlim(-1, 33)
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 101, 20):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('% with at least 1 viral load', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    plt.step(p01.t_vl[p01.t_vl<2],
            p01.ci1[p01.t_vl<2], lw=2.5, color="green")
    plt.text(2, 110, "Percentage of patients with at least one VL", fontsize=17, ha="left")


def animate(i):
    ax.clear()
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylim(0, 115)
    plt.xlim(-1, 33)
    plt.yticks(range(0, 101, 20), [str(x) + "%" for x in range(0, 101, 20)], fontsize=14)
    plt.xticks(fontsize=14)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for y in range(0, 101, 20):
        plt.plot(range(0, 33), [y] * len(range(0, 33)), "--", lw=0.5, color="black", alpha=0.3)

    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    ax.set_ylabel('% with at least 1 VL', fontsize=16)
    ax.set_xlabel('Months since linkage to care', fontsize=16)
    pl = plt.step(p01.t_vl[p01.t_vl<=i],
                  p01.ci1[p01.t_vl<=i], lw=2.5, color="green")
    months=i;
    lab =  plt.text(2, 110, "Percentage of patients with at least 1 VL through %s months" % months, fontsize=17, ha="left")
    return pl, lab

from matplotlib import animation
ani = animation.FuncAnimation(fig, animate, frames=33, interval=1, blit=False)
ffmpeg_args = '-r 40'
ffmpeg_args = ' '.join([ffmpeg_args, '-c:v libx264']).strip()
ffmpeg_args = ' '.join([ffmpeg_args, '-pix_fmt yuv420p']).strip()
ani.save("/Users/jkedwar/Dropbox/Research/drcascade/analysis/plots/firstvl.mp4", writer = 'ffmpeg', extra_args=ffmpeg_args.split(' '), fps=3)
