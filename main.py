class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

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


def main():
    while True:
        show_menu()
        selected_menu = get_menu_choice()

        if selected_menu == 1:
            print("퀴즈 풀기 기능을 선택했습니다.")
        elif selected_menu == 2:
            print("퀴즈 추가 기능을 선택했습니다.")
        elif selected_menu == 3:
            print("퀴즈 목록 기능을 선택했습니다.")
        elif selected_menu == 4:
            print("점수 확인 기능을 선택했습니다.")
        elif selected_menu == 5:
            print("퀴즈 게임을 종료합니다.")
            break


main()