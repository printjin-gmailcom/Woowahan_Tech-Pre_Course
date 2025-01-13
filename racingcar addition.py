import random

class Car:
    def __init__(self, name, performance=0.5):
        if len(name) > 5:
            raise ValueError("자동차 이름은 5자 이하만 가능합니다.")
        self.name = name
        self.position = 0
        self.wins = 0
        self.performance = performance  # 성능 추가: 0.0 ~ 1.0, 높을수록 잘 전진
        self.fuel = 10  # 기본 연료 값
        self.condition = 100  # 자동차 상태 (100이 최고 상태)

    def advance(self):
        if self.fuel > 0 and self.condition > 30:  # 연료가 있고, 상태가 30 이상일 때만 전진
            self.position += 1
            self.fuel -= 1  # 연료 소모

    def get_position_string(self):
        return "-" * self.position

    def reset_position(self):
        self.position = 0
        self.fuel = 10  # 연료를 초기화

    def increment_wins(self):
        self.wins += 1

    def repair(self):
        self.condition = 100  # 상태를 복구

class RacingGame:
    MINIMUM_ADVANCE_CONDITION = 4

    def __init__(self):
        self.cars = []
        self.records = []
        self.track_condition = random.choice(["dry", "wet", "icy"])  # 경기 환경 추가
        self.weather = random.choice(["clear", "rain", "fog"])  # 날씨 추가

    def start(self):
        while True:
            self.run_race()

            print("\n경주 기록:")
            self.show_all_records()

            print("\n자동차별 승리 횟수:")
            self.show_car_wins()

            if not self.ask_to_restart():
                break

    def run_race(self):
        car_names_input = self.input_car_names()
        self.create_cars(car_names_input)

        number_of_rounds = self.input_number_of_rounds()
        round_records = []

        print(f"\n오늘의 경기 환경: 트랙 상태는 '{self.track_condition}', 날씨는 '{self.weather}'입니다.\n")

        for round_number in range(1, number_of_rounds + 1):
            print(f"\n{round_number}번째 라운드 진행 중...")
            self.race_cars()
            self.print_race_result()

            round_records.append(self.save_round_result())

        self.records.append(round_records)
        self.announce_winners()
        self.reset_cars()

    def input_car_names(self):
        while True:
            car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분): ")
            car_names_list = car_names.split(",")
            if self.is_valid_car_names(car_names_list):
                return car_names_list

    def is_valid_car_names(self, car_names):
        if len(set(car_names)) != len(car_names):
            print("자동차 이름에 중복이 있습니다. 다시 입력하세요.")
            return False
        if any(name.strip() == "" for name in car_names):
            print("빈 이름이 있습니다. 다시 입력하세요.")
            return False
        return True

    def input_number_of_rounds(self):
        while True:
            try:
                return int(input("시도할 횟수는 몇 회인가요?: "))
            except ValueError:
                print("유효하지 않은 입력입니다. 숫자를 입력하세요.")

    def create_cars(self, car_names_input):
        for name in car_names_input:
            # 각 자동차에 성능과 기본 연료 추가
            performance = random.uniform(0.4, 0.9)  # 0.4 ~ 0.9 사이의 성능 값 랜덤 생성
            self.cars.append(Car(name.strip(), performance))

    def race_cars(self):
        for car in self.cars:
            random_value = random.randint(0, 9)
            weather_effect = self.get_weather_effect()
            track_effect = self.get_track_effect()

            # 성능과 날씨, 트랙 조건을 반영한 이동 조건
            if random_value >= self.MINIMUM_ADVANCE_CONDITION * car.performance * weather_effect * track_effect:
                car.advance()

            # 자동차 상태 랜덤 저하
            car.condition -= random.randint(1, 10)

            if car.condition <= 30:
                print(f"{car.name}의 상태가 좋지 않아 이동이 느려집니다!")

    def get_weather_effect(self):
        if self.weather == "rain":
            return 0.8  # 비가 올 경우 이동 속도가 느려짐
        elif self.weather == "fog":
            return 0.9  # 안개일 경우 속도 약간 저하
        return 1.0  # 맑을 때는 영향 없음

    def get_track_effect(self):
        if self.track_condition == "wet":
            return 0.8  # 젖은 트랙일 경우 이동이 느려짐
        elif self.track_condition == "icy":
            return 0.7  # 얼음 트랙일 경우 더 느려짐
        return 1.0  # 건조한 트랙일 때는 영향 없음

    def print_race_result(self):
        for car in self.cars:
            print(f"{car.name} : {car.get_position_string()} (연료: {car.fuel}, 상태: {car.condition})")

    def save_round_result(self):
        return {car.name: car.position for car in self.cars}

    def announce_winners(self):
        max_position = max(car.position for car in self.cars)
        winners = [car for car in self.cars if car.position == max_position]
        for winner in winners:
            winner.increment_wins()

        winner_names = ", ".join([winner.name for winner in winners])
        print(f"\n최종 우승자 : {winner_names}")

    def reset_cars(self):
        for car in self.cars:
            car.reset_position()

    def show_all_records(self):
        for race_number, race_record in enumerate(self.records, 1):
            print(f"\n{race_number}번째 경주 기록:")
            for round_number, round_record in enumerate(race_record, 1):
                print(f"  {round_number}번째 라운드: {round_record}")

    def show_car_wins(self):
        for car in self.cars:
            print(f"{car.name}의 승리 횟수: {car.wins}")

    def ask_to_restart(self):
        while True:
            restart_input = input("\n다시 경주를 하시겠습니까? (y/n): ").lower()
            if restart_input == 'y':
                return True
            elif restart_input == 'n':
                return False
            else:
                print("잘못된 입력입니다. y 또는 n을 입력하세요.")

if __name__ == "__main__":
    game = RacingGame()
    game.start()
