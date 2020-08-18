import reliability as rel
import matplotlib.pyplot as plt
import scipy.stats as ss

def test_functions():
    llf = rel.Distributions.Loglogistic_Distribution(alpha=100, beta=5, gamma=6)
    llf.plot()
    xvals = llf.random_samples(number_of_samples=100)
    print('PDF:', any(llf.PDF(xvals) == ss.fisk.pdf(xvals, c=5, loc=6, scale=100)))
    print('CDF:', any(llf.CDF(xvals) == ss.fisk.cdf(xvals, c=5, loc=6, scale=100)))
    print('SF:', any(llf.SF(xvals) == ss.fisk.sf(xvals, c=5, loc=6, scale=100)))
    # test for HF missing
    # test for CHF missing
    print('Quantile:', llf.quantile(0.5) == ss.fisk.ppf(0.5, c=5, loc=6, scale=100))
    print('Iverse_SF:', llf.inverse_SF(0.5) == ss.fisk.isf(0.5, c=5, loc=6, scale=100))
    # test for MRL missing
    print('Mean:', llf.mean == ss.fisk.mean(c=5, loc=6, scale=100))
    print('Median:', llf.median == ss.fisk.median(c=5, loc=6, scale=100))
    # test for Mode missing, used the formula from wikipedia
    # test for b5 and b95 are missing
    print('Variance:', llf.variance == ss.fisk.var(c=5, loc=6, scale=100))
    print('Standard Deviation:', llf.standard_deviation == ss.fisk.std(c=5, loc=6, scale=100))
    print('Kurtosis:', llf.kurtosis == ss.fisk.stats(c=5, loc=6, scale=100, moments='k') + 3)
    print('Skewness:', llf.skewness == ss.fisk.stats(c=5, loc=6, scale=100, moments='s'))
test_functions()