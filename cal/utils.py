# from datetime import datetime, timedelta
from calendar import HTMLCalendar
from tasks.models import Task


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, assignee=None):
        self.year = year
        self.month = month
        self.assignee = assignee
        super(Calendar, self).__init__()

    def formatday(self, day, tasks):
        tasks_per_day = tasks.filter(due_date__day=day)
        d = ''
        for task in tasks_per_day:
            if task.is_completed is True:
                d += f'<div style="background-color: lightgreen"><li> {task.name} </li></div>'
            else:
                d += f'<li> {task.name} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, tasks):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, tasks)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        tasks = Task.objects.filter(due_date__year=self.year, due_date__month=self.month)

        cal = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, tasks)}\n'
        return cal

    # tying to get tasks to turn green or whatever when task is completed
    # AHHHHHHHHHHHHHHHHH got that shit to work finally!!!!!!!!!!!!

    # def color_calendar(self):
    #     tasks = Task.objects.all()
    #     for task in tasks:
    #         if task.is_completed is True:
    #             cal = '<div style="background-color: green">{{ task.name }}</div>'
    #     return cal
