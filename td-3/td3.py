from enum import Enum


class Classification(Enum):
    POISSON = 1
    INSECTE = 8
    OISEAUX = 2
    MAMMIFERE = 3
    AMPHIBIEN = 5
    REPTILE = 6
    INVERTEBRE = 7


class Animal:

    def __init__(self, name, classification=None):
        self._classification = classification
        self._name = name

    @property
    def classification(self):
        return self._classification

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Chat(Animal):

    def __init__(self, name, isCute=True):
        super().__init__(name, Classification.MAMMIFERE)
        self._isCute = isCute


