# 項目11　イテレータを並列に処理するにはzipを使う

'''
1. 冒頭

複数のイテレータを並列処理するには組み込み関数zip
を利用する事が効果的です。

今回は名前リスト(names)に含まれる最も長い名前と、
その文字数をカウントするプログラムについて考慮します。
'''

# 名前は適当に乃木坂から引っ張りました。
names = ['Nishino', 'Shiraishi', 'Saitou', 'Ikuta']
letters = [len(x) for x in names]

# まずは何も考えずに機能を満たす処理を記述

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]

    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name, max_letters)

'''
2. 上記プログラムの課題

Pythonでなく、自分でC言語とかで実装しないと
いけないなら、確かに上記の処理でも問題ありませんが、
今用いている言語はPythonなので、いささかスッキリした
記述ではありませんね。ループ内に添字iが2回登場するし、、
enumerateを使えばもう少しスッキリ記述できそうです。
'''

# といってもlongest_nameから添字が取れただけ。。
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name, max_letters)

'''
3. よりスッキリさせる為に並列処理ならzipを使いましょう

Pythonの組み込み関数であるzipを用いる事でイテレータの
並列処理が可能です。
たとえば今までの処理をzip関数を用いて下記のように書き換える
事が可能です。
'''

# めちゃめちゃスッキリしました。
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

'''
4. zipの課題

zip関数の入力に異なる長さのものが存在する場合、
挙動がおかしくなります。具体例としてnamesに適当
な名前を追加して処理を実行してみましょう。
入力される対象が同じ長さなら問題ありません。
不安な場合はitertoolsに含まれるzip_longest関数を
使用する事で、要素数の多い方でzipのループを回して
くれます。
'''

names.append('Matsumura')
for name, count in zip(names, letters):
    print(name, count) # 表示されるはずのMatsumuraがいない。

print("")

# 不安ならitertools.zip_longest関数を使用する。
import itertools

for name, count in itertools.zip_longest(names, letters):
    print(name, count)  # Matsumuraと同じindexでのcount==Noneとなっている


'''
5. まとめ
・組み込み関数zipが複数のイテレータを処理するのに便利
・zipを使う事で処理を明確にすることができる。
・異なる長さの入力を用いると、挙動不審となるので注意
・異なる長さを入力してしまう不安がある場合、itertools.zip_longest関数を使う。

以上
'''
