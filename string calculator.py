import re

class StringAdditionCalculator:
    def __init__(self, input_string):
        self.input_string = input_string

    def add(self):
        if not self.input_string:
            return 0

        # 커스텀 구분자 처리
        delimiters = [',', ':']
        custom_delimiter_match = re.match(r"//(.+)\n(.*)", self.input_string)
        if custom_delimiter_match:
            custom_delimiter = custom_delimiter_match.group(1)
            self.input_string = custom_delimiter_match.group(2)
            delimiters.append(re.escape(custom_delimiter))

        # 구분자를 기준으로 숫자 추출
        numbers = re.split('|'.join(delimiters), self.input_string)
        return self.calculate_sum(numbers)

    def calculate_sum(self, numbers):
        total = 0
        negatives = []

        for num in numbers:
            if num:
                value = int(num)
                if value < 0:
                    negatives.append(value)
                total += value

        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

        return total


# 사용자 입력 받기
input_string = input("계산할 문자열을 입력하세요: ")

try:
    calculator = StringAdditionCalculator(input_string)
    result = calculator.add()
    print(f"Result: {result}")
except ValueError as e:
    print(e)
