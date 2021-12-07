'''Второе задание'''

class Clothes:
    def __init__(self, param):
        self.param = param

class Coat(Clothes):

     @property
     def consumption(self):
         return round((self.param / 6.5) + 0.5)

class Costume(Clothes):

     @property
     def consumption(self):
         return round((2 * self.param) + 0.3)



coat = Coat(36)
costume = Costume(166)

print(coat.consumption)
print(costume.consumption)


