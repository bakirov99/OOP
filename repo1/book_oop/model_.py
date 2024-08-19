import datetime
from typing import cast, Set, Iterable
from enum import Enum


class Species(Enum):
    Setosa = "Iris-setosa"
    Versicolour = 'Iris-versicolour'
    Virginica = 'Iris-virginica'


class Hyperparameter:
    pass


class Domain(Set[str]):
    def validate(self, value: str) -> str:
        if value in self:
            return value
        raise ValueError(f'invalid {value!r}')


class InvalidSampleError(ValueError):
    """Source data file has invalid data representation"""


class OutlierError(ValueError):
    """Value lies outside the excepted range."""


class Sample:
    def __init__(self, sepal_length: float, sepal_width: float,
                 petal_length: float, petal_width: float):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width


class KnowSample(Sample):

    def __init__(self, species: str, sepal_length: float, sepal_width: float,
                 petal_length: float, petal_width: float) -> None:
        super().__init__(sepal_length=sepal_length, sepal_width=sepal_width,
                         petal_width=petal_width, petal_length=petal_length)
        self.species = species

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "KnowSample":
        species = Domain()
        try:
            return cls(species=species.validate(row['species']), sepal_length=float(row['sepal_length']),
                       sepal_width=float(row['sepal_width']), petal_length=float(row['petal_length']),
                       petal_width=float(row['petal_length']), )
        except ValueError as ex:
            raise InvalidSampleError(f"invalid {row!r}")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.sepal_length=}, {self.sepal_width=}, {self.petal_length=}, "
                f"{self.petal_width=}, species={self.species!r},")


class TrainingKnowSample(KnowSample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "TrainingKnowSample":
        return cast(TrainingKnowSample, super().from_dict(row))


class TestingKnowSample(KnowSample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "TestingKnowSample":
        return cast(TestingKnowSample, super().from_dict(row))


class TrainingData:

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded = datetime.datetime
        self.tested: datetime.datetime
        self.training: list[TrainingKnowSample] = []
        self.testing: list[TestingKnowSample] = []
        self.tuning: list[Hyperparameter] = []

    def load(self, raw_data_iter: Iterable[dict[str, str]]) -> None:
        bad_count = 0
        for n, row in enumerate(raw_data_iter):
            try:
                if n % 5 == 0:
                    test = TestingKnowSample.from_dict(row)
                    self.testing.append(test)
                else:
                    train = TrainingKnowSample.from_dict(row)
                    self.training.append(train)
            except InvalidSampleError as ex:
                print(f"Row {n+1}: {ex}")
                bad_count += 1
        if bad_count != 0:
            print(f"{bad_count} invalid rows")
            return
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)


if __name__ == '__main__':
    row = {"sepal_length": '5.1', "sepal_width": '3.5',
           "petal_length": '1.4', "petal_width": '0.2',
           "species": "Iris-setosa"}
