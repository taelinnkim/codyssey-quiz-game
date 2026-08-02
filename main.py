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
DEFAULT_QUIZZES = [
    Quiz(
        "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
        ["input()", "print()", "open()", "return()"],
        2,
    ),
        Quiz(
        "사용자의 키보드 입력을 받을 때 사용하는 함수는?",
        ["input()", "print()", "type()", "len()"],
        1,
    ),
        Quiz(
        "Python에서 여러 값을 순서대로 저장하는 자료형은?",
        ["int", "bool", "list", "str"],
        3,
    ),
        Quiz(
        "조건에 따라 다른 코드를 실행할 때 사용하는 문법은?",
        ["if", "for", "class", "import"],
        1,
    ),
        Quiz(
        "Git에서 변경사항을 하나의 기록으로 저장하는 명령어는?",
        ["git pull", "git clone", "git commit", "git status"],
        3,
    ),
]
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.high_score = 0

    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            quiz.display()

            while True:
                user_input = input("정답 번호를 입력하세요 (1~4): ").strip()

                if user_input == "":
                        print("입력값이 없습니다. 1~4 사이의 숫자를 입력하세요.")
                        continue

                try:
                        user_answer = int(user_input)
                except ValueError:
                        print("숫자만 입력할 수 있습니다.")
                        continue

                if 1 <= user_answer <= 4:
                        break

                print("1~4 사이의 숫자를 입력하세요.")

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n최종 점수: {score}/{len(self.quizzes)}")       

        if score > self.high_score:
            self.high_score = score
            print("새로운 최고 점수입니다!")

    def show_score(self):
        print(f"현재 최고 점수: {self.high_score}/{len(self.quizzes)}")
            
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
    game = QuizGame(DEFAULT_QUIZZES)

    while True:
        show_menu()
        selected_menu = get_menu_choice()

        if selected_menu == 1:
             game.play_quiz()
        elif selected_menu == 2:
            print("퀴즈 추가 기능을 선택했습니다.")
        elif selected_menu == 3:
            print("퀴즈 목록 기능을 선택했습니다.")
        elif selected_menu == 4:
            game.show_score()
        elif selected_menu == 5:
            print("퀴즈 게임을 종료합니다.")
            break


main()