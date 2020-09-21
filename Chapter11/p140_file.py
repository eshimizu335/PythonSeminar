# 1ファイル入出力の例題
# 作業中のフォルダを調べるためにOSモジュールをインポート

import os

# カレントディレクトリを得て画面に表示
print(os.getcwd())

# 日本語ファイル.txtという名称のファイルを作成し内容を書き出す

f = open('日本語ファイル.txt', 'w')
f.write('日本語\n 日本語\n 日本語\n')
f.close()

# 日本語ファイル.txtを読み込み用にopenしてその内容を表示
f = open('日本語ファイル.txt', 'r')
s = f.read()
f.close()
print(s)