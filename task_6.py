class task_board:
    def __init__(self):
        self.solved = [] # Решены
        self.basic = [] # Базовые
        self.finalize = [] # Доработка

    def add_basic(self, name):
        self.basic.append(name)

    def go_solved(self, name):
        if name not in self.basic:
            self.finalize.remove(name)
        else:
            self.basic.remove(name)
        self.solved.append(name)

    def go_finalize(self, name):
        self.solved.remove(name)
        self.finalize.append(name)

    def get_list_basic(self):
        print('Base: ', self.basic)

    def get_list_solved(self):
        print('Finish: ',self.solved)

    def get_list_finalize(self):
        print('Try again: ', self.finalize)


task = task_board()
task.add_basic('Почистить зубы')
task.add_basic('Сделать зарядку')
task.add_basic('Покушать')
task.get_list_basic()
print()
task.go_solved('Почистить зубы')
task.get_list_basic()
task.get_list_solved()
print()
task.go_finalize('Почистить зубы')
task.get_list_basic()
task.get_list_solved()
task.get_list_finalize()

