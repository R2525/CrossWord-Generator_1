import random
import numpy as np




#임의 단어 리스트
letterList=["aab","bbc","caacd","dabwwde","ewaea","ssdabdnas","sudo","wobasdh","dibdm","hiss","alskasms","insites","dasfsdf","dihwanalsnd","ipnwin,","dlka","nsdnwin","aoihgda","sbdkanf","ohsdfus","dfgbds","gjmsdwudg","vasxn","bczxnfvi","prothjusyh","gfxzhcxznf","mneifhji","osehfznb","cvmzxbcz","vxcyqaf","dyuwe","bqofeop","tjproy","dfgbmcvb","cvnbaks","fgasbeyau","fgsdf","ojibwre","jfgasnn","vkjdaas","vgfyuv","usaf","hlgfadn","hbfadjgv","hiacyo","cckjgl","ksdkjt","yopas","dlkneao","hlmxc","vihea","ljkb","nzdx"]
letterList2=["aab","bbc"]

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
array1 = np.full((18,18)," ", dtype = str)
#18x18 배열 생성 내부 " "로 지정(back)
array2 = np.full((18,18),"  ")
#선택된 단어리스트(어떤 단어들이 사용됬는지 확인)
aList = ["aab"]
for t in range(18):
    array1[0][t] = t
    array1[t][0] = t
    if t >= 10:
        array1[0][t] = t-10
        array1[t][0] = t-10
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

    AlphaSelect(letter)


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

    AlphaSelect(letter)

cando = []
foundAlpha =[]
def WordReader_H(letter,hor_locate,ver_locate):
    for x in letter:
        if '!' in array2[ver_locate,hor_locate]:
            '''array2[ver_locate, hor_locate - 1- len(letter)] = ' '
            array2[ver_locate, hor_locate + len(letter)] = ' '
            array2[ver_locate, hor_locate - 1 - len(letter)] = "@"
            array2[ver_locate, hor_locate + len(letter)] = "@"'''
            Select2ndFunc()
            #AlphaSelect(letter)
            cando.append(1)
            break
        elif '!' not in array1[ver_locate,hor_locate] or "x" not in array2[p_Y,p_X-1] or "x" not in array2[p_Y,p_X+len(letter)]:
            foundAlpha.append(array1[ver_locate,hor_locate])

            cando.append(0)

        else:
            cando.append(1)
            Select2ndFunc()
            #AlphaSelect(letter)

        hor_locate+=1
    print("head", array1[p_Y[-1], p_X[-1] - 1], "tail", array1[p_Y[-1], p_X[-1] + len(letter)])
    print(p_X[-1], p_Y[-1])
    print("found1",foundAlpha)
    foundAlpha.clear()

def WordReader_V(letter,hor_locate,ver_locate):
    #or 'x' in array2[ver_locate - 1 - len(letter), hor_locate]
    for x in letter:
        if '!' in array2[ver_locate,hor_locate]:
            '''array2[ver_locate - len(letter)-1, hor_locate] = ' '
            array2[ver_locate + len(letter), hor_locate] = ' '
            '''
            cando.append(1)
            Select2ndFunc()
            #AlphaSelect(letter)
            break
        elif '!' not in array1[ver_locate,hor_locate] or "x" not in array2[p_Y-1,p_X] or "x" not in array2[p_Y+len(letter),p_X] :
            foundAlpha.append(array1[ver_locate,hor_locate])

            cando.append(0)
        else:
            cando.append(1)
            Select2ndFunc()
            #AlphaSelect(letter)

        ver_locate+=1
    print("head", array1[p_Y[-1] - 1, p_X[-1]], "tail", array1[p_Y[-1] + len(letter), p_X[-1]])
    print(p_X[-1], p_Y[-1])
    print("found2",foundAlpha)
    foundAlpha.clear()

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

cList =[]           #랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
c_2List = []        #랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist =[]   #알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha =[]     #알파벳 단어 갯수를 저장 하는 리스트                    ex) abc =3
def AlphaSelect(letter):#단어에서 랜덤한 알파벳(번수) 지정
    aList.append(letter)
    count=len(letter)
    letterAlpha.append(count)
    countSelect=random.randrange(2,count+1)
    cList.append(countSelect)
    c_2List.append(letter[countSelect-1])
    #print("랜덤한 숫자",countSelect,"단어 알파벳 수",count)
    Select2ndFunc()     #Select2ndFunc 으로 연결
    print("alist 현재까지 사용된 단어들:",aList[-7:-1])
    print("clist숫자 리스트          :" ,cList[-7:-1])
    print("c_2list 알파벳 리스트      :",c_2List)
    #print("단어의 알파벳 갯수",letterAlpha)

frontWord=[]
# 다음 단어 서칭(리스트) 중복단어 서칭 필요
def Select2ndFunc():
    for x in letterList:
        if c_2List[-1] in x:
            select2ndlist.append(x)
    #print("searching Alpha : ",c_2List[-1],"포함된 단어 서칭", select2ndlist)
    picknum = len(select2ndlist)
    #print("찾은 단어 갯수",picknum)
    pickword = random.randrange(0,picknum)
    #print("그중 단어 선택(번수)",pickword)
    selectedWord = select2ndlist[pickword]
    print("선택된 다음 단어",selectedWord)
    letterList2.append(select2ndlist[pickword])
    print("선택된 단어들", letterList2[-7:-1])
    frontWord.append(selectedWord.index(c_2List[-1]))
    #print("지정 알파벳 앞에 있는 알파벳 갯수",frontWord)
    select2ndlist.clear()
    #WordPrinter()   #WordPrinter로 연결

#단어의 좌표 계산 밑
#필요한 요소 [단어 시작 좌표 리스트 ,랜덤 숫자(cList),frontWord[]
nSt =0          #실행 횟수(수직 수평 돌아가면서 실핼)
p_X =[6,6,6,6]       #단어 생생할때의 x좌표
p_Y =[6,6,6,6]         #단어 생생할때의 y좌표

alphaPosition = [],[] #cList 에서의 값을 가져와 짝수 홀수로 나눈다(x, y )
wordPosition = []
#test
counting = 10


movenext =0
#for i in letterList:
for i in range(10):
    if(counting % 2 == 0):
        print("1")
        WordReader_H(letterList2[-1],p_X[-1],p_Y[-1])
        if cando[-1] ==0:
            # Hor_test(letterList2[-1],p_X[-1],p_Y[-1])
            Hor_change(letterList2[-1], p_X[-1], p_Y[-1])
            # array1[p_Y[-1], p_X[-1]] = i -> 단어 시작 좌표 가져올때 사용 가능
            alphaPosition[0].append(cList[-1])
            p_X.append(p_X[-1] + cList[-1] - 1)
            p_Y.append(p_Y[-1] - frontWord[-1])
            letterList.remove(letterList2[-1])
            movenext == 0
        elif cando[-1] ==1:

            if movenext > 0:
                del  p_Y[-1]
                del  p_X[-1]
                movenext += 1
            pass
        print("nextmove", movenext)
        print(letterList2[-2])
        print("xh",p_X)
        print("yh",p_Y)
        #print(alphaPosition)
        counting -= 1
        print(array1)
        #print(array2)


    elif(counting % 2 ==1):
        print("2")
        WordReader_V(letterList2[-1], p_X[-1], p_Y[-1])
        if cando[-1] == 0:
            # Ver_change(i,a,b)
            Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
            # array1[p_Y[-1], p_X[-1]] = i
            alphaPosition[1].append(cList[-1])
            p_Y.append(p_Y[-1] + cList[-1] - 1)
            p_X.append(p_X[-1] - frontWord[-1])
            letterList.remove(letterList2[-1])
            movenext == 0
        elif cando[-1] ==1:
            if movenext > 0:
                del  p_Y[-1]
                del  p_X[-1]
                movenext += 1
            pass
        print("nextmove", movenext)
        print(letterList2[-2])
        print("xv",p_X)
        print("yv",p_Y)
        #print(alphaPosition)
        counting -= 1
        print(array1)
        #print(array2)

delete_ver_result = delete_ver_line(array2)
delete_hor_result = delete_hor_line(array2)

# 행 열 둘 다 삭제
result = delete_hor_line(delete_ver_result)
print(result)

'''delete_ver_result = delete_ver_line(array1)
delete_hor_result = delete_hor_line(array1)

# 행 열 둘 다 삭제
result = delete_hor_line(delete_ver_result)'''


print("단어들aList",aList)
print("랜덤 숫자cList",cList)
print("랜덤 알파벳c_2List",c_2List)
print(letters)

#선정한 숫자에 해당하는 알파벳을 추출
#추출한 알파벳이 포함된 단어 추출 및 랜덤 선정
#letter에 반환
