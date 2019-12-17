class GameCharacter:
    # global variable
    speed = 5

    # constructor
    def __init__(self, name, width, height, x_pos, y_pos):
        # fields
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    # methods
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


gameCharacter = GameCharacter("objectGC", 50, 100, 100, 100)
print(gameCharacter.name)
gameCharacter.name = "GameCharacterObject"
print(gameCharacter.name)

print(gameCharacter.x_pos)
print(gameCharacter.y_pos)
gameCharacter.move(50, 25)
print(gameCharacter.x_pos)
print(gameCharacter.y_pos)


class PlayerCharacter(GameCharacter):
    speed = 10

    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        super().move(0, by_y_amount)


playerCharacter = PlayerCharacter("objectPC", 200, 200)
print(playerCharacter.name)
print(playerCharacter.x_pos)
print(playerCharacter.y_pos)
playerCharacter.move(25)
print(playerCharacter.x_pos)
print(playerCharacter.y_pos)
