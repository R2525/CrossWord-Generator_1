import random
import numpy as np

#임의 단어 리스트
letterList=["aab","bbc","ccd","dde","eea","sdnas","sudo","woh","dibdm","hiss","alsksms","insites"]
letterList2=["aab"]

'''
#랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)
cList =[]
#랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)
c_2List = []
#알파벳에 맞게 지정된 새로운 단어리스트
select2ndlist =[]

'''

#18x18 배열 생성 내부 " "로 지정
array1 = np.full((18,18)," ", dtype=str)

#선택된 단어리스트(어떤 단어들이 사용됬는지 확인)
aList = []

#수평 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Hor_change(letter,hor_locate,ver_locate):
    w1=0
    w2=1
    for i in letter:
        y = letter[slice(w1, w2)]
        w1 += 1
        w2 += 1
        array1[ver_locate, hor_locate] = y
        hor_locate += 1

    AlphaSelect(letter)



#수직 단어 생성(변경) [들어갈 단어, x자표, y자표]
def Ver_change(letter , hor_locate, ver_locate):
    w1 = 0
    w2 = 1
    for i in letter:
        y = letter[slice(w1, w2)]
        w1 += 1
        w2 += 1
        array1[ver_locate, hor_locate] = y
        ver_locate += 1

    AlphaSelect(letter)



cList =[]           #랜덤히 단어에서 선정된 숫자 리스트(좌표 계산할때 사용)    ex) word = abc alpha =b cList =[2]
c_2List = []        #랜덤히 단어에서 선정된 알파벳 리스트(단어 검색)          ex) word = abc random = 3 c_2List [r]
select2ndlist =[]   #알파벳에 맞게 지정된 새로운 단어리스트
letterAlpha =[]     #알파벳 단어 갯수를 저장 하는 리스트                    ex) abc =3
def AlphaSelect(letter):#단어에서 랜덤한 알파벳(번수) 지정
    aList.append(letter)
    count=len(letter)
    letterAlpha.append(count)
    countSelect=random.randrange(1,count+1)
    cList.append(countSelect)
    c_2List.append(letter[countSelect-1])
    print("랜덤한 숫자",countSelect,"단어 알파벳 수",count)
    Select2ndFunc()     #Select2ndFunc 으로 연결
    print("alist 현재까지 사용된 단어들:",aList)
    print("clist숫자 리스트          :" ,cList)
    print("c_2list 알파벳 리스트      :",c_2List)
    print("단어의 알파벳 갯수",letterAlpha)



frontWord=[]
# 다음 단어 서칭(리스트) 중복단어 서칭 필요
def Select2ndFunc():
    for x in letterList:
        if c_2List[-1] in x:
            select2ndlist.append(x)

    print("searching Alpha : ",c_2List[-1],"포함된 단어 서칭", select2ndlist)
    picknum = len(select2ndlist)
    #print("찾은 단어 갯수",picknum)
    pickword = random.randrange(0,picknum)
    #print("그중 단어 선택(번수)",pickword)
    selectedWord = select2ndlist[pickword]
    print("선택된 단어",selectedWord)
    letterList2.append(select2ndlist[pickword])
    print("선택된 단어들", letterList2)
    frontWord.append(selectedWord.index(c_2List[-1]))
    print("지정 알파벳 앞에 있는 알파벳 갯수",frontWord)
    select2ndlist.clear()
    #WordPrinter()   #WordPrinter로 연결


'''
def WordPrinter():
    global  nSt
    #수평
    if nSt % 2 == 0:

        #print("수평")
        alphaPosition[0].append(cList[-1])
        #print("x y 좌표 추가",alphaPosition)

        p_X.append(p_X[-1] + alphaPosition[0][-1])
        Hor_change(select2ndlist[-1], p_X[-1], p_Y[-1])

        #print("시작자표 계산기",p_X)
        nSt += 1
    #수직
    else:
        #print("수직")
        alphaPosition[1].append(cList[-1])
        #print("xs", alphaPosition)
        nSt += 1
'''
#단어의 좌표 계산 밑
#필요한 요소 [단어 시작 좌표 리스트 ,랜덤 숫자(cList),frontWord[]
nSt =0          #실행 횟수(수직 수평 돌아가면서 실핼)
p_X =[6]       #단어 생생할때의 x좌표
p_Y =[6]         #단어 생생할때의 y좌표

alphaPosition = [],[] #cList 에서의 값을 가져와 짝수 홀수로 나눈다(x, y )
wordPosition = []
#test
counting = 10



#for i in letterList:
for i in range(10):
    if(counting % 2 == 0):

        Hor_change(letterList2[-1], p_X[-1], p_Y[-1])
        alphaPosition[0].append(cList[-1])
        p_X.append(p_X[-1]+cList[-1]-1)
        p_Y.append(p_Y[-1]-frontWord[-1])

        print(p_X)
        print(p_Y)
        print(alphaPosition)
        counting -= 1
        print(array1)

    elif(counting % 2 ==1):
        #Ver_change(i,a,b)
        Ver_change(letterList2[-1], p_X[-1], p_Y[-1])
        alphaPosition[1].append(cList[-1])
        p_Y.append(p_Y[-1] + cList[-1] - 1)
        p_X.append(p_X[-1] - frontWord[-1])
        print(p_X)
        print(p_Y)
        print(alphaPosition)
        counting -= 1
        print(array1)

def Hor_test(letter,hor_locate,ver_locate):
    w1=0
    w2=1
    for i in letter:
        #if array1.data is " ":

        y = letter[slice(w1, w2)]
        w1 += 1
        w2 += 1
        array1[ver_locate, hor_locate] = y
        hor_locate += 1

    AlphaSelect(letter)

print("단어들aList",aList)
print("랜덤 숫자cList",cList)
print("랜덤 알파벳c_2List",c_2List)

print(array1)

#선정한 숫자에 해당하는 알파벳을 추출
#추출한 알파벳이 포함된 단어 추출 및 랜덤 선정
#letter에 반환

