from abc import ABC, abstractmethod, ABCMeta


# inteface
class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self): ...


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("날고 있다")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("날지 못한다.")


# interface
class QuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self): ...


class Quack(QuackBehavior):

    def quack(self):
        print("꽥")


class Squeak(QuackBehavior):

    def quack(self):
        print("삑")


class MuteQuack(QuackBehavior):

    def quack(self):
        print("조용")


class Duck(ABC):

    def __init__(self, flybehavior: FlyBehavior, quackbehavior: QuackBehavior):
        self.flybehavior: FlyBehavior = flybehavior
        self.quackbehavior: QuackBehavior = quackbehavior

    @abstractmethod
    def displiay(self): ...

    def perform_fly(self):
        self.flybehavior.fly()

    def perform_quack(self):
        self.quackbehavior.quack()

    def swim(self):
        print("모든 오리는 물에 뜹니다.가짜 오리도 뜨죠")

    def setflybehavior(self, flybehavior: FlyBehavior):
        self.flybehavior = flybehavior

    def setquackbehavior(self, quackbehavior: QuackBehavior):
        self.quackbehavior = quackbehavior


class MallardDuck(Duck):

    def __init__(self):
        super().__init__(
            quackbehavior=Quack(),
            flybehavior=FlyWithWings()
        )

    def displiay(self):
        print("저는 물오리입니다.")


class ModelDuck(Duck):

    def __init__(self):
        super().__init__(
            flybehavior=FlyNoWay(),
            quackbehavior=Quack()
        )

    def displiay(self):
        print("저는 모형 오리입니다.")


class FlyRocketPowerd(FlyBehavior):

    def fly(self):
        print("로켓 추진으로 날아갑니다.")


if __name__ == '__main__':
    # mallard_duck = MallardDuck()
    # mallard_duck.perform_fly()
    # mallard_duck.perform_quack()

    duck_model = ModelDuck()
    duck_model.perform_fly()
    duck_model.setflybehavior(FlyRocketPowerd())
    duck_model.perform_fly()
