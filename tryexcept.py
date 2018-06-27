def tryexcept():
    a=10
    b=0
    try:
        c=a/b
        print c
    except ZeroDivisionError:
        print "div by zero"

    print "out side tryexcept"

tryexcept()
