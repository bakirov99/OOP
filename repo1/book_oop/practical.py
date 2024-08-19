from model_ import Domain


if __name__ == '__main__':
    species = Domain({"Iris-setosa", 'Iris-versicolour', 'Iris-virginica'})
    print(species.validate("Iris-versicolour"))
    print(species.validate('Odobenidae'))













