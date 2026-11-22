'''
파일명: user_manager.py
작성자: 김윤빈
'''

functions = [
    "abs", "all", "any", "bin", "bool",
    "bytearray", "bytes", "complex", "dict",
    "dir", "eval", "float", "help", "id",
    "input", "int", "isinstance", "len",
    "list", "max", "min", "object", "open",
    "print", "range", "reversed", "set",
    "sorted", "str", "sum", "tuple", "type"
]

favorites = []


# 즐겨찾기 추가
def add_favorite(topic):
    if topic not in functions:
        return False, "존재하지 않는 함수입니다."

    if topic not in favorites:
        favorites.append(topic)
        return True, f"{topic}이(가) 즐겨찾기에 추가되었습니다."

    return False, "이미 즐겨찾기에 있습니다."


# 즐겨찾기 삭제
def remove_favorite(topic):
    if topic in favorites:
        favorites.remove(topic)
        return True, f"{topic}이(가) 즐겨찾기에서 삭제되었습니다."

    return False, "즐겨찾기에 없는 항목입니다."


# 즐겨찾기 목록 조회
def show_favorites():
    return favorites.copy()


# 즐겨찾기 여부 확인
def is_favorite(topic):
    return topic in favorites


# 전체 함수 목록 반환
def get_functions():
    return functions.copy()