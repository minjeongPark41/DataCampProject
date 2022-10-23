# 파이썬으로 DB 연결해서 가지고 오기

import pymysql

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
    try:
        # DB 연결 코드 
        
        # DB 연결용 메서드
        connection = pymysql.connect(host='localhost', user='root', password='8584', db='test')
        # ㄴ 여기서 db='test' 는 ddl.spl에서 CREATE DATABASE 뒤에 써준 이름 
        # print(connection) -> <pymysql.connections.Connection object at 0x0000020AE045E650>. 연결된 것!
        
    finally:
        pass
    
open_library()