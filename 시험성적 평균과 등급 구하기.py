국어, 영어, 수학 = input().split()
평균 = round((float(국어) + float(영어) + float(수학)) / 3, 2) 
if 평균 >= 90:
    등급 = 'A'
elif 90 > 평균 >= 80:
    등급 = 'B'
elif 80 > 평균 >= 70:
    등급 = 'C'
elif 70 > 평균 >= 60:
    등급 = 'D'
else:
    등급 = 'F'
print('%.2f'% 평균, 등급)
