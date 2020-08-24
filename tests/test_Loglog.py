from reliability.Fitters import Fit_Everything, Fit_Loglogistic_2P
from reliability.Distributions import  Loglogistic_Distribution, Weibull_Distribution
from reliability.Datasets import automotive
import matplotlib.pyplot  as plt
a = automotive()

def test_Fit_Loglogistic_2P():
    data = Loglogistic_Distribution(alpha=50, beta=2).random_samples(20, seed=5)
    fit = Fit_Everything(failures=data, show_probability_plot=True, print_results=True)
    plt.show()
