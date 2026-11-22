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

#즐겨찾기 추가
def add_favorite(topic):
    if topic not in favorites:
        favorites.append(topic)
        print(f"{topic}이(가) 즐겨찾기에 추가되었습니다.")

    else:
        print("이미 즐겨찾기에 있습니다.")

#즐겨찾기 삭제
def remove_favorite(topic):
    if topic in favorites:
        favorites.remove(topic)
        print(f"{topic}이(가) 즐겨찾기에 삭제되었습니다.")
    else:
        print("즐겨찾기에 없는 항목입니다.")

#즐겨찾기 목록 조회
def show_favorites():
    if not favorites:
        print("즐겨찾기 목록이 비어 있습니다.")
    else:
        print("===즐겨찾기 목록===")
        for topic in favorites:
            print(topic)

if __name__ == "__main__":
    add_favorite("abs")
    add_favorite("print")
    add_favorite("len")

    show_favorites()

    remove_favorite("abs")

    show_favorites()