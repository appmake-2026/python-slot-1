import tkinter as tk
import random

#各リールが回転中かどうか
spinning = [False,False,False]

#表示する数字
numbers =[1,1,1]

#リールを回転させる関数+
def spin(index):
    
    if spinning[index]:
        
        #1～9のランダムな数字
        numbers[index] = random.randint(1,9)
        
        #画面の数字を更新
        labels[index]["text"] = numbers[index]
        
        #50ミリ秒後にもう一度spinを実行
        root.after(50,spin,index)
        
#スタートボタン
def start():
    
    #結果表示を消す
    result_label["text"] =""
    
    #三つのリールを回転状態にする
    for i in range(3):
        spinning[i] = True
        spin(i)
        
#ストップボタン
def stop(index):
    
    #指定されたリールを停止
    spinning[index] = False
    
    #3つすべて停止しているか確認
    if spinning == [False,False,False]:
        
        check_result()
        
#結果判定
def check_result():
    
    #777なら大当たり
    if numbers == [7,7,7] :
        
        result_label["text"] ="🌷 大当たり! 🌷"
        
    else:
        result_label["text"] ="ハズレ"
        
#メイン画面表示
root = tk.Tk()

root.title("シンプルスロット")
root.geometry("500x300")

#数字表示用ラベル
labels = []

for i in range(3):
    
    label = tk.Label(
        root,
        text="1",
        font=("Arial",50),
        width=3,
        relief="solid"
    )
    
    label.grid(row=0,column=i,padx=10,pady=20)
    
    labels.append(label)
    
#ストップボタン３つ
for i in range(3):
    
    button = tk.Button(
        root,
        text="STOP",
        font=("Arial",15),
        command = lambda i=i : stop(i)
    )
    
    button.grid(row=1,column=i,padx=10)
    
#スタートボタン
start_button = tk.Button(
    root,
    text="START",
    font=("Arial",18),
    command=start
)

start_button.grid(
    row=2,
    column=0,
    columnspan=3,
    pady=20
)

#結果表示
result_label = tk.Label(
    root,
    text="",
    font=("Arial",25)
)

result_label.grid(
    row=3,
    column=0,
    columnspan=3
)

#画面表示
root.mainloop()