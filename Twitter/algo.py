from joblib import dump, load

clf = load('algo.joblib')

test_value = str(input("Tweet test: "))

print(clf.predict(test_value))