# 짝짓기
# ["Tom","Jerry","Mike"]
# Tom - Jerry, Tom - Mike, Jerry - Mike

def name_matching(list1):
    size = len(list1)
    for i in range(size-1):
        for j in range(i+1, size):
            print(list1[i],"-",list1[j])


if __name__=="__main__":
    list1 = ["Tom", "Jerry", "Mike"]
    name_matching(list1)