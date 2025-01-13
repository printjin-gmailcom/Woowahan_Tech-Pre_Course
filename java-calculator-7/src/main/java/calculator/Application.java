package calculator;

import camp.nextstep.edu.missionutils.Console;

public class Application {

    public static void main(String[] args) {
        // 사용자 입력 받기
        System.out.println("덧셈할 문자열을 입력해 주세요.");
        String input = Console.readLine();

        try {
            int result = add(input);
            System.out.println("결과 : " + result);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    // 문자열 덧셈 계산기 함수
    public static int add(String input) {
        if (input == null || input.isEmpty()) {
            return 0; // 빈 문자열일 경우 0 반환
        }

        // 커스텀 구분자 처리
        String delimiter = ",|:"; // 기본 구분자 (쉼표와 콜론)
        if (input.startsWith("//")) {
            int delimiterIndex = input.indexOf("\n");
            if (delimiterIndex == -1) {
                throw new IllegalArgumentException("잘못된 구분자 형식입니다."); // 구분자가 잘못된 경우 예외 처리
            }
            delimiter = input.substring(2, delimiterIndex); // 커스텀 구분자 추출
            input = input.substring(delimiterIndex + 1); // 구분자 이후의 입력값 추출
        }

        // 구분자를 기준으로 숫자를 분리하고 더하기
        String[] tokens = input.split(delimiter);
        int sum = 0;
        for (String token : tokens) {
            if (!token.isEmpty()) { // 빈 문자열이 아닌 경우만 처리
                int number = toPositiveInt(token);
                sum += number;
            }
        }

        return sum;
    }

    // 음수 값이 들어오면 예외 처리
    private static int toPositiveInt(String token) {
        int number;
        try {
            number = Integer.parseInt(token); // 숫자 변환
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("잘못된 숫자 형식입니다: " + token); // 숫자가 아닐 경우 예외 처리
        }

        if (number < 0) {
            throw new IllegalArgumentException("음수는 입력할 수 없습니다."); // 음수일 경우 예외 처리
        }
        return number;
    }
}
