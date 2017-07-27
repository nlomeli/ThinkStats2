def make_hist(vals):
    hist = {}
    for val in vals:
        hist[val] = hist.get(val, 0) + 1
    return hist

# like collections.Counter
# like thinkstats2.hist

def cohen_effect_size(group1, group2):
    """
    group1: pandas.core.series.Series
    group2: pandas.core.series.Series
    """
    import math
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = group1.count(), group2.count()

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
