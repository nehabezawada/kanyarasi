# An assigned exception is raised.


class A(Exception):
    def __init__(self):
        pass


a = A
raise a
