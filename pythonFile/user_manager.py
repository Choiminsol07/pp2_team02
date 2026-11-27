'''
파일명: user_manager.py
작성자: 김윤빈
'''

class UserManager:
    def __init__(self):
        self.functions = [
            "abs", "all", "any", "bin", "bool",
            "bytearray", "bytes", "complex", "dict",
            "dir", "eval", "float", "help", "id",
            "input", "int", "isinstance", "len",
            "list", "max", "min", "object", "open",
            "print", "range", "reversed", "set",
            "sorted", "str", "sum", "tuple", "type"
        ]

        self.favorites = []


    # 즐겨찾기 추가
    def add_favorite(self, topic):
        if topic not in self.functions:
            return False, "존재하지 않는 함수입니다."

        if topic not in self.favorites:
            self.favorites.append(topic)
            return True, f"{topic}이(가) 즐겨찾기에 추가되었습니다."

        return False, "이미 즐겨찾기에 있습니다."


    # 즐겨찾기 삭제
    def remove_favorite(self, topic):
        if topic in self.favorites:
            self.favorites.remove(topic)
            return True, f"{topic}이(가) 즐겨찾기에서 삭제되었습니다."

        return False, "즐겨찾기에 없는 항목입니다."


    # 즐겨찾기 목록 조회
    def show_favorites(self):
        return self.favorites.copy()


    # 즐겨찾기 여부 확인
    def is_favorite(self, topic):
        return topic in self.favorites


    # 전체 함수 목록 반환
    def get_functions(self):
        return self.functions.copy()