'''
파일명: main.py
작성자: 조영채
역할: 프로그램 실행 및 통합
'''

from database import FunctionDatabase, FunctionInfo
from user_manager import UserManager
from guiprogram import FunctionApp

def main():
    app = FunctionApp()
    app.run()

if __name__ == "__main__":
    main()