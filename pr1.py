import datetime
import time


class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        self.start_time = datetime.datetime.now()
        return f"Начало '{self.name}' положено. At '{self.start_time}' !"
    
    def pass_quest(self):
        self.end_time = datetime.datetime.now()
        self.completion_time = self.end_time - self.start_time
        return f'Квест "{self.name}" окончен. Время выполнения квеста: {self.completion_time}'
    
    def __str__(self):
        return f'Цель квеста {self.name} - {self.description}.'
        


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal)
print(new_quest.name)
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())

print(new_quest)