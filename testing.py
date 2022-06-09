

import random
import numpy as np
import re



#임의 단어 리스트
letterList=["start","aab","bbc","caacd","dabwwde","ewaea","ssdabdnas","sudo","wobasdh","dibdm","hiss","alskasms","insites","dasfsdf","dihwanalsnd","ipnwin,","dlka","nsdnwin","aoihgda","sbdkanf","ohsdfus","dfgbds","gjmsdwudg","vasxn","bczxnfvi","prothjusyh","gfxzhcxznf","mneifhji","osehfznb","cvmzxbcz","vxcyqaf","dyuwe","bqofeop","tjproy","dfgbmcvb","cvnbaks","fgasbeyau","fgsdf","ojibwre","jfgasnn","vkjdaas","vgfyuv","usaf","hlgfadn","hbfadjgv","hiacyo","cckjgl","ksdkjt","yopas","dlkneao","hlmxc","vihea","ljkb","nzdx"]
letterList2=["start"]



'''
#랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)
cList =[]
#랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)
c_2List = []
#알파벳에 맞게 지정된 새로운 단어리스트
select2ndlist =[]
ㅁㅁ
'''

""
letters =0
#18x18 배열 생성 내부 " "로 지정(front)
array1 = np.full((20,20)," ", dtype = str)
#18x18 배열 생성 내부 " "로 지정(back)
array2 = np.full((20,20)," ")
#선택된 단어리스트(어떤 단어들이 사용됬는지 확인)
aList = ["aab"]

array1[4,9] = "c"


array1[4,12]= "s"
array1[4,13]= "s"
array2[4,9] = "x"


array2[4,12]= "x"
array2[4,13]= "x"

array2[0,0] = "!"
array2[0,3] ="!"
array2[2,5] ="!"
array1[2,3] ="e"
array1[2,4] ="r"
array1[2,6] ="d"


array1[5,12]= "y"
array1[6,12]= "s"
array1[7,12]= "t"
array1[8,12]= "e"
array1[9,12]= "m"
array2[5,12]= "x"
array2[6,12]= "x"
array2[7,12]= "x"
array2[8,12]= "x"
array2[9,12]= "x"
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

alphas =[]
random_Alha_Num =[]           #랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
random_Alha = []        #랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist =[]   #알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha =[]
frontWord=[]

#수평 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Hor_change(letter,hor_locate,ver_locate):
    w1=0
    w2=1
    global letters
    letters += 1
    array2[ver_locate, hor_locate - 1] = "!"
    array2[ver_locate, hor_locate + len(letter)] = "!"
    for i in letter:
        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        hor_locate += 1
    position_Calculator(letter)



#수직 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Ver_change(letter , hor_locate, ver_locate):
    w1 = 0
    w2 = 1
    global letters
    letters += 1
    array2[ver_locate - 1, hor_locate] = "!"
    array2[ver_locate + len(letter), hor_locate] = "!"
    for i in letter:

        array1[ver_locate, hor_locate] = i
        array2[ver_locate, hor_locate] = "x"
        ver_locate += 1
    position_Calculator(letter)


'''
def Select2ndFunc():
    for x in letterList:
        if random_Alha[-1] in x:
            select2ndlist.append(x)'''





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




'''def WordReader_H(letter, hor_locate, ver_locate):
    existcount = 0
    able =0
    global tryednum

    for x in letter:
        if '!' in array2[ver_locate, hor_locate] or "x" in array2[p_Y[-1], p_X[-1] - 1] or "x" in array2[p_Y[-1], p_X[-1] + len(letter)] or "!" in array2[p_Y[-1], p_X[-1] - 1] or "!" in array2[p_Y[-1], p_X[-1] + len(letter)]:

            # Select2ndFunc()
            #AlphaSelect(letter)
            print("XXXXXXXXXXXXXXXXXXXXXXXX")
            cando.append(1)
            break
        # elif '!' not in array1[ver_locate,hor_locate] :
        else:
            foundAlpha.append(array1[ver_locate, hor_locate])
            a = "".join(foundAlpha[-4:-1])
            b = re.sub(r"\s", "", a)
            existcount = len(b)
            # print("existcount",existcount)
            print("OOOOOOOOOOOOOOOOOOOOOOOOOOO1")
            if existcount >= 3:
                print(existcount, " 3 overed")
                cando.append(1)
                #tryednum += 1
                #AlphaSelect(letter)
                break
            else:
                cando.append(0)
        else:
            cando.append(1)
            #Select2ndFunc()
            AlphaSelect(letter)
            break
        hor_locate += 1
    if able == 1:
        cando.append(1)
    else:
        cando.append(0)

    print("try", tryednum)
    print("head", array1[p_Y[-1], p_X[-1] - 1], "tail", array1[p_Y[-1], p_X[-1] + len(letter)])
    print(p_X[-1], p_Y[-1])
    print("found1", foundAlpha)
    # foundAlpha.clear()'''


'''def WordReader_H(letter, hor_locate, ver_locate):
    existcount = 0
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
    print("o3.1")
    needcount += 1
'''

print(array1)
print(array2)
needcount =0


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
                return 0

            #print(foundAlpha)

            a = "".join(foundAlpha)
            #print(a)
            print(foundAlpha)
            hor_locate += 1
            able = 0
        elif array2[ver_locate,hor_locate] =="!":
            able =1
            #print("x")
            foundAlpha.clear()
            return 0
    #print("o3.1")
    needcount += 1

WordReader_H("sjnds",9,4)
    #foundAlpha.clear()
random_Alha_str =""
count =0
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


    '''if count % 2 == 0 and cando[-1] ==0:
        Hor_change(letterList2[-1], p_X[-1],p_Y[-1])
        print("Hor")
    if count % 2 == 1 and cando[-1] ==0:
        Ver_change(letterList2[-1], p_X[-1],p_Y[-1])f
        print("Ver")'''
    print("count",count)
    print("가능성",cando)

'''
movenext =0
for i in range(10):
    print("count", count)
    print("가능성", cando)
    if count % 2 == 0:      #수평 계산 및 검사
        WordReader_H(letterList2[-1], p_X[-1], p_Y[-1])
        if cando[-1] ==0:
            Hor_change(letterList2[-1], p_X[-1], p_Y[-1])

            p_X.append(p_X[-1] + random_Alha_Num[-1] -1)
            p_Y.append(p_Y[-1] - frontWord[-1])

            movenext ==0
        elif cando[-1] ==1:
            del p_X[-1]
            del p_Y[-1]
            del select2ndlist[-1]
            del [frontWord[-1]]
            count -= 1
            position_Calculator(letterList2[-1])
            if movenext >= 0:
                #del  p_Y[-1]
                #del  p_X[-1]

                movenext += 1
                count -= 1
                print("nextmove", movenext)
                if movenext > 3:
                    count -= 1

    elif count % 2==1:    #수직 계산 및 검사
        WordReader_V(letterList2[-1], p_X[-1], p_Y[-1])
        if cando[-1] == 0:
            Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
            p_Y.append(p_Y[-1] + random_Alha_Num[-1] -1)
            p_X.append(p_X[-1] - frontWord[-1])

            movenext==0
        elif cando[-1] ==1:
            del p_X[-1]
            del p_Y[-1]
            del select2ndlist[-1]
            del [frontWord[-1]]
            count -= 1
            position_Calculator(letterList2[-1])
            if movenext >= 0:
                #del  p_Y[-1]
                #del  p_X[-1]

                movenext += 1
                count -= 1
                print("nextmove", movenext)
                if movenext > 3:
                    count -= 1
    print("xh", p_X)
    print("yh", p_Y)
    print(array1)
    print(array2)
    print(i)
'''


def word_search(a,b,c): #a가 앞에 단어 b가 끝에 단어 c가 a와 b사이에 들어갈 단어수
    b_w_n = "."*c
    f_search_list = re.findall(r'{0}{1}{2}'.format(a,b_w_n,b), "startdwasdbhsjbcdsbhvdssdjksabdha sbhrd dsajnd")
    print(f_search_list)

word_search("s","r",2)