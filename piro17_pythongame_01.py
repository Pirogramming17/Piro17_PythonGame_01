import random

playerstatus=[]
namebase=['성하', '수경', '태윤', '승현', '명지']

# 함수명에 이니셜 혹은 게임명을 적어 겹칠 일이 없게 해주쎄용!
# 충돌을 막기 위해 최대한 공통부분을 수정하지 말아주세요! 나중에 깔끔하게 하면 됩니다

# 태윤-아파트 1
# 명지-지하철 2
# 수경-369 3
# 성하-업다운 4
# 승현-더게임오브데스 5

class player: 
    #주량 이름 현재마신양 
    def __init__(self, name, dead, cur):
        self.name = name
        self.dead = dead
        self.cur = cur

def hp():
    gotosleep=[]
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(playerstatus)):
        print(playerstatus[i].name,"은(는) 지금까지",playerstatus[i].cur,"!", "치사량까지",playerstatus[i].dead-playerstatus[i].cur )
        if(playerstatus[i].dead-playerstatus[i].cur==0 ):
            gotosleep.append(playerstatus[i].name)
 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if len(gotosleep)>=1:
        print(gotosleep[0],"(이)가 전사했습니다...꿈나라에서는 편히 쉬시길...zzz")
        exit()

def Updown(playerstatus):
    players= []
    for i in range(len(playerstatus)):
        players.append(playerstatus[i].name)

    updownNumber = random.randint(1, 50);
    updownHigh = 50;
    updownLow = 1;
    updown = 0;
    updownPlayer = random.randint(0, len(players) - 1);
    while True:
        if updownPlayer == 0:
            try:
                updown = int(input("당신의 숫자는?"))
            except ValueError:
                print("숫자를 입력하세요!")
                continue;
            if updown < updownLow or updown > updownHigh:
                print("숫자를 다시 입력하세요!")
                continue;
            else:
                if updown == updownNumber:
                    print("정답입니다!")
                    break;
                elif updown > updownNumber:
                    print("Down!")
                    updownHigh = updown - 1;
                elif updown < updownNumber:
                    print("Up!")
                    updownLow = updown + 1;
                updownPlayer +=1;
                updownPlayer %= len(players)
        else:
            updown = random.randint(updownLow, updownHigh);
            print(players[updownPlayer] + "의 숫자는 " + str(updown) + "입니다.");
            if updown == updownNumber:
                print("정답입니다!")
                break;
            elif updown > updownNumber:
                print("Down!")
                updownHigh = updown - 1;
            elif updown < updownNumber:
                print("Up!")
                updownLow = updown + 1;
            updownPlayer +=1;
            updownPlayer %= len(players);
    #결과출력
    print("정답자는 " + players[updownPlayer] + "입니다.\n 다른사람들은 모두 한잔씩 드세요!");
    return updownPlayer;
    
#################################################
print("ALCOHOL GAME")
print('어 술게임 좀 해요? 아 잘 모르시는구나ㅎ 그러면 어쩔 수 없죠~ 마시면서 배우는 술게임~!')
start = input('게임을 진행할까요/? (y/n) : ')
if start == 'y':
    playerName = input('오늘 거하게 취해볼 당신의 이름은? : ')
    
    while True:
    
        playerCup = int(input('당신의 치사량(주량)은 얼마만큼인가요? (1~5중 선택해주세요) : '))
    
        if (1<=playerCup<=5) :
            break
        else: 
            print("올바른 값을 입력해 주세요.")
    

    
    #player 인스턴스 생성
    inputplayer=player(playerName, playerCup, 0)
    playerstatus.append(inputplayer)
    #유저 네임과 namebase 겹치면 안되니까 지워줌
    if playerName in namebase:
        namebase.remove(playerName)
         
    
    while True:
        
        playerNum = int(input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
        if (1<=playerNum<=3) :
            break
        else: 
            print("올바른 값을 입력해 주세요.")
    
    #computer 인스턴스 생성 개수 입력받아서 랜덤으로 이른,주량 정함
    friends=random.sample(namebase,playerNum) #이름 랜덤으로 뽑아서 리스트 생성
    
    for i in range(playerNum):
        
        x=player(friends[i],random(1,5),0)
        playerstatus.append(x)
        print("오늘 함께 취할 친구는", x.name,"입니다!","(치사량:", x.dead,")")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    hp()
    
    print('오늘의 Alcohol GAME')
    print('1. 아파트')
    print('2. 지하철 2호선')
    print('3. 369')
    print('4. 업다운')
    print('5. 더 게임 오브 데스')
    
    while True:
        ####이부분만 건들여 주세요 함수 선언은 자유롭게
        choice = input("오늘의 게임은??? (1-5번 중에 골라주세요) : ")
        if choice == "1":
        #김태윤

        elif choice == "2":
        #장명지    

        elif choice == "3":
        #강수경

        elif choice == "4":
        #황성하

        elif choice == "5":
        #신승현
            
        else:
            print("올바른 번호를 입력해주세요")
            continue
            
        #현재 상태 보여주고 판단
        hp()    

# 'n' 을 선택, 게임이 시작되지 않습니다
else:
    exit()
