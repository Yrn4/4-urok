
from abc import ABC, abstractmethod
class DataProcessor(ABC):
    def __init__(self, data):
        self.data= data

    @abstractmethod
    def process(self):
        pass

    @staticmethod
    def validate_data(data):
        return isinstance(data, list) and len(data) > 0

    @staticmethod
    def format_output(result):
        return f"Результат: {result}"

class NumberProcessor(DataProcessor):
    def process(self):
        if not self.validate_data(self.data
):
            print("Некорректноые данные")
        return sum(self.data
)

processor = NumberProcessor([1, 2, 3, 4, 5])
result = processor.process()
print(NumberProcessor.format_output(result))