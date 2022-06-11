# 동명이인 찾기
# ["Tom","Jerry","Mike","Tom"]

# 딕셔너리
# key:value
# {"Tom":1, "Jerry":2}


# 중복된 이름을 set() 구조에 추가한 후 리턴
def dup_name(list1):

    name_dict = {}

    # 반복문 - 이름이 등장한 횟수를 딕셔너리로 만듦
    for name in list1:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    #print(name_dict) # {'Tom':2, 'Jerry':1, 'mike':1}
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)


if __name__ == "__main__":
    list1 = ["Tom", "Jerry", "Mike", "Tom"]
    print(dup_name(list1))
