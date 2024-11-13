class Person:

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    def name(self):
        return self._name
    
    def age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s的%s正在玩飞行棋.' % (self._age,self._name))
        else:
            print('%s的%s正在玩斗地主.' % (self._age,self._name))

def main():
    person = Person('王大锤', 12)
    person.play()
    person.set_age(22)
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute

if __name__ == '__main__':
    main()
