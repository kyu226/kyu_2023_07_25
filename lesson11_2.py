import random
def getscore():
    score=[]
    for i in range(5):
        score.append(random.randint(50,100))
    return score
def get_name(nums:int)->list:
    with open('names.txt',encoding='utf-8',newline='') as file:
        name_str=file.read()
        all_names_list=name_str.split(sep="\n")
        names_list=random.choices(all_names_list,k=nums)#取出一定數量姓名
    return names_list

nums_int=int(input("請輸入學生數:"))
#取得nums個姓名
names_list=get_name(nums_int)
students=[]
for i in range(nums_int):
    scores=getscore()
    new_list=[names_list[i]]+scores
    students.append(new_list)

print(students)

