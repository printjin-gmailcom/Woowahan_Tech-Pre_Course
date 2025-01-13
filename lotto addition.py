import random
import json
import os
from datetime import datetime

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
            amount = int(input("구입금액을 입력해 주세요 (최대 100,000원): "))
            if amount % 1000 != 0 or amount > 100000:
                raise ValueError
            return amount
        except ValueError:
            print("[ERROR] 구입 금액은 1,000원 단위여야 하며, 최대 100,000원까지 가능합니다.")

def choose_lotto_type():
    choice = input("자동으로 로또 번호를 생성하시겠습니까? (y/n): ")
    return choice.lower() == 'y'

def purchase_lottos(amount, auto=True):
    count = min(amount // 1000, 100)  # 최대 구매 제한 100장
    print(f"{count}개를 구매했습니다.")
    lottos = []
    for _ in range(count):
        if auto:
            numbers = random.sample(range(1, 46), 6)
        else:
            numbers = get_manual_numbers()
        lottos.append(Lotto(numbers))
        print(f"로또 번호: {numbers}")
    return lottos

def get_manual_numbers():
    while True:
        try:
            numbers = list(map(int, input("로또 번호 6개를 입력해 주세요 (쉼표로 구분): ").split(",")))
            return Lotto(numbers).numbers  # validation check
        except ValueError as e:
            print("[ERROR]", e)

def save_purchase(lottos):
    history = load_history()
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "lottos": [lotto.numbers for lotto in lottos]
    }
    history.append(entry)
    with open("purchased_lottos.json", "w") as file:
        json.dump(history, file)
    print("구매한 로또가 저장되었습니다.")

def load_history():
    if os.path.exists("purchased_lottos.json"):
        with open("purchased_lottos.json", "r") as file:
            return json.load(file)
    return []

def save_results_to_file(results, total_prize, purchase_amount):
    results_data = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": {prize.getDescription(): count for prize, count in results.items()},
        "total_prize": total_prize,
        "purchase_amount": purchase_amount,
        "profit_rate": (total_prize / purchase_amount) * 100
    }
    with open("lotto_results.json", "a") as file:
        json.dump(results_data, file)
        file.write("\n")
    print("당첨 결과가 lotto_results.json 파일에 저장되었습니다.")

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

def display_results(results, purchase_amount, decimal_places=2):
    print("당첨 통계\n---")
    total_prize = 0
    for prize, count in results.items():
        print(f"{prize[3]} - {count}개")
        total_prize += count * prize[2]
    profit_rate = round((total_prize / purchase_amount) * 100, decimal_places)
    print(f"총 수익률은 {profit_rate:.{decimal_places}f}%입니다.")
    return total_prize

def display_history():
    history = load_history()
    if not history:
        print("기록된 구매 내역이 없습니다.")
        return
    print("구매 내역:")
    for entry in history:
        print(f"{entry['date']}: {entry['lottos']}")

def bonus_game(purchase_amount):
    if purchase_amount >= 5000000:
        print("축하합니다! 추가 보너스 게임이 제공됩니다.")
        purchase_lottos(1000, auto=True)

def main():
    # 기존에 저장된 구매 내역을 불러옵니다.
    purchased_lottos = load_history()
    if purchased_lottos:
        print("저장된 로또 구매 내역이 있습니다.")
        display_history()

    purchase_amount = get_purchase_amount()
    auto = choose_lotto_type()
    new_lottos = purchase_lottos(purchase_amount, auto)
    save_purchase(new_lottos)

    winning_lotto = get_winning_lotto()
    bonus_number = get_bonus_number()

    results = check_winning(new_lottos, winning_lotto, bonus_number)
    total_prize = display_results(results, purchase_amount, decimal_places=2)
    
    # 결과를 파일에 저장합니다.
    save_results_to_file(results, total_prize, purchase_amount)
    
    # 보너스 게임 조건 확인
    bonus_game(total_prize)

if __name__ == "__main__":
    main()
