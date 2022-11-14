# 클래스 만들기
'''
-> 클래스로 만들 데이터 - 게시글
-> 클래스 속성: 글번호, 제목, 본문 내용, 조회수
-> 클래스 메서드: 게시물 수정, 조회수 증가, 속성 가져오기(메서드를 통해 가져오는 것 - 게시글 목록, 상세 확인용)
'''

class Post :
    """
        게시물 클래스
        param id : 글 번호
        param title : 글 제목
        param content : 글 내용
        param view_count : 조회수
    """

    def __init__(self, id, title, content, views_count) :
        self.id = id
        self.title = title
        self.content = content
        self.views_count = views_count

    def set_post(self, id, title, content, views_count) :
        self.id = id
        self.title = title
        self.content = content
        self.views_count = views_count

    def add_views_count(self) :
        self.views_count += 1
    
    def get_id(self) :
        return self.id

    def get_title(self):
        return self.title

    def get_content(self) :
        return self.content

    def get_views_count(self):
        return self.views_count
    

if __name__ == "__main__" :  #모듈 내에서 테스트 진행(자기자신을 출력할 때에만 __main__이 나타남)
    post = Post(1, "테스트", "테스트입니다.", 0)
#    post.set_post(1, "테스트2", "테스트2입니다.", 0)
#    post.add_views_count()
    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_views_count()}")