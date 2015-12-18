

class Ding(object):
    name = None

    def __init__(self):
        self.name = 'qusi'


class B(Ding):
    def __init__(self):
        super(B, self).__init__()

    def pp(self):
        print super(B, self).name

    def pp2(self):
        print self.name

cc = B()
cc.pp()
cc.pp2()
