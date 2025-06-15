from datetime import datetime

# 사용자 입력 받기
diary = input("오늘 하루는 어땠나요?\n")

# 현재 날짜+시간 구하기
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")  # 파일명용
display_time = now.strftime("%Y-%m-%d %H:%M:%S")  # 내용용

# 새로운 파일 생성해서 저장
with open(f"{timestamp}_diary.txt", "w", encoding="utf-8") as file:
    file.write(f"[{display_time}]\n")
    file.write(diary + "\n")

print(f"{timestamp}_diary.txt 파일에 일기가 저장되었습니다!")
import os
print("현재 경로:", os.getcwd())
