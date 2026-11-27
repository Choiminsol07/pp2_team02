'''
파일명: database.py
작성자: 박지연
'''

import json

class FunctionInfo:
    def __init__(self, name, category, description, example, result):
        self.name = name
        self.category = category
        self.description = description
        self.example = example
        self.result = result

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "example": self.example,
            "result": self.result
        }


class FunctionDatabase:
    def __init__(self):
        self.functions = []

    def save_json(self):
        data = []

        for f in self.functions:
            data.append(f.to_dict())

        with open("data/functions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("JSON 저장 완료")

    def load_json(self):

        try:
            with open("data/functions.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            self.functions = []

            for function_dict in data:
                function = FunctionInfo(**function_dict)
                self.functions.append(function)

            print("JSON 불러오기 완료")

        except FileNotFoundError:
            print("JSON 파일이 없습니다.")

    def print_functions(self):

        print("\n================================")
        print("       파이썬 함수 백과사전")
        print("================================")

        for f in self.functions:

            print(f"\n[함수명] {f.name}")
            print(f"[카테고리] {f.category}")
            print(f"[설명] {f.description}")
            print(f"[예제] {f.example}")
            print(f"[결과] {f.result}")

            print("--------------------------------")

    # 함수명으로 함수 정보 찾기
    def get_function(self, name):
        for f in self.functions:
            if f.name == name:
                return f

        return None

    # 전체 함수명 목록 반환
    def get_function_names(self):
        return [f.name for f in self.functions]

    # 함수명으로 함수 정보 조회
    def get_function(self, name):
        for f in self.functions:
            if f.name == name:
                return f

        return None

    # 전체 함수명 목록 반환
    def get_function_names(self):
        return [f.name for f in self.functions]