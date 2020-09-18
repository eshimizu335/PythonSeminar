# クラスの練習
class MyClass():    # クラス定義
    # 以下はクラス変数
    a = "マイクラス"
    __b = 0 # アクセス保護される変数

    # 以下は生成する際に呼ばれる変数, mydataの初期値を引数で与える
    def __init__(self, data):   # 引数dataをとる初期化メソッド
        # __numberはインスタンスの通し番号
        self.__number = MyClass.__b
        self.mydata = data
        print("MyClass Object is created, number:", self.__number)
        # クラス変数を1増やす
        MyClass.__b += 1

    # 通し番号を表示するメソッド
    def show_number(self):
        print(self.__number)

#
# ここからメインプログラム
#
if __name__=="__main__":    # モジュールでインポートされたときには実行しない
    print("MyClassのクラス変数a:",MyClass.a)

    instance1 = MyClass(1)
    instance2 = MyClass(10)
    instance1.show_number()
    instance2.show_number()

    print("mydata of instance1: ", instance1.mydata)
    print("mydata of instance2: ", instance2.mydata)
    instance1.mydata += 1
    instance2.mydata += 2
    print("mydata of instance1: ", instance1.mydata)
    print("mydata of instance2: ", instance2.mydata)
