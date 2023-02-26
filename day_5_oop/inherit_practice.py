"""
inherit：继承
可以扩展已经存在的代码模块（类）
"""
class School(object):   # 新式类，也是基类
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staff = []

    def enroll(self, stu_obj):
        print(f"为学院{stu_obj.name}办理注册手续")
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print(f"为学院{staff_obj.name}雇用了新员工")
        self.staff.append(staff_obj)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print(f"""
        ---- infor of Teacher: {self.name} ----
        Name: {self.name}
        Age: {self.age}
        Sex: {self.sex}
        Salary: {self.salary}
        Couse: {self.course}
        """)
    
    def teach(self):
        print(f"{self.name} is teaching course [{self.course}]")

class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print(f"""
        ---- infor of Teacher: {self.name} ----
        Name: {self.name}
        Age: {self.age}
        Sex: {self.sex}
        ID: {self.stu_id}
        Grade: {self.grade}
        """)

    def pay_tuition(self, amount):
        print(f"{self.name} has paid tuition for ${amount}")

school = School("McMaster University", "Hamilton")

t1 = Teacher("Ming", 38, "M", 2000000, "Linux")
t2 = Teacher("Yang", 34, "F", 1500000, "PythonDevOps")

s1 = Student("Shidi", 10, "F", 1001, "PythonDevOps")
s2 = Student("Christopher", 6, "M", 1002, "Linux")

# t1.tell()
# s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staff)

school.staff[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)