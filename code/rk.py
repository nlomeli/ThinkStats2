# By week 39, 51% of black children have been born, while the figure for whites
# is 33%; by week 40, the figures are 70 and 55% respectively
# (Niswander and Gordon, 1972).

import numpy as np
import nsfg

from collections import defaultdict

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
