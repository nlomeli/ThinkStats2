"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

# National Survey of Family Growth (NSFG)
# 2002 codebook:
# ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NSFG/Cycle6Codebook-Female.pdf
# read 2002FemResp.dat.gz
# pregnum is a recode that indicates how many times each respondent has been pregnant
# or NUMPREGS?
# print the value counts for this variable
# and compare them to the published results in the NSFG codebook
# You can also cross-validate the respondent and pregnancy files by comparing
# pregnum for each respondent with the number of records in the pregnancy file.
# You can use nsfg.MakePregMap to make a dictionary that maps from each
# caseid to a list of indices into the pregnancy DataFrame.

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file) # <class 'thinkstats2.FixedWidthVariables'>
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows) # <class 'pandas.core.frame.DataFrame'>
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables form the respondent frame.

    df: DataFrame
    """
    pass


def ValidatePregnum(resp):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    """
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)

    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(sys.argv[0])
