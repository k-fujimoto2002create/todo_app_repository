def add() :
    categorylist = ["仕事", "勉強", "生活", "その他"]
    newtask = input("新しいタスクを入力してください：")
    while True :
        category = input("カテゴリーを入力してください（仕事・勉強・生活・その他）：")
        if category in categorylist :
            break
        else :
            print("仕事・勉強・生活・その他の中から選んでください")
            continue
    newdict = {"task":newtask, "category":category, "comp":False}
    return newdict

def display(datalist) :
    if datalist :
        for i, data in enumerate(datalist, 1) :
            if data["comp"] :
                print(f"★ {i}. {data["task"]} [{data["category"]}]")
            else :
                print(f"{i}. {data["task"]} [{data["category"]}]")
    else :
        print("データがありません。先にデータを読み込むか、新たに作成してください")

def complete(datalist) :
    while True :
        display(datalist)
        value = input("完了したタスクを番号で選択してください（qで終了）：")
        if value == "q" :
            break
        try :
            num = int(value)
            if num > len(datalist) :
                print("正しい番号を入力してください")
            else :
                index = num - 1
                data = datalist[index]
                data["comp"] = True
        except ValueError :
            print("半角数字で入力してください")

def delete(datalist) :
    while True :
        display(datalist)
        value = input("消去するタスクを選んでください（すべて消去する[all]、終了する[q]）：")
        if value == "all" :
            INDEX = 0
            num = 1
            length = len(datalist)
            while num <= length :
                del datalist[INDEX]
                num += 1
            break
        elif value == "q" :
            break
        else :
            try :
                num = int(value)
                if num > len(datalist) :
                    print("正しい番号を入力してください")
                else :
                    index = num - 1
                    del datalist[index]
            except ValueError :
                print("半角数字で入力してください")

def save(datalist) :
    file = "todo_list.txt"
    with open(file, "wt", encoding="utf-8") as fileobj :
        for data in datalist :
            fileobj.write(f"{data["task"]},{data["category"]},{int(data["comp"])}\n")

def load(datalist) :
    file = "todo_list.txt"
    with open(file, "rt", encoding="utf-8") as fileobj :
        while True :
            line = fileobj.readline()
            aline = line.rstrip()
            if aline :
                data = aline.split(",")
                task = data[0]
                category = data[1]
                comp = bool(int(data[2]))
                datadict = {"task":task, "category":category, "comp":comp}
                datalist.append(datadict)
            else :
                break                

def terminate() :
    print("終了しました。")