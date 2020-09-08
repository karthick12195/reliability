from reliability.Fitters import Fit_Everything, Fit_Loglogistic_2P, Fit_Loglogistic_3P
from reliability.Distributions import  Loglogistic_Distribution, Weibull_Distribution
from reliability.Datasets import automotive
import matplotlib.pyplot  as plt
a = automotive()

def test_Fit_Loglogistic():
    data = Loglogistic_Distribution(alpha=10, beta=3, gamma=5).random_samples(100, seed=5)
    fit = Fit_Everything(failures=data, show_probability_plot=True, print_results=True)
    plt.show()

test_Fit_Loglogistic()