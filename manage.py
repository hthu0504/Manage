from Classroom import Classes
from Person import Student, Teacher

class manage:
    def __init__(self):
        self.teacher = []
        self.student = []

    def Check(self, lst, namea, birtha):
        for i in range(len(lst)):
            if lst[i].name == namea and lst[i].birth == birtha:
                return i 
        return -1  # không tồn tại tên đó trong lớp 

    def AddStudent(self, name, lop, birth):
        if self.Check(self.student, name, birth) == -1:
            self.student.append(Student(name, lop, birth))
        else:
            print("Học sinh đã tồn tại")

    def AddDetailstoStudent(self, name, birth, details):
        index = self.Check(self.student, name, birth)
        if index != -1:
            self.student[index].details = details  # thêm thông tin cho học sinh
        else:
            print("Không tìm thấy học sinh")

    def RemoveStudent(self, name, birth):
        index = self.Check(self.student, name, birth)
        if index != -1:  # tồn tại học sinh
            self.student.pop(index)
        else:
            print('Không có học sinh này trong lớp')

    def AddTeacher(self, name, subj, birth):
        if self.Check(self.teacher, name, birth) == -1:
            self.teacher.append(Teacher(name, subj, birth))
        else:
            print("Giáo viên đã tồn tại")

    def AddDetailstoTeacher(self, name, birth, details):
        index = self.Check(self.teacher, name, birth)
        if index != -1:
            self.teacher[index].details = details  # thêm thông tin cho giáo viên
        else:
            print("Không tìm thấy giáo viên")

    def RemoveTeacher(self, name, birth):
        index = self.Check(self.teacher, name, birth)
        if index != -1:
            self.teacher.pop(index)
        else:
            print('Không có giáo viên này trong lớp')