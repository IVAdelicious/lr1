import random
import json
# core.py
class Human:
    def __init__(self, name, level, hp, mp, strength, agility, intelligence):
        self.name = name
        self.level = level
        self._hp = hp  # Инкапсуляция: защищённое поле
        self._max_hp = hp
        self._mp = mp  # Инкапсуляция: защищённое поле
        self._max_mp = mp
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.effects = [] # Список текущих эффектов
    def take_damage(self, damage):
        """Уменьшает HP персонажа на величину урона."""
        # Эффекты абсорба урона
        for effect in self.effects:
            if effect.type == "absorb_damage":
                absorb = min(damage, effect.value)
                damage -= absorb
                effect.value -= absorb
                print(f"{self.name} поглотил {absorb} урона эффектом {effect.name}!")
                if effect.value <= 0:
                    self.effects.remove(effect) # Удаляем эффект, если он закончился
                    print(f"Эффект {effect.name} закончился!")
                break  # Только один эффект абсорба срабатывает за раз
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0
        print(f"{self.name} получил {damage} урона. Осталось HP: {self._hp}")
    def attack(self, target):
        """Выполняет атаку на цель."""
        damage = self.strength # Базовая атака зависит от силы
        print(f"{self.name} атакует {target.name}!")
        target.take_damage(damage)
    @property
    def hp(self):
        """Возвращает текущее HP."""
        return self._hp
    @hp.setter
    def hp(self, value):
        """Устанавливает значение HP, не допуская выхода за границы."""
        self._hp = max(0, min(value, self._max_hp))
    @property
    def mp(self):
        """Возвращает текущее MP."""
        return self._mp
    @mp.setter
    def mp(self, value):
        """Устанавливает значение MP, не допуская выхода за границы."""
        self._mp = max(0, min(value, self._max_mp))
    @property
    def is_alive(self):
        """Возвращает True, если персонаж жив."""
        return self._hp > 0
    def add_effect(self, effect):
        """Добавляет эффект к персонажу."""
        self.effects.append(effect)
        print(f"{self.name} получил эффект {effect.name}!")
    def remove_effect(self, effect):
        """Удаляет эффект с персонажа."""
        if effect in self.effects:
            self.effects.remove(effect)
            print(f"Эффект {effect.name} снят с {self.name}!")
        else:
            print(f"Эффект {effect.name} не найден у {self.name}.") # Debug
    def update_effects(self):
        """Обновляет длительность и срабатывание эффектов в конце хода."""
        for effect in list(self.effects):  # Iterate over a copy to allow removal
            if effect.type == "damage_over_time":
                print(f"{self.name} получает {effect.value} урона от {effect.name}!")
                self.take_damage(effect.value)
            effect.duration -= 1
            if effect.duration <= 0:
                self.remove_effect(effect)
    # Магические методы
    def __str__(self):
        return f"{self.name} (Level: {self.level}, HP: {self.hp}, MP: {self.mp})"
    def __repr__(self):
        return f"Human(name='{self.name}', level={self.level}, hp={self.hp}, mp={self.mp}, strength={self.strength}, agility={self.agility}, intelligence={self.intelligence})"
    def __eq__(self, other):
        if isinstance(other, Human):
            return self.name == other.name and self.level == other.level
        return False
    def __hash__(self):
        return hash((self.name, self.level))
class Warrior(Human):
    def __init__(self, name, level, hp=120, mp=40, strength=15, agility=10, intelligence=5):
        super().__init__(name, level, hp, mp, strength, agility, intelligence)
    def powerful_strike(self, target):
        """Наносит увеличенный урон, потребляет MP."""
        if self.mp >= 20:
            self.mp -= 20
            damage = self.strength * 2
            print(f"{self.name} использует Мощный Удар на {target.name}!")
            target.take_damage(damage)
        else:
            print(f"{self.name} недостаточно MP для Мощного Удара!")
class Mage(Human):
    def __init__(self, name, level, hp=80, mp=100, strength=5, agility=5, intelligence=15):
        super().__init__(name, level, hp, mp, strength, agility, intelligence)
    def magic_missile(self, target):
        """Наносит магический урон, потребляет MP."""
        if self.mp >= 30:
            self.mp -= 30
            damage = self.intelligence * 2
            print(f"{self.name} использует Магическую Ракету на {target.name}!")
            target.take_damage(damage)
        else:
            print(f"{self.name} недостаточно MP для Магической Ракеты!")
class Healer(Human):
    def __init__(self, name, level, hp=90, mp=120, strength=4, agility=8, intelligence=13):
        super().__init__(name, level, hp, mp, strength, agility, intelligence)
    def healing_touch(self, target):
        """Лечит цель, потребляет MP."""
        if self.mp >= 40:
            self.mp -= 40
            heal_amount = self.intelligence * 2
            target._hp += heal_amount
            if target._hp > target._max_hp:
                 target.hp = target._max_hp
            print(f"{self.name} использует Лечебное Прикосновение на {target.name} и восстанавливает {heal_amount} HP!")
        else:
            print(f"{self.name} недостаточно MP для Лечебного Прикосновения!")
class Boss(Human):
    def __init__(self, name="Босс", level=5, hp=300, mp=100, strength=20, agility=5, intelligence=10):
        super().__init__(name, level, hp, mp, strength, agility, intelligence)
        self.phase = 1
        self.strategy = self.strategy_phase_1
    def take_damage(self, damage):
        """Уменьшает HP босса и меняет фазу при необходимости."""
        super().take_damage(damage)
        if self._hp <= 150 and self.phase == 1:
            self.phase = 2
            self.strategy = self.strategy_phase_2
            print("Босс переходит во вторую фазу!")
        elif self._hp <= 50 and self.phase == 2:
            self.phase = 3
            self.strategy = self.strategy_phase_3
            print("Босс переходит в финальную фазу!")
    def attack(self, target):
        """Босс выполняет атаку, выбирая стратегию в зависимости от фазы."""
        self.strategy(target)
    def strategy_phase_1(self, target):
        """Стратегия для первой фазы: обычная атака."""
        print("Босс использует Обычную Атаку!")
        damage = self.strength
        target.take_damage(damage)
    def strategy_phase_2(self, target):
        """Стратегия для второй фазы: усиленная атака."""
        print("Босс использует Усиленную Атаку!")
        damage = self.strength * 1.5
        target.take_damage(damage)
    def strategy_phase_3(self, target):
        """Стратегия для третьей фазы: самая мощная атака."""
        print("Босс использует Яростный Удар!")
        damage = self.strength * 2
        target.take_damage(damage)
class Effect:
    def __init__(self, name, type, value, duration):
        self.name = name
        self.type = type#"buff", "debuff", "damage_over_time", "absorb_damage"
        self.value = value
        self.duration = duration
    def __str__(self):
        return f"{self.name} ({self.type}, {self.value}, Duration: {self.duration})"
# items.py
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def use(self, target):
        """Применяет эффект предмета на цель (переопределяется в подклассах)."""
        print(f"{self.name} использован на {target.name}.")
class HealingPotion(Item):
    def __init__(self):
        super().__init__("Зелье Лечения", "Восстанавливает HP.")
    def use(self, target):
        super().use(target)
        heal_amount = 50
        target._hp += heal_amount
        if target._hp > target._max_hp:
            target.hp = target._max_hp
        print(f"{target.name} восстанавливает {heal_amount} HP.")
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} добавлен в инвентарь.")
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} удален из инвентаря.")
        else:
            print(f"{item.name} отсутствует в инвентаре.")
    def use_item(self, item, target):
        if item in self.items:
            item.use(target)
            self.remove_item(item)
        else:
            print(f"{item.name} отсутствует в инвентаре.")
    def __str__(self):
        if not self.items:
            return "Инвентарь пуст."
        else:
            item_names = [item.name for item in self.items]
            return f"Инвентарь: {', '.join(item_names)}"
class Battle:
    def __init__(self, party, boss, seed=None):
        self.party = party
        self.boss = boss
        self.turn = 1
        if seed is not None:
            random.seed(seed)#Установка seed для повторяемости
    def start_battle(self):
        """Запускает бой."""
        print("Бой начинается!")
        while all(member.is_alive for member in self.party) and self.boss.is_alive:
            print(f"\n--- Ход {self.turn} ---")
            self.run_turn()
            self.turn += 1
        if all(member.is_alive for member in self.party):
            print("Пати победила!")
        else:
            print("Босс победил!")
    def run_turn(self):
        """Выполняет один ход боя."""
        # 1. Обновляем эффекты для всех персонажей и босса
        for character in self.party + [self.boss]:
            character.update_effects() # Обновляем длительность эффектов и применяем урон/лечение
        # 2. Определяем порядок хода (по ловкости)
        turn_order = sorted(self.party + [self.boss], key=lambda x: x.agility, reverse=True)
        # 3. Каждый персонаж выполняет действие
        for character in turn_order:
            if character.is_alive:
                if character == self.boss:
                    # Босс всегда атакует случайно выбранного живого члена пати
                    available_targets = [member for member in self.party if member.is_alive]
                    if available_targets:
                        target = random.choice(available_targets)
                        character.attack(target)
                else:
                    self.player_turn(character)#Обрабатываем ход игрока
    def player_turn(self, character):
        """Обрабатывает ход игрока."""
        print(f"\nХод {character.name}:")
        print("1. Атаковать")
        print("2. Использовать навык")
        print("3. Использовать предмет")
        print("4. Пропустить ход")
        while True:
            try:
                choice = int(input("Выберите действие: "))
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 4.")
        if choice == 1:
            available_targets = [self.boss]#Пока только босс
            target = available_targets[0]#Берем босса
            character.attack(target)#Обычная атака
        elif choice == 2:
            if isinstance(character, Warrior):
                print("1. Мощный удар")
                while True:
                   try:
                       skill_choice = int(input("Выберите навык: "))
                       break
                   except ValueError:
                       print("Некорректный ввод")
                if skill_choice == 1:
                    available_targets = [self.boss]#Пока только босс
                    target = available_targets[0]#Берем босса
                    character.powerful_strike(target)
            elif isinstance(character, Mage):
                 print("1. Магическая ракета")
                 while True:
                   try:
                       skill_choice = int(input("Выберите навык: "))
                       break
                   except ValueError:
                       print("Некорректный ввод")
                 if skill_choice == 1:
                    available_targets = [self.boss]#Пока только босс
                    target = available_targets[0]#Берем босса
                    character.magic_missile(target)
            elif isinstance(character, Healer):
                print("1. Лечебное прикосновение")
                while True:
                   try:
                       skill_choice = int(input("Выберите навык: "))
                       break
                   except ValueError:
                       print("Некорректный ввод")
                if skill_choice == 1:
                    available_targets = [member for member in self.party if member.is_alive]
                    print("Выберите цель для лечения:")
                    for i, target in enumerate(available_targets):
                        print(f"{i+1}. {target.name}")
                    while True:
                        try:
                            target_index = int(input("Введите номер цели: ")) - 1
                            if 0 <= target_index < len(available_targets):
                                target = available_targets[target_index]
                                break
                            else:
                                print("Некорректный номер цели.")
                        except ValueError:
                            print("Некорректный ввод. Введите номер цели.")
                    character.healing_touch(target)
        elif choice == 3:
            if hasattr(character, 'inventory') and character.inventory.items:
                print(character.inventory)#Выводим инвентарь
                print("Выберите предмет для использования (введите номер):")
                for i, item in enumerate(character.inventory.items):
                    print(f"{i+1}. {item.name}")
                while True:
                    try:
                        item_index = int(input("Введите номер предмета: ")) - 1
                        if 0 <= item_index < len(character.inventory.items):
                            selected_item = character.inventory.items[item_index]
                            break
                        else:
                            print("Некорректный номер предмета.")
                    except ValueError:
                        print("Некорректный ввод. Введите номер предмета.")
                available_targets = [member for member in self.party if member.is_alive]#Лечим союзников
                print("Выберите цель для использования предмета:")
                for i, target in enumerate(available_targets):
                    print(f"{i+1}. {target.name}")
                while True:
                    try:
                        target_index = int(input("Введите номер цели: ")) - 1
                        if 0 <= target_index < len(available_targets):
                            target = available_targets[target_index]
                            break
                        else:
                            print("Некорректный номер цели.")
                    except ValueError:
                        print("Некорректный ввод. Введите номер цели.")
                character.inventory.use_item(selected_item, target)
            else:
                print("У вас нет предметов в инвентаре.")
        elif choice == 4:
            print(f"{character.name} пропускает ход.")
        else:
            print("Некорректный выбор. Потеря хода.")
if __name__ == "__main__":
    warrior = Warrior("Артур", 3)
    mage = Mage("Мерлин", 3)
    healer = Healer("Анна", 3)
    warrior.inventory = Inventory()
    warrior.inventory.add_item(HealingPotion())
    warrior.inventory.add_item(HealingPotion())
    party = [warrior, mage, healer]
    boss = Boss("Дракон", 5)
    battle = Battle(party, boss, seed=42)
    battle.start_battle()
