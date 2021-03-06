'''
1. 冒頭

Pythonの構文にリスト内包表記と言うものがある。
用途としては現存しているリストに、何かしらの処理を
加えて、新規リストを作成する場合等が挙げられる。

項目7として提唱しているのは、Pythonの組み込み関数
である"map"や"filter"を用いるよりも、リスト内包表記
を使用しましょう、その方が処理内容が明確になります。
と、いうものです。
'''
# 例:リスト内の各数の二乗を計算したい場合
# [処理内容 for 処理したい変数 in 処理したい変数が含まれるリスト]
lst = [1, 2, 3, 4, 5, 6]
square = [x ** 2 for x in lst]
print(square)

'''
2. map関数での表現

前記のリスト内包表記はmap関数を用いても同様の処理は
実現可能。ただし処理が見辛く、明確な処理であるとは
言いづらい。

ちなみに返り値はmapobjectである為、変換処理が必要。
'''
sqare = map(lambda x:x ** 2, lst)
print(list(sqare))

'''
3. mapとfilterの組み合わせは見辛い
   リスト内包表記で同様の処理は実現可能。

リスト内包表記では、入力リストから、特定要素を
フィルタリングして、その要素に対応する結果を簡単かつ
明瞭に算出可能。
同様の処理はmapとfilterを用いても可能だが、
明らかに見辛く、良いソースとは言えない。
'''

## 偶数のみに処理を適用する場合

# リスト内包表記の場合
# 内包表記の後にif文を追記するだけ。
even_sqare = [x ** 2 for x in lst if x % 2 == 0]
print(even_sqare)

# map&filterの場合
buf = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst))
even_sqare == list(buf)
print(even_sqare)

# どっちの方が見やすいですか？私は圧倒的に前者(リスト内包表記）です。

'''
4. まとめ

・リスト内包表記はlambda式を使用しないので、明確/明瞭な記述が可能
・リスト内包表記は入力リストから要素を抜き出すのが容易だが、
　map, filterの組み合わせでは記述を読み解くのがめんどくさい。

以上
'''
