# 項目14: Noneを返すよりは例外を選ぶ

'''
1. 冒頭

Noneを返す事で特別な意味を示す関数は、Noneだけでなく、他の値
例えばゼロ, 空文字列等においても条件式にかけると'False'と判定
される為、エラーを引き起こしやすい。なのでNoneを返すのではなく
例外を上げて特別な処理を示す方が良いよ、というお話
'''

# 下記の例は一見正しい動作をしそう。
# でも、呼び出し元の関数がNoneに注目していれば
# OKだが、例えばTrueやFalseに注目した場合は
# どうなるか?
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

ret1 = divide(5, 0)
ret2 = divide(0, 5)

# Noneに注目した場合は正常動作する
if ret1 is None:
    print('invalid Input')
else:
    print(ret1)

if ret2 is None:
    print('invalid Input')
else:
    print(ret2)

# True/Falseに注目した場合は?
if ret1 is True:
    print(ret1)
else:
    print('invalid Input')

# この部分の挙動がおかしい。0 / 5を実施しているので
# invalidではない。
if ret2 is True:
    print(ret2)
else:
    print('invalid Input')

'''
2. Noneを返さない記述

前述の理由から、Noneを返すと碌な事がないことが
わかりましたので、Noneを返さない記述を考えて
みます。そこで提案されているのが、例外を呼び出し元
に挙げて、呼び出し側に処理を促すというものです。
'''
# 先程Noneを返していた関数を書き換える。
# raiseを加えると故意に例外を発生させる
# 事が可能です。ただし、例外が生じた場合に
# どう対処すべきなのかを関数内に明記しておく
# 必要があります。

def divide2(a, b):
    '''
    正常入力: aをbで除算した結果を返します。
    異常入力: ValueErrorとして例外を起こします。
             呼び出し側で例外処理を実施してください。
    '''
    try:
        return a/b
    except ZeroDivisionError:
        raise ValueError

x, y = 0, 0

# より安全な処理をする為には呼び出し側にも協力を仰ぐ
# その為にも関数内などに用途と例外についての処理内容を
# 明記しておく必要がある点に留意する。
try:
    result = divide2(x, y)
except ValueError:
    print('Invalid Inputs')
else:
    print('Result is {}'.format(result))

'''
4. まとめ

・Noneを返す事で特別な意味を示す関数はNoneだけでなく
　他の値(ゼロ, 空配列など)に置いても同様に、'False'
　として判定されるのでエラーを引き起こしやすい。

・Noneを返さない事がエラーを防ぐ方法として考えられる。
　その為に例外を上げて、呼び出し元のコードで適切に処理
　するように促す。その為にも関数内に処理内容と例外通知
　内容について明記する。

以上
'''
