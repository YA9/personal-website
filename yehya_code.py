class Student:
    def __init__(self, name, model, institution, skills):
        self.name = name
        self.model = model
        self.institution = institution
        self.skills = skills


yalbakri = Student(
    "Yehya Albakri",
    "Full Stack Software Developer",
    "Olin College of Engineering",
    "Python, R, HTML, CSS, MATLAB, OCaml"
)

print('Name: ', yalbakri.name)
print('Engineer type: ', yalbakri.model)
print('Current institution: ', yalbakri.institution)
print('Skills: ', yalbakri.skills)
