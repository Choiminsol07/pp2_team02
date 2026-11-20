
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


class FunctionManager:
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
            print("JSON 파일을 찾을 수 없습니다.")

        except json.JSONDecodeError:
            print("JSON 파일의 형식이 잘못되었습니다.")
            
        except TypeError:
            print("JSON 데이터의 항목이 올바르지 않습니다.")

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