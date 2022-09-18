from datetime import datetime, timedelta


class TaskStorage:
    def __init__(self):
        # todo получение списка задач из памяти
        self.all_tasks_list = []

    def add_task(self, task: Task):
        self.all_tasks_list.append(task)


class Task:
    def __init__(self, name: str, days_interval: int, steps_amount:int, description=None):
        """
        :param name: Название задачи
        :param days_interval: Срок на выполнение (в днях)
        :param steps_amount: Количество шагов
        :param description: Описание
        """

        self._name = name
        self._days_interval = days_interval

        self._steps_amount = steps_amount
        self._finished_steps = 0

        self._description = description
        self._state = 'progress'
        self._start_date = datetime.now()
        self._end_date = self.start_date + timedelta(days_interval)

        self._progress = self.get_progress()

    def get_progress(self):
        return self._finished_steps // self._steps_amount

