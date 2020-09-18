# エラーへの対処
# 入力を得て検査するプログラム

while True:
    x = input("正の数値を入力してください ")
    try:
        x = float(x)
    except ValueError:  # ValueErrorへの対応
        print(x, "は数値に変換できません")
        continue
    except: # その他のエラーへの対応
        print("予期していないエラーです")
        exit()
    if (x<=0):  # 正の値であることの検査
        print(x,"は正の数値ではありません")
        continue
# 正しい入力が得られたときの処理
    print(x)
    break