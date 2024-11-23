from random import randint


class Cat:
    name = None
    age = 1
    satiety = 40
    happiness = 40
    is_sleeping = False
    avatar = 'img/1_70.jpg'

    @classmethod
    def _feeding(cls):
        if not cls.is_sleeping:
            cls.satiety += 15
            cls.happiness += 5
        if cls.satiety > 100:
            cls.happiness -= 30

    @classmethod
    def _playing(cls):
        if cls.is_sleeping:
            cls.is_sleeping = False
            cls.happiness -= 5
        else:
            cls.happiness += 15
            cls.satiety -= 10
            if randint(1,3) == 1:
                cls.happiness = 0


    @classmethod
    def _sleeping(cls):
        cls.is_sleeping = True

    @classmethod
    def action(cls, name_action):
        if name_action == 'feeding':
            cls._feeding()
        elif name_action == 'playing':
            cls._playing()
        elif name_action == 'sleeping':
            cls._sleeping()

        if cls.satiety > 100:
            cls.satiety = 100
        if cls.happiness > 100:
            cls.happiness = 100

        if cls.satiety < 0:
            cls.satiety = 0
        if cls.happiness < 0:
            cls.happiness = 0

        if cls.happiness >= 70:
            cls.avatar = 'img/70_100.jpeg'
        elif cls.happiness > 1:
            cls.avatar = 'img/1_70.jpg'
        else:
            cls.avatar = 'img/0.webp'




