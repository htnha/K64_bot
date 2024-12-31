from student_Nha import Nha
from student_Long import Long
# Create a list of animals
k64_class = [Nha(),Long(),]

# Polymorphic behavior
for student in k64_class:
    print(student.speak())