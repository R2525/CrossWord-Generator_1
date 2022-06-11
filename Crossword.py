import numpy as np
import random
import re
import copy

array1 = np.full((100, 100), " ", dtype=str)
array2 = np.full((100, 100), " ")
with open("words.txt") as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
letterList = []
for i in lines:
    if re.search('\W|\d|[A-Z]', i) == None and 4 <= len(i) <= 10:
        letterList.append(i)

# print(letterList)

# 처음 시작 자표와 단어는 정해두고 시작
able = 0
foundAlpha = []
tryednum = 0
p_X = [50]  # 단어 생생할때의 x좌표
p_Y = [50]

# 사용된 단어들
letterList2 = ["qwertyuiopasdfghjklzxcvbnm"]
random_Alha_Num = []  # 랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
random_Alha = []  # 랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist = []  # 알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha = []  # 단어에 사용된 알파벳 갯수 (단어의 길이) ex) abcd -> 4
frontWord = []  # 앞에 몇개의 알파벳이 있는지 ex) 선택된 Alpha : b     aaceb -> 앞에 있는 알파 : 4


# 불필요한 행 열 삭제 함수
def delete_ver_line(array):
    array_ver_result = array
    ver_line_list = []
    middle = 0
    for i in range(0, len(array[0])):
        delete_ver_count = 0
        for x in range(0, len(array)):
            if array[x, i] == " ":
                delete_ver_count += 1
        if delete_ver_count == len(array):
            ver_line_list.append(i)
    for y in ver_line_list:
        y -= middle
        array_ver_result = np.delete(array_ver_result, y, axis=1)
        middle += 1
    return array_ver_result


def delete_hor_line(array):
    array_hor_result = array
    hor_line_list = []
    middle = 0
    for i in range(0, len(array)):
        delete_hor_count = 0
        for x in range(0, len(array[0])):
            if array[i, x] == " ":
                delete_hor_count += 1
        if delete_hor_count == len(array[0]):
            hor_line_list.append(i)
    for y in hor_line_list:
        y -= middle
        array_hor_result = np.delete(array_hor_result, y, axis=0)
        middle += 1
    return array_hor_result


def making_test(test_array):
    for x in range(0, len(test_array)):
        for y in range(0, len(test_array[0])):
            if re.search('[a-z]', test_array[x, y]) != None and re.search('\d', test_array[x, y]) == None:
                test_array[x, y] = "■"
            elif test_array[x, y] == "!":
                test_array[x, y] = " "
    return test_array


# 알파벳 안에 있는 랜덤 알파벳 선정
def random_Alphafuc(letter):
    global needcount
    global random_Alha_str
    length = len(letter)
    letterAlpha.append(length)
    countSelect = random.randrange(1, length - 1)
    print("임의 숫자", countSelect)
    random_Alha_Num.append(countSelect)  # 랜덤 숫자
    random_Alha.append(letter[countSelect])  # 랜덤 숫자에 해당하는 알파벳 a
    print("ran_A", random_Alha[-1])
    a = "".join(random_Alha[-1])  # str 형으로 변환
    random_Alha_str = a.strip()
    print("str", random_Alha_str)


# alpha 를 기반으로 한 단어 검색 및 선정
def select_2nd_Word(alpha):
    global needcount
    global selectedWord
    for x in letterList:
        if alpha in x:
            select2ndlist.append(x)

    pickword = random.randrange(0, len(select2ndlist))
    selectedWord = select2ndlist[pickword]
    print("선택된 다음 단어", selectedWord)  # 다음 단어 선택
    print("선택된 단어들", letterList2)
    frontWord.append(selectedWord.find(random_Alha_str))
    print("front", frontWord)
    select2ndlist.clear()


# 수평 단어 검사기(check)
def check_Hor(letter, hor_locate, ver_locate):
    num = 0
    global able
    global blank
    global multi
    global random_Alha_str
    if array2[ver_locate, hor_locate - 1] == '!' or array2[ver_locate, hor_locate - 1] == 'x' or array2[
        ver_locate, hor_locate + len(letter)] == "!" or array2[ver_locate, hor_locate + len(letter)] == "x":
        able = 1
        return 1
    for x in letter:
        if array2[ver_locate, hor_locate] == "!":
            able = 1
            foundAlpha.clear()
            return 1
        elif array2[ver_locate, hor_locate] != "!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            if array2[ver_locate, hor_locate] == "x":
                num += 1
                if num > 2:
                    able = 1
                    foundAlpha.clear()
                    return 1

            hor_locate += 1
            able = 0
    print("found1", foundAlpha)
    b = " ".join(foundAlpha)
    b = b.strip()
    multi = b.split(" ")
    blank = multi.count('')

    blank //= 2
    print("MT", multi)
    print("multi[0]", len(multi[0]))
    print("Blank", blank)
    word_search_calc(multi, blank)


# 수직 단어 검사기(check)
def check_Ver(letter, hor_locate, ver_locate):
    num = 0
    global able
    global blank
    global multi
    global random_Alha_str
    if array2[ver_locate - 1, hor_locate] == '!' or array2[ver_locate - 1, hor_locate] == 'x' or array2[
        ver_locate + len(letter), hor_locate] == "!" or array2[ver_locate + len(letter), hor_locate] == "x":
        able = 1
        return 1
    for x in letter:
        if array2[ver_locate, hor_locate] == "!":
            able = 1
            foundAlpha.clear()
            return 1
        elif array2[ver_locate, hor_locate] != "!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            if array2[ver_locate, hor_locate] == "x":
                num += 1
                if num > 2:
                    able = 1
                    foundAlpha.clear()
                    return 1

            ver_locate += 1
            able = 0
    print("found2", foundAlpha)
    b = " ".join(foundAlpha)
    b = b.strip()
    multi = b.split(" ")
    blank = multi.count('')
    blank //= 2
    print(multi[-1])
    print("MT", multi)
    print("multi[0]", len(multi[0]))
    print("Blank", blank)
    word_search_calc(multi, blank)


def word_search_calc(list_, blank_):
    global word2n
    if len(list_) >= 2:
        print(len(list_))
        word_search(list_[0], list_[-1], blank_)
    elif len(list_) < 2:
        print(list_)
        print(len(list_))
        print("one")
        print(blank_)


def word_search(a, b, c):  # a가 앞에 단어 b가 끝에 단어 c가 a와 b사이에 들어갈 단어수

    b_w_n = "." * c
    f_search_list = re.findall(r'{0}{1}{2}'.format(a, b_w_n, b), " ".join(letterList))
    # print("f_search_list",f_search_list)
    pickword = random.randrange(0, len(f_search_list))
    print(pickword)
    word2n = letterList[pickword]
    print("sdjkasnd--------", word2n)


# 수평 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Hor_change(letter, hor_locate, ver_locate):
    array2[ver_locate, hor_locate - 1] = "!"
    array2[ver_locate, hor_locate + len(letter)] = "!"

    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        hor_locate += 1


# 수직 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Ver_change(letter, hor_locate, ver_locate):
    array2[ver_locate - 1, hor_locate] = "!"
    array2[ver_locate + len(letter), hor_locate] = "!"

    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        ver_locate += 1


def hor_Start():
    global selectedWord
    global random_Alha_str
    global X
    global Y
    global blank
    global multi

    random_Alphafuc(letterList2[-1])

    select_2nd_Word(random_Alha_str)

    X = (p_X[-1] + random_Alha_Num[-1])
    Y = (p_Y[-1] - frontWord[-1])
    check_Ver(selectedWord, X, Y)
    foundAlpha.clear()
    '''if able ==0:

        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)
        Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
        print("_________Succes___________")

    if able ==1:
        print("---------Error---------")
        hor_Start()'''

    print(random_Alha)
    print(selectedWord)
    print(p_X, p_Y)
    print(frontWord)


def ver_Start():
    global selectedWord
    global random_Alha_str
    global X
    global Y
    global blank
    global multi
    global word2n

    random_Alphafuc(letterList2[-1])
    select_2nd_Word(random_Alha_str)

    Y = (p_Y[-1] + random_Alha_Num[-1])
    X = (p_X[-1] - frontWord[-1])
    check_Hor(selectedWord, X, Y)
    foundAlpha.clear()
    '''if able == 0:

        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)
        Hor_change(letterList2[-1], p_X[-1], p_Y[-1])
        print("_________Succes___________")

    if able == 1:
        print("---------Error---------")
        ver_Start()'''

    print(random_Alha)
    print(selectedWord)
    print(p_X, p_Y)  # 좌표
    print(frontWord)


word2n = "abandum"
check_Ver(letterList2[0], p_X[0], p_Y[0])
# 십자풀이 실행
for i in range(4):

    # Hor_change(letterList2[-1], p_X[-1], p_Y[-1])
    hor_Start()
    if able == 0:
        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)
        Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
        print("_________Succes___________")

    if able == 1:
        print("---------Error---------")
        hor_Start()
    # Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
    ver_Start()
    if able == 0:
        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)
        Hor_change(letterList2[-1], p_X[-1], p_Y[-1])
        print("_________Succes___________")

    if able == 1:
        print("---------Error---------")
        ver_Start()

del letterList2[0]
delete_ver_result = delete_ver_line(array1)
delete_hor_result = delete_hor_line(array1)

# 불필요한 행 열 둘 다 삭제
result = delete_hor_line(delete_ver_result)
print(result)

print(letterList2)  # 사용된 단어

test_array = copy.deepcopy(result)
display_test = making_test(test_array)

print(display_test)