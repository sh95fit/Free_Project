# 게시글 수정, 삭제, 저장하기
'''
게시글 수정
- 사용자가 새로 제목, 본문을 입력한다
- Post.py 내 set_post 메서드로 Post 객체 수정

게시글 삭제
- post_list에서 해당 Post 객체를 삭제해준다

게시글 저장하기
- post_list에 저장된 내용을 data.csv 파일에 저장
'''

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


# 게시글 수정
def update_post(target_post) :
    """게시글 수정 함수"""
    print("\n\n- 게시글 수정 -")
    title = input("제목을 입력해 주세요\n>>> ")
    content = input("본문을 입력해 주세요\n>>> ")
    target_post.set_post(target_post.id, title, content, target_post.views_count)
    print("# 게시글이 수정되었습니다.")

# 게시글 삭제
def delete_post(target_post) :
    post_list.remove(target_post)

# 게시글 저장
def save_post() :
    """게시글 저장 함수"""
    f = open(file_path, 'w', encoding = "UTF-8", newline  = "")
    writer = csv.writer(f)
    for post in post_list :
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_views_count()]
        writer.writerow(row)
    f.close()
    print("# 저장이 완료되었습니다.")
    print("# 프로그램 종료")


# 수정 테스트를 위해 추가--------------------------------------------------

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
            target_post = post

    while True :
        print("Q) 수정 : 1  삭제 : 2  (메뉴로 돌아가려면 -1을 입력)")
        try : 
            select = int(input(">>> "))
            if select == 1 :
                update_post(target_post)
                break
            elif select == 2 :
                delete_post(target_post)
                break
            elif select == -1 :
                break
            else :
                print("잘못 입력하였습니다.")
        except ValueError :
            print("숫자를 입력해 주세요.")
#---------------------------------------------------------------------



# 시작 - 메인 While 루프
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
            pass
        elif select == 2:
            list_post()
        elif select == 3 :
            save_post()
            break



