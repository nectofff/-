import abc
class Match(abc.ABC):
    def __init__(self, a:int|float, b:int|float):
        try:
            self.a = int(a) 
            self.b = int(b)   
        except ValueError:
            self.a = float(a) 
            self.b = float(b)  
        
    
    @abc.abstractmethod
    def operation(self)->int|float:
        return 0

class Summ(Match):
    def operation(self):
        return self.a + self.b
    
class Diff(Match):
    def operation(self):
        return self.a - self.b

class Mult(Match):
    def operation(self):
        return self.a * self.b

class Div(Match):
    def operation(self):
        return self.a / self.b
    
class Percent(Match):
    def operation(self):
        return (self.a * self.b) / 100

class Reader(abc.ABC):
    def __init__(self, commands:list = [0, 0, 0]):
        self.command = commands[0]
        self.a = commands[1]
        self.b = commands[2]
    
    @abc.abstractmethod
    def read(self)->None:
        print("Введите команду:", end ="")
        self.command = input()
        if self.command != "0" and self.command != "6" and self.command != "7": 
            print("Введите первое число:", end ="")
            self.a = input()
            print("Введите второе число:", end ="")
            self.b = input()
        print("\n")

    @abc.abstractmethod
    def get_data(self)->list:
        return [self.command, self.a, self.b]

class ReaderConsole(Reader):
    def read(self)->None:
        super().read()
    def get_data(self):
        return super().get_data()

class Writer(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def user_menu_write()->None:
        pass

    @staticmethod
    @abc.abstractmethod
    def result_write(res):
        pass


class WriterConsole(Writer):
    def user_menu_write():
        print("Команды: \n1:Сумма двух чисел\n2:Разность двух чисел")
        print("3:Умножение чисел\n4:Деление чисел")
        print("5:Нахождение процента от числа(число; процент)")
        print("6:Список истории\n7:История по индексу")
        print("0:Выход")
        print("\nВвод ")

    def result_write(res):
        print("Ответ:", res)
        print("\n")

class OperationHistory(abc.ABC):
    @abc.abstractmethod
    def append_history(self, history:list, result):
        pass

    @abc.abstractmethod
    def get_history(self):
        pass

class OperationHistoryConsole(OperationHistory):
    def __init__(self):
        self.historyList = []
    
    def append_history(self, history:list, result):
        history.append(result)
        self.historyList.append(history)

    def get_history(self):
        for i in range(len(self.historyList)):
            hist = self.historyList[i]
            print(i, "Комманда:", hist[0], "\n  Первое значение:", hist[1], "\n  Второе значение:", hist[2], "\n  Ответ:", hist[3])

        print("\n")
    
    def get_index_history(self, ind):
        if ind > len(self.historyList) or ind < 0:
            print("Ошибка индекса")
        else:
            hist = self.historyList[ind]
            print(ind, "Комманда:", hist[0], "\n  Первое значение:", hist[1], "\n  Второе значение:", hist[2], "\n  Ответ:", hist[3])
            


def main() -> None:
    history = OperationHistoryConsole()    
    while True:
        WriterConsole.user_menu_write()

        rd = ReaderConsole()
        rd.read()

        dataList:list = rd.get_data()
        result = 0

        if dataList[0] == "1": result = Summ(dataList[1], dataList[2]).operation()
        if dataList[0] == "2": result = Diff(dataList[1], dataList[2]).operation()
        if dataList[0] == "3": result = Mult(dataList[1], dataList[2]).operation()
        if dataList[0] == "4": result = Div(dataList[1], dataList[2]).operation()
        if dataList[0] == "5": result = Percent(dataList[1], dataList[2]).operation()
        if dataList[0] == "6": history.get_history()
        if dataList[0] == "7": 
            print("Введите индекс:", end="")
            history.get_index_history(int(input()))

        history.append_history(dataList, result)

        if dataList[0] == "0": break

        WriterConsole.result_write(result)




if __name__ == "__main__":
    main()
