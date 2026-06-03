#creaate a resume builder using multilevel inheritance 
#craeet a class resuem 10th to store personla details in 10Th academic details
#create a class resume 12th that inherits resume 10th to store 12th academic details
#create a class resume collage that inherits resume 12th to store collage details  like degree acadmic

#use construcotr to initilsie all data 
#use methods to display resume at each level of inheritance

#create objcets for a 12th pass  studnet and a degree studnet and display their resume details


class Resume10th:
    def __init__(self,name,age, marks_10th , school_name ,board):
        self.name = name
        self.age = age
        self.marks_10th = marks_10th
        self.school_name = school_name
        self.board = board
    def show_10th(self):
        print(f'''
        Name: {self.name}
        Age: {self.age}
        Marks in 10th: {self.marks_10th}
        School Name: {self.school_name}
        Board: {self.board}
        ''')
class Resume12th(Resume10th):
    def __init__(self, name, age, marks_10th, school_name, board, marks_12th, stream):
        super().__init__(name, age, marks_10th, school_name, board)
        self.marks_12th = marks_12th
        self.stream = stream
    def show_12th(self):
        print(f'''
        Name: {self.name}
        Age: {self.age}
        Marks in 12th: {self.marks_12th}
        Stream: {self.stream}
        ''')


class ResumeCollege(Resume12th):
    def __init__(self, name, age, marks_10th, school_name, board, marks_12th, stream, degree, college_name):
        super().__init__(name, age, marks_10th, school_name, board, marks_12th, stream)
        self.degree = degree
        self.college_name = college_name

    def show_college(self):
        print(f'''
        Name: {self.name}
        Age: {self.age}
        Marks in 10th: {self.marks_10th}
        Marks in 12th: {self.marks_12th}
        Stream: {self.stream}
        Degree: {self.degree}
        College Name: {self.college_name}
        ''')


student_12th = Resume12th("Asha", 17, 89, "ABC School", "CBSE", 92, "Science")
student_degree = ResumeCollege("Ravi", 21, 91, "XYZ School", "State Board", 88, "Commerce", "B.Com", "City College")

student_12th.show_10th()
student_12th.show_12th()
student_degree.show_10th()
student_degree.show_12th()
student_degree.show_college()