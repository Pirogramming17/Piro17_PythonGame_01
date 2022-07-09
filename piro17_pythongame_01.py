players = ['player', 'computer1', 'computer2', 'computer3']  # the others are computers


# player 를 '입력하는 이' 로 가정하고 코딩하시면 됩니다
# 함수명에 이니셜 혹은 게임명을 적어 겹칠 일이 없게 해주쎄용!
# 충돌을 막기 위해 최대한 공통부분을 수정하지 말아주세요! 나중에 깔끔하게 하면 됩니다

# 태윤-아파트 1
# 명지-지하철 2
# 수경-369 3
# 성하-업다운 4
# 승현-더게임오브데스 5

class Info:
    def __init__(self):
        self.yourCap = int(input("당신의 주량은 몇 잔?"))
        self.p1_Cap = int(input("컴퓨터1의 주량은 몇 잔?"))
        self.p2_Cap = int(input("컴퓨터2의 주량은 몇 잔?"))
        self.p3_Cap = int(input("컴퓨터3의 주량은 몇 잔?"))
        print()

    def WhoIsWinner(self):
        """술게임의 전체 승자 출력"""
        """중요 ! 매 게임이 한 판 끝날 때마다 '정산' 진행되어야 함."""
        """(즉, 본 함수 WhoisWinner 실행)"""
        if self.p1_Cap == 0:
            print('\n컴퓨터1이 뻗어버렸습니다!')
        elif self.p2_Cap == 0:
            print('\n컴퓨터2이 뻗어버렸습니다!')
        elif self.p3_Cap == 0:
            print('\n컴퓨터3이 뻗어버렸습니다!')
        elif self.yourCap == 0:
            print('\n당신이 뻗어버렸습니다!')
        else:
            print('\n아무도 뻗은 사람이 없습니다! 다음 게임을 계속 진행하십시오.')


class Player:
    def __init__(self):


# class alrExists(Exception):
#     def __init__(self):
#         super().__init__('Already exist name!')


##############  menu 1
def Menu1():


##############  menu 2
def Menu2():


##############  menu 3
def Menu3():


##############  menu 4
def Menu4():


def Menu5():


#################################################
print("ALCOHOL GAME")
print('어 술게임 좀 해요? 아 잘 모르시는구나ㅎ 그러면 어쩔 수 없죠~ 마시면서 배우는 술게임~!')
start = input('게임을 진행할까요/? (y/n) : ')
if start == 'y':
    playerName = input('오늘 거하게 취해볼 당신의 이름은? : ')
    playerCap = input('당신의 치사량(주량)은 얼마만큼인가요? (1~5중 선택해주세요) : ')
    playerNum = int(input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
    # 이 이후에 나머지 player 들을 랜덤으로 정하고 치사량이 출력되는 코드가 필요합니다 (게임 리스트 출력하기)
    # 이건 list 써서 금방 할 수 있는데
    # 시간 관계상 일단 내비둘게요!
    print('오늘의 Alcohol GAME')
    print('1. 아파트')
    print('2. 지하철 2호선')
    print('3. 369')
    print('4. 업다운')
    print('5. 더 게임 오브 데스')
    while True:
        # 두번째 게임부터는 자동으로 choice 가 내려져야 하기 때문에 이 코드 역시 바뀔겁니다!
        choice = input("오늘의 게임은??? (1-5번 중에 골라주세요) : ")
        if choice == "1":
        # 여기에 exception 해결하시고 menu 를 쓰시던 여기에 쓰시던 게임 코드 작성하시면 됩니다

        elif choice == "2":


        elif choice == "3":

        elif choice == "4":

        elif choice == "5":
        else:

# 'n' 을 선택, 게임이 시작되지 않습니다
else:
    exit()
