from abc import ABC, abstractmethod

class computer(ABC):
    def process(self,app):
        pass

    def run(self,app):
        self.process(app)

class Mobile(computer):
    def process(self,app):
        print(f"Mobile is runing {app}")

class Lpatop(computer):
    def process(self,app):
        print("laptop is running Windows")

samsung = Mobile
samsung.run("Google Chrome")