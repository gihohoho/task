import random

random_number = random.randint(1, 100)
# print(random_number)

count = 0
num = int(input("1~100사이의 숫자를 입력해 주세요."))

while True:
    try:
        if 1 > num or num > 100:
            print(f'{num}은 1~100사이의 숫자가 아닙니다. 다시 입력해 주세요.')
            num = int(input(""))

        elif num < random_number:
            print(f'{num}보다 큽니다. 다시 입력해 주세요.')
            num = int(input(""))
            count = count+1

        elif num > random_number:
            print(f'{num}보다 작습니다. 다시 입력해 주세요.')
            num = int(input(""))
            count = count+1

        elif num == random_number:
            count = count+1
            print(f'정답입니다. 총 {count}번 시도했습니다.')
            Continue = str(input("계속하시겠습니까? [YES] [NO]"))
            if Continue == "YES":
                random_number = random.randint(1, 100)
                num = int(input("1~100사이의 숫자를 입력해 주세요."))
                count = 0
            elif Continue == "NO":
                break

    except ValueError:
        print("알맞은 숫자를 입력하세요.")
        num = int(input(""))

    except:
        print("알맞은 숫자를 입력하세요.")
        num = int(input(""))
