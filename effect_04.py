## 複雑な式の代わりにヘルパー関数を利用する。 ##
"""
1. 冒頭

URLのクエリー文字列を復元する場合を例に考える
ここでクエリー文字列は整数値を表しているとする。

reprについては下記が分かりやすい
https://gammasoft.jp/blog/use-diffence-str-and-repr-python/
"""

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&&green=',
                    keep_blank_values=True)

print(repr(my_values))



"""
2. 処理の都合上、デフォルト値を設定する

上記においても、値を持つもの、持たないもの、全く値が存在しないもの
と様々な返り値をもつ。
→値を持たないもの、全く値を持たないもの= 0, Noneについては
デフォルト値を0とする方が処理の都合上良さそうなのは明白である。

red: keyがmy_valuesに存在する。値は文字列'5'となる
green: keyがmy_valuesに存在するが, 値が0である為, 判定式がFalse→0が代入される
other: keyがmy_valuesに存在しない→判定式がFalse, 0が代入される。
"""

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
other = my_values.get('other', [''])[0] or 0
print(red, green, other)



"""
3. 整数型にキャストしてみる
全ての引数が整数値で、数式で利用できる事を保証する為には
intがたでキャストする手法があるが、そうするともはや読むに
耐えないソースとなってしまう。
"""
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
other = int(my_values.get('other', [''])[0] or 0)

"""
4. そこでif/elseの三項式を導入してみる
読みやすくはなったが、記述が煩わしい。
red, green, other全ての値に対して同様の処理を
施す必要がある。
"""
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0
green = my_values.get('green', [''])
green = int(green[0]) if green[0] else 0
other = my_values.get('other', [''])
other = int(other[0]) if other[0] else 0
print(red, green, other)

"""
5. ここでお待ちかねのヘルパー関数化
ヘルパー関数を利用する事で記述が明確になり
スッキリできます。
式が複雑になってきたら、より小さなブロックに
分割して、ヘルパー関数を作成する事で可読性に
富んだコーディングが可能。
"""
def get_first_int(values, key, default=0):
    found = values.get(key, [''])

    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
other = get_first_int(my_values, 'other')
print(red, green, other)
