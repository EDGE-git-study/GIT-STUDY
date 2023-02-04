def add(n1, n2):
    print(n1+n2)

def subtract(n1,n2):
    print(n1-n2)

print("메뉴를 선택하세요> 1: 덧셈, 2:뺄셈, 3:곱셈, 4:나눗셈, 5:종료")
menunum=10
while True:
    
    A = int(input('input 1 : '))
    B = int(input('input 2 : '))
    menunum=int(input("메뉴 번호 입력: "))

    

    if menunum==1:
        add(A,B)
    elif menunum==2:
        subtract(A,B)
    elif menunum==3:
        print(3)
    elif menunum==4:
        print(4)
    elif menunum==5:
        break

