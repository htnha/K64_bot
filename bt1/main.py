from student_Nha import Nha
from student_Long import Long
from student_Ekalat import Ekalat
from student_Dung import Dung
from student_Tham import Tham
from student_Linh import Linh
# Create a list of animals
k64_class = [Nha(),Long(),Dung(), Ekalat(), Tham(), Linh()]
for student in k64_class:
    try:
        print(student.speak())
        print(student.address())
    except:
        print("Co loi cho sinh vien:" + student.name())
