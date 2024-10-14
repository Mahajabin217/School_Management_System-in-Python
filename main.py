from school import School
from person import Teacher,Student
from subject import Subject
from classroom import Class_Room

school = School ("XYZ", "Dhaka")

# Adding classrooms
one = Class_Room("One")
two = Class_Room("Two")
three = Class_Room("Three")

school.add_classrooms(one)
school.add_classrooms(two)
school.add_classrooms(three)

# Adding Students
a = Student("A",one)
b = Student("B",two)
c = Student("C",three)

school.student_admission(a)
school.student_admission(b)
school.student_admission(c)

#Adding Teachers
sita = Teacher("Sita")
gita = Teacher("Gita")
mita = Teacher("Mita")

# Adding Subjects
bangla = Subject("Bangla",sita)
math = Subject("Math",gita)
english = Subject("English",mita)    

one.add_subjects(bangla)
one.add_subjects(math)
one.add_subjects(english)
two.add_subjects(bangla)
two.add_subjects(math)
two.add_subjects(english)
three.add_subjects(bangla)
three.add_subjects(math)
three.add_subjects(english)

one.take_semester_final_exam()
two.take_semester_final_exam()
three.take_semester_final_exam()

print(school)