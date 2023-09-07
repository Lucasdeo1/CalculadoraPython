def sum(a, b):
    return a +b

def sub(a,b):
    return a-b

if __name__=="__main__":
    
    print('Sejam bem vindos a calculadora em python!')
    
    a = int(input('type a number: '))
    b = int(input('type a second number: '))
    op = 0
    while op!=5:
        print('1-Sum\n2-subtract\n3-multiply\n4-divide\n5-exit')
        op=int(input('Choice a option'))
        if op == 1:
            res = sum(a,b)
            print('the value of sum this two number is',res) 
        if op == 2:
            res = sub(a,b)
            print('the value of subtract this two number is',res)
            
    print('application finished, thanks for used and see you next!')   
    