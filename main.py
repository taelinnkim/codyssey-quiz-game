def show_menu():
    print("=" * 40)
    print("        파이썬·컴퓨터 기초 퀴즈")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def get_menu_choice():
    while True:
        user_input = input("메뉴를 선택하세요: ").strip()

        if user_input == "":
            print("입력값이 없습니다. 1~5 사이의 숫자를 입력하세요.")
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print("숫자만 입력할 수 있습니다.")
            continue

        if 1 <= choice <= 5:
            return choice

        print("1~5 사이의 숫자를 입력하세요.")


show_menu()
selected_menu = get_menu_choice()
print(f"선택한 메뉴: {selected_menu}")