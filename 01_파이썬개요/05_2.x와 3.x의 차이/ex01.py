"""

파이썬 2.x 와 3.x 의 차이
- 3.x 기준으로 설명한다.

3.x 에서는 모든 변수가 객체(Object)로 처리된다.

print문의 괄호가 필수이다.
    - 2.x
        ex) print("hello")
              print "hello"
    - 3.x
        ex) print("hello")

정수의 나누기 결과가 float이다.
    - 2.x
        나누기 연산 결과가 정수이다.
    - 3.x
        나누기 연산 결과가 실수이다.

long 형이 없어졌다.
    - 2.x
        ex) 1073741824 #<type 'int'>
              1267650600228229401496703205376 #<type 'long'>
    - 3.x
        ex) 1073741824 #<type 'int'>
              1267650600228229401496703205376 #<type 'int'>
            
xrange를 지원하지 않는다.
    
    
UTF-8를 기본으로 지원한다.
    - 2.x
        ASCII str를 기본으로 한다.
        ex) type("hello") #<type 'str'>
              type(u"hello") #<type 'unicode'>
    - 3.x
        UTF-8 유니코드를 기본으로 한다.
        ex) type("hello") #<class 'str'>
              type(u"hello") #<class 'str'>






"""






