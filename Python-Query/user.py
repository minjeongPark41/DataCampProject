import pymysql

# Module which justifies classes and actions about 'User'

'''
    user_id : User's MK (Main Key)
    course_name : 'Data Analysis'
    name : person name
    current_rented_books: how many books the person rent
    rent_free_date : The day person can borrow books 'again' after delay of renting books
    rentable : status whether person can borrow or not
'''

class User:
    def __init__(self, user_id, course_name, name, current_rented_books, rent_free_date, rentable):
        self.user_id = user_id
        self.course_name = course_name
        self.name = name
        self.current_rented_books = current_rented_books
        self.rent_free_date = rent_free_date
        self.rentable = rentable
    
    def __str__(self):
        return f'{self.user_id, self.course_name, self.name, self.current_rented_books, self.rent_free_date, self.rentable}'
        
# new_user = User(1, 'da', 'abc', 0, '2022', 'able')
# print(new_user)
# print(new_user.course_name)

# test.py 단에서 '전체 User 정보 조회' 할 때의 함수
def find_users(connection, cursor):
    print("bring and find whole User data from DB")
    
    # db에서 전체 user 데이터를 불러와서 조회
    try:
        sql = 'SELECT * FROM users'
        cursor.execute(sql) # 쿼리 진행시켜
        data = cursor.fetchall() # 그 결과를 뱉어내
        print("쿼리 결과", data)
    except pymysql.Error as error:
        error_code, message = error.args
        print("에러들", error_code, message)
        
# User 회원가입 - insert
def register_user(conn, cursor):
    format = '''
        user_id, 기수명, 이름을 ,로 구분하여 입력: 
    '''
    
    user_id, course_name, name = input(format).split(',')
    # user_id, 기수명, 이름을 ,로 구분하여 입력: 이라고 terminal에 나타나서 입력하게 됨
    
    try:
        sql - INSERT INTO users (user_id, course_name, name) VALUES (%s, %s, %s)'
        # INSERT INTO users VALUES ('u-g-1','AI-13','yoo')
        value = (user_id, course_name, name)
        cursor.execte(sql, value)
        conn.commit()
        
    except pymysql.Error as error:
        error_code, message = error.args
        print(error_code, message)
        
# 특정 user 정보 조회
# 특정한 정보니까 WHERE 들어감. 즉, 매번 바뀌는 동적인 데이터
# ㄴ 맵핑하는 코드 필요. 여기서 input()

def find_specific_user(connection, cursor):
    user_id = input("'user_id' which you want to input")
    
    try:
        #sql = f'SELECT*FROM users WHERE user_id = \'{user_id}\'
        # 동적 바인딩 (동적 파라미터로) 
        sql = 'SELECET * FROM users WHERE user_id = %s'
        value = user_id
        
        cursor.execute(sql, value) # 쿼리 진행