from urllib.parse import parse_qs
my_value = parse_qs("red=5&blue=0&green=0")

# getメソッドは辞書にキーが存在しない場合、
# 第二引数を返す→””が帰り値となる。
# red = my_value.get("red", [""])[0] or 0
# green = my_value.get("green", [""])[0] or 0
# blue = my_value.get("blue", [""])[0] or 0

# 引数が整数である事を保証して数式で扱えるように
# intでラップして文字列を整数にパースすると良い
# red = int(my_value.get("red", [""])[0] or 0)

# これは見辛くて解読できないから、普通はif/else文で
# 記述する。三項演算を使っても良いけど、通常のif/elseよりも
# 情報量が少なくなってしまうので、ヘルパー関数をかくことが
# 唯一の救いである

def get_first_int(values, key, default=0):
    found = values.get(key, [""])

    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

if __name__ == "__main__":
    ret = get_first_int(my_value, "red")
    print(ret)
# 要するに、繰り返し使用する条件判定があるならば
# ヘルパー関数にしておいたほうが可読性が上がるって話
