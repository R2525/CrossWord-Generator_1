import numpy as np
import random
import re

array1 = np.full((100,100)," ", dtype=str)
array2 = np.full((100,100)," ")
with open("words.txt") as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
letterList = []
for i in lines:
    if re.search('\W|\d|[A-Z]', i) == None and 4 <= len(i) <= 10:
        letterList.append(i)

print(letterList)

#처음 시작 자표와 단어는 정해두고 시작
able =0
foundAlpha =[]
tryednum = 0
p_X =[50]       #단어 생생할때의 x좌표
p_Y =[50]

#사용된 단어들
letterList2=["start"]
random_Alha_Num =[]           #랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
random_Alha = []        #랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist =[]   #알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha =[]     #단어에 사용된 알파벳 갯수 (단어의 길이) ex) abcd -> 4
frontWord=[]        #앞에 몇개의 알파벳이 있는지 ex) 선택된 Alpha : b     aaceb -> 앞에 있는 알파 : 4

#알파벳 안에 있는 랜덤 알파벳 선정
def random_Alphafuc(letter):
    global needcount
    global random_Alha_str
    length=len(letter)
    letterAlpha.append(length)
    countSelect = random.randrange(1, length-1 )
    print("임의 숫자",countSelect)
    random_Alha_Num.append(countSelect)         #랜덤 숫자
    random_Alha.append(letter[countSelect]) #랜덤 숫자에 해당하는 알파벳 a
    print("ran_A",random_Alha[-1])
    a = "".join(random_Alha[-1])                    #str 형으로 변환
    random_Alha_str = a.strip()
    print("str",random_Alha_str)

#alpha 를 기반으로 한 단어 검색 및 선정
def select_2nd_Word(alpha):
    global needcount
    global selectedWord
    for x in letterList:
        if alpha in x:
            select2ndlist.append(x)

    pickword = random.randrange(0, len(select2ndlist))
    selectedWord = select2ndlist[pickword]
    print("선택된 다음 단어", selectedWord)    #다음 단어 선택
    print("선택된 단어들", letterList2)
    frontWord.append(selectedWord.find(random_Alha_str))
    print("front", frontWord)
    select2ndlist.clear()

#수평 단어 검사기(check)
def check_Hor(letter, hor_locate, ver_locate):
    num =0
    global able
    if array2[ver_locate,hor_locate-1]=='!'  or array2[ver_locate,hor_locate-1] =='x' or array2[ver_locate, hor_locate +len(letter)] == "!" or array2[ver_locate, hor_locate +len(letter)] == "x":
        able =1
        return 1
    for x in letter:
        if array2[ver_locate,hor_locate] =="!":
            able =1
            foundAlpha.clear()
            return 1
        elif array2[ver_locate,hor_locate] !="!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            if array2[ver_locate,hor_locate] =="x":
                num += 1
                if num > 2:
                    able =1
                    foundAlpha.clear()
                    return 1
            a = "".join(foundAlpha)
            print("found",foundAlpha)
            hor_locate += 1
            able = 0
            return 0

#수직 단어 검사기(check)
def check_Ver(letter, hor_locate, ver_locate):
    num =0
    global able
    if array2[ver_locate-1,hor_locate]=='!'   or array2[ver_locate-1,hor_locate] =='x' or array2[ver_locate+len(letter), hor_locate ] == "!" or array2[ver_locate+len(letter), hor_locate ] == "x":
        able =1
        return 1
    for x in letter:
        if array2[ver_locate,hor_locate] =="!":
            able =1
            foundAlpha.clear()
            return 1
        elif array2[ver_locate,hor_locate] !="!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            if array2[ver_locate,hor_locate] =="x":
                num += 1
                if num > 2:
                    able =1
                    foundAlpha.clear()
                    return 1
            a = "".join(foundAlpha)
            print("found",foundAlpha)
            print(a)
            hor_locate += 1
            able = 0
            return 0


def word_search(a,b,c): #a가 앞에 단어 b가 끝에 단어 c가 a와 b사이에 들어갈 단어수
    b_w_n = "."*c
    f_search_list = re.findall(r'{0}{1}{2}'.format(a,b_w_n,b),  " ".join(letterList))
    global void_n
    void_n = c
    print(f_search_list)

#수평 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Hor_change(letter,hor_locate,ver_locate):
    array2[ver_locate, hor_locate - 1] = "!"
    array2[ver_locate, hor_locate + len(letter)] = "!"
    array1[ver_locate, hor_locate - 1] = "!"
    array1[ver_locate, hor_locate + len(letter)] = "!"
    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        hor_locate += 1

#수직 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Ver_change(letter , hor_locate, ver_locate):
    array2[ver_locate - 1, hor_locate] = "!"
    array2[ver_locate + len(letter), hor_locate] = "!"
    array1[ver_locate - 1, hor_locate] = "!"
    array1[ver_locate + len(letter), hor_locate] = "!"
    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        ver_locate += 1

def hor_Start():
    global selectedWord
    global random_Alha_str

    random_Alphafuc(letterList2[-1])
    select_2nd_Word(random_Alha_str)
    X = (p_X[-1] + random_Alha_Num[-1]  )
    Y = (p_Y[-1] - frontWord[-1])
    check_Hor(selectedWord, X, Y)
    if able ==0:
        letterList2.append(selectedWord)

        p_X.append(X)
        p_Y.append(Y)

    if able ==1:
        print("---------Error---------")
        # del p_X[-1]
        # del p_Y[-1]
        #del random_Alha_Num[-1]
        # del frontWord[-1]
        # del selectedWord[-1]

        hor_Start()
    print(random_Alha)
    print(selectedWord)
    print(p_X,p_Y)
    print(frontWord)
    print(array1)
def ver_Start():
    global selectedWord
    global random_Alha_str

    random_Alphafuc(letterList2[-1])
    select_2nd_Word(random_Alha_str)
    Y = (p_Y[-1] + random_Alha_Num[-1] )
    X = (p_X[-1] - frontWord[-1])
    check_Ver(selectedWord, X, Y)
    if able == 0:

        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)

    if able == 1:
        print("---------Error---------")
        # del p_X[-1]
        # del p_Y[-1]
        #del random_Alha_Num[-1]
        # del frontWord[-1]
        # del selectedWord[-1]

        ver_Start()

    print(random_Alha)
    print(selectedWord)
    print(p_X,p_Y)  #좌표
    print(frontWord)
    print(array1)   #배열

#불필요한 행 열 삭제 함수
def delete_ver_line (array):
    array_ver_result = array
    ver_line_list = []
    middle = 0
    for i in range(0, len(array[0])):
        delete_ver_count = 0
        for x in range(0, len(array)):
            if array[x,i] == " ":
                delete_ver_count += 1
        if delete_ver_count == len(array):
            ver_line_list.append(i)
    for y in ver_line_list:
        y -= middle
        array_ver_result = np.delete(array_ver_result, y, axis=1)
        middle += 1
    return array_ver_result

def delete_hor_line (array):
    array_hor_result = array
    hor_line_list = []
    middle = 0
    for i in range(0, len(array)):
        delete_hor_count = 0
        for x in range(0, len(array[0])):
            if array[i,x] == " ":
                delete_hor_count += 1
        if delete_hor_count == len(array[0]):
            hor_line_list.append(i)
    for y in hor_line_list:
        y -= middle
        array_hor_result = np.delete(array_hor_result, y, axis=0)
        middle += 1
    return array_hor_result

#십자풀이 실행
for i in range(2):
    Hor_change(letterList2[-1], p_X[-1], p_Y[-1])
    hor_Start()
    Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
    ver_Start()
hor_Start()

delete_ver_result = delete_ver_line(array1)
delete_hor_result = delete_hor_line(array1)

# 불필요한 행 열 둘 다 삭제
result = delete_hor_line(delete_ver_result)
print(result)
del letterList2[-1] #사용되지 않는 마지막 단어 삭제
del letterList2[-1] #사용되지 않는 마지막 단어 삭제

print(letterList2) #사용된 단어
