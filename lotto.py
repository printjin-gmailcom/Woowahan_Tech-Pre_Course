import random

class Lotto:
    def __init__(self, numbers):
        self.validate(numbers)
        self.numbers = sorted(numbers)

    def validate(self, numbers):
        if len(numbers) != 6:
            raise ValueError("[ERROR] 로또 번호는 6개여야 합니다.")
        if len(set(numbers)) != len(numbers):
            raise ValueError("[ERROR] 로또 번호에 중복된 숫자가 있습니다.")
        for number in numbers:
            if number < 1 or number > 45:
                raise ValueError("[ERROR] 로또 번호는 1부터 45 사이의 숫자여야 합니다.")

    def get_match_count(self, other):
        return len(set(self.numbers) & set(other.numbers))

class Prize:
    FIRST = (6, False, 2_000_000_000, "6개 일치 (2,000,000,000원)")
    SECOND = (5, True, 30_000_000, "5개 일치, 보너스 볼 일치 (30,000,000원)")
    THIRD = (5, False, 1_500_000, "5개 일치 (1,500,000원)")
    FOURTH = (4, False, 50_000, "4개 일치 (50,000원)")
    FIFTH = (3, False, 5_000, "3개 일치 (5,000원)")
    NONE = (0, False, 0, "당첨되지 않음")

    @staticmethod
    def get_prize(match_count, bonus_match):
        for prize in [Prize.FIRST, Prize.SECOND, Prize.THIRD, Prize.FOURTH, Prize.FIFTH]:
            if prize[0] == match_count and prize[1] == bonus_match:
                return prize
        return Prize.NONE

def get_purchase_amount():
    while True:
        try:
            amount = int(input("구입금액을 입력해 주세요: "))
            if amount % 1000 != 0:
                raise ValueError
            return amount
        except ValueError:
            print("[ERROR] 구입 금액은 1,000원 단위여야 합니다.")

def purchase_lottos(amount):
    count = amount // 1000
    print(f"{count}개를 구매했습니다.")
    lottos = [Lotto(random.sample(range(1, 46), 6)) for _ in range(count)]
    for lotto in lottos:
        print(lotto.numbers)
    return lottos

def get_winning_lotto():
    while True:
        try:
            numbers = list(map(int, input("당첨 번호를 입력해 주세요: ").split(",")))
            return Lotto(numbers)
        except ValueError as e:
            print("[ERROR]", e)

def get_bonus_number():
    while True:
        try:
            bonus = int(input("보너스 번호를 입력해 주세요: "))
            if bonus < 1 or bonus > 45:
                raise ValueError
            return bonus
        except ValueError:
            print("[ERROR] 보너스 번호는 1부터 45 사이의 숫자여야 합니다.")

def check_winning(purchased_lottos, winning_lotto, bonus_number):
    results = {Prize.FIRST: 0, Prize.SECOND: 0, Prize.THIRD: 0, Prize.FOURTH: 0, Prize.FIFTH: 0, Prize.NONE: 0}
    for lotto in purchased_lottos:
        match_count = lotto.get_match_count(winning_lotto)
        bonus_match = bonus_number in lotto.numbers
        prize = Prize.get_prize(match_count, bonus_match)
        results[prize] += 1
    return results

def display_results(results, purchase_amount):
    print("당첨 통계\n---")
    total_prize = 0
    for prize, count in results.items():
        print(f"{prize[3]} - {count}개")
        total_prize += count * prize[2]
    profit_rate = (total_prize / purchase_amount) * 100
    print(f"총 수익률은 {profit_rate:.1f}%입니다.")

def main():
    purchase_amount = get_purchase_amount()
    purchased_lottos = purchase_lottos(purchase_amount)

    winning_lotto = get_winning_lotto()
    bonus_number = get_bonus_number()

    results = check_winning(purchased_lottos, winning_lotto, bonus_number)
    display_results(results, purchase_amount)

if __name__ == "__main__":
    main()
