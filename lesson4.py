from datetime import datetime

class Logger:
    def log_action(self, action):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] LOG: {action}")


class User:
    def __init__(self, username, email):
        self.username = username
        self.__email = email
        self.created_at = datetime.now()

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if self.is_email_valid(new_email):
            self.__email = new_email
        else:
            print("❌ Invalid Email format")

    def get_info(self):
        return f"User: {self.username}, Email: {self.get_email()}"

    @staticmethod
    def is_email_valid(email):
        return "@" in email and "." in email

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['email'])

    def __str__(self):
        return f"{self.username} ({self.get_email()})"


class Employee(User):
    def __init__(self, username, email, position, salary):
        super().__init__(username, email)
        self.position = position
        self.__salary = salary 

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("❌ Salary must be positive")

    def get_info(self):
        return f"{super().get_info()}, Position: {self.position}, Salary: {self.__salary}"


class Manager(Employee, Logger):
    def __init__(self, username, email, position, salary):
        Employee.__init__(self, username, email, position, salary)
        self.team = []

    def add_to_team(self, employee):
        if isinstance(employee, Employee):
            self.team.append(employee)
            self.log_action(f"{employee.username} добавлен в команду менеджера {self.username}")
        else:
            print("❌ Можно добавлять только сотрудников")

    def show_team(self):
        print(f"👥 Команда менеджера {self.username}:")
        for emp in self.team:
            print(f" - {emp.username} ({emp.position})")


class Project:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.participants = []
        self.tasks = []

    def add_participants(self, employee):
        if isinstance(employee, Employee):
            self.participants.append(employee)
            print(f"✅ {employee.username} добавлен в проект {self.name}")
        else:
            print("❌ Error: можно добавлять только сотрудников")

    def add_tasks(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            print(f"📌 Добавлена задача: {task.title}")
        else:
            print("❌ Error: объект не является задачей")

    def show_tasks(self):
        print(f"📋 Задачи проекта: {self.name}")
        for task in self.tasks:
            print(f" - {task.title} [Статус: {task.status}]")


class Task:
    def __init__(self, title, description, assigned_to):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = "Not Started"

    def start_task(self):
        self.status = "In Progress"

    def complete_task(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} - {self.status}"


manager = Manager("John", "john@gmail.com", "Team Lead", 7000)
dev1 = Employee("alice", "alice@gmail.com", "Back-End Dev", 3500)
dev2 = Employee("bob", "bob@gmail.com", "Front-End Dev", 4000)

manager.add_to_team(dev2)
manager.add_to_team(dev1)
manager.show_team()

project = Project("Geeks Coin", manager)
project.add_participants(dev1)
project.add_participants(dev2)

task1 = Task("Create New API", "Dev Back-End API", dev1)
task2 = Task("Home Page", "Front-End Dev", dev2)
project.add_tasks(task1)
project.add_tasks(task2)
project.show_tasks()

task1.start_task()
task1.complete_task()

print("\n✅ После обновления статуса задач:")
project.show_tasks()
