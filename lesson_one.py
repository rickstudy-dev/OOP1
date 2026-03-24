class Sword:
    def __init__(self, name, blade_lenght, grip, material = 'сталь'):
        self.name = name
        self.blade_lenght = blade_lenght
        self.material = material
        self.grip = grip
        self.strength = 100
        print(f'A new sword {name} created!!!')

    def slashing_blow(self):
        self.strength -= 10
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_lenght}.')
    
    # Метод «Выполнить укол».
    def piercing_strike(self):
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    # Метод «Заточить клинок».
    def sharpen(self):
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.') 

    def __str__(self):
        return (

            f'Меч — «{self.name}». ' 
            f'Выкован из материала {self.material}, '
            f'длина клинка — {self.blade_lenght}, '
            f'прочность — {self.strength}.'
        )  

first_swarm = Sword('Training',  1.5, 'one hand')
print(first_swarm.slashing_blow())
print(first_swarm.sharpen())
print(first_swarm.piercing_strike())
print('---------------------------')
print(first_swarm)
print('----------------------------')
first_swarm.slashing_blow()
print('---------------------------')
print(first_swarm)