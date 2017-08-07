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

def normalize(d):
    total = sum(d.values())
    for val, prob in d.items():
        d[val] = prob/total
    return d

def pmf_mean(pmf): return sum([val*prob for val, prob in pmf.Items()])
#pmf_mean = lambda pmf:sum([val*prob for val, prob in pmf.Items()])

def pmf_var(pmf):
    mean = pmf_mean(pmf)
    return sum([prob*(val-mean)**2 for val, prob in pmf.Items()])

def observed_pmf(actual_pmf, observer_speed):
    biased_values = {}
    for val, prob in actual_pmf.Items():
        biased_values[val] = prob*abs(val-observer_speed)
    biased_pmf = thinkstats2.Pmf(biased_values)
    biased_pmf.Normalize()
    return biased_pmf

#def percentile(score, list_of_scores):
#    num_scores = len(list_of_scores)
#    list_of_scores.sort(reverse=True)
#    index = list_of_scores.index(score) # incorrect--score would have to be in list
#    return 100*(num_scores-index)/num_scores

def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count+=1
    return 100*count/len(scores)

def PercentileValue(scores, percentile_rank):
    """
    Returns the minimum score with percentile rank greater than or equal to
    percentile_rank
    """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score

def Percentile(scores, rank):
    scores.sort()
    index_range = len(scores)-1
    decimal_rank = rank/100
    return scores[round(index_range*decimal_rank)]

def Percentile2(scores, percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) // 100
    return scores[index]

def cdf(x, t):
    count = 0
    for val in t:
        if val <= x:
            count+=1
    return count/len(t)

def EvalCdf(t, x):
    count = 0.0
    for value in t:
        if value <= x:
            count += 1
    prob = count / len(t)
    return prob

def PositionToPercentile(position, field_size):
    beat = field_size - position
    percentile = 100.0*(beat+1)/field_size
    return percentile

def PercentileToPosition(percentile, field_size):
    beat = field_size*percentile/100 - 1
    position = field_size - beat
    return position

def EvalNormalCdf(x, mu=0, sigma=1):
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)

def MakeNormalModel(weights):
    """Plots a CDF with a Normal model.

    weights: sequence
    """
    cdf = thinkstats2.Cdf(weights, label='weights')
    mean, var = thinkstats2.TrimmedMeanVar(weights)
    std = np.sqrt(var)
    print('n, mean, std', len(weights), mean, std)
    xmin = mean - 4*std
    xmax = mean + 4*std
    xs, ps = thinkstats2.RenderNormalCdf(mean, std, xmin, xmax)
    thinkplot.Plot(xs, ps, label='model', linewidth=4, color='0.8')
    thinkplot.Cdf(cdf)
    thinkplot.Show()

def MakeNormalPlot(weights):
    """Generates a normal probability plot of birth weights.

    weights: sequence
    """
    mean, var = thinkstats2.TrimmedMeanVar(weights, p=0.01)
    std = np.sqrt(var)
    xs = [-5, 5]
    xs, ys = thinkstats2.FitLine(xs, mean, std)
    thinkplot.Plot(xs, ys, color='0.8', label='model')
    xs, ys = thinkstats2.NormalProbability(weights)
    thinkplot.Plot(xs, ys, label='weights')
    thinkplot.Show

import random

def expovariate(lam):
    p = random.random()
    x = -np.log(1-p) / lam
    return x

#def paretovariate(alph):

class NormalPdf(Pdf):

    def __init__(self, mu=0, sigma=1, label=''):
        self.mu = mu
        self.sigma = sigma
        self.label = label

    def Density(self, xs):
        return scipy.stats.norm.pdf(xs, self.mu, self.sigma)

    def GetLinspace(self):
        low, high = self.mu-3*self.sigma, self.mu+3*sigma
        return np.linspace(low, high, 101)


def f(**kwargs):
    print(kwargs.get('fname'))
    print(kwargs.get('lname'))
    print(kwargs['fname'])
    print(kwargs['lname'])

f(fname='Nathan',lname='Lomeli')
