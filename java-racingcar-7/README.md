# 자동차 경주 게임 (Java)

## 프로젝트 개요

이 프로젝트는 Java를 사용하여 구현된 간단한 자동차 경주 게임입니다. 사용자가 입력한 자동차 이름과 시도 횟수에 따라 자동차들이 전진하며 우승자를 가립니다.

## 기능 요구 사항

- 사용자는 경주할 자동차의 이름을 입력할 수 있습니다. 각 이름은 쉼표로 구분되며 5자 이하로 제한됩니다.
- 경주할 횟수를 입력합니다.
- 각 자동차는 무작위 값을 통해 전진하거나 멈춥니다. 무작위 값이 4 이상일 때만 전진합니다.
- 각 라운드가 끝날 때마다 자동차의 전진 상태가 출력됩니다.
- 경주가 끝나면 가장 멀리 이동한 자동차(들)가 우승자로 출력됩니다.

## 입력 형식

1. 경주할 자동차 이름을 입력하세요. (이름은 쉼표로 구분):
   - 예시: `pobi,woni,jun`
2. 시도할 횟수를 입력하세요:
   - 예시: `5`

## 출력 형식

- 각 라운드 결과 예시:

  ```
  pobi : --
  woni : ----
  jun : ---
  ```

- 최종 우승자 출력 예시:
  ```
  최종 우승자 : pobi, jun
  ```

## 기술 스택

- **Java 21**
- **Gradle** (빌드 도구)
- **JUnit 5** (테스트 도구)

## 실행 방법

1. 프로젝트를 클론합니다.

   ```bash
   git clone https://github.com/woowacourse-precourse/java-racingcar-7.git
   cd java-racingcar-7

   ```

2. Gradle을 사용하여 테스트 및 빌드를 실행합니다.
   bash
   코드 복사
   ./gradlew clean test # (Mac/Linux)
   gradlew.bat clean test # (Windows)

3. Application.java 파일을 실행하여 프로그램을 시작합니다.

   

## **관련 사이트**
https://www.woowacourse.io/
- https://github.com/woowacourse-precourse/java-racingcar-7
