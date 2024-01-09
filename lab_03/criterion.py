import scipy.stats as sp
#from numpy import mean

class RandomnessCriterion:

    def __init__(self):
        pass

    def get_coeff_chi2(self, seq):
        if (max(seq) - min(seq)) == 0:
            return 0

        p = 1 / (max(seq) - min(seq))
        n = len(seq)
        v = 0
        coeff = 0

        for el in range(min(seq), max(seq) + 1, 1):
            y = seq.count(el)
            y2 = y*y
            v += y2 / p

        v = v / n - n

        coeff = sp.chi2.cdf(v, max(seq) - min(seq) - 1)
        return coeff

    def get_coeff_my(self, seq):

        evenNumbers = list()
        oddNumbers = list()

        for numb in seq:
            if numb & 1:
                oddNumbers.append(numb)
            else:
                evenNumbers.append(numb)

        if len(evenNumbers) == 0 or len(oddNumbers) == 0:
            return 0

        avgEvenNumbers = sum(evenNumbers) / len(evenNumbers)
        avgOddNumbers = sum(oddNumbers) / len(oddNumbers)
        avgArr = [avgEvenNumbers, avgOddNumbers]
        return min(avgArr) / max(avgArr)
