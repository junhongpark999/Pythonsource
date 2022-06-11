frend_info = {
    "Summer": ["John", "Justin", "Mike"],
    "John": ["Summer", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"],
}


def all_friends(g, name):
    # 앞으로 처리 해야 할 사람들을 큐(리스트)에 저장
    queue = []
    # 큐에 추가한 사람들 기록(set)
    end = set()

    # name 을 queue, end 추가
    queue.append(name)
    end.add(name)

    # 반복문 : 큐에 사람이 있을 때까지
    while queue:
        # 큐에서 한 사람씩 꺼내서
        person = queue.pop(0)
        # 꺼낸 이름 출력
        print(person)

    # 반복문 - 꺼낸 이름을 키 값으로 해서 아직 큐에 추기된 적이 없는 사람을
        for p in g[person]:
            if p not in end:
    # 큐에 추가하고 집합에도 추가
                queue.append(p)
                end.add(p)



if __name__ == "__main__":
    all_friends(frend_info, "Summer")
