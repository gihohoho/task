class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        return (f'이름 : [{self.name}], 아이디 : [{self.username}]')


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


m1 = Member('이기호', '기호123', 'dlrlgh123')
m2 = Member('권수민', '수민123', 'rnjstnals123')
m3 = Member('이재윤', '재윤123', 'dlwodbns123')
D1 = m1.display()
D2 = m2.display()
D3 = m3.display()
print(D1)
print(D2)
print(D3)

Members = [

]
