#메일 내용을 message 변수에 담고

#      누구에게 보낼지 이름을 입력 받아서

# 메일 내용을 완성해서 출력한다.
import random

def make_lotto():
    listN=[]
    while len(listN)<6 :
        num = random.randint(1,46)

        if num not in listN:
            listN.append(random.randint(1,46))
    return listN

print(make_lotto())

message = """안녕하세요, {0}님
파이썬 수업에 오신걸 환영합니다
오늘의 행운의 로또 번호는 {1} 입니다.
남은 기간 즐겁고 행복한 공부가 되길 기원합니다
"""
who = input("누구에게 보낼건가요?")
data = make_lotto()

complete_message = message.format(who,data)

print(complete_message)