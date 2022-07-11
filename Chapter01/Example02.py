from abc import ABC, abstractmethod, ABCMeta


class Duck(ABC):

    @abstractmethod
    def display(self): ...


class FlyableDuck(Duck):

    @abstractmethod
    def fly(self): ...


class QuackableDuck(Duck):

    @abstractmethod
    def quack(self): ...


class MallardDuck(Duck):

    def display(self): ...


class RedHeadDuck(Duck):

    def display(self): ...


# TODO:  고무 오리는 날지 못한다 !
class RubberDuck(QuackableDuck):

    def display(self): ...
