import tkinter

WIDTH = 10  # 横のマスの数
HEIGHT = 10  # 縦のマスの数

chip = 0  # 選択中のチップ番号
map_data = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]  # 完成用マップデータ(初期値は全て０)


# マップ描画関数
def draw_map():
    cvs_map.delete("MAP")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            cvs_map.create_image(
                60 * x + 30, 60 * y + 30, image=imgs[map_data[y][x]], tag="BG"
            )


# チップをセットする関数
def set_map(e):
    x = int(e.x / 60)
    y = int(e.y / 60)
    if 0 <= x and x <= WIDTH and 0 <= y and y <= HEIGHT:
        map_data[y][x] = chip
        draw_map()


# チップ描画関数
def draw_chip():
    cvs_chip.delete("CHIP")
    for i in range(len(imgs)):
        cvs_chip.create_image(30 + i * 60, 30, image=imgs[i], tag="CHIP")
    # 選択中のチップに赤枠を表示
    cvs_chip.create_rectangle(
        2 + 60 * chip,
        2 + 60 * (chip // 10),
        58 + 60 * chip,
        58 + 60 * (chip // 10),
        outline="red",
        width=3,
        tag="CHIP",
    )


# チップ選択関数
def select_chip(e):
    global chip
    x = int(e.x / 60)
    y = int(e.y / 60)
    if y * 10 + x < len(imgs):
        chip = y * 10 + x
        draw_chip()


def put_data():
    c = 0
    text.delete("1.0", "end")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            text.insert("end", str(map_data[y][x]) + ",")
            if map_data[y][x] == 3:
                c = c + 1
        text.insert("end", "\n")
    text.insert("end", "candy = " + str(c))


root = tkinter.Tk()
root.geometry(str(60 * WIDTH + 640) + "x" + str(60 * HEIGHT + 20))
root.title("マップエディタ")
cvs_map = tkinter.Canvas(width=WIDTH * 60, height=HEIGHT * 60, bg="gray")
cvs_map.place(x=10, y=10)
cvs_map.bind("<Button-1>", set_map)
cvs_map.bind("<B1-Motion>", set_map)
cvs_chip = tkinter.Canvas(width=600, height=300, bg="black")
cvs_chip.place(x=WIDTH * 60 + 20, y=10)
cvs_chip.bind("<Button-1>", select_chip)
text = tkinter.Text(width=50, height=20)
text.place(x=WIDTH * 60 + 20, y=330)
btn = tkinter.Button(
    text="データ出力", font=("Times New Roman", 16), fg="blue", command=put_data
)
btn.place(x=WIDTH * 60 + 400, y=330)

imgs = [
    tkinter.PhotoImage(file="images/chip00.png"),
    tkinter.PhotoImage(file="images/chip01.png"),
    tkinter.PhotoImage(file="images/chip02.png"),
    tkinter.PhotoImage(file="images/chip03.png"),
]
draw_map()
draw_chip()
root.mainloop()
