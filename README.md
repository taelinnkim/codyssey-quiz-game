# Python Console Quiz Game

Python 기초 문법과 컴퓨터 지식을 학습할 수 있는 터미널 기반 퀴즈 게임입니다.

## 주요 기능

- 객관식 퀴즈 풀기
- 정답과 오답 확인
- 퀴즈 추가
- 전체 퀴즈 목록 확인
- 최고 점수 확인
- 퀴즈와 최고 점수를 JSON 파일에 저장
- 프로그램 재실행 시 저장 데이터 불러오기
- 잘못된 입력 예외 처리
- 저장 파일이 없거나 손상된 경우 기본 퀴즈 사용
- `Ctrl+C` 입력 시 안전하게 저장하고 종료

## 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
python3 main.py
```

## 메뉴

```text
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

## 프로젝트 파일

```text
codyssey-quiz-game/
├── main.py
├── state.json
├── README.md
└── .gitignore
```

* `main.py`: 퀴즈 게임 실행 코드
* `state.json`: 퀴즈 목록과 최고 점수 저장
* `README.md`: 프로젝트 설명
* `.gitignore`: Git에서 제외할 파일 설정

## 프로그램 구조

### Quiz 클래스

개별 퀴즈의 문제, 선택지, 정답을 관리합니다.

### QuizGame 클래스

퀴즈 진행, 퀴즈 추가, 점수 확인, JSON 저장 기능을 관리합니다.

## 저장 데이터 예시

```json
{
  "quizzes": [
    {
      "question": "Python에서 화면에 내용을 출력할 때 사용하는 함수는?",
      "choices": [
        "input()",
        "print()",
        "open()",
        "return()"
      ],
      "answer": 2
    }
  ],
  "high_score": 0
}
```

## 개발 환경

* Python 3.12
* Git
* GitHub
* Visual Studio Code

