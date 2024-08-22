class Student:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

n=int(input())
students=[]
for _ in range(n):
    input_tuple = tuple(input().split())
    name,kor,eng,math=input_tuple[0],int(input_tuple[1]),int(input_tuple[2]),int(input_tuple[3])
    students.append(Student(name,kor,eng,math))

students.sort(key=lambda x:x.kor+x.eng+x.math)

for student in students:
    print(student.name,student.kor,student.eng,student.math)