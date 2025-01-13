import random

class Car:
    def __init__(self, name):
        if len(name) > 5:
            raise ValueError("자동차 이름은 5자 이하만 가능합니다.")
        self.name = name
        self.position = 0

    def advance(self):
        self.position += 1

    def get_position_string(self):
        return "-" * self.position


class RacingGame:
    MINIMUM_ADVANCE_CONDITION = 4

    def __init__(self):
        self.cars = []

    def start(self):
        car_names_input = self.input_car_names()
        self.create_cars(car_names_input)

        number_of_rounds = self.input_number_of_rounds()

        for _ in range(number_of_rounds):
            self.race_cars()
            self.print_race_result()

        self.announce_winners()

    def input_car_names(self):
        car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분): ")
        return car_names.split(",")

    def input_number_of_rounds(self):
        return int(input("시도할 횟수는 몇 회인가요?: "))

    def create_cars(self, car_names_input):
        for name in car_names_input:
            self.cars.append(Car(name.strip()))

    def race_cars(self):
        for car in self.cars:
            random_value = random.randint(0, 9)
            if random_value >= self.MINIMUM_ADVANCE_CONDITION:
                car.advance()

    def print_race_result(self):
        for car in self.cars:
            print(f"{car.name} : {car.get_position_string()}")
        print()

    def announce_winners(self):
        max_position = max(car.position for car in self.cars)
        winners = [car.name for car in self.cars if car.position == max_position]
        print("최종 우승자 : " + ", ".join(winners))


if __name__ == "__main__":
    game = RacingGame()
    game.start()
