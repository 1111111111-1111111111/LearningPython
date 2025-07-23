from tools import *
def main():
    """
    启动函数
    :return:
    """
    menu = {
        "1": add,
        "2": show,
        "3": modify,
        "4": delect,
        "5": exit,
    }
    while True:
        display()
        cmd = input("请输入您要进行的操作：")
        if cmd in menu:
            menu[cmd]()
        else:
            print("指令有误，请重新输入！")


