class Greeting(object):
    def say(self, name):
        print 'Hello, %s!' % name

if __name__ == '__main__':
    greet = Greeting()
    greet.say('object')
