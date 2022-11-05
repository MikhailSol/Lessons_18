import string


### Домашнее задание № 1###
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def print(self):
#         print(self.lang)
#         print(self.letters)
#
#     def letters_num(self):
#         len(self.letters)
#
#
# class EngAlphabet(Alphabet):
#     __letters_num = 26
#
#     def __init__(self):
#         super().__init__('En', string.ascii_uppercase)
#
#     def is_en_letter(self, letters):
#         if letters in self.lang:
#             return True
#         else:
#             return False
#
#     def letters_num(self):
#         return EngAlphabet.__letters_num
#
#     @staticmethod
#     def example():
#         print("I'm bead speak English")
#
#
# eng_a = EngAlphabet()
# eng_a.print()
# print(eng_a.letters_num())
# print(eng_a.is_en_letter('F'))
# print(eng_a.is_en_letter('Щ'))
# eng_a.example()

### Домашнее задание № 2 ###
class Human:
    default_name = "Mikhail"
    default_age = 34

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__hause = None

    def info(self):
        print(self.default_name)
        print(self.default_age)
        print(self.__money)
        print(self.__hause)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def earn_money(self, amount):
        self.__money += amount
        print(amount, self.__money)

    def __make_dial(self, hause, cash):
        self.__house = hause
        self.__money = self.__money - cash

    def buy_house(self, dis, home):
        if self.__money >= dis:
            self.__make_dial(hause, cash)

if __name__ == '__main__':
    Human.default_info()

    alexander = Human('Sasha', 27)
    alexander.info()

    alexander.earn_money(5000)
    alexander.earn_money(20000)
    alexander.info()


class Hause:
    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, dis):
        new_dis = self._price * (100 - dis) / 100
        return new_dis


class SmallHause(Hause):
    oject = 40

    def __init__(self, price):
        super().__init__(SmallHause.oject, price)

#
#
# if __name__ == '__main__':
#     Human.default_info()
#
#     alexander = Human('Sasha', 27)
#     alexander.info()
#
#     alexander.earn_money(5000)
#     alexander.earn_money(20000)
#     alexander.info()

### Дошнее задание ###
class Tomato:
    states = {1: 'росток', 2: 'помидор зеленый', 3: 'помидор красный'}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state = self._state + 1
            next_state = self._state
            return next_state


    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush():
    def __init__(self, kolichestvo):
        self.tomatoes = None
        tomatoes = []
        for i in range(0, kolichestvo):
            tomatoes.append(i)

    def grow_all(self):
        for pomidor in self.tomatoes:
            pomidor.grow()

    def all_are_ripe(self):         # не доделано
        for tom_a_to in self.tomatoes:


    def give_away_all(self):             # не доделано


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):         # нет понятия


    def harvest(self):          # нет понятия

    @staticmethod
    def knowledge_base():
        print("Томаты не простые. Сложно реализовать данную задачу. Необходимо понять как работает ООП.")