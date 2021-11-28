import os
from pick.pick_test import PickTest
from pprint import pprint

if __name__ == "__main__":
    # 定义保存的路径，os.path.dirname(__file__)：获取当前脚本所在的路径  "result/html_reuslt" "result/bs_theme_product"
    path = os.path.join(
        os.path.dirname(__file__),
        "result/html_reuslt"
    )
    pick = PickTest(path)
    # data = pick.pick()
    # pprint(data)
    pick.saveData()
