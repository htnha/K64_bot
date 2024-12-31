from student_Nha import Nha
from student_Long import Long
<<<<<<< HEAD
from student_Dung import Dung
# Create a list of animals
k64_class = [Nha(),Long(),Dung()]
=======
from student_Ekalat import Ekalat
# Create a list of animals
k64_class = [Nha(),Long(),]
k64_class = [Nha(),Ekalat(),]
>>>>>>> 06b426df14b060c40890f69692afbcb356321601

# Polymorphic behavior
for student in k64_class:
    print(student.speak())