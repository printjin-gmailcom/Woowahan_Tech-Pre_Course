물론입니다! **로또 프로그램**을 위한 README를 자동차 경주 게임 설명 형식처럼 작성해 드리겠습니다.

---

# 로또 번호 생성기 (Python)

## 개요

이 프로젝트는 Python을 사용하여 로또 번호를 생성하고 당첨 결과를 계산하는 프로그램입니다. 기본적인 로또 번호 생성 기능 외에도 다양한 추가 기능을 통해 사용자 경험을 개선했습니다. 사용자가 입력한 구입 금액에 따라 로또 번호를 생성하며, 당첨 번호와 보너스 번호를 입력받아 결과를 출력합니다.

---

## 기능 요구 사항 (기본 기능)

- **구입 금액 입력**: 사용자는 구입할 로또의 총 금액을 입력합니다. 1장당 1,000원이며, 입력한 금액에 따라 구매 가능한 로또 개수가 결정됩니다.
- **로또 번호 생성**: 각 로또는 1부터 45 사이의 중복되지 않는 6개의 숫자로 구성됩니다.
- **당첨 번호 입력**: 사용자는 1부터 45 사이의 숫자로 구성된 당첨 번호 6개를 입력합니다.
- **보너스 번호 입력**: 추가로 보너스 번호 1개를 입력받습니다.
- **당첨 결과 확인**: 사용자가 구매한 로또와 당첨 번호를 비교하여 당첨 내역과 등수를 확인합니다.
- **수익률 계산**: 총 구매 금액 대비 수익률을 계산하여 출력합니다.

---

## 입력 형식

1. 구입 금액을 입력합니다. (1,000원 단위로 입력)
   - 예시: `8000`
2. 당첨 번호를 입력합니다. (쉼표로 구분된 숫자 6개)
   - 예시: `1,2,3,4,5,6`
3. 보너스 번호를 입력합니다.
   - 예시: `7`

---

## 출력 형식

1. **로또 번호 출력**: 입력한 금액에 따라 생성된 로또 번호들이 출력됩니다.
   - 예시:
     ```plaintext
     8개를 구매했습니다.
     [8, 21, 23, 41, 42, 43]
     [3, 5, 11, 16, 32, 38]
     ...
     ```
2. **당첨 내역 출력**: 각 등수에 해당하는 당첨 횟수를 표시합니다.
   - 예시:
     ```plaintext
     3개 일치 (5,000원) - 1개
     4개 일치 (50,000원) - 0개
     5개 일치 (1,500,000원) - 0개
     5개 일치, 보너스 볼 일치 (30,000,000원) - 0개
     6개 일치 (2,000,000,000원) - 0개
     ```
3. **수익률 출력**: 총 수익률을 계산하여 표시합니다.
   - 예시: `총 수익률은 62.5%입니다.`

---

## 추가 기능 사항

- **자동/수동 선택 기능**: 로또 번호를 자동으로 생성하거나, 사용자가 직접 번호를 입력하여 수동으로 구매할 수 있습니다.
- **구입 내역 저장 및 불러오기**: 로또 구매 내역을 파일에 저장하고, 프로그램 종료 후에도 재실행 시 불러와서 확인할 수 있습니다.
- **상세 결과 기록 및 통계**: 각 당첨 번호에 대한 당첨 횟수와 누적 수익률을 저장하여 통계로 제공합니다.
- **보너스 게임 기능**: 일정 당첨 금액 이상을 달성하면 추가 보너스 게임을 무료로 제공합니다.
- **로또 번호 히스토리 조회 기능**: 사용자가 지금까지 구매한 로또 번호의 기록을 조회할 수 있습니다.
- **최대 구매 제한**: 구매 가능한 최대 로또 장수를 제한하여 지나치게 많은 구매를 방지합니다 (예: 최대 100장).
- **결과 파일 저장 기능**: 당첨 결과와 수익률을 파일에 기록하여 향후 기록으로 남길 수 있습니다.
- **다양한 출력 포맷 지원**: 결과를 소수점 자리수 설정 등으로 포맷팅하여 깔끔하게 출력할 수 있습니다.

---

## 기술 스택

- Python 3.8+

---

## 실행 방법

1. 프로젝트 파일을 클론합니다.

   ```bash
   git clone https://github.com/your-username/python-lotto-enhanced.git
   cd python-lotto-enhanced
   ```

2. 프로그램을 실행합니다.

   ```bash
   python lotto.py
   ```

3. **구입 금액**, **당첨 번호**, **보너스 번호**를 입력하여 결과를 확인합니다.

---

이 README는 로또 프로그램의 사용 방법과 주요 기능을 쉽게 이해할 수 있도록 구성되었습니다. 필요 시 이 README를 기반으로 추가 기능 설명이나 예시를 추가하여 사용자 안내를 보강할 수 있습니다.