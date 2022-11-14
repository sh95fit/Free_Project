# 게시글 목록 작성하기
'''
고려해야할 사항
- 없는 글번호 요청 시 예외처리 및 무한 반복
- 메뉴로 돌아갈 수 있는 기능 필요(ex> -1 입력 시 메뉴로 돌아가기)
- 올바른 글번호 입력 시 상세페이지로 이동

게시글 상세
- 사용자가 입력한 글번호와 같은 게시글 찾기
- 조회수 증가 및 상세 내용 출력
- 수정, 삭제 기능을 수행할 때 Post 객체 넘겨주기
'''
from Post_Loading import post_list 


# 게시글 목록
def list_post() :
    """게시글 목록 함수"""
    print("\n\n- 게시글 목록 -")
    id_list = []
    for post in post_list :
        print("번호 : ", post.get_id())
        print("제목 : ", post.get_title())
        print("본문 : ", post.get_content())
        print("조회수 : ", post.get_views_count())
        print("")
        id_list.append(post.get_id())

    while True :
        print("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try :
            id = int(input(" >>> "))
            if id in id_list :
                detail_post(id)
                break
            elif id == -1 :
                break
            else :
                print("없는 글 번호 입니다.")
        except ValueError :
            print("숫자를 입력해주세요.")


# 게시글 상세보기 페이지
def detail_post(id) :
    """게시글 상세 보기 함수"""
    print("\n\n- 게시글 상세 -")
    for post in post_list :
        if post.get_id() == id :
            # 조회수 1 증가
            post.add_views_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("내용 : ", post.get_content())
            print("조회수 : ", post.get_views_count())

    while True :
        print("Q) 수정 : 1  삭제 : 2  (메뉴로 돌아가려면 -1을 입력)")
        try : 
            select = int(input(">>> "))
            if select == 1 :
                print("수정")
                break
            elif select == 2 :
                print("삭제")
                break
            elif select == -1 :
                break
            else :
                print("잘못 입력하였습니다.")
        except ValueError :
            print("숫자를 입력해 주세요.")


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
#            write_post()
            pass
        elif select == 2:
            list_post()
        elif select == 3 :
            print("프로그램 종료")
            break