def hello():
    print('Hello') 
def sawatdee():
    print('สวัสดี')
def nihao():
    print('หนีห่าว')
def konnichiwa():
    print('คนนิจิวะ')

while True:
    friend = input('Where are you from? :')
    
    if friend == 'thai':
        sawatdee()
    elif friend == 'chaina':
        nihao()
    elif friend == 'japan':
        konnichiwa()
    elif friend == 'usa':
        hello()
    elif friend == 'exit':
        print('ออกจากระบบ')
        break        
    else:
        print('ไม่พบข้อมูลในระบบ')

