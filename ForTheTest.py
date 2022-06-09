import numpy as np
import random
import re

array1 = np.full((18,18)," ", dtype=str)
array1[4,9] = "c"
array1[4,10]= "r"
array1[4,11]= "o"
array1[4,12]= "s"
array1[4,13]= "s"
array1[5,12]= "y"
array1[6,12]= "s"
array1[7,12]= "t"
array1[8,12]= "e"
array1[9,12]= "m"
array2 = np.full((18,18)," ")
array2[0,0] = "!"
array2[0,3] ="!"
array2[2,5] ="!"
array1[2,3] ="e"
array1[2,4] ="r"
array1[2,6] ="d"
able =0
foundAlpha =[]
for t in range(18):
    array1[0][t] = t
    array1[t][0] = t
    if t >= 10:
        array1[0][t] = t-10
        array1[t][0] = t-10
cando = [0]
foundAlpha = []
tryednum = 0
p_X =[5]       #단어 생생할때의 x좌표
p_Y =[5]


letterList=["start","aab","bbc","caacd","dabwwde","ewaea","ssdabdnas","sudo","wobasdh","dibdm","hiss","alskasms","insites","dasfsdf","dihwanalsnd","ipnwin,","dlka","nsdnwin","aoihgda","sbdkanf","ohsdfus","dfgbds","gjmsdwudg","vasxn","bczxnfvi","prothjusyh","gfxzhcxznf","mneifhji","osehfznb","cvmzxbcz","vxcyqaf","dyuwe","bqofeop","tjproy","dfgbmcvb","cvnbaks","fgasbeyau","fgsdf","ojibwre","jfgasnn","vkjdaas","vgfyuv","usaf","hlgfadn","hbfadjgv","hiacyo","cckjgl","ksdkjt","yopas","dlkneao","hlmxc","vihea","ljkb","nzdx"]
letterList2=["start"]
alphas =[]
random_Alha_Num =[]           #랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
random_Alha = []        #랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist =[]   #알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha =[]
frontWord=[]

def Select2ndFunc(alpha):
    for x in letterList:
        if alpha in x:
            select2ndlist.append(x)

    pickword = random.randrange(0, len(select2ndlist))
    selectedWord = select2ndlist[pickword]
    letterList2.append(select2ndlist[pickword])
    print("선택된 다음 단어", selectedWord)    #다음 단어 선택
    print("선택된 단어들", letterList2[-7:-1])
    frontWord.append(letterList2[-1].find(random_Alha_str))
    print("front", frontWord)


def position_Calculator(letter):
    global count
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
    Select2ndFunc(random_Alha_str)  # 알파벳 a이 속한 단어 구하기
     #다음 단어 안에 알파벳 a 위치 찾기
    count +=1

def WordReader_H(letter, hor_locate, ver_locate):
    existcount = 0
    print(array2[ver_locate, hor_locate - 1])
    global able
    print(able)
    global tryednum
    if array2[ver_locate,hor_locate-1]=='!'   or array2[ver_locate,hor_locate-1] =='!' or array2[ver_locate, hor_locate +len(letter)] == "!" or array2[ver_locate, hor_locate +len(letter)] == "x":
        able =1
        return 1
    for x in letter:
        if "!" not in array2[ver_locate,hor_locate]:
            foundAlpha.append(array1[ver_locate, hor_locate])
            print(foundAlpha)
            a = "".join(foundAlpha)
            print(a)
            hor_locate += 1
            able = 0
        elif "!" in array2[ver_locate,hor_locate]:
            able =1
            print("x")
            foundAlpha.clear()
            return 0

def WordReader_V(letter, hor_locate, ver_locate):
    global able
    print(able)
    global tryednum
    if array2[ver_locate-1,hor_locate]=='!'   or array2[ver_locate-1,hor_locate] =='!' or array2[ver_locate+len(letter), hor_locate ] == "!" or array2[ver_locate+len(letter), hor_locate ] == "x":
        able =1
        return 1
    for x in letter:
        if "!" not in array2[ver_locate,hor_locate]:
            foundAlpha.append(array1[ver_locate, hor_locate])
            print(foundAlpha)
            a = "".join(foundAlpha)
            print(a)
            hor_locate += 1
            able = 0
        elif "!" in array2[ver_locate,hor_locate]:
            able =1
            print("x")
            foundAlpha.clear()
            return 0



WordReader_H("weje",3,2)



print(able)
print(array2)

print(array1)


class SomeClass:
    def __init__(self, something):
        print("lol")
        print()
    def inter(self):
        print(self)


a = SomeClass("some_fvalue")
a.some_function()

