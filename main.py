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
    choice = input("메뉴를 선택하세요: ").strip()
    return choice


show_menu()
selected_menu = get_menu_choice()
print(f"선택한 메뉴: {selected_menu}")