class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classrooms(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject] = teacher

    def student_admission(self,student):
        classname = student.classroom.name 
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_GPA(grade):
        grade_con = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_con[grade]
    
    @staticmethod
    def GPA_to_grade(GPA):
        if GPA >= 4.50 and GPA <= 5.00:
            return 'A+'
        elif GPA >= 3.50 and GPA < 4.50:
            return 'A'
        elif GPA >= 3.00 and GPA < 3.50:
            return 'A-'
        elif GPA >= 2.50 and GPA < 3.00:
            return 'B'
        elif GPA >= 2.00 and GPA < 2.50:
            return 'C'
        elif GPA >= 1.00 and GPA < 2.00:
            return 'D'
        else:
            return 'F'
        
    def __repr__(self):
        # All classrooms
        # All subjects
        subject = ''
        for key,value in self.classrooms.items(): # we'll visit every classroom
            subject += f"{key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)

        # All students
        print("All Students")
        result = ''
        for key,value in self.classrooms.items(): # we'll visit every classroom
            result += f"{key.upper()} Classroom Students\n"
            for student in value.students:
                result += f"{student.name}\n"
            print(result)
        # All teachers
        # All student results
        print("Student Results")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.final_grade())
        return ''

