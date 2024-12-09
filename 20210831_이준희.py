
# coding: utf-8

# # #. 정렬 알고리즘을 이용한 기말 프로그래밍 과제
# - 과제 주제: 학생 성적 관리 시스템
#     - 학생 성적 데이터가 주어졌을 때, 다양한 정렬 알고리즘을 활용해 데이터를 정렬하고 분석하는 프로그램을 작성하세요.
#     - 이 과제를 통해 정렬 알고리즘의 원리를 이해하고, 실제 데이터에 적용하는 방법을 익히게 됩니다.
# - 과제 요구사항
#   - 학생 정보 생성 및 저장:
#     - 30명의 학생 정보를 무작위로 생성하세요. 각 학생의 정보는 다음과 같습니다:
#       - 이름: 알파벳 대문자 두 글자 (예: AB, CD)
#       - 나이: 18 ~ 22 사이의 정수
#       - 성적: 0 ~ 100 사이의 정수
#       - 생성된 학생 정보를 리스트에 저장하세요. 각 학생의 정보는 딕셔너리 형태({"이름": "AB", "나이": 19, "성적": 85})로 저장합니다.
# 
#   - 정렬 기능 구현:
#     - 다음 네 가지 정렬 알고리즘을 구현하세요.
#       - 선택 정렬, 삽입 정렬, 퀵 정렬
#       - 기수 정렬 (성적 기준으로 정렬할 때만 사용 가능)
#     - 각 정렬 알고리즘은 특정 필드를 기준으로 학생 리스트를 정렬할 수 있어야 합니다:
#       - 이름 (알파벳 순서)
#       - 나이 (오름차순)
#       - 성적 (오름차순)
#   
#   - 메뉴 및 사용자 입력:
#     - 프로그램 시작 시, 사용자에게 다음 메뉴를 제공합니다:
#       - 이름을 기준으로 정렬
#       - 나이를 기준으로 정렬
#       - 성적을 기준으로 정렬
#       - 프로그램 종료
#     - 사용자 입력에 따라 정렬 기준과 정렬 알고리즘을 선택하도록 합니다.
#     - 정렬된 결과를 화면에 출력하세요.
# 
#   - 단계별 출력 (선택 사항):
#     - 선택한 정렬 알고리즘의 정렬 과정을 단계별로 출력하는 기능을 구현합니다.
#       - 예를 들어, 선택 정렬의 경우 각 단계마다 리스트 상태를 출력하여 정렬 과정이 어떻게 진행되는지 보여줍니다.
# 
# - 제출물
#     - 코드: 파이썬 파일로 정렬 프로그램의 전체 코드 제출.
#     - 개인 github에 결과물 업로드하기
#     - github 계정(주소)은 cyber 캠퍼스에 업로드하기

# In[ ]:


import random

# 1. 학생 정보 생성
def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 2. 정렬 알고리즘
# 선택 정렬
def selection_sort(data, key, step=False):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j][key] < data[min_idx][key]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        if step:
            print(f"Step {i+1}: {data}\n")
    return data

# 삽입 정렬
def insertion_sort(data, key, step=False):
    for i in range(1, len(data)):
        key_item = data[i]
        j = i - 1
        while j >= 0 and data[j][key] > key_item[key]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item
        if step:
            print(f"Step {i}: {data}\n")
    return data

# 퀵 정렬
def quick_sort(data, key, step=False):
    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            if step:
                print(f"Pivot at index {pivot_index}: {arr}\n")
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high][key]
        i = low - 1
        for j in range(low, high):
            if arr[j][key] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(data, 0, len(data) - 1)
    return data

# 기수 정렬
def radix_sort(data, key, step=False):
    max_val = max(student[key] for student in data)
    exp = 1
    while max_val // exp > 0:
        counting_sort(data, key, exp, step)
        exp *= 10
    return data

def counting_sort(data, key, exp, step):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for student in data:
        index = (student[key] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (data[i][key] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    for i in range(n):
        data[i] = output[i]
    if step:
        print(f"After exp {exp}: {data}\n")

# 3. 메뉴 및 사용자 입력 (수정)
def main():
    students = generate_students(10)  # 예시로 10명의 학생 데이터를 생성
    while True:
        print("\n=== 학생 성적 관리 시스템 ===")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 종료")
        choice = input("정렬기준을 선택하세요 (1, 2, 3, 4): ")

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        key_map = {"1": "이름", "2": "나이", "3": "성적"}
        if choice in key_map:
            key = key_map[choice]
            while True:  # 정렬 메뉴 반복
                print("\n1. 선택 정렬")
                print("2. 삽입 정렬")
                print("3. 퀵 정렬")
                print("4. 기수 정렬 (성적 기준으로 정렬할 때만 사용 가능)")
                algo_choice = input("정렬 알고리즘을 선택하세요 (1, 2, 3, 4): ")

                algorithms = {"1": selection_sort, "2": insertion_sort, "3": quick_sort, "4": radix_sort}
                if algo_choice in algorithms:
                    step = input("단계별 출력을 보시겠습니까? (y/n): ").lower() == "y"
                    data_copy = students.copy()
                    if algo_choice == "4" and key != "성적":
                        print("기수 정렬은 성적 기준으로만 사용 가능합니다.")
                    else:
                        sorted_data = algorithms[algo_choice](data_copy, key, step)
                        print("\n=== 정렬 결과 ===")
                        for student in sorted_data:
                            print(student)
                    break  # 정렬 완료 후 상위 메뉴로 이동
                else:
                    print("잘못된 입력입니다. 정렬 메뉴를 다시 선택하세요.")
        else:
            print("잘못된 입력입니다. 처음 메뉴로 돌아갑니다.")

if __name__ == "__main__":
    main()

