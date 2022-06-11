# 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 학생
# 번호에 해당하는 이름을 순차탐색으로 찾아 돌려주는 함수 작성
# 찾는 학생의 번호가 없다면  ?리턴


def search_name(stu_no, stu_name, num):
    for idx, no in enumerate(stu_no):
        if no == num:
            return stu_name[idx]
    return "?"


if __name__ == "__main__":
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]

    print(search_name(stu_no, stu_name, 39))
    print(search_name(stu_no, stu_name, 67))
    print(search_name(stu_no, stu_name, 190))
