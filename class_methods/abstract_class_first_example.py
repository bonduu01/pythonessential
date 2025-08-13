import abc


class Blueprint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class Greenfield(Blueprint):
    def hello(self):
        print("Welcome to green field")


gf = Greenfield()
gf.hello()
