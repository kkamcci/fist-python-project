print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print("Leader is in charge")



랜덤함수
from random import * # random library에 있는 함수를 사용

print(random()) #0.0이상 1.0 미만의 임의의 값을 생성
print(random()*10) #0.0이상 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0.0이상 10.0 미만의 임의의 정수값을 생성
print(int(random() * 10)) # 0.0이상 10.0 미만의 임의의 정수값을 생성
print(int(random() * 10)) # 0.0이상 10.0 미만의 임의의 정수값을 생성
print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성
print(int(random() * 10)+1) # 1.0이상 10.0 이하의 임의의 정수값을 생성

print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)
print(int(random() * 65)+1) # 1.0이상 65.0 이하의 임의의 정수값을 생성(로또)

print(randrange(1,66)) # 1~66미만의 임의의 값 생성
print(randrange(1,66)) # 1~66미만의 임의의 값 생성
print(randrange(1,66)) # 1~66미만의 임의의 값 생성
print(randrange(1,66)) # 1~66미만의 임의의 값 생성
print(randrange(1,66)) # 1~66미만의 임의의 값 생성
print(randrange(1,66)) # 1~66미만의 임의의 값 생성

상속
일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#공격유닛
class AttackUnit(Unit):
     def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage   
    
     def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
     def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
             print("{0} : 파괴되었습니다.".format(self.name))

#파이어뱃 : 공격유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")

#공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)




다중상속 : 부모가 둘이 상인것(unit : 부모,attackunit : 자녀)
드랍쉽 : 공중 유닛, 수송기.마린/파이어뱃/탱크등을 수송.공격X

날수 있는 기능을 가진 클래스
class Flyable:
       def __init__(self, flying_speed):
             self.flying_speed = flying_speed
       def fly(self,name, location):
         print("{0} : {1}방향으로 날아갑니다.[속도 : {2}]"\
               .format(name, location, self.flying_speed)) 

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
       def __init__(self, name, hp, damage, flying_speed):
             AttackUnit.__init__(self, name, hp, damage)
             Flyable.__init__(self,flying_speed)

#발키리  :공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


메소드 오버라이딩

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
       print("[지상 유닛 이동]")
       print("{0} : {1}방향으로 이동합니다.[속도 {2}]"\
             .format(self.name, location, self.speed))
