class Student:
  def __init__(self,name):
    self.name = name

  def show(self):
    print(f"name is {self.name}")


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
    marks is {self.marks}
    ''')
   

