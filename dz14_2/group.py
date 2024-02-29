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
