import re
import logging

# 로깅 설정
logging.basicConfig(filename='calculator_errors.log', level=logging.ERROR)

def add(numbers: str, delimiter=',') -> int:
    try:
        # 커스텀 구분자 처리
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        # 입력 검증: 빈 문자열일 경우 0 반환
        if not numbers:
            return 0

        # 구분자를 기준으로 숫자 분리 (기본은 ','와 '\n')
        number_list = re.split(f"[{delimiter}\n]", numbers)
        
        # 숫자 이외의 입력이 있을 경우 예외 처리
        try:
            number_list = list(map(int, number_list))  # 문자열을 숫자로 변환
        except ValueError:
            logging.error(f"Non-integer value found in input: {numbers}")
            raise ValueError("All inputs must be integers.")

        # 음수 체크 및 에러 로깅
        negatives = [n for n in number_list if n < 0]
        if negatives:
            logging.error(f"Negative numbers detected: {negatives}")
            raise ValueError(f"Negatives not allowed: {negatives}")

        # 1000 이상의 숫자는 무시하는 기능 추가
        number_list = [n for n in number_list if n <= 1000]

        # 숫자의 합 계산
        return sum(number_list)

    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Exception: {e}")
        return None

def format_result(result, decimal_places=2):
    """결과를 소수점 자리까지 포맷하여 출력"""
    if result is None:
        return "No result due to error."
    return f"The result is: {result:.{decimal_places}f}"

# 유닛 테스트 코드 추가
import unittest

class TestStringAdditionCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_ignore_large_numbers(self):
        self.assertEqual(add("2,1001"), 2)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            add("1,-2")

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            add("1,abc")

if __name__ == '__main__':
    unittest.main()
