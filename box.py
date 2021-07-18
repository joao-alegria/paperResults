#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import csv
import os
import sys
def __read_csv(path, column):
    # prepare the CSV reading
    csv_file = open(path, mode="r")
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()    # discard the header
    vals = list()
    for row in csv_reader:
        # determine delta in ms
        vals.append(float(row[column]))
    return vals
def __add_xx(df, vals, step, op):
  data = dict()
  data['time'] = vals
  data['step'] = len(vals) * [step]
  data['operation'] = len(vals) * [op]
  df = df.append(pd.DataFrame(data), ignore_index=True)
  return df
# in0  = __read_csv('step0.csv')
# in1  = __read_csv('step1.csv')
# in2  = __read_csv('step2.csv')
labels   = ["Step1","Step2","GetMtd","GetInt","Inter","Mtd","Stage1","Step4","Stage2"]
df = pd.DataFrame()
# --- LOCAL ---
# in3   = [3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 10, 4, 3, 4, 14, 3, 3, 3, 5, 4, 3, 3]
# in45  = [35212, 33907, 33440, 35890, 35577, 38456, 39668, 36784, 42303, 41308, 55032, 35575, 35648, 37367, 38883, 36155, 44086, 40173, 44758, 46017, 41764, 39468]
# in6   = [124206, 82594, 135386, 147378, 132075, 133221, 126360, 173764, 152416, 193461, 216328, 128059, 148025, 156705, 131348, 150852, 143400, 150174, 141671, 125299, 175192, 146545]
# total = [164433, 204668, 169633, 192885, 172188, 176419, 168281, 229241, 195737, 249954, 290882, 168744, 187781, 200930, 174886, 195435, 191726, 197289, 190641, 175977, 229356, 196360]
mtdStep11=__read_csv('resultsMtd.csv',0)
mtdStep12=__read_csv('resultsMtd.csv',1)
mtdStep21=__read_csv('resultsMtd.csv',2)
mtdStep22=__read_csv('resultsMtd.csv',3)
mtdGetMtd1=__read_csv('resultsMtd.csv',4)
mtdGetMtd2=__read_csv('resultsMtd.csv',5)
mtdGetInter1=__read_csv('resultsMtd.csv',6)
mtdGetInter2=__read_csv('resultsMtd.csv',7)
mtdAddpeer1=__read_csv('resultsMtd.csv',8)
mtdAddpeer2=__read_csv('resultsMtd.csv',9)
mtdMtd1=__read_csv('resultsMtd.csv',10)
mtdMtd2=__read_csv('resultsMtd.csv',11)
mtdStage1=__read_csv('resultsMtd.csv',12)
mtdStep41=__read_csv('resultsMtd.csv',13)
mtdStep42=__read_csv('resultsMtd.csv',14)
mtdStage2=__read_csv('resultsMtd.csv',15)



interStep11=__read_csv('resultsInterdomain.csv',0)
interStep12=__read_csv('resultsInterdomain.csv',1)
interStep21=__read_csv('resultsInterdomain.csv',2)
interStep22=__read_csv('resultsInterdomain.csv',3)
interGetInter1=__read_csv('resultsInterdomain.csv',4)
interGetInter2=__read_csv('resultsInterdomain.csv',5)
interAddpeer1=__read_csv('resultsInterdomain.csv',6)
interAddpeer2=__read_csv('resultsInterdomain.csv',7)
interStage1=__read_csv('resultsInterdomain.csv',8)
interStep41=__read_csv('resultsInterdomain.csv',9)
interStep42=__read_csv('resultsInterdomain.csv',10)
interStage2=__read_csv('resultsInterdomain.csv',11)
# in11=__read_csv('resultsMtd.csv',0)
# in12=__read_csv('resultsMtd.csv',1)
# in21=__read_csv('resultsMtd.csv',2)
# in22=__read_csv('resultsMtd.csv',3)
# in31=__read_csv('resultsMtd.csv',4)
# in32=__read_csv('resultsMtd.csv',5)
# in4=__read_csv('resultsMtd.csv',6)
# in51=__read_csv('resultsMtd.csv',7)
# in52=__read_csv('resultsMtd.csv',8)
# in6=__read_csv('resultsMtd.csv',9)
# values   = [Step11,Step12,Step21,Step22,GetMtd1,GetMtd2,GetInter1,GetInter2,Addpeer1,Addpeer2,Mtd1,Mtd2,Stage1,Step41,Step42,Stage2]
op = 'Scenario1-Domain1'
# ---------------------------------------------------
df = __add_xx(df, interStep11, labels[0], op)
df = __add_xx(df, interStep21, labels[1], op)
df = __add_xx(df, [0 for x in mtdGetMtd1], labels[2], op)
df = __add_xx(df, interGetInter1, labels[3], op)
df = __add_xx(df, interAddpeer1, labels[4], op)
df = __add_xx(df, [0 for x in mtdMtd1], labels[5], op)
df = __add_xx(df, interStage1, labels[6], op)
df = __add_xx(df, interStep41, labels[7], op)
df = __add_xx(df, interStage2, labels[8], op)
# ---------------------------------------------------
# --- ID node1 old ---
# in3   = [13, 3, 4, 6, 4, 4, 4, 4, 4, 4, 4, 4]
# in45  = [72631, 69531, 66758, 66095, 56896, 54530, 66793, 68347, 51399, 56024, 61374, 64473]
# in6   = [421343, 419944, 214471, 403502, 416739, 403911, 272507, 359620, 521841, 484875, 462998, 473935]
# total = [494805, 494570, 283539, 474311, 478481, 463145, 347034, 432133, 578292, 545798, 528420, 553776]
# values   = [in0, in1, in2, in3, in45, in6]
op = 'Scenario1-Domain2'
# ---------------------------------------------------
df = __add_xx(df, interStep12, labels[0], op)
df = __add_xx(df, interStep22, labels[1], op)
df = __add_xx(df, [0 for x in mtdGetMtd2], labels[2], op)
df = __add_xx(df, interGetInter2, labels[3], op)
df = __add_xx(df, interAddpeer2, labels[4], op)
df = __add_xx(df, [0 for x in mtdMtd2], labels[5], op)
df = __add_xx(df, interStage1, labels[6], op)
df = __add_xx(df, interStep42, labels[7], op)
df = __add_xx(df, interStage2, labels[8], op)

op = 'Scenario2-Domain1'
# ---------------------------------------------------
df = __add_xx(df, mtdStep11, labels[0], op)
df = __add_xx(df, mtdStep21, labels[1], op)
df = __add_xx(df, mtdGetMtd1, labels[2], op)
df = __add_xx(df, mtdGetInter1, labels[3], op)
df = __add_xx(df, mtdAddpeer1, labels[4], op)
df = __add_xx(df, mtdMtd1, labels[5], op)
df = __add_xx(df, mtdStage1, labels[6], op)
df = __add_xx(df, mtdStep41, labels[7], op)
df = __add_xx(df, mtdStage2, labels[8], op)


op = 'Scenario2-Domain2'
# ---------------------------------------------------
df = __add_xx(df, mtdStep12, labels[0], op)
df = __add_xx(df, mtdStep22, labels[1], op)
df = __add_xx(df, mtdGetMtd2, labels[2], op)
df = __add_xx(df, mtdGetInter2, labels[3], op)
df = __add_xx(df, mtdAddpeer2, labels[4], op)
df = __add_xx(df, mtdMtd2, labels[5], op)
df = __add_xx(df, mtdStage1, labels[6], op)
df = __add_xx(df, mtdStep42, labels[7], op)
df = __add_xx(df, mtdStage2, labels[8], op)
# ---------------------------------------------------
# --- ID node2 hal ---
# in3   = [3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 3]
# in45  = [47155, 66908, 60328, 42132, 49959, 57012, 61126, 40387, 51631, 41728, 46593, 46304]
# in6   = [173557, 170167, 153011, 182284, 168026, 172878, 143821, 158485, 154525, 239278, 144473, 143009]
# total = [224853, 244142, 217922, 228522, 221495, 237890, 209869, 203147, 211307, 304600, 195591, 193472]
# values   = [in0, in1, in2, in3, in45, in6]
# op = 'interdomain-B'
# ---------------------------------------------------
# df = __add_xx(df, in0, labels[0], op)
# df = __add_xx(df, in1, labels[1], op)
# df = __add_xx(df, in2, labels[2], op)
# df = __add_xx(df, in3, labels[3], op)
# df = __add_xx(df, in45, labels[4], op)
# df = __add_xx(df, in6, labels[5], op)
# ---------------------------------------------------
fig, ax = plt.subplots()
sns_plot = sns.boxplot(x = 'step', y = 'time',
                       hue = 'operation', palette='Set2',
                       linewidth = 0.1, fliersize = 0.1,
                       data = df)
sns.despine(offset=10, trim=True)
ax.set_xlabel('Steps')
ax.set_ylabel('Time (ms)')
plt.ylim(bottom=0)
plt.yscale('symlog')
ax.legend().set_title('')
fig.savefig(sys.argv[1] + '.png')
fig.savefig(sys.argv[1] + '.pdf')
plt.close()