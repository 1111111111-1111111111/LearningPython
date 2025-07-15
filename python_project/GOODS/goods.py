import time
goods = {
    1: {"name": "小米14", "price": 500, "num": 10},
    2: {"name": "苹果15", "price": 500, "num": 10},
    3: {"name": "华为p60", "price": 500, "num": 10},
    4: {"name": "PPO", "price": 500, "num": 10},
    5: {"name": "vivo", "price": 500, "num": 10},
}
user_info = {"name": "老王", "balance": 1000}
# 购物车
user_buy_goods = {}
info = """
欢迎来到xx的手机商城
1:查看用户信息
2:查看商品详细信息
3:余额充值
4:购买商品
5:查看自己购买的商品
6:退出
"""
while True:
    print(info)
    choice = input("请输入您的选择：")
    if choice == "1":
        # 1:查看用户信息
        print(f"用户姓名：{user_info['name']}\n用户余额：{user_info['balance']}")
    elif choice == "2":
        # 2:查看商品详细信息
        for key, value in goods.items():
            print(f"商品编号：{key} 商品名称：{value['name']} 商品价格：{value['price']} 商品数量：{value['num']}")
    elif choice == "3":
        # 3:余额充值
        money = input("请输入您要充值的金额：")
        user_info["balance"] += int(money)
        print(f"用户当前余额：{user_info['balance']}")
    elif choice == "4":
        # 4:购买商品
        buy = input("请您输入您要购买的商品(cid,count)：")
        buy_split = buy.split(",")
        cid, count = int(buy_split[0]), int(buy_split[1])
        # 判断商品是否存在
        if cid not in goods:
            print("您所购买的商品不存在！")
            continue
        # 判断库存数量
        if count > goods[cid]["num"]:
            print("库存不足!")
            continue
        # 判断是否余额充足
        if user_info["balance"] >= goods[cid]["price"] * count:
            user_info["balance"] -= goods[cid]["price"] * count
            print(f"已成功购买商品！\n您当前余额为{user_info['balance']}")
            goods[cid]["num"] -= count
            user_buy_goods[len(user_buy_goods)+1] = {
                "name": goods[cid]["name"],
                "count": count,
                "total_price":  goods[cid]["price"] * count,
                "time": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            print("您的余额不足，请充值后再次购买！")
            continue
    elif choice == "5":
        # 5:查看自己购买的商品
        print(f"商品名称  购买数量  共消费金额  购买时间")
        for key, value in user_buy_goods.items():
            print(f"{value['name']}\t\t{value['count']}\t\t{value['total_price']}\t\t{value['time']}")
    elif choice == "6":
        # 6:退出
        print("欢迎下次光临！")
        break
    else:
        # 其它
        print("您的输入有误，请重新输入！")







