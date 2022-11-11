# 게시글 로딩하기
'''
data.csv 파일이 있으면
    게시글을 로딩 한다.
data.csv 파일이 없으면
    data.csv 파일을 만든다.

게시글 로딩 로직
data.csv 파일을 읽는다.
데이터를 한 줄 마다
    Post 인스턴스를 만든다.
Post 리스트에 인스턴스를 저장한다.
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


# 테스트
#print(post_list[0].get_title())