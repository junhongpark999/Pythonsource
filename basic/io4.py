# json 읽고 쓰기

import json

# data = (
#     '{"id": "hong","language": "python","edition": "3.9","author": "Guido van Rossum"}'
# )

# # 문자열 형태를 json 로드
# json_data = json.loads(data)

# print(
#     type(json_data),
#     json_data["id"],
#     json_data["language"],
#     json_data["edition"],
#     json_data["author"],
# )


data = (
    '{"id": "hong","language": "python","edition": "3.9","author": "Guido van Rossum"}'
)

# json_data = json.dumps(data)

# print(type(json_data))
# print(json_data)


# key, value
# data["language"] = ["java", "script"]
# with open("data/test1.json", "w") as f:
#     json.dump(data, f, indent=2)


# with open("data/test1.json","r") as f:
#     json_data = json.load(f)

#     print(json_data)

with open("data/users.json", "r") as f:
    json_data = json.load(f)

    # print(json_data)
    for person in json_data:
        # print(person)
        for k, v in person.items():
            print(k, v)
