# 拉取文件
```bash
# 克隆整个完整的项目
git clone https://github.com/1111111111-1111111111/LearningPython.git

# 克隆单个文件
wget https://github.com/1111111111-1111111111/LearningPython/{文件路径}
如 克隆READEM文件
wget https://github.com/1111111111-1111111111/LearningPython/README.md

# 本地获取已克隆，需要获取最新更新
git pull orgin main

```

# Python 小练习

## 2025-7-15 购物车系统 GOODS/goods.py
```bash
实现如下功能:
info = """
    欢迎来到xx的手机商城
    1:查看用户信息
    2:查看商品详细信息
    3:余额充值
    4:购买商品
    5:查看自己购买的商品
    6:退出
"""
```

## 2025-7-16 学生信息管理系统 STUDENTS_SYSTEM/studentsSystem1.py
```bash
实现如下要求:
"""
创建一个学生管理系统
可以实现学生信息的录入(学号、姓名、年龄)
以及增删查改功能
"""
```

## 2025-7-23 学生信息管理系统（利用模块化的思想）STUDENTS_SYSTEM/studentSystem2
```bash
main.py  主程序
run.py  启动程序
file.py  文件的相关操作
tools.py  增删改查等业务逻辑的实现
students.txt  存储学生信息
```

## 2025-8-15 模拟网盘 CLOUD_STORAGE/cloudStorage.py
```bash
模式:
    C/S 模式

项目路径:
    server
        
    client

    main.py  


业务逻辑:
    1. 注册
    2. 登录
    3. 查看目录 ls
    4. 下载
    5. 上传

涉及到的知识点:
    文件相关操作
    socket 套接字
    粘包
    IO多路复用
    ...

```



    
