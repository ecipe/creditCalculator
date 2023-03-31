x = [0]
y = [0]
k = 0
while True:
    n = int(input('작업을 선택하세요.\n1. 입력\n2. 계산\n'))
    if(n==1):
        x.append(int(input('\n학점을 입력하세요: \n')))
        abc = input('평점을 입력하세요: \n')
        if(abc == 'A+'):
            sc = 4.5
        elif (abc == 'A'):
            sc = 4.0
        elif (abc == 'B+'):
            sc = 3.5
        elif (abc == 'B'):
            sc = 3.0
        elif (abc == 'C+'):
            sc = 2.5
        elif (abc == 'C'):
            sc = 2.0
        elif (abc == 'D+'):
            sc = 1.5
        elif (abc == 'D+'):
            sc = 1.5
        elif (abc == 'D'):
            sc = 1.0
        else:
            sc = 0.0
        y.append(sc)
        k += 1
        print('입력되었습니다.\n\n')


    if(n==2):
        break

# F 과목 저장돼 있는 순서 골라내기
m=0
arrF = [0]
for i in range(1, k+1):
    if(y[i]==0.0):
        arrF.append(i)
        m+=1
    else: continue

# F 과목 학점도 합친 열람용 전체 학점
sum, sumf = 0, 0
for i in range(1, k+1):
    sum += x[i]

# F 과목 총학점
f=0
for i in range(1, m+1):
    f += x[arrF[i]]

sumf = sum-f # F 과목 학점을 뺀 제출용 학점

# 열람용 GPA
GPA1, GPA, GPAf = 0, 0, 0
for i in range(1, k+1):
    GPA1 += x[i]*y[i]

GPAf = GPA1/sum

# 제출용 GPA
GPA = GPA1/sumf


print(f'\n제출용: {sumf}학점 (GPA: {GPA:.2f})')
print(f'열람용: {sum}학점 (GPA: {GPAf:.2f})')
print('\n프로그램을 종료합니다.')