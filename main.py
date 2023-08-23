import random

num = int(input("1~100사이의 숫자를 입력해 주세요."))
while True:
    try:
        computer = random.choice(['가위', '바위', '보'])
    except:
        print("[가위,바위,보]만 입력해주세요.")
        user = input("")
