def settings(title, **kwargs):
    print 'title:', title
    for key in kwargs:
        print '    %s: %s' % (key, kwargs[key])

settings('nothing extra')
settings('colors', red=0.0, green=0.5, blue=1.0)
