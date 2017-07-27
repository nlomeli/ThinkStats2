# By week 39, 51% of black children have been born, while the figure for whites
# is 33%; by week 40, the figures are 70 and 55% respectively
# (Niswander and Gordon, 1972).

import numpy as np
import nsfg

from collections import defaultdict

from scratch import cohen_effect_size

# Chapter 1

preg = nsfg.ReadFemPreg()
resp = nsfg.ReadFemResp()

prglngth = defaultdict(list)
wksgest = defaultdict(list)
for _, row in preg.iterrows():
    if row.outcome == 1:
        if row.prglngth == row.prglngth:
            prglngth[int(row.caseid)].append(row.prglngth)
        if row.wksgest == row.wksgest:
            wksgest[int(row.caseid)].append(row.wksgest)

racemap = {} # 4.0 black, 5.0 white
for _, row in resp.iterrows():
    racemap[int(row.caseid)] = row.rscreenrace

lengths = defaultdict(list)
weeks = defaultdict(list)

for caseid, rscreenrace in racemap.items():
    if rscreenrace:
        lengths[rscreenrace].extend(prglngth[caseid])
        weeks[rscreenrace].extend(wksgest[caseid])

print(len(lengths[4.0]))
print(len(lengths[5.0]))

print(len(weeks[4.0]))
print(len(weeks[5.0]))

import statistics as stats

print(stats.mean(lengths[4.0]))
print(stats.mean(lengths[5.0]))

print(stats.mean(weeks[4.0]))
print(stats.mean(weeks[5.0]))

# Chapter 2

import pandas as pd

preg_resp = pd.merge(preg, resp, how='outer', on='caseid')
live_black = preg_resp[(preg_resp.outcome==1) & (preg_resp.rscreenrace==4)]
live_white = preg_resp[(preg_resp.outcome==1) & (preg_resp.rscreenrace==5)]

live_black.wksgest.mean() # 38.297374897456933
live_black.wksgest.std() # 2.999480409069573
live_white.wksgest.mean() # 38.739771409640547
live_white.wksgest.std() # 2.7372870459379532

print((live_white.wksgest.mean() - live_black.wksgest.mean()) / live_black.wksgest.std())
print((live_black.wksgest.mean() - live_white.wksgest.mean()) / live_white.wksgest.std())

# proportion of live births by 40 weeks)
print(live_black.wksgest[live_black.wksgest<40].count() / live_black.wksgest.count())
print(live_white.wksgest[live_white.wksgest<40].count() / live_white.wksgest.count())

live_black.totalwgt_lb.mean() # 6.9
live_white.totalwgt_lb.mean() # 7.4

live_black.agepreg.median() # 22.66
live_white.agepreg.median() # 25.08

live_black.agepreg.mode() # 18.83
live_white.agepreg.mode() # 21.58

import thinkstats2
import thinkplot

black_wgt_hist = thinkstats2.Hist(live_black.totalwgt_lb)
white_wgt_hist = thinkstats2.Hist(live_white.totalwgt_lb)

#width =
thinkplot.PrePlot(2)
thinkplot.Hist(black_wgt_hist, align='center')#, width=width)
thinkplot.Hist(white_wgt_hist, align='center')#, width=width)
thinkplot.Show(xlabel='lbs', ylabel='count')

black_wks_hist = thinkstats2.Hist(live_black.wksgest)
white_wks_hist = thinkstats2.Hist(live_white.wksgest)

width = 1
thinkplot.PrePlot(2)
thinkplot.Hist(black_wks_hist, align='center', width=width)
thinkplot.Hist(white_wks_hist, align='center', width=width)
thinkplot.Show(xlabel='weeks', ylabel='count')

cohen_effect_size(live_black.wksgest, live_white.wksgest)
cohen_effect_size(live_white.wksgest, live_black.wksgest)

cohen_effect_size(live_black.totalwgt_lb, live_white.totalwgt_lb)

cohen_effect_size(live_black.agepreg, live_white.agepreg)

# consider whether gestation and weight effects persist after "controlling for":
# resp.age
# resp.totincr - total income for the respondent's Family
# note that
# resp.age_r is respondent's age at time of interview
# resp.numfmhh is number of people in respondent's household
# resp.parity is number children borne by the respondent
#
# in later years, multiple births is a computed variable: nbrnlv_s
cohen_effect_size(resp[resp.totincr==2].parity, resp[resp.totincr==13].parity)

resp[(resp.rscreenrace==4)].totincr.median()
resp[(resp.rscreenrace==5)].totincr.median()

resp[(resp.rscreenrace==4)].parity.mean()
resp[(resp.rscreenrace==5)].parity.mean()

cohen_effect_size(resp[(resp.rscreenrace==4)].parity, resp[(resp.rscreenrace==5)].parity)
