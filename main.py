# Импортируем библиотеку random для случайного выбора атакующего
import random

# Класс для героя
class Hero:
    def __init__(self, name):
        # Инициализация атрибутов героя
        self.name = name  # Имя героя
        self.health = 100  # Начальное здоровье
        self.attack_power = 20  # Сила удара

    def attack(self, other):
        # Метод для атаки другого героя
        other.health -= self.attack_power  # Уменьшаем здоровье противника на значение силы удара
        print(f"{self.name} атаковал {other.name} на {self.attack_power} урона.")

    def is_alive(self):
        # Проверка, жив ли герой (здоровье больше 0)
        return self.health > 0

# Класс для игры
class Game:
    def __init__(self, player_name, computer_name):
        # Инициализация игрока и компьютера
        self.player = Hero(player_name)  # Игрок
        self.computer = Hero(computer_name)  # Компьютер (враг)

    def start(self):
        # Метод запуска игры
        print("Начинаем битву!")
        # Пока оба героя живы, игра продолжается
        while self.player.is_alive() and self.computer.is_alive():
            # Выбираем, кто будет атаковать (игрок или компьютер)
            attacker = random.choice([self.player, self.computer])
            if attacker == self.player:
                # Игрок атакует компьютера
                self.player.attack(self.computer)
            else:
                # Компьютер атакует игрока
                self.computer.attack(self.player)

            # Выводим текущее здоровье обоих героев
            print(f"{self.player.name}: {self.player.health} здоровья")
            print(f"{self.computer.name}: {self.computer.health} здоровья\n")

        # Игра окончена, проверяем, кто победил
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

# Пример запуска игры
game = Game("Игрок", "Компьютер")
game.start()
