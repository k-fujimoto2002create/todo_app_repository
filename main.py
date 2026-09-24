from todo import add, display, complete, delete, edit, save, load, terminate
from os import chdir

path = input("作業するフォルダのパスを入力してください：")
path.replace("\\", "/")
chdir(path)
datalist = []

while True :
    command = input("メニュー > 1.タスクを追加 2.タスクを一覧表示 3.完了したタスク 4.タスクを削除 5.タスクを編集 6.データを保存 7.データ読み込み 8.終了：")
    if command == "1" :
        newdata = add()
        datalist.append(newdata)
    elif command == "2" :
        display(datalist)
    elif command == "3" :
        complete(datalist)
    elif command == "4" :
        delete(datalist)
    elif command == "5" :
        edit(datalist)
    elif command == "6" :
        save(datalist)
        print("データを保存しました")
    elif command == "7" :
        load(datalist)
        print("データを読み込みました")
    elif command == "8" :
        terminate()
        break
    else :
        print("半角数字で正しい番号を入力してください")