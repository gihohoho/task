import random

user = input("가위 바위 보 !!! (입력해주세요.)")
count_win = 0
count_lose = 0
count_same = 0

while True:
    try:
        # computer = random.choice(['가위', '바위', '보'])
        computer = '가위'

        # 무승부
        if user == computer:
            print(f'컴퓨터는 {computer}를 냈습니다.')
            print("무승부")
            count_same = count_same + 1

            Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
            if Continue == "Y" or "Y".lower():
                user = input("가위 바위 보 !!! (입력해주세요.)")
            elif Continue == "N" or "N".lower():
                print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                break
        # computer 가위
        elif computer == '가위':
            print(f'컴퓨터는 {computer}를 냈습니다.')
            if user == '바위':
                print("승리")
                count_win = count_win + 1

                Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
                if Continue == "Y" or "Y".lower():
                    user = input("가위 바위 보 !!! (입력해주세요.)")
                elif Continue == "N" or "N".lower():
                    print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                    break

            elif user == '보':
                print("패배")
                count_lose = count_lose + 1

                Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
                if Continue == "Y" or "Y".lower():
                    user = input("가위 바위 보 !!! (입력해주세요.)")
                elif Continue == "N" or "N".lower():
                    print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                    break
        # computer 바위
        elif computer == '바위':
            print(f'컴퓨터는 {computer}를 냈습니다.')
            if user == '보':
                print("승리")
                count_win = count_win + 1

                Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
                if Continue == "Y" or "Y".lower():
                    user = input("가위 바위 보 !!! (입력해주세요.)")
                elif Continue == "N" or "N".lower():
                    print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                    break

            elif user == '가위':
                print("패배")
                count_lose = count_lose + 1

                Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
                if Continue == "Y" or "Y".lower():
                    user = input("가위 바위 보 !!! (입력해주세요.)")
                elif Continue == "N" or "N".lower():
                    print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                    break
        # computer 보
        elif computer == '보':
            print(f'컴퓨터는 {computer}를 냈습니다.')
            if user == '가위':
                print("승리")
                count_win = count_win + 1

                Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
                if Continue == "Y" or "Y".lower():
                    user = input("가위 바위 보 !!! (입력해주세요.)")
                elif Continue == "N" or "N".lower():
                    print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                    break

            elif user == '바위':
                print("패배")
                count_lose = count_lose + 1

                Continue = str(input("계속하시겠습니까? [YES]=Y [NO]=N "))
                if Continue == "Y" or "Y".lower():
                    user = input("가위 바위 보 !!! (입력해주세요.)")
                elif Continue == "N" or "N".lower():
                    print(f'승리:{count_win}회,패배:{count_lose}회,무승부:{count_same}회')
                    break

    except:
        print("[가위,바위,보]만 입력해주세요.")
        user = input("")
