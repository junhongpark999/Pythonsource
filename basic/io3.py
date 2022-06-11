# csv 파일 입출력
import csv

# with open("data/sample1.csv","r")as f:
#     reader = csv.reader(f)
#     # 헤더명 제거
#     next(reader)

#     print(reader)
#     print(type(reader))
#     print(dir(reader))
#     print()
#     for c in reader:
#         print(c)


# with open("data/sample2.csv","r") as f:
#     reader = csv.reader(f,delimiter="|")

#     for c in reader:
#         print(c)


# # csv ==> dict 형태로 읽어오기
# with open("data/sample1.csv","r") as f:
#     reader = csv.DictReader(f)

#     for c in reader:
#         print(c) # {'번호': '1', '이름': '김정수', '가입일시': '2017-01-19 11:30:00', '나이': '25'}
#         for k,v in c.items():
#             print(k,v)
#         print()


# # sample3 읽기
# with open("data/sample3.csv","r") as f:
#     reader = csv.reader(f)

#     for c in reader:
#         print(c)


# # 1차원 리스트 csv 파일로 저장
# list1 = [1,2,3,4,5] # list1 = list(range(1,6))

# with open("data/sample4.csv","w") as f:
#     wt = csv.writer(f)

#     wt.writerow(list1)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open("data/sample5.csv", "w", newline="") as f:

    wt = csv.writer(f)

    # for row in list1:
    #     wt.writerow(row)
    
    wt.writerows(list1)
