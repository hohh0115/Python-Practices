import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('Welcome!')
window.geometry('450x300')

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='random_files/images/welcome.gif')
image = canvas.create_image(7, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# label => user name & password
tk.Label(window, text='User Name:').place(x=100, y=150)
tk.Label(window, text='Password:').place(x=100, y=190)

# 輸入框
text_user_name = tk.StringVar()
text_user_name.set('example@python.com')
text_password = tk.StringVar()
tk.Entry(window, textvariable=text_user_name).place(x=180, y=150)
tk.Entry(window, textvariable=text_password, show='*').place(x=180, y=190)   # show='*' 代表輸入的內容顯示為*

def user_login():
    user_name = text_user_name.get()
    password = text_password.get()
    try:
        with open('random_files/user_info/user_info.pickle', 'rb') as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('random_files/user_info/user_info.pickle', 'wb') as user_file:
            user_info = {'admin':'admin'}
            pickle.dump(user_info, user_file)
    if user_name in user_info:
        if password == user_info[user_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + user_name)
        else:
            tk.messagebox.showerror(title='Error', message='Wrong Password!')
    else:
        is_sign_up = tk.messagebox.askyesno(title='Sign up?', message='You have not signed up yet. Sign up today?')
        if is_sign_up:
            user_signup()

def user_signup():
    def sign_to_Python():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        with open('random_files/user_info/user_info.pickle', 'rb') as user_file:
            exist_user_info = pickle.load(user_file)
        if not nn or not np or not npf:
            tk.messagebox.showerror('Error', 'No Empty!')
        elif np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_user_info:
            tk.messagebox.showerror(title='Error', message='The user has already signed up!')
        else:
            exist_user_info[nn] = np
            with open('random_files/user_info/user_info.pickle', 'wb') as user_file:
                pickle.dump(exist_user_info, user_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# 按鈕
tk.Button(window, text='Login', command=user_login).place(x=120, y=230)
tk.Button(window, text='Sign Up', command=user_signup).place(x=260, y=230)

window.mainloop()
