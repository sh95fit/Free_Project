import os
import csv
from Post import Post

# 파일 경로 설정
file_path = "./Prac1_ConsoleBlog/data.csv"

# post 객체를 저장할 리스트 생성
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path) :
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding = "UTF-8")
    reader = csv.reader(f)
    for data in reader : 
        # Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else :
    f = open(file_path, "w", encoding = "UTF-8", newline="")
    f.close()

# 게시글 쓰기
def write_post() :
    """게시글 쓰기 함수"""
    print("\n\n- 게시글 쓰기 - ")
    title = input("제목을 입력해 주세요\n >>> ")
    content = input("내용을 입력해 주세요\n >>> ")
    # 글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글 등록이 완료되었습니다.")

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


# 게시글 목록
def list_post() :
    """게시글 목록 함수"""
    print("\n\n- 게시글 목록 -")
    id_list = []
    for post in post_list :
        print("번호 : ", post.get_id())
        print("제목 : ", post.get_title())
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
            write_post()
        elif select == 2:
            list_post()
        elif select == 3 :
            print("프로그램 종료")
            break