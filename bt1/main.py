from student_Nha import Nha
from student_Long import Long
from student_Dung import Dung
# Create a list of animals
k64_class = [Nha(),Long(),Dung()]

# Polymorphic behavior
for student in k64_class:
    print(student.speak())