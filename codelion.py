"""
import random
import time

for i in range(1,5,2):
    print(random.choice(["된장국","라면","부대찌개"]))
    break

while True:
    print(random.choice(["된장국","라면","부대찌개"]))
    time.sleep(1)
    break

dinner = random.choice(["된장국","라면","부대찌개"])
print(dinner)

### dictionary

information={"이름":"김태진","나이":"22","직업":"학생"}

print(information.get("직업"))
information["취미"] = "독서"
information["사는 곳"] = "수원"
del information["직업"]

print(information)
print(len(information))
information.clear()
print(information)


#list : index로 값 받기

foods = ["피자","버거","빵"]
print(foods[0])
print(foods[-2])
foods.append("김밥")
del foods[1]
print(foods)


information={"이름":"김태진","나이":"22","직업":"학생"}

for x,y in information.items():
    print(x)
    print(y)


foods = ["된장찌개", "김칫국", "부대찌개","김칫국"]
foods_set1 = set(foods)
print(foods)
print(foods_set1)

menu1 = {"된장찌개","북어국","김칫국"}
menu2 = {"된장찌개","감자탕","추어국"}
합집합 = menu1 | menu2
교집합 = menu1 & menu2
차집합 = menu1 - menu2

import random
menu = ['짜장면','탕수육','팔보채']
food = random.choice(menu)
if food == '짜장면':
    print('곱빼기주세요')
else:
    print('그냥주세요')

lunch = ['돈까스','김밥','냉면','쫄면']

while True:
    print(lunch)
    food=input("먹고싶은 음식을 입력해주세요 :")
    if (food=="q"):
        break
    else:
        lunch.append(food)

set_lunch = set(lunch)
while True :
    print(set_lunch)
    food = input("삭제할 음식을 입력해주세요 : ")
    if (food == "q"):
        break
    else:
        set_lunch = set_lunch - set([food])
print(set_lunch,'중에서 선택합니다')

import random
import time
for x in range(5,0,-1):
    print(x)
    time.sleep(1)
print(random.choice(list(set_lunch)))

total_dictionary={}
while True:
    question=input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question]=""

for i in total_dictionary:
    print(i)
    answer=input("답변을 입력해주세요 : ")
    total_dictionary[i]=answer
print(total_dictionary)

total_list=[]
while True:
    question=input("질문을 입력해주세요 :")
    if question=="q":
        break
    else:
        total_list.append({'질문':question,'답변':''})


for i in total_list:
    print(i['질문'])
    answer=input('답변을 입력해주세요 : ')
    if answer=="q":
        break
    else:
        i['답변']=answer
print(total_list)
"""
list={'행복':'정말','그닥':'아니'}
print(dict(list))