import tkinter as tk

"""
# Label & Button 標籤和按鈕
# Label 是用於顯示內容的
# 建立master
window = tk.Tk()
window.title('title001')
window.geometry('300x500')

content = tk.StringVar()
l = tk.Label(window,
    # text='OMG! this is TK!',    # 标签的文字
    textvariable=content,
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
l.pack()    # 固定窗口位置

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        content.set('you hit me')
    else:
        on_hit == False
        content.set('you hit me again')

b = tk.Button(window, text='hit me', width=15, height=3, command=hit_me)
b.pack()

window.mainloop()
"""

"""
# Entry & Text 輸入, 文本框
# 建立master
window = tk.Tk()
window.title('title001')
window.geometry('400x300')

# 輸入框
entry = tk.Entry(window, show='*')    # show='*' 代表輸入的內容顯示為*
# entry = tk.Entry(window, show='1')    # 代表輸入的內容顯示為1
entry.pack()

def insert_point():
    insert_content = entry.get()
    text.insert('insert', insert_content)

def insert_end():
    insert_content = entry.get()
    insert_list = ['a', 'b', 'c', 'd', insert_content]
    for i in insert_list:
        text.insert('end', i+'\n')  # insert到結尾

    # text.insert(1.1, insert_content)    # insert到第一列第index=1位
# 按鈕
button1 = tk.Button(window, text='insert point', width=15, height=1, command=insert_point)
button1.pack()
button2 = tk.Button(window, text='insert end', width=15, height=1, command=insert_end)
button2.pack()

# Text顯示框
text = tk.Text(window, height=10)
text.pack()

window.mainloop()
"""

"""
# Listbox 列表部件
# 建立master
window = tk.Tk()
window.geometry('400x300')
window.title('listbox')

# 顯示用的label
selected_content = tk.StringVar()
label = tk.Label(
    window,
    bg='yellow',
    width=4,
    textvariable=selected_content   # label的顯示內容由listbox選中的內容而定
)
label.pack()

def print_content():
    selected = listbox.get(listbox.curselection())  # 從listbox拿出選定的值
    selected_content.set(selected)  # 把選定的值給予label顯示

button = tk.Button(
    window,
    text='print selected content',
    width=20,
    height=2,
    command=print_content
)
button.pack()

listbox_value = tk.StringVar()
listbox_value.set((11,22,33,44,55))
listbox = tk.Listbox(window, listvariable=listbox_value)    # 給予默認值

# 默認值之外，也可以另外插入
list_items = (1,2,3,4)
for i in list_items:
    listbox.insert('end', i)    # 在最後一個位置插入

listbox.insert(0, '頭香')    # 在index=0的地方插入
listbox.insert(2, 'second')    # 在index=2的地方插入
listbox.delete(2)
listbox.pack()

window.mainloop()
"""

"""
# RadionButton
# 建立master
window = tk.Tk()
window.geometry('400x300')
window.title('RadionButton')

# 建立顯示用的label
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

# 若為StringVar，開始時每個radiobutton都會是選擇的狀態，
var = tk.StringVar()
# 若想要默認時選擇一個，就加上默認值強迫選擇一個(value='A' or .set('A'))
# var = tk.StringVar(value='A')
# var.set('A')
# 若想要什麼都不選，就給一個不會出現的value值
# var = tk.StringVar(value='xx')
var.set(None)

def print_selection():
    text = 'you have selected ' + var.get()
    label.config(bg='red', text=text)

# 供選擇的radiobutton
/*
 * To get a proper radio behavior,
 * make sure to have all buttons in a group point to the same variable
 * (associate the same variable to all buttons in the same group.),
 * and use the value option to specify what value each button represents
 */
buttons = ['A', 'B', 'C']
for i in buttons:
    radiobutton = tk.Radiobutton(
        window,
        text='Option '+ i,
        variable=var,
        value=i,
        command=print_selection
    )
    radiobutton.pack()

window.mainloop()
"""

"""
# Scale
# 建立master
window = tk.Tk()
window.geometry('400x300')
window.title('Scale')

# 建立顯示用label
label = tk.Label(window, bg='yellow', width=20)
label.pack()

# scale widget的command option可以傳參數
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/scale.html
def print_selection(value):
    label.config(text='you have selected ' + value)

scale = tk.Scale(
    window,
    label='try me',
    from_=5,    # 開始
    to=11,  # 結束
    orient=tk.HORIZONTAL,   # 滾動方向
    length=500,
    showvalue=0,
    tickinterval=2,    # 座標的間隔
    resolution=0.01,    # the smallest increment of the scale's value
    command=print_selection
)
scale.pack()

window.mainloop()
"""

"""
# checkbutton
# 建立master
window = tk.Tk()
window.geometry('400x300')
window.title('checkbutton')

# 建立顯示用的label
label = tk.Label(window, bg='yellow', width=50)
label.pack()

# checkbutton
var_dict = dict()
button_list = ['Python', 'C++', 'PHP', 'Java', 'JavaScript']

def print_selection():
    love_count = 0
    love_list = []
    for key, value in var_dict.items():  # dict的for loop
        if value.get() == 1:
            love_count += 1
            love_list.append(button_list[key])

    if love_count == 0:
        label.config(text='I love nothing')
    else:
        text = 'I love ' + ', '.join(love_list)
        label.config(text=text)

for idx, val in enumerate(button_list):  # list的for loop
    var_dict[idx] = tk.IntVar()
    checkbutton = tk.Checkbutton(
        window,
        text=val,
        variable=var_dict[idx],  # Normally this variable is an IntVar
        onvalue=1,  # 當我們選中了這個checkbutton，onvalue的值1就會放入到var1中，然後var1將其賦值給參數variable
        offvalue=0,
        command=print_selection
    )
    checkbutton.pack()

window.mainloop()
"""

"""
# Canvas
# 建立master
window = tk.Tk()
window.geometry('400x300')
window.title('Canvas')

# canvas範圍
canvas = tk.Canvas(window, height=100, width=200)
# 圖片
image_file = tk.PhotoImage(file='random_files/images/ins.gif')
# anchor=nw則是把圖片的左上角作為錨定點(東南西北中，NW=西北)
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
# 建圖型
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)  # 從坐標(50,50)到(80,80)畫一條直線
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形

canvas.pack()

def moveit():
    canvas.move(rect, 0, 5)

b = tk.Button(window, text='move', command=moveit).pack()

window.mainloop()
"""

"""
# menubar
# 建立master
window = tk.Tk()
window.geometry('300x200')
window.title('Menubar')

# 顯示用label
label = tk.Label(window, bg='yellow', text='')
label.pack()

counter = 0
def do_job():
    global counter
    label.config(text='do '+ str(counter))
    counter+=1

# 在window上加入一個 Menubar 作為整體框架, 然後再在 Menubar 中加一些部件.
menubar = tk.Menu(window)

# menubar的部件選項"file"，並裝入menubar中
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
# menubar的部件選項"Edit"，並裝入menubar中
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)

# 建立file的選項列表
# 第一個是可以列出submenu的選項，叫做"Import"
submenu = tk.Menu(filemenu)  # 在`File`上建一个空的選項
submenu.add_command(label="Submenu1", command=do_job)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)  # 给放入的菜单`submenu`命名为`Import`

# 接下來為file加入其他選項
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # Add a separator after the last currently defined option.
filemenu.add_command(label='Exit', command=window.quit)

# 建立edit的選項列表
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
editmenu.add_command(label='Add', command=do_job)

# 把包含上面那些的Menubar放到window中
window.config(menu=menubar)
window.mainloop()
"""

"""
# Frame
# A frame is basically just a container for other widgets.
# Your application's root window is basically a frame.

# 建立master
window = tk.Tk()
window.title('Frame')
window.geometry('400x300')

tk.Label(window, bg='yellow', text='main', width=50).pack()

# main frame
frame = tk.Frame(window)
frame.pack()

# sub frame
frame_left = tk.Frame(frame, cursor='mouse')
frame_right = tk.Frame(frame, cursor='cross_reverse')
frame_left.pack(side='left')
frame_right.pack(side='right')

tk.Label(frame_left, bg='blue', text='left', width=20).pack()
tk.Label(frame_right, bg='red', text='right', width=20).pack()
window.mainloop()
"""

"""
# messagebox 彈窗
# messagebox 在import tkinter時通常不會被自動地import進來，要特別指定
import tkinter.messagebox
window = tk.Tk()
window.title('messagebox')
window.geometry('400x300')

def hit_me():
   tk.messagebox.showinfo(title='Hi', message='hahahaha')
   tk.messagebox.showwarning(title='warning title', message='warning msg')
   tk.messagebox.showerror(title='error title', message='error msg')
   tk.messagebox.askretrycancel(title='retry title', message='retry msg')
   tk.messagebox.askquestion(title='question title', message='question msg')

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()
"""

"""
# pack grid place 放置位置
window = tk.Tk()
window.title('messagebox')
window.geometry('400x300')

# tk.Label(window, text='1').pack(side='top')  #上
# tk.Label(window, text='1').pack(side='bottom')  #下
# tk.Label(window, text='1').pack(side='left')  #左
# tk.Label(window, text='1').pack(side='right')  #右

for i in range(4):  # 4 列
    for j in range(3):  # 3行
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)    # padx就是單元格左右間距 pady就是單元格上下間距

tk.Label(window, text=1).place(x=20, y=10, anchor='nw')  # 從window的左上角為(0, 0)，右邊+x，下方+y

window.mainloop()
"""

"""
app = tk.Tk()

frames = []
widgets = []

def createwidgets():
    global widgetNames
    global frameNames

    frame = tk.Frame(app, borderwidth=2, relief="groove")
    frames.append(frame)

    frame.pack(side="top", fill="x")

    for i in range(3):
        widget = tk.Entry(frame)
        widgets.append(widget)

        widget.pack(side="left")

createWidgetButton = tk.Button(app, text="createWidgets", command=createwidgets)
createWidgetButton.pack(side="bottom", fill="x")

app.mainloop()
"""