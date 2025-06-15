# bmi_calculator.py

# 사용자로부터 키와 몸무게 입력 받기
height_cm = float(input("당신의 키(cm)를 입력하세요: "))
weight_kg = float(input("당신의 몸무게(kg)를 입력하세요: "))

# cm를 m로 변환
height_m = height_cm / 100

# BMI 계산
bmi = weight_kg / (height_m ** 2)

# 결과 출력
print(f"당신의 BMI는 {bmi:.2f} 입니다.")


# BMI 등급 분류
if bmi < 18.5:
    category = "저체중"
elif bmi < 23:
    category = "정상"
elif bmi < 25:
    category = "과체중"
else:
    category = "비만"

print(f"당신은 '{category}'입니다.")
