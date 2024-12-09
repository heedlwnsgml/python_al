{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ffe9c5c-43e0-4a5c-acf5-ca8ced054a8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self, elem, next=None):\n",
    "        self.data = elem\n",
    "        self.link = next\n",
    "\n",
    "\n",
    "class Book:  # 도서 추가에 제목과 저자를 같이 하기 위한 클래스\n",
    "    def __init__(self, book_id, title, author, year):\n",
    "        self.book_id = book_id\n",
    "        self.title = title\n",
    "        self.author = author\n",
    "        self.year = year\n",
    "\n",
    "    def __str__(self):  # 도서 제목과 저자를 한 줄로 출력하기 위해\n",
    "        return f\"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]\"\n",
    "\n",
    "\n",
    "class LinkedList:\n",
    "    def __init__(self):\n",
    "        self.head = None  # 빈 단순연결 리스트\n",
    "\n",
    "    def isEmpty(self):\n",
    "        return self.head is None\n",
    "\n",
    "    def display(self):  # 현재 도서 목록 출력\n",
    "        if self.isEmpty():\n",
    "            print(\"현재 등록된 도서가 없습니다.\")\n",
    "            return\n",
    "\n",
    "        print(\"현재 등록된 도서 목록:\")\n",
    "        ptr = self.head\n",
    "        while ptr is not None:\n",
    "            print(ptr.data, end='  ')\n",
    "            ptr = ptr.link\n",
    "        print()\n",
    "\n",
    "    def add_book(self, book_id, title, author, year):  # 새로운 도서를 리스트에 추가한다.\n",
    "        elem = Book(book_id, title, author, year)\n",
    "        node = Node(elem, None)\n",
    "        node.link = self.head\n",
    "        self.head = node\n",
    "        print(f\"도서 '{node.data.title}'가 추가되었습니다.\")\n",
    "\n",
    "    def remove_book(self, title):  # 주어진 책 제목에 해당하는 도서를 리스트에서 삭제한다.\n",
    "        if self.isEmpty():\n",
    "            print(\"삭제할 도서가 없습니다.\")\n",
    "            return\n",
    "\n",
    "        ptr = self.head\n",
    "        before = None\n",
    "\n",
    "        while ptr is not None:\n",
    "            if ptr.data.title == title:\n",
    "                if before is None:  # 첫 번째 노드 삭제\n",
    "                    self.head = ptr.link\n",
    "                else:\n",
    "                    before.link = ptr.link\n",
    "                print(f\"도서 '{title}'가 삭제되었습니다.\")\n",
    "                return\n",
    "            before = ptr\n",
    "            ptr = ptr.link\n",
    "        print(f\"도서 '{title}'가 목록에 없습니다.\")\n",
    "\n",
    "    def find(self, title):  # 주어진 책 제목에 해당하는 도서를 조회하고, 해당 도서의 정보를 출력한다.\n",
    "        ptr = self.head\n",
    "        while ptr is not None:\n",
    "            if ptr.data.title == title:\n",
    "                print(ptr.data)  # 도서 정보 출력\n",
    "                return\n",
    "            ptr = ptr.link\n",
    "        print(f\"도서 '{title}'가 목록에 없습니다.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "14d2ae45-0219-4007-bb4e-7e21ddc9c6b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def menu():\n",
    "    print(\"=== 도서 관리 프로그램 ===\")\n",
    "    print(\"1. 도서 추가\")\n",
    "    print(\"2. 도서 삭제 (책 제목으로 삭제)\")\n",
    "    print(\"3. 도서 검색 (책 제목으로 조회)\")\n",
    "    print(\"4. 전체 도서 목록 출력\")\n",
    "    print(\"5. 종료\")\n",
    "\n",
    "\n",
    "def check_num():  # 정수 입력 확인 함수\n",
    "    while True:  # 무한 루프 시작\n",
    "        testing = input(\"숫자를 입력하세요: \")  # 입력 프롬프트 추가\n",
    "        try:  \n",
    "            return int(testing)  # 정수로 변환하여 반환\n",
    "        except ValueError:\n",
    "            print(\"잘못된 입력입니다. 다시 시도하세요.\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "078b346a-9eee-4989-a749-c2f44a1aaa7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "잘못된 선택입니다. 다시 시도하세요.\n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "잘못된 입력입니다. 다시 시도하세요.\n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  1\n",
      "책 번호를 입력하세요 :  r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "잘못된 입력입니다. 다시 시도하세요.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "책 번호를 입력하세요 :  100\n",
      "책 제목을 입력하세요 :  파이썬과 알고리즘\n",
      "저자를 입력하세요:  김유희\n",
      "출판 연도를 입력하세요 :  2023\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "도서 '파이썬과 알고리즘'가 추가되었습니다.\n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 등록된 도서 목록:\n",
      "[책 번호: 100, 제목: 파이썬과 알고리즘, 저자: 김유희, 출판 연도: 2023]  \n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  1\n",
      "책 번호를 입력하세요 :  100\n",
      "책 제목을 입력하세요 :  자바\n",
      "저자를 입력하세요:  김유희2\n",
      "출판 연도를 입력하세요 :  0202\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "도서 '자바'가 추가되었습니다.\n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 등록된 도서 목록:\n",
      "[책 번호: 100, 제목: 자바, 저자: 김유희2, 출판 연도: 202]  [책 번호: 100, 제목: 파이썬과 알고리즘, 저자: 김유희, 출판 연도: 2023]  \n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  2\n",
      "삭제할 책 제목을 입력하세요:  자바\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "도서 '자바'가 삭제되었습니다.\n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  3\n",
      "조회할 도서 제목을 입력하세요:  파이썬과 알고리즘\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[책 번호: 100, 제목: 파이썬과 알고리즘, 저자: 김유희, 출판 연도: 2023]\n",
      "\n",
      "=== 도서 관리 프로그램 ===\n",
      "1. 도서 추가\n",
      "2. 도서 삭제 (책 제목으로 삭제)\n",
      "3. 도서 검색 (책 제목으로 조회)\n",
      "4. 전체 도서 목록 출력\n",
      "5. 종료\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "메뉴를 선택하세요 :  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "프로그램을 종료합니다\n"
     ]
    }
   ],
   "source": [
    "choice = 0\n",
    "Error_count = 0\n",
    "library = LinkedList()\n",
    "\n",
    "while choice != 6:\n",
    "    menu()\n",
    "    choice = input(\"메뉴를 선택하세요 : \")\n",
    "    \n",
    "    try:  \n",
    "        choice = int(choice)\n",
    "    except ValueError:\n",
    "        print(\"잘못된 입력입니다. 다시 시도하세요.\\n\")\n",
    "        Error_count += 1\n",
    "        continue\n",
    "    \n",
    "    if choice == 1:\n",
    "        while True:  # 책 번호 입력\n",
    "            try:\n",
    "                book_id = int(input(\"책 번호를 입력하세요 : \"))\n",
    "                break  # 입력이 성공하면 루프 종료\n",
    "            except ValueError:\n",
    "                print(\"잘못된 입력입니다. 다시 시도하세요.\\n\")\n",
    "                Error_count += 1\n",
    "        \n",
    "        title = input(\"책 제목을 입력하세요 : \")\n",
    "        author = input(\"저자를 입력하세요: \")\n",
    "        \n",
    "        while True:  # 출판 연도 입력\n",
    "            try:  \n",
    "                year = int(input(\"출판 연도를 입력하세요 : \"))\n",
    "                break  # 입력이 성공하면 루프 종료\n",
    "            except ValueError:\n",
    "                print(\"잘못된 입력입니다. 다시 시도하세요.\\n\")\n",
    "                Error_count += 1     \n",
    "            \n",
    "        library.add_book(book_id, title, author, year)\n",
    "        print()\n",
    "        \n",
    "    elif choice == 2:\n",
    "        title = input(\"삭제할 책 제목을 입력하세요: \")\n",
    "        library.remove_book(title)\n",
    "        print()\n",
    "        \n",
    "    elif choice == 3:\n",
    "        title = input(\"조회할 도서 제목을 입력하세요: \")\n",
    "        library.find(title)\n",
    "        print()\n",
    "        \n",
    "    elif choice == 4:\n",
    "        library.display()\n",
    "        print()    \n",
    "        \n",
    "    elif choice == 5:\n",
    "        print(\"프로그램을 종료합니다\")\n",
    "        break\n",
    "        \n",
    "    else:\n",
    "        if Error_count == 0:\n",
    "            print(\"잘못된 선택입니다. 다시 시도하세요.\\n\")\n",
    "        else:\n",
    "            Error_count = 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f124595-9f6f-4f1c-a7af-7551a908f30d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
