h = int(input('請輸入身高:'))
w = int(input('請輸入體重:'))
BMI = w/(h/100)**2
print(BMI)
if 18<= BMI < 23:
    print("正常")
if  BMI >= 23:
    print("過胖")
if  BMI < 18:
    print("過瘦")