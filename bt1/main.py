from student_Nha import Nha
from student_Long import Long
from student_Ekalat import Ekalat
# Create a list of animals
k64_class = [Nha(),Long(),]
k64_class = [Nha(),Ekalat(),]

# Polymorphic behavior
for student in k64_class:
    print(student.speak())