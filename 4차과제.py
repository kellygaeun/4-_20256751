schedule = [[[] for day in range(32)] for month in range(13)] #3차원 배열 자료 참고 했습니다.

def start():
    print("\n---------------------------")
    print("     일정 등록 시스템입니다.")
    print("---------------------------")
    print("1. 일정 등록")
    print("2. 일정 확인")
    print("3. 일정 지우기")
    print("4. 일정 수정")
    print("\n종료를 원하면 'quit'를 입력하세요.\n")

def run():
    while True:
        start()
        choice = input("번호를 선택하세요: ").strip()

        if choice == '1':
            mon, day =getDate()
            registerSchedule(mon, day)

        elif choice == '2':
            option = input("일정 확인 옵션 (월별로 확인=1, 특정 날짜 확인=2): ").strip()

            if option == '1':
                try:
                    mon = int(input("몇 월인가요? (1~12): "))
                    if mon>=1 and mon <= 12:
                        checkSchedule(mon)
                    else:
                        print("1~12 사이의 숫자를 입력해주세요.")
                except ValueError:
                    print("숫자만 입력해주세요.")

            elif option == '2':
                mon, day = getDate()
                checkSchedule(mon, day)

            else:
                print("1 또는 2를 입력해주세요.")


        elif choice == '3':
            mon, day =getDate()
            removeSchedule(mon, day)

        elif choice == '4':
            mon, day =getDate()
            editSchedule(mon, day)

        elif choice.lower() == 'quit':
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 번호를 입력하세요")

def getDate():
    while True:
        try:
            mon=int(input("\n일정날은 몇월인가요?(숫자만 입력해주세요): "))
            day=int(input("일정날은 몇일인가요?(숫자만 입력해주세요): "))

            if (mon>=1 and mon<=12 and day>=1 and day<=31):
               return mon, day
            else:
                print("날짜를 제대로 입력해주세요.")
        except ValueError:
            print("숫자만 입력해주세요.")

def registerSchedule(m, d):
    do=input("\n일정 내용: ").strip()
    if do:
        schedule[m][d].append(do)
    else:
        print("제대로 된 일정을 입력해주세요.")
        
def checkSchedule(m, d=None):
    if d is None:
        doSchedule=False
        print(f"{m}월 전체 일정:")
        for i in range(1, 32):
            do=schedule[m][i]
            if do:
                doSchedule=True
                print(f"{i}일: ")
                for j in range(len(do)):
                    print(f"{j+1}. {do[j]}")
                print()
        if not doSchedule:
            print(f"{m}월 일정이 없습니다.")
    else:
        do=schedule[m][d]
        print(f"\n{m}월 {d}일 일정: ")
        if do:
            for i in range(len(do)):
                print(f"{i+1}. {do[i]}")
        else:
            print(f"{m}월 {d}일 일정이 없습니다.")            
    
def removeSchedule(m, d):
    do=schedule[m][d]

    if not do:
        print("삭제할 일정이 없습니다.")
    else: 
        print(f"{m}월 {d}일 일정")
        for i in range(len(do)):
            print(f"{i+1}. {do[i]}")
        try:
            num=int(input("\n삭제할 일정의 번호를 입력해주세요: "))
            if num<=len(do) and num>0:
                do.pop(num-1)
                print("삭제 완료 되었습니다.")
            else:
                print("없는 번호입니다.")
        except ValueError:
            print("숫자만 입력하세요.")
    
def editSchedule(m, d):
    do=schedule[m][d]

    if not do:
        print("수정할 일정이 없습니다.")
    else:
        print(f"{m}월 {d}일 일정")
        for i in range(len(do)):
            print(f"{i+1}. {do[i]}")
        try:
            num=int(input("\n수정할 일정의 번호를 입력해주세요: "))
            if num<=len(do) and num>0:
                edit=input("수정할 내용을 입력해주세요: ")
                do[num-1]=edit
                print("수정 완료 되었습니다.")
            else:
                print("없는 번호입니다.")
        except ValueError:
            print("숫자만 입력하세요.")

run()
