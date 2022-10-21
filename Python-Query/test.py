# 파이썬으로 DB 연결해서 가지고 오기

# 도서를 대여하는 함수가 있다고 하자.
def open_library():
    format = '''
        원하시는 동작을 선택하세요
            1. 전체 User 조회
            2. User 등록
            3. 특정 User 조회
            4. 전체 도서 조회
            5. 대여 가능 도서 조회
            6. 도서명으로 조회
            7. 도서 대여
            8. 도서 반납
            9. User 탈퇴
            0. 프로그램 종료
    '''
    
    print(format)
    
open_library()