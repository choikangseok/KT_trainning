#메일 내용을 message 변수에 담고

#      누구에게 보낼지 이름을 입력 받아서

# 메일 내용을 완성해서 출력한다.


while True:
    message = """안녕하세요, {0}님
    파이썬 수업에 오신걸 환영합니다
    오늘은 {1}일째 수업입니다.
    남은 기간 즐겁고 행복한 공부가 되길 기원합니다
    """
    who = input("누구에게 보낼까요? (종료 : C 입력)")
    if who == "C":
        break
    date = input("오늘은 몇일째 수업인가요?")

    complete_message = message.format(who,date)

    print(complete_message)
    print("hellowks")