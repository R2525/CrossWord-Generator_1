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

#모든 단어 리스트 (.txt 파일에서 받아 오는 방식으로 변경 예정)
#letterList=["start","aab","bbc","caacd","dabwwde","ewaea","ssda","bdnas","sudo","wobasdh","dibdm","hiss","alskasms","insites","dasfsdf","dihwa","nalsnd","ipnwin,","dlka","nsdnwin","aoihgda","sbdkanf","ohsdfus","dfgbds","gjmsdwudg","vasxn","bczxnfvi","prothjusyh","gfxz"",hcxznf","mneifhji","osehfznb","cvmz","xbcz","vxcyqaf","dyuwe","bqofeop","tjproy","dfgbmcvb","cvnbaks","fgasbeyau","fgsdf","ojibwre","jfgasnn","vkjdaas","vgfyuv","usaf","hlgfadn","hbfadjgv","hiacyo","cckjgl","ksdkjt","yopas","dlkneao","hlmxc","vihea","ljkb","nzdx"]
#사용된 단어들
letterList2=["start"]
alphas =[]
random_Alha_Num =[]           #랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
random_Alha = []        #랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist =[]   #알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha =[]     #단어에 사용된 알파벳 갯수 (단어의 길이) ex) abcd -> 4
frontWord=[]        #앞에 몇개의 알파벳이 있는지 ex) 선택된 Alpha : b     aaceb -> 앞에 있는 알파 : 4
count =0
needcount = 0

def not_used():
    #수직 수평 좌표 계산 방법
    p_X.append(p_X[-1] + random_Alha_Num[-1] - 1)
    p_Y.append(p_Y[-1] - frontWord[-1])

    p_Y.append(p_Y[-1] + random_Alha_Num[-1] - 1)
    p_X.append(p_X[-1] - frontWord[-1])


#알파벳 안에 있는 랜덤 알파벳 선정
def position_Calculator(letter):
    global needcount
    global random_Alha_str
    length=len(letter)

    letterAlpha.append(length)
    countSelect = random.randrange(2, length + 1)
    random_Alha_Num.append(countSelect)         #랜덤 숫자
    random_Alha.append(letter[countSelect - 1]) #랜덤 숫자에 해당하는 알파벳 a
    print("ran_A",random_Alha[-1])
    a = "".join(random_Alha[-1])                    #str 형으로 변환
    random_Alha_str = a.strip()
    print("str",random_Alha_str)
    #letterList.remove(letterList2[-1])
     #다음 단어 안에 알파벳 a 위치 찾기
    needcount += 1
    #print("o1")



#alpha 를 기반으로 한 단어 검색 및 선정
def Select2ndFunc(alpha):
    global needcount
    global selectedWord
    for x in letterList:
        if alpha in x:
            select2ndlist.append(x)

    pickword = random.randrange(0, len(select2ndlist))
    selectedWord = select2ndlist[pickword]
    #letterList2.append(select2ndlist[pickword])
    print("선택된 다음 단어", selectedWord)    #다음 단어 선택
    print("선택된 단어들", letterList2)
    frontWord.append(selectedWord.find(random_Alha_str))
    print("front", frontWord)
    needcount += 1
    #print("o2")



#수평 단어 검사기(check)
def WordReader_H(letter, hor_locate, ver_locate):
    num =0
    #print("letter",letter)
    #print(array2)
    #print(array1)
    #print("X", p_X)
    #print("Y", p_Y)
    global needcount
    if array2[ver_locate,hor_locate-1]=='!'   or array2[ver_locate,hor_locate-1] =='x' or array2[ver_locate, hor_locate +len(letter)] == "!" or array2[ver_locate, hor_locate +len(letter)] == "x":
        able =1
        #print("2.1")
        return 1
    for x in letter:
        if  array2[ver_locate,hor_locate] !="!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            if array2[ver_locate,hor_locate] =="x":
                num += 1
            if num > 2:
                able =1
                foundAlpha.clear()
                return 0

            #print(foundAlpha)

            a = "".join(foundAlpha)
            #print(a)
            print("found",foundAlpha)
            hor_locate += 1
            able = 0
        elif array2[ver_locate,hor_locate] =="!":
            able =1
            #print("x")
            foundAlpha.clear()
            return 0
    #print("o3.1")

    needcount += 1
#수직 단어 검사기(check)
def WordReader_V(letter, hor_locate, ver_locate):
    num =0
    #print(array2)
    #print(array1)
    #print("X",p_X)
    #print("Y",p_Y)
    global needcount
    if array2[ver_locate-1,hor_locate]=='!'   or array2[ver_locate-1,hor_locate] =='!' or array2[ver_locate+len(letter), hor_locate ] == "!" or array2[ver_locate+len(letter), hor_locate ] == "x":
        able =1
        #print("1.1")
        return 1
    for x in letter:
        if array2[ver_locate,hor_locate] !="!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            if array2[ver_locate,hor_locate] =="x":
                num += 1
            if num > 2:
                able =1
                foundAlpha.clear()
                return 0

            a = "".join(foundAlpha)
            print("found",foundAlpha)
            print(a)

            hor_locate += 1
            able = 0
            #print("ss")
        elif array2[ver_locate,hor_locate]=="!":
            able =1
            #print("x")
            foundAlpha.clear()
            return 0
    #print("o3.2")

    needcount += 1

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
    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        hor_locate += 1


#수직 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Ver_change(letter , hor_locate, ver_locate):

    array2[ver_locate - 1, hor_locate] = "!"
    array2[ver_locate + len(letter), hor_locate] = "!"
    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        ver_locate += 1



'''def ckeckRoutine(letter, hor_locate, ver_locate):
    global count
    global needcount
    global selectedWord

    if count % 2 ==0:

        X = (p_X[-1] + random_Alha_Num[-1] - 1)
        Y = (p_Y[-1] - frontWord[-1])
        WordReader_H(selectedWord, X, Y)

        print(letter)
    elif count % 2 ==1:
        Y = (p_Y[-1] + random_Alha_Num[-1] - 1)
        X = (p_X[-1] - frontWord[-1])
        WordReader_V(selectedWord, X, Y)

    position_Calculator(letter)
    print(needcount)

    Select2ndFunc(random_Alha_str)
    print(needcount)

    if needcount == 3:
        print("------------------ready---------------------")
        print(letter)
        p_X.append(X)
        p_Y.append(Y)
        letterList2.append(selectedWord)
        count =+1
    else:
        print("----------------not ready--------------------")
        needcount =0
        print(letter)
        ckeckRoutine(selectedWord, X, Y)
    needcount = 0
    print("x", p_X, "y", p_Y)
'''



#
# WordReader_H("dabwwde",p_X[-1],p_Y[-1])
# ckeckRoutine(letterList2[-1],p_X[-1],p_Y[-1])
#
# WordReader_H("a",1,1)
# count +=1

def hStart():
    global selectedWord
    global random_Alha_str
    Hor_change(letterList2[-1],p_X[-1],p_Y[-1])
    position_Calculator(letterList2[-1])
    Select2ndFunc(random_Alha_str)
    X = (p_X[-1] + random_Alha_Num[-1] - 1)
    Y = (p_Y[-1] - frontWord[-1])
    WordReader_H(selectedWord, X, Y)
    if able ==0:
        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)
    if able ==1:
        hStart()
    print(random_Alha)
    print(selectedWord)
    print(p_X,p_Y)
    print(frontWord)
    print(array1)
def vStart():
    global selectedWord
    global random_Alha_str
    Ver_change(letterList2[-1],p_X[-1],p_Y[-1])
    position_Calculator(letterList2[-1])
    Select2ndFunc(random_Alha_str)
    Y = (p_Y[-1] + random_Alha_Num[-1] - 1)
    X = (p_X[-1] - frontWord[-1])
    WordReader_V(selectedWord, X, Y)
    if able == 0:
        letterList2.append(selectedWord)
        p_X.append(X)
        p_Y.append(Y)
    if able == 1:
        vStart()
    print(random_Alha)
    print(selectedWord)
    print(p_X,p_Y)
    print(frontWord)
    print(array1)

for i in range(4):
    hStart()
    vStart()




print(random_Alha)
print(selectedWord)
print(p_X,p_Y)
print(frontWord)
print(array1)


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

delete_ver_result = delete_ver_line(array1)

print(delete_ver_result)

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

delete_hor_result = delete_hor_line(array1)

print(delete_hor_result)

# 행 열 둘 다 삭제
result = delete_hor_line(delete_ver_result)

print(result)




print(letterList2)
del letterList2[-1]