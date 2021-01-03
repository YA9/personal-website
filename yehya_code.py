
class Student:
    def __init__(self, name, etype, institution, skills):
        self.name = name
        self.etype = etype
        self.institution = institution
        self.skills = skills


yalbakri = Student(
    "Yehya Albakri",
    "Full Stack Software Developer",
    "Olin College of Engineering",
    "Python, R, HTML, CSS, C, Java, MATLAB, OCaml")

print('Name: ', yalbakri.name)
print('Engineer type: ', yalbakri.etype)
print('Current institution: ', yalbakri.institution)
print('Skills: ', yalbakri.skills)
