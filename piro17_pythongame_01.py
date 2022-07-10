import random
from tkinter import Y
import requests
from bs4 import BeautifulSoup as bs
from soupsieve import select


from soupsieve import select

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
        print(playerstatus[i].name,"은(는) 지금까지",playerstatus[i].cur,"! 치사량까지",playerstatus[i].dead-playerstatus[i].cur )
        if(playerstatus[i].dead-playerstatus[i].cur==0 ):
            gotosleep.append(playerstatus[i].name)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if len(gotosleep)>=1:
        print(gotosleep[0],"(이)가 전사했습니다...꿈나라에서는 편히 쉬시길...zzz")
        exit()
        
class exceedLimit(Exception):
    def __init__(self):
        super().__init__('도달할 수 없는 층입니다!')


def three_six_nine_player(i):
    
    a = ['3', '6', '9']
    num = input('당신의 답은?: ')
    count = (lambda x: sum([x.count(n) for n in a]))(str(i))
            
            
    if count:
            answer = '짝'
            if num == answer:
                print("맞았습니다!")
            else:
                print('Game over!')
                return 1
            
    else:
        if str(i) == num:
            print(num)
        else:
            print('Game over!')
            return 1
                        
                        
def three_six_nine_computer(i):
    num=i
    
    a = ['3', '6', '9']
    count = (lambda x: sum([x.count(n) for n in a]))(str(i))
    
    
    if count:
            list=[i, '짝','짝','짝','짝','짝','짝']
            num=random.choice(list)
            print('당신의 답은?: ',num)
            answer = '짝'
            if num == answer:
                print("맞았습니다!")
            else:
                print('Game over!')
                return 1
                
            
    else:
        list=[i,i,i,i,i,i,i,i,i, '짝']
        num=random.choice(list)
        print('당신의 답은?: ',num)
        if i == num:
            #print(num)
            print("맞았습니다!")
        else:
            print('Game over!')
            return 1
    
    
def Updown(playerstatus):
    print('''
------------------------------------------------------------------------------

 _   _ ______  ______                           _____                         
| | | || ___ \ |  _  \                         |  __ \                        
| | | || |_/ / | | | |  ___  __      __ _ __   | |  \/  __ _  _ __ ___    ___ 
| | | ||  __/  | | | | / _ \ \ \ /\ / /| '_ \  | | __  / _` || '_ ` _ \  / _ \
| |_| || |     | |/ / | (_) | \ V  V / | | | | | |_\ \| (_| || | | | | ||  __/
 \___/ \_|     |___/   \___/   \_/\_/  |_| |_|  \____/ \__,_||_| |_| |_| \___|
                                                                              
                                                                              

------------------------------------------------------------------------------                                                                       
''')
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
    print("정답자는 " + players[updownPlayer] + "입니다.\n정답자는 한잔 드세요!");
    return updownPlayer;
    
#################################################
print("ALCOHOL GAME")
print('어 술게임 좀 해요? 아 잘 모르시는구나ㅎ 그러면 어쩔 수 없죠~ 마시면서 배우는 술게임~!')
start = input('게임을 진행할까요/? (y/n) : ')
if start == 'y':
    playerName = input('오늘 거하게 취해볼 당신의 이름은? : ')

    while True:
        try:
            playerCup = int(input('당신의 치사량(주량)은 얼마만큼인가요? (1~5중 선택해주세요) : '))
        except ValueError:
            print("숫자를 입력해 주세요!")
        else:
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
        try:
            playerNum = int(input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
        except ValueError:
            print("숫자를 입력해 주세요!")
        else:
            if (1<=playerNum<=3) :
                break
            else:
                print("올바른 값을 입력해 주세요.")

    #computer 인스턴스 생성 개수 입력받아서 랜덤으로 이른,주량 정함
    friends=random.sample(namebase,playerNum) #이름 랜덤으로 뽑아서 리스트 생성

    for i in range(playerNum):
        
        x=player(friends[i],random.randint(1,5),0)
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
    selectNumber = 0;
    while True:
        ####이부분만 건들여 주세요 함수 선언은 자유롭게

        
        if selectNumber == 0:
            choice = input("오늘의 게임은??? (1-5번 중에 골라주세요) : ")
        else: 
            choice = str(random.randint(1,5));
            print(playerstatus[selectNumber].name,'가 선택한 게임은', choice, '입니다.')
        
        selectNumber +=1;
        selectNumber %= playerNum+1;

        if choice == "1":
        #김태윤
            print(
                """
                 :::::::::::::
                #============$
                $@@@@@@@@@@@@@
                  #         ! 
                  # @@$.@@@ !
                  #-; @.@ = !
                  # ;;: ;;; !
                  #.@@#.@@@ !
                  #-; @.@ = ! .@$;
                  #-*~@.@~$ ! ,$ @  -~
                  #         ! ~= @.~#;#
                  #  .,,,   ! @  $~;*.#
                  #  :   ,  ! @ @=:*  @
                  #  :   ,  !,$   @#  @
                  #  :   ,  ! @ @=:!  ,=
                  #  :   ,  !  @@~ ;~*.#
                *$@$$#$$$$$$#$.@@  *#@@ 
                #.           ~  @   !$
                :::::::::::::::::::::::~~.""")
            print(playerName, '님이 좋아하는 아파트~게임~ 아파트아파트아파트~~!!!', sep='')
            print('선택하신 층수에 도달할때까지 팀원 중 한명씩 올라갑니다! 선택하신 층수에 도착하는 사람이 마시는 사람~!')
            while True:
                try:
                    floorLimit = int(input('오늘은 몇층까지 올라가나요~~~??? (층수는 1 에서 30 사이로 골라주세요!) : '))
                    if floorLimit < 1 or floorLimit > 30:
                        raise exceedLimit
                except exceedLimit as e:
                    print(e)
                else:
                    # continue game

                    thisOrder = random.sample(playerstatus, playerNum+1)
                    for i in range(floorLimit):
                        currPerson = thisOrder[i % len(thisOrder)]
                        print(currPerson.name, i + 1, '층')
                        if i == floorLimit - 1:
                            # we are at the end floor ... 'currPerson' lost
                            # TODO: now update currPerson's cur drink status
                            print(currPerson.name, '님은 저희와 함께 갈 수 없게 되었습니다... ㅎ 한잔하세요!')
                            currPerson.cur += 1
                    break
        elif choice == "2":
            
            answer = []

            while True :
                try:
                    line = int(input("지하철 노선을 입력하세요(1~9) : "))
                except ValueError:
                    print("올바른 숫자를 입력해 주세요.")
                    continue
                if 1<= line <= 9:
                    break
                else:
                    print("다시입력하세요(ex.1)")

            url = "http://openapi.seoul.go.kr:8088/456468477370693137374e75764b54/xml/SearchSTNBySubwayLineInfo/1/97/ / /{line}호선".format(line=line)

            res = requests.get(url)
            soup = bs(res.text, 'xml')
            for i in soup.find_all('STATION_NM'):
                answer.append(i.text);


            computerAnswer = answer;
            url = "http://openapi.seoul.go.kr:8088/456468477370693137374e75764b54/xml/SearchSTNBySubwayLineInfo/1/97/ / /{line}호선".format(line=(line%9)+1)
            res = requests.get(url)
            soup = bs(res.text, 'xml')
            for i in soup.find_all('STATION_NM'):
                computerAnswer.append(i.text);


            already=[]
            subwayPlayerNum = selectNumber;
            while True :
                
                if subwayPlayerNum == 0:
                    station=input('{line}의 정차역 입력(종료=0):'.format(line=line))
                else:
                    station = random.choice(computerAnswer);
                    print(playerstatus[subwayPlayerNum].name, "의 입력은", station, "입니다.")

                if station == '0':
                    print("지하철 게임 종료!")
                    break
                else:
                    if(station in answer):
                        if(station not in already):
                            already.append(station)
                            print(already)
                            print("존재하는 역입니다! 통과!!!")
                        else:
                            print("이미 입력하신 역입니다!! 벌칙!!!")
                            break
                    else:
                        print("존재하지 않는 역입니다!! 벌칙!!!")
                        break
                subwayPlayerNum +=1;
                subwayPlayerNum %= playerNum+1;


            print(playerstatus[subwayPlayerNum].name,'님이 한잔 마십니다!')
            playerstatus[subwayPlayerNum].cur += 1 
        #장명지    

        elif choice == "3":
        #강수경
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            print(    
            
"""  ____ ___  ___  _   ____ ___  ___  _   ____ ___  ___  _   ____ ___  ___  _ 
<__ /| __>| . || | <__ /| __>| . || | <__ /| __>| . || | <__ /| __>| . || |
 <_ \| . \`_  /|_/  <_ \| . \`_  /|_/  <_ \| . \`_  /|_/  <_ \| . \`_  /|_/
<___/`___/ /_/ <_> <___/`___/ /_/ <_> <___/`___/ /_/ <_> <___/`___/ /_/ <_>""")
            
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("순서대로 숫자를 외치되 숫자안에 3,6,9 가 들어가면 박수를 한번만 쳐주세요!")
            
            three_game_seq=[i for i in range(playerNum+1)]
            three_random=random.sample(three_game_seq,playerNum+1)
            three_save=[playerstatus[three_random[i]].name for i in range(playerNum+1)]
            
            print("게임 순서는 ",end='')
            for i in range(playerNum+1):
                print(three_save[i],end=' ')
            print("순으로 진행됩니다!") 
            i=1
            three_flag=0
            while True:
                
                for j in range(playerNum+1):
                    print(three_save[j],"의 순서 입니다!")
                    if three_save[j]==playerName:
                        
                        if(three_six_nine_player(i)==1):
                            playerstatus[three_random[j]].cur=playerstatus[three_random[j]].cur+1
                            break
                        i=i+1
                    
                        
                    else:
                        
                        if(three_six_nine_computer(i)==1):
                            playerstatus[three_random[j]].cur=playerstatus[three_random[j]].cur+1
                            
                            break
                        i=i+1
                else:
                    continue
                break
      
        elif choice == "4":
        #황성하
            updownResult = Updown(playerstatus);
            playerstatus[updownResult].cur += 1;

        elif choice == "5":
            print('''
 _____  _     _____   _____ ____  _      _____   ____  _____   ____  _____ ____  _____  _      
/__ __\/ \ /|/  __/  /  __//  _ \/ \__/|/  __/  /  _ \/    /  /  _ \/  __//  _ \/__ __\/ \ /|  
  / \  | |_|||  \    | |  _| / \|| |\/|||  \    | / \||  __\  | | \||  \  | / \|  / \  | |_||  
  | |  | | |||  /_   | |_//| |-||| |  |||  /_   | \_/|| |     | |_/||  /_ | |-||  | |  | | ||  
  \_/  \_/ \|\____\  \____\\_/ \|\_/  \|\____\  \____/\_/     \____/\____\\_/ \|  \_/  \_/ \|  
            ''')
            game_num_ssh = int(input("2 이상 8 이하의 정수를 외쳐 주세요! "))
    
            point_ssh = []

            i_ssh = 0
            while i_ssh+1 <= playerNum + 1:
                p_num_ssh = random.randint(1, playerNum + 1)
                if p_num_ssh == i+1:
                    continue
                else:
                    point_ssh.append(p_num_ssh)
                i_ssh += 1
                        

            for index, value in enumerate(point_ssh):
                print(playerstatus[index].name + '👉' + playerstatus[value-1].name)

            i_ssh = 0
            count_ssh = 1
            while count_ssh <= game_num_ssh:
                print(f'{playerstatus[i_ssh].name} : {i+1}! 🧨 👉 {playerstatus[point_ssh[i_ssh]-1].name}')
                if count_ssh == game_num_ssh:
                    print(playerstatus[i_ssh].name + ' : ' + '으악😵')
                    playerstatus[i_ssh].cur += 1
                    break
                else:     
                    i_ssh = point_ssh[i_ssh] - 1
                    count_ssh += 1
                    continue

            
        else:
            print("올바른 번호를 입력해주세요")
            continue

        #현재 상태 보여주고 판단
        hp()

    # 'n' 을 선택, 게임이 시작되지 않습니다
else:
    exit()
    
    

