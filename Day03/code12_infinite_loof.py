# 무한 반복 예제 
#key = input('이름을 입력하세요')
# print(f'안녕하세요, {key}님!')

num= 0

while True :
    print('메뉴를 선택하세요.')
    print(' 1. 회원 입력 ')
    print(' 2. 회원 검색 ')
    print(' 3. 회원 수정 ')
    print(' 4. 회원 삭제 ')
    print(' 5. 프로그램 종료 ')
    num= input('메뉴 번호 입력 > ')
    num= int(num)

    if num == 1:
        print('회원 입력 시작!')
    elif num == 2 :
        print('회원 검색 시작!')
    elif num == 3 :
        print('회원 수정 시작!')
    elif num == 4 :
        print('회원 삭제 시작!')
    elif num == 5 :
        print('프로그램 종료')
        break
    else :
         continue
        