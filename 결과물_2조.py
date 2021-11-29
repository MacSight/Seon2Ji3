import random

def TodayUnn() :
    dns=["금전운","명예운","건강운","애정운","학업운","대인관계운"]
    luckcol=["빨간색","파란색","노란색","초록색","보라색","검정색","흰색"]
    unn=random.choice(dns)

    print("~ ~ ~ ~ ~행운의 별자리 운세~ ~ ~ ~ ~\n")
    date=int(input("오늘의 날짜를 입력해 주세요. (예시:11월 13일 > 1113): "))
    birth=int(input("당신의 생일을 입력해 주세요. (예시:1월 22일 > 122): "))
    star=str(input("당신의 별자리를 입력해 주세요.: "))
    print()

    if date>=birth:
        x=date-birth
    else:
        x=birth-date
    
    luck = x % 100
    col = x % 7

    print("오늘의 행운 퍼센트는",luck,"%로.")

    if luck>=80:
        print(unn,"이 매우 좋은 하루입니다.")
    elif luck>=40 and luck<80:
        print("평범한 날입니다.")
    else:
        print(unn,"이 매우 안좋으니 주의가 필요합니다.")


    print("오늘의",star,"자리의 행운의 색깔은",luckcol[col],"입니다.")


    print("오늘도 좋은 하루 보내세요\n")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")

def FortuneCookie() :
    cookie = {}
    lucky = [
            '선택을 하되, 후회하지 말자',
            '뭐든 할 수 있다.',
            '고민이 다 풀릴 것입니다.',
            '뜻이 있는 곳에 길이 있다.',
            '하고 싶은 일을 미루지 말고 도전해라',
            '당신은 소중한 사람입니다.',
            '내일은 오늘보다 더 행복해질 것입니다.',
            '자신감을 가지고 도전하세요!',
            '기분 좋은 일이 곧 생길 예정입니다.',
            ]
    lucknum = len(lucky)

    print("~ ~ ~ ~ ~ 포춘쿠키 뽑기 ~ ~ ~ ~ ~\n")
    count = int(input("만들 포춘쿠키의 개수를 정하세요: "))
    for i in range(1,count+1) :
        cookie[i] = lucky[random.randrange(lucknum)]
 
    while True :  
        mychoice = int(input("1 ~ %d번의 포춘쿠키 중 원하는 쿠키를 하나 고르세요(그만하고 싶으면 0 입력): " %count))

        if mychoice in cookie :
            myluck = cookie[mychoice]
            del cookie[mychoice]
            print("-"*50)
            print(myluck.center(40))
            print("-"*50)
            print()

        elif mychoice == 0 :
            break

        else :
            print("이미 뽑았거나 없는 번호입니다. 다른 번호를 고르세요\n")

    print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")


while True :
    what = input("오늘의 운세는 1, 포춘쿠키는 2, 프로그램을 종료하고싶으면 0을 입력하세요 : ")

    if what == '1' :
        TodayUnn()

    elif what == '2' :
        FortuneCookie()
    else :
        print("프로그램을 종료합니다.")
        break
