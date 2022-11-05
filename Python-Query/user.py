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
        cursor.excute(sql) # 쿼리 진행시켜
        data = cursor.fetchall() # 그 결과를 뱉어내