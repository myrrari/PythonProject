#1명은 치킨, 3명은 커피쿠폰

#조건1 댓글 20명, 아이디는 1부터 20
#조건2 무작위 추첨, 중복 불가
#조건3 random 모듈의 shuffle 과 sample

#cf.
#from random import *
#list = [1,2,3,4,5]
#shuffle(list)
#print(list)
#print(sample(list,1))
#list에서 1개를 뽑는 샘플링

from random import *
id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 :", sample(id,1))
print("커피 당첨자 :", sample(id,3))
#당첨자가 중복될 수 있으므로 문제가 있음 ㅠㅠ
print(" -- 축하합니다 -- ")

#강의 정답
from random import *
users = range(1, 21) #1부터 21미만까지의 수
# print(type(users))
users = list(users)
# print(type(users))

shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")

# ! 중요 ! format 기억

# number = 20
# welcome = '환영합니다'
# base = '{} 번 손님 {}'

# #아래 3개의 print는 같은 값을 출력
# print(number,'번 손님',welcome)
# print(base.format(number,welcome))
# print('{} 번 손님 {}'.format(number,welcome))
# #=>20 번 손님 환영합니다