import numpy as np
import random
import re

array1 = np.full((18,18)," ", dtype=str)

array2 = np.full((18,18)," ")
'''array1[4,9] = "c"
array1[4,10]= "r"
array1[4,11]= "o"
array1[4,12]= "s"
array1[4,13]= "s"
array1[5,12]= "y"
array1[6,12]= "s"
array1[7,12]= "t"
array1[8,12]= "e"
array1[9,12]= "m"
array2[0,0] = "!"
array2[0,3] ="!"
array2[2,5] ="!"
array1[2,3] ="e"
array1[2,4] ="r"
array1[2,6] ="d"'''

for t in range(18):     #array1 좌표 표시 (편의성 추후 삭제)
    array1[0][t] = t
    array1[t][0] = t
    if t >= 10:
        array1[0][t] = t-10
        array1[t][0] = t-10



#처음 시작 자표와 단어는 정해두고 시작

able =0
foundAlpha =[]
tryednum = 0
p_X =[5]       #단어 생생할때의 x좌표
p_Y =[5]

#모든 단어 리스트 (.txt 파일에서 받아 오는 방식으로 변경 예정)
letterList=["start","aab","bbc","caacd","dabwwde","ewaea","ssdabdnas","sudo","wobasdh","dibdm","hiss","alskasms","insites","dasfsdf","dihwanalsnd","ipnwin,","dlka","nsdnwin","aoihgda","sbdkanf","ohsdfus","dfgbds","gjmsdwudg","vasxn","bczxnfvi","prothjusyh","gfxzhcxznf","mneifhji","osehfznb","cvmzxbcz","vxcyqaf","dyuwe","bqofeop","tjproy","dfgbmcvb","cvnbaks","fgasbeyau","fgsdf","ojibwre","jfgasnn","vkjdaas","vgfyuv","usaf","hlgfadn","hbfadjgv","hiacyo","cckjgl","ksdkjt","yopas","dlkneao","hlmxc","vihea","ljkb","nzdx"]
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
    print("o1")


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
    frontWord.append(letterList2[-1].find(random_Alha_str))
    print("front", frontWord)
    needcount += 1
    print("o2")



#수평 단어 검사기(check)
def WordReader_H(letter, hor_locate, ver_locate):
    existcount = 0
    print("letter",letter)
    print(array2)
    print(array1)
    print("X", p_X)
    print("Y", p_Y)
    global needcount
    if array2[ver_locate,hor_locate-1]=='!'   or array2[ver_locate,hor_locate-1] =='x' or array2[ver_locate, hor_locate +len(letter)] == "!" or array2[ver_locate, hor_locate +len(letter)] == "x":
        able =1
        print("2.1")
        return 1
    for x in letter:
        if  array2[ver_locate,hor_locate] !="!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            print(foundAlpha)
            a = "".join(foundAlpha)
            print(a)
            hor_locate += 1
            able = 0
        elif array2[ver_locate,hor_locate] =="!":
            able =1
            print("x")
            foundAlpha.clear()
            return 0
    print("o3.1")
    needcount += 1
#수직 단어 검사기(check)
def WordReader_V(letter, hor_locate, ver_locate):
    print(array2)
    print(array1)
    print("X",p_X)
    print("Y",p_Y)
    global needcount
    if array2[ver_locate-1,hor_locate]=='!'   or array2[ver_locate-1,hor_locate] =='!' or array2[ver_locate+len(letter), hor_locate ] == "!" or array2[ver_locate+len(letter), hor_locate ] == "x":
        able =1
        print("1.1")
        return 1
    for x in letter:
        if array2[ver_locate,hor_locate] !="!":
            foundAlpha.append(array1[ver_locate, hor_locate])
            print(foundAlpha)
            a = "".join(foundAlpha)
            print(a)
            hor_locate += 1
            able = 0
            print("ss")
        elif array2[ver_locate,hor_locate]=="!":
            able =1
            print("x")
            foundAlpha.clear()
            return 0
    print("o3.2")
    needcount += 1



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



def ckeckRoutine(letter, hor_locate, ver_locate):
    global count
    global needcount
    global selectedWord
    position_Calculator(letter)
    print(needcount)

    Select2ndFunc(random_Alha_str)
    print(needcount)
    if count % 2 ==0:

        X = (p_X[-1] + random_Alha_Num[-1] - 1)
        Y = (p_Y[-1] - frontWord[-1])
        WordReader_H(selectedWord, X, Y)

        print(letter)
    elif count % 2 ==1:
        Y = (p_Y[-1] + random_Alha_Num[-1] - 1)
        X = (p_X[-1] - frontWord[-1])
        WordReader_V(selectedWord, X, Y)


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

#
# WordReader_H("dabwwde",p_X[-1],p_Y[-1])
# ckeckRoutine(letterList2[-1],p_X[-1],p_Y[-1])
#
# WordReader_H("a",1,1)
# count +=1
ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
Hor_change(letterList2[-1],p_X[-1],p_Y[-1])
count+=1
ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
count +=1
ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
Hor_change(letterList2[-1],p_X[-1],p_Y[-1])

count +=1
ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
Ver_change(letterList2[-1], p_X[-1], p_Y[-1])

count += 1
ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
Hor_change(letterList2[-1],p_X[-1],p_Y[-1])

count +=1


'''for i in range(10):
    ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
    print("kdsfnsdfiu",letterList2[-1], p_X[-1], p_Y[-1])
    if count % 2 ==0:
        Hor_change(letterList2[-1],p_X[-1],p_Y[-1])
        needcount = 0
    if count % 2 ==1:
        Ver_change(letterList2[-1],p_X[-1],p_Y[-1])
        needcount = 0
    print("ddkd")


    print("x",p_X,"y",p_Y)
    print(array1)
    #(array2)

print(array1)'''
#ckeckRoutine(letterList2[-1], p_X[-1], p_Y[-1])
