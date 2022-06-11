# 학생 3명의 정보

# 변수
# 학생 1
student_name1 = "Kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [{"gender": "male"}, {"score1": 97}, {"score2": 88}]


# 학생 2
student_name2 = "Park"
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [{"gender": "female"}, {"score1": 87}, {"score2": 96}]


# 학생 3
student_name3 = "Choi"
student_number_3 = 3
student_grade_3 = 3
student_detail_3 = [{"gender": "male"}, {"score1": 66}, {"score2": 78}]

# print("이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s" % (student_name1,student_number_1,student_grade_1,student_detail_1))
# print("이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s" % (student_name2,student_number_2,student_grade_2,student_detail_2))
# print("이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s" % (student_name3,student_number_3,student_grade_3,student_detail_3))


# list
# student_name_list = ["Kim", "park", "Choi"]
# student_numbers_list = [1, 2, 3]
# student_grade_list = [1, 2, 3]
# student_details_list = [
#     {"gender": "male", "score1": 97, "score2": 88},
#     {"gender": "female", "score1": 87, "score2": 96},
#     {"gender": "male", "score1": 66, "score2": 78},
# ]

# del student_name_list[1]
# del student_numbers_list[1]
# del student_grade_list[1]
# del student_details_list[1]

# print(student_name_list)
# print(student_numbers_list)
# print(student_grade_list)
# print(student_details_list)


# 클래스
class Student:  # 괄호는 필수는 아님 , 상속의 개념이 있을때는 필요함
    def __init__(
        self, name, number, grade, details
    ):  # __init__ : 생성자, self => this 와 같은 개념
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    # toString() 과 같은 개념
    def __str__(self):
        return "name : {}, number : {}, grade : {}, details : {}".format(
            self.name, self.number, self.grade, self.details
        )


# 객체 생성
student1 = Student("Kim", 1, 1, {"gender": "male", "score1": 97, "score2": 88})
student2 = Student("Park", 2, 2, {"gender": "female", "score1": 87, "score2": 96})
student3 = Student("Choi", 3, 3, {"gender": "male", "score1": 66, "score2": 78})

print(student1)  # <__main__.Student object at 0x00000227A24DBFD0>
print(student2)
print(student3)
