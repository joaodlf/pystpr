from __future__ import division  # Float division
from matplotlib import pyplot
import pandas
import numpy
import scipy.stats as stats

# Change default pyplot style
pyplot.style.use("ggplot")


class Pmf:
    """
    Probability Mass Functions
    """
    def __init__(self):
        self._pmf = []

    def add(self, sample, label, color):
        """
        Computes the PMF for a sample, extra options to be used for plotting
        :param sample:
        :param label:
        :param color:
        :return:
        """
        total_elements = len(sample)
        unique, counts = numpy.unique(sample, return_counts=True)

        unique_counts = numpy.asarray((unique, counts)).T

        pmf = {}
        for x in unique_counts:
            pmf[x[0]] = int(x[1]) / int(total_elements)

        self._pmf.append({
            "values": pmf,
            "label": label,
            "color": color
        })

        return pmf

    def plot(self):
        """
        Plots all the added samples
        :return:
        """
        if not self._pmf:
            raise ValueError("You must first compute at least one PMF!")

        merged_values = []
        merged_keys = []

        bar_width = 0.2;
        bar_width_space = 0;
        for pmf in self._pmf:
            pmflen = len(pmf["values"])
            merged_values.append(numpy.arange(pmflen))
            merged_keys = list(set(merged_keys) | set(pmf["values"].keys()))

            pyplot.bar(numpy.arange(pmflen) + bar_width_space, pmf["values"].values(), width=bar_width,
                       alpha=0.5,
                       label=pmf["label"],
                       color=pmf["color"])

            bar_width_space += bar_width

        pyplot.xticks(numpy.unique(numpy.concatenate(merged_values)) + bar_width_space / 2, merged_keys)
        pyplot.ylabel("Probability")
        pyplot.legend(loc="upper right")
        pyplot.tight_layout()
        return pyplot.show()


class Cdf:
    """
    Cumulative Distribution Functions
    """
    def __init__(self):
        self._cdf = []

    def add(self, sample):
        """
        Adds a sample to be plotted, note: We don't compute the CDF here to improve performance, typically we only
        care about plotting these samples.
        :param sample:
        :return:
        """
        self._cdf.append({
            "sample": sample,
        })

    @staticmethod
    def percentile(sample, percentile_rank, interpolation="linear"):
        """
        Returns the value corresponding to a percentile rank
        :param sample:
        :param percentile_rank:
        :param interpolation:
        :return:
        """
        return numpy.percentile(sample, percentile_rank, interpolation=interpolation)

    @staticmethod
    def percentile_rank(sample, value):
        """
        Returns the percentile rank of a given value
        :param sample:
        :param value:
        :return:
        """
        return stats.percentileofscore(sample, value)

    @staticmethod
    def iqr(sample, interpolation="linear"):
        """
        Returns the interquartile range of a given sample
        :param sample:
        :param interpolation:
        :return:
        """
        return stats.iqr(sample, interpolation=interpolation)

    def plot(self):
        """
        Plots all the added samples
        :return:
        """
        if not self._cdf:
            raise ValueError("You must first compute at least one CDF!")

        mins = []
        maxs = []
        for cdf in self._cdf:
            sample = pandas.Series(cdf["sample"])
            sorted_sample = numpy.sort(sample)
            total = len(sample)

            mins.append(sorted_sample[0])
            maxs.append(sorted_sample[-1])

            y = numpy.array(range(total))/float(total)
            pyplot.step(sorted_sample, y)

        mins = sorted(mins)
        maxs = sorted(maxs)
        pyplot.ylabel("CDF")
        # Force the xlim edges
        pyplot.xlim(mins[0] - 1, maxs[-1] + 1)
        pyplot.tight_layout()
        return pyplot.show()
