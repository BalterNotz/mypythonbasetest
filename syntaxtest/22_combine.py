# 组合

class Fish:
    pass


class Turtle:
    pass


class Pool:
    def __init__(self):
        self.fish = Fish()
        self.turtle = Turtle()


p = Pool()
print(p.turtle, p.fish)
