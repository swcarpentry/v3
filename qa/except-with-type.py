values = [0, 1, 'momentum']
for i in range(4):
    try:
        print 'dividing by value', i
        x = 1.0 / values[i]
        print 'result is', x
    except ZeroDivisionError, e:
        print 'divide by zero:', e
    except IndexError, e:
        print 'index error:', e
    except:
        print 'some other error:', e
