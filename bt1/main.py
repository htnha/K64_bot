from student_Nha import Nha
from student_Long import Long
from student_Ekalat import Ekalat
from student_Dung import Dung
from student_Tham import Tham
from student_Phong import Phong
# Create a list of animals
k64_class = [Nha(),Long(),Dung(), Ekalat(), Tham(), Phong()]
for student in k64_class:
    print(student.speak())
