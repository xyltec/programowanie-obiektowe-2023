

class A:

    def __init__(self, content_type: str):
        self.__content_type = content_type

    def get_content_type(self):
        return self.__content_type

    def __foo(self):
        print('oh no!')



a = A('water')
# a.__foo()

a.__content_type = 'sake'

print(a.get_content_type())

print(a.__dict__)