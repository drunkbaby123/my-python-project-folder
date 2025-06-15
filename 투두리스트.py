import json
import os

TODO_FILE = "todo_list.json"

# 저장된 할 일 불러오기
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# 할 일 목록 저장하기
def save_todo_list(todo_list):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(todo_list, file, ensure_ascii=False, indent=2)

# 할 일 출력
def print_todo_list(todo_list):
    print("\n===== 할 일 목록 =====")
    for idx, item in enumerate(todo_list, 1):
        status = "[X]" if item["done"] else "[ ]"
        print(f"{idx}. {status} {item['task']}")
    print("======================")

# 메인 루프
def main():
    todo_list = load_todo_list()

    while True:
        print_todo_list(todo_list)
        print("1) 할 일 추가  2) 완료 체크  3) 삭제  4) 종료")
        choice = input(">> 입력: ")

        if choice == "1":
            task = input("추가할 할 일 내용: ")
            todo_list.append({"task": task, "done": False})

        elif choice == "2":
            num = int(input("완료할 번호: ")) - 1
            if 0 <= num < len(todo_list):
                todo_list[num]["done"] = True

        elif choice == "3":
            num = int(input("삭제할 번호: ")) - 1
            if 0 <= num < len(todo_list):
                todo_list.pop(num)
 
        elif choice == "4":
            save_todo_list(todo_list)
            print("저장 완료! 프로그램 종료.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
