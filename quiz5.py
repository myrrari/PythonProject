#50명 승객 매칭, 총 탑승 승객 수
#승객 별 운행 시간은 5~50분
#5~15분 승객만 매칭해야

from random import *
count = 0 #총 탑승승객수
for customer in range(1,51):
    time = randrange(5, 51)
    if time >= 5 and time <=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
print("총 탑승 승객 : {0} 명".format(count))

#for문에도 ':' 적어줘야 함.

#첫번째 customer을 이용해 밑으로 쭉쭉 내려가면, 
#첫번째 customer가 있고 time이 랜덤으로 하나 뽑힌 상태에서
#그 time이 5와 15사이인지 if로 확인하고 해당된다면, if 밑 프린트와 카운트 플러스1
#그 time이 if조건에 해당되지 않는다면, 한줄 더 밑으로 내려가서 else 밑 프린트 출력
#if에 해당되거나, 혹은 if가 아닌 else를 거치는 첫번째 customer가 끝나면
#for문을 통해 두번째 customer도 똑같이 밑으로 쭉쭉 내려가는 과정 거침.
#그렇게 51미만까지의 원소를 customer라는 변수에 대입해서 for문 완료.
#이후 for문을 빠져나와 또다른 print인 총 탑승승객수 출력.