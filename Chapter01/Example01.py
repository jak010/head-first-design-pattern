from abc import ABC, abstractmethod


class Duck(ABC):

    @abstractmethod
    def quack(self): ...

    @abstractmethod
    def swim(self): ...

    @abstractmethod
    def display(self): ...


class MallardDuck(Duck):

    def display(self): ...


class RedHeadDuck(Duck):

    def display(self): ...


# TODO:  고무 오리는 날지 못한다 !
class RubberDuck(Duck):

    def display(self): ...
