for num in [-1, 0, 1]:
    try:
        inverse = 1/num
    except:
        print 'inverting', num, 'caused error'
    else:
        print 'inverse of', num, 'is', inverse
