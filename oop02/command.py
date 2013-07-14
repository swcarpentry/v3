# base:start
class AbstractCommand(object):
    '''Base class for commands.'''
    def is_undoable(self):
        return False # by default, can't undo/redo operations
    def do(self, robot):
        raise NotImplementedError("Don't know how to do %s" % self.name)
    def undo(self, robot):
        pass
    def redo(self, robot):
        pass
# base:end

# move:start
class MoveCommand(AbstractCommand):
    '''Move the robot arm.'''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_undoable(self):
        return True

    def do(self, robot):
        robot.translate(self.x, self.y, self.z)

    def undo(self, robot):
        robot.translate(-self.x, -self.y, -self.z)

    def redo(self, robot):
        self.do(robot)
# move:end

# test:start
robot = Robot()
commands = [MoveCommand(5.0, 2.0, 2.3),
            RotateCommand(-90.0, 0.0, 0.0),
            MoveCommand(1.0, 2.0, 2.0),
            CloseHandCommand()]
for c in commands:
    c.do(robot)
# test:end
