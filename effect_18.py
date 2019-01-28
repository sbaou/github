# 項目18: 可変長引数を使って、見た目をすっきりさせる

'''
1. 冒頭

省略可能な位置引数(スター引数 : *args)を使うことで関数呼出しがすっきりし、
見た目の雑音を減らす事が可能。
'''

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
# 引数を渡す際、値がなくても空配列を渡す必要がある。
log('My numbers are', [1, 2])
log('Hi there', [])


def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
# 可変長引数を渡しているので、値がなくても動作する。
log2('My numbers are', 1, 2)
log2('Hi there')

favorites = [1, 3, 5, 7, 10]
log2('My favorite num', *favorites)
