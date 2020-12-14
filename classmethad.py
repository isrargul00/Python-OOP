class cilent:

    def __init__(self,name):
        self.name = name


    def get_name(self):
        return self.name


    @classmethod
    def name(cls):
        print(cls.name)



obj = cilent('john')

print(obj.get_name())

cilent.name()
