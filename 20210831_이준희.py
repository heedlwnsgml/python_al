
# coding: utf-8

# In[3]:


import random
import json

# 1. 학생 정보 생성 및 저장
def generate_students(num_students=30, save_to_file=False, filename=" "):
    students = []
    for _ in range(num_students):
        name = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    if save_to_file:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)
    return students

# 2. 정렬 알고리즘
# 선택 정렬
def selection_sort(data, key, step=False):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j][key] < data[min_idx][key]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        if step:
            print(f"Step {i + 1}: {data}\n")
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

# 기수 정렬 (계수 정렬 포함)
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

    # 계수 생성
    for student in data:
        index = (student[key] // exp) % 10
        count[index] += 1

    # 누적합 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 출력 배열 생성
    for i in range(n - 1, -1, -1):
        index = (data[i][key] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    # 정렬된 배열 복사
    for i in range(n):
        data[i] = output[i]

    if step:
        print(f"After exp {exp}: {data}\n")

# 3. 메뉴 및 사용자 입력
def main():
    file_name = input("파일 이름을 입력하세요 (확장자 없이 입력하세요): ")
    
    # 파일명이 확장자를 포함하지 않으면 '.json' 추가
    if not file_name.endswith(".json"):
        file_name += ".json"
    
    students = generate_students(30, save_to_file=True, filename=file_name)  # 30명의 학생 데이터를 생성 및 저장
    history = []  # 사용자 선택 내역을 기록할 리스트

    while True:
        print("\n=== 학생 성적 관리 시스템 ===")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 종료")
        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ")

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        key_map = {"1": "이름", "2": "나이", "3": "성적"}
        if choice in key_map:
            key = key_map[choice]
            user_choice = {"정렬 기준": key}  # 사용자의 선택 저장
            while True:
                
                if choice == "3":
                    while True:
                        print("\n1. 선택 정렬")
                        print("2. 삽입 정렬")
                        print("3. 퀵 정렬")
                        print("4. 기수 정렬")
                        algo_choice = input("정렬 알고리즘을 선택하세요 (1, 2, 3, 4): ")
                        if algo_choice in ["1", "2", "3", "4"]:
                            user_choice["알고리즘"] = algo_choice  # 선택한 알고리즘 저장
                            break
                        else:
                            print("잘못된 입력입니다. 1, 2, 3, 4 중 하나를 입력해주세요.\n")
                else:
                    while True:
                        print("\n1. 선택 정렬")
                        print("2. 삽입 정렬")
                        print("3. 퀵 정렬")
                        algo_choice = input("정렬 알고리즘을 선택하세요 (1, 2, 3): ")
                        if algo_choice in ["1", "2", "3"]:  # 1, 2, 3 중 하나가 입력되면
                            user_choice["알고리즘"] = algo_choice  # 선택한 알고리즘 저장
                            break  # 유효한 입력이면 반복 종료
                        else:
                            print("잘못된 입력입니다. 1, 2, 3 중 하나를 입력해주세요.\n")

                algorithms = {"1": selection_sort, "2": insertion_sort, "3": quick_sort, "4": radix_sort}
                if algo_choice in algorithms:
                    # 단계별 출력 여부 확인
                    while True:
                        step = input("단계별 출력을 보시겠습니까? (y/n): ").lower()
                        if step == "y" or step == "n":
                            step = step == "y"  # "y"이면 True, "n"이면 False
                            user_choice["단계별 출력"] = step  # 단계별 출력 여부 저장
                            break
                        else:
                            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")
                    
                    data_copy = students.copy()
                    if algo_choice == "4" and key != "성적":
                        print("기수 정렬은 성적 기준으로만 사용 가능합니다.")
                    else:
                        sorted_data = algorithms[algo_choice](data_copy, key, step)
                        print("\n=== 정렬 결과 ===")
                        for student in sorted_data:
                            print(student)
                        
                        # 사용자 선택 내역에 정렬된 데이터를 추가
                        user_choice["정렬 결과"] = sorted_data
                        history.append(user_choice)  # 사용자가 선택한 내역과 결과를 기록
                    break
                else:
                    print("잘못된 입력입니다. 정렬 메뉴를 다시 선택하세요.")
        else:
            print("잘못된 입력입니다. 처음 메뉴로 돌아갑니다.")

    # 사용자가 종료한 후 선택 내역을 파일로 저장
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
    print(f"사용자의 선택 내역과 실행 결과가 '{file_name}' 파일에 저장되었습니다.")


if __name__ == "__main__":
    main()

