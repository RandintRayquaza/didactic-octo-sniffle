class Student:
  def __init__(self,name):
    self.name = name

  def show(self):
    print(f'''
          name is {self.name}
''')


class school(Student):
  def __init__(self,name,grade,section,marks):
    super().__init__(name)
    self.grade = grade
    self.section = section
    self.marks = marks


  def show(self):
    super().show()
    print(f'''
        grade is {self.grade} 
        section is {self.section}
        marks are {self.marks}
        ''')
   
class collage(school):
    def __init__(self,name,grade,section,marks,jee_marks,c_name ,c_location):
      super().__init__(name,grade,section,marks)
      self.jee_marks = jee_marks
      self.c_name = c_name
      self.c_location = c_location

    def show(self):
        super().show()
        print(f''' 
        JEE marks are {self.jee_marks}
        College name is {self.c_name}
        College location is {self.c_location}
        ''')

s1 = collage("Aryan", "12th", "A", 85, 250, "CGC U", " Mohali")
s1.show()
s2 = school("Rahul", "10th", "B", 90)
s2.show()
s3 = Student("Ankit")
s3.show()