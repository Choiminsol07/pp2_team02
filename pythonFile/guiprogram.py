
'''
파일명: guiprogram.py
작성자: 최민솔
'''

import tkinter as tk
from database import FunctionDatabase
from user_manager import UserManager

class FunctionApp:
    def __init__(self):
        # 메인 창 생성
        self.window = tk.Tk()
        self.window.title("파이썬 함수 백과사전")
        self.window.geometry("950x750")
        self.window.configure(bg="white")


        # 데이터베이스 연결
        self.db = FunctionDatabase()
        self.db.load_json()

        # 사용자 관리 연결
        self.user_manager = UserManager()
        self.user_manager.functions = self.db.get_function_names()

        # 현재 화면에 표시되는 함수 이름 저장
        self.displayed_names = []

        # 화면 구성 함수 호출
        self.create_title()
        self.create_search()
        self.create_main_frame()
        self.create_function_list()
        self.create_detail_frame()
        self.create_bottom_buttons()

        # 전체 함수 목록 출력
        self.show_all()


    # 제목
    def create_title(self):
        title = tk.Label(self.window, text="파이썬 함수 백과사전", font=("맑은 고딕", 22, "bold"), bg="black", fg="white")
        title.pack(pady=20)


    # 검색창
    def create_search(self):
        search_frame = tk.Frame(self.window, bg="white")
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(search_frame, width=40, font=("맑은 고딕", 12))
        self.search_entry.pack(side="left", padx=5)

        search_button = tk.Button(search_frame, text="검색", width=10, bg="black", fg="white", command=self.search_function)
        search_button.pack(side="left")


    # 메인 화면
    def create_main_frame(self):
        self.main_frame = tk.Frame(self.window, bg="black")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=15)


    # 함수 목록
    def create_function_list(self):
        left_frame = tk.Frame(self.main_frame, bg="white")
        left_frame.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(left_frame, text="함수 예시", font=("맑은 고딕", 14, "bold"), bg="white").pack(pady=15)

        self.function_list = tk.Listbox(left_frame, font=("맑은 고딕", 12), height=15)
        self.function_list.pack(fill="both", expand=True, padx=15, pady=10)

        # 함수를 선택하면 설명창에 표시
        self.function_list.bind("<<ListboxSelect>>", self.select_function)


    # 오른쪽 설명 화면
    def create_detail_frame(self):
        right_frame = tk.Frame(self.main_frame, bg="white")
        right_frame.pack(side="right", fill="both", expand=True, padx=5)

        tk.Label(right_frame, text="함수 설명", font=("맑은 고딕", 14, "bold"), bg="white").pack(pady=15)

        self.detail_text = tk.Label(right_frame, text="함수를 선택하면\n이곳에 설명이 표시됩니다.", font=("맑은 고딕", 12), bg="white", justify="center")
        self.detail_text.pack(fill="both", expand=True)

        # 즐겨찾기 버튼
        self.favorite_button = tk.Button(right_frame, text="즐겨찾기", font=("맑은 고딕", 11), width=15, bg="blue", command=self.add_favorite)
        self.favorite_button.pack(pady=20)


    # 하단 버튼
    def create_bottom_buttons(self):
        bottom_frame = tk.Frame(self.window, bg="white")
        bottom_frame.pack(pady=15)

        tk.Button(bottom_frame, text="전체 함수", width=15,command=self.show_all).pack(side="left", padx=10)

        tk.Button( bottom_frame, text="즐겨찾기 목록", width=15, command=self.show_favorites).pack(side="left", padx=10)


    def search_function(self):
        keyword = self.search_entry.get().strip().lower()

        names = self.db.get_function_names()
        result = [name for name in names if keyword in name.lower()]

        self.display_functions(result)

        if not result:
            self.detail_text.config(text="검색 결과가 없습니다.")


    # 목록을 화면에 출력하는 함수
    def display_functions(self, names):
        self.function_list.delete(0, tk.END)
        self.displayed_names = names.copy()

        for name in names:
            self.function_list.insert(tk.END, name)


    # 함수 선택
    def select_function(self, event):
        selected = self.function_list.curselection()

        if not selected:
            return

        name = self.displayed_names[selected[0]]
        function = self.db.get_function(name)

        if function is None:
            return

        info = (
            f"함수명: {function.name}\n\n"
            f"카테고리: {function.category}\n\n"
            f"설명: {function.description}\n\n"
            f"예제:\n{function.example}\n\n"
            f"결과:\n{function.result}"
        )

        self.detail_text.config(text=info)

        if self.user_manager.is_favorite(name):
            self.favorite_button.config(text="즐겨찾기 삭제")
        else:
            self.favorite_button.config(text="즐겨찾기 추가")


    # 즐겨찾기 추가 및 삭제
    def add_favorite(self):
        selected = self.function_list.curselection()

        if not selected:
            return

        name = self.displayed_names[selected[0]]

        if self.user_manager.is_favorite(name):
            success, message = self.user_manager.remove_favorite(name)
        else:
            success, message = self.user_manager.add_favorite(name)

        self.detail_text.config(text=message)

        if self.user_manager.is_favorite(name):
            self.favorite_button.config(text="즐겨찾기 삭제")
        else:
            self.favorite_button.config(text="즐겨찾기 추가")


    # 전체 함수 목록
    def show_all(self):
        names = self.db.get_function_names()
        self.display_functions(names)


    # 즐겨찾기 목록
    def show_favorites(self):
        favorites = self.user_manager.show_favorites()
        self.display_functions(favorites)

        if not favorites:
            self.detail_text.config(text="즐겨찾기 목록이 비어 있습니다.")


    # 프로그램 실행
    def run(self):
        self.window.mainloop()