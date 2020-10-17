class NotRealizedMethodError(Exception):
    def __init__(self, message="Метод не реализован."):
        self.__message = message
        super().__init__(self.__message)
