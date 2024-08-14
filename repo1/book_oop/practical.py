from model_ import TestingKnowSample, InvalidSampleError


if __name__ == '__main__':
    invalid_species = {'sepal_length': '5.1', 'sepal_width': '3.5',
                       'petal_length': '1.4', 'petal_width': '0.2',
                       'species': "nothing known by this app"}
    rks = TestingKnowSample.from_dict(invalid_species)
    print(rks)















