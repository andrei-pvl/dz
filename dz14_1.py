class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name} {self.first_name}. Age: {self.age}. Gender: {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f'{super().__str__()}. Record_book: {self.record_book}'


class GroupException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exc_message(self):
        return self.message


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupException("There can not be more than 10 students!")
        self.group.add(student)

    def delete_student(self, last_name):
        found_student = self.find_student(last_name)
        if found_student is not None:
            self.group.remove(found_student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ", ".join(str(el) for el in self.group)

        return f'Number:{self.number}\n {all_students} '


gr = Group('PD1')
st11 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

for i in range(10):
    st = Student('Male', 30, f'Steve{i}', 'Jobs', 'AN142')
    gr.add_student(st)

try:
    gr.add_student(st11)
except GroupException as err:
    print(err.get_exc_message())
