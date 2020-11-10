import sys
sys.path.append('src')
from naive_bayes_classifier import NaiveBayesClassifier
from dataframe import DataFrame

df = DataFrame.from_array(
    [
        [False, False, False],
        [True, True, True],
        [True, True, True],
        [False, False, False],
        [False, True, False],
        [True, True, True],
        [True, False, False],
        [False, True, False],
        [True, False, True],
        [False, True, False]
    ],
    columns = ['errors', 'links', 'scam']
)
naive_bayes = NaiveBayesClassifier(df, dependent_variable='scam')

print('\nTesting...\n')
print("    Testing NaiveBayes's probability")
assert naive_bayes.probability('scam', True) == 0.4, "NaiveBayes's probability was not right, it should be 0.4, but was {}".format(naive_bayes.probability('scam', True))
print("    NaiveBayes's probability Passed!!!\n")

print("    Testing NaiveBayes's probability")
assert naive_bayes.probability('scam', False) == 0.6, "NaiveBayes's probability was not right, it should be 0.6, but was {}".format(naive_bayes.probability('scam', False))
print("    NaiveBayes's probability Passed!!!\n")

print("    Testing NaiveBayes's conditional_probability")
assert naive_bayes.conditional_probability(('errors',True), given=('scam',True)) == 1, "NaiveBayes's conditional_probability was not right, it should be 1, but was {}".format(naive_bayes.conditional_probability(('errors',True), given=('scam',True)))
print("    NaiveBayes's conditional_probability Passed!!!\n")

print("    Testing NaiveBayes's conditional_probability")
assert naive_bayes.conditional_probability(('links',False), given=('scam',True)) == 0.25, "NaiveBayes's conditional_probability was not right, it should be 0.25, but was {}".format(naive_bayes.conditional_probability(('links',False), given=('scam',True)))
print("    NaiveBayes's conditional_probability Passed!!!\n")

print("    Testing NaiveBayes's conditional_probability")
assert naive_bayes.conditional_probability(('errors',True), given=('scam',False)) == 0.16666666666666666, "NaiveBayes's conditional_probability was not right, it should be 0.16666666666666666, but was {}".format(naive_bayes.conditional_probability(('errors',True), given=('scam',False)))
print("    NaiveBayes's conditional_probability Passed!!!\n")

print("    Testing NaiveBayes's conditional_probability")
assert naive_bayes.conditional_probability(('links',False), given=('scam',False)) == 0.5, "NaiveBayes's conditional_probability was not right, it should be 0.5, but was {}".format(naive_bayes.conditional_probability(('links',False), given=('scam',False)))
print("    NaiveBayes's conditional_probability Passed!!!\n")

observed_features = {
    'errors': True,
    'links': False
}

print("    Testing NaiveBayes's likelihood")
assert naive_bayes.likelihood(('scam',True), observed_features) == 0.1, "NaiveBayes's likelihood was not right, it should be 0.1, but was {}".format(naive_bayes.likelihood(('scam',True), observed_features))
print("    NaiveBayes's likelihood Passed!!!\n")

print("    Testing NaiveBayes's likelihood")
assert naive_bayes.likelihood(('scam',False), observed_features) ==  0.049999999999999996, "NaiveBayes's likelihood was not right, it should be  0.049999999999999996, but was {}".format(naive_bayes.likelihood(('scam',False), observed_features))
print("    NaiveBayes's likelihood Passed!!!\n")

print("    Testing NaiveBayes's classify")
assert naive_bayes.classify('scam', observed_features) == True, "NaiveBayes's classify was not right, it should be True, but was {}".format(naive_bayes.classify('scam', observed_features))
print("    NaiveBayes's classify Passed!!!\n")

print('All Tests PASS!!')