# 메뉴 출력하기, 게시물 쓰기
'''
# 메뉴 출력하기
 출력할 내용
- Hun's Blog -
- 메뉴를 선택해 주세요 -
1. 게시글 쓰기
2. 게시글 목록
3. 프로그램 종료

* 범위가 넘어가는 경우, 문자열을 받는 경우 예외 처리 필요!
* 프로그램 종료 전까지 무한 반복! while True 사용

# 게시물 쓰기
 출력할 내용
 - 게시글 쓰기 -
 제목을 입력해 주세요 >>> 
 파이썬 공부 1일차
 본문을 입력해 주세요 >>>
 프로젝트 진행중
 # 개시글이 등록되었습니다.

 * 게시글 등록 과정
   1. Post 인스턴스 생성
   2. Post 리스트에 저장
'''

while True :
    print("\n\n- Hun's Blog -")
    print("- 메뉴를 선택해주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")

    try :
        select = int(input(">>> "))
    except ValueError :
        print("숫자를 입력해주세요")
    else :
        if select == 1 :
            print("게시글 쓰기")
        elif select == 2:
            print("게시글 목록")
        elif select == 3 :
            print("프로그램 종료")
            break
