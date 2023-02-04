def multiply(arg1, arg2):
    result = arg1 * arg2
    print(result)

def add(n1, n2):
    print(n1+n2)

def subtract(n1,n2):
    print(n1-n2)

def division(n1, n2):
    print(n1/n2)

print("메뉴를 선택하세요> 1: 덧셈, 2:뺄셈, 3:곱셈, 4:나눗셈, 5:종료")
while True:
    
    A = int(input('input 1 : '))
    B = int(input('input 2 : '))
    menunum=int(input("메뉴 번호 입력: "))

    

    if menunum==1:
        add(A,B)
    elif menunum==2:
        subtract(A,B)
    elif menunum==3:
        multiply(A,B)
    elif menunum==4:
        division(A,B)
    elif menunum==5:
        break
