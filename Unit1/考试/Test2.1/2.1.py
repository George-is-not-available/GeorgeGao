class A:
    def __test(self , a):
        print(a)

    def test(self , a):
        self.__test(a)


A().test(1)