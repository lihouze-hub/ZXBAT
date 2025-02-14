import tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, font, simpledialog
import os
import subprocess
import winshell
import tempfile
import shutil

batpy='''
import os
import subprocess
import winshell
import tempfile
import shutil
bat_file_path = os.path.join(os.path.dirname(__file__), 'stript.bat')
temp_dir = tempfile.mkdtemp()
shortcut_path = os.path.join(temp_dir, 'run_bat.lnk')
icon_file_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
with winshell.shortcut(shortcut_path) as shortcut:
    shortcut.path = bat_file_path
    shortcut.working_directory = os.path.dirname(bat_file_path)
    if icon_file_path:
        shortcut.icon_location = (icon_file_path, 0)
    shortcut.description = 'Run BAT script with custom title and icon'
try:
    subprocess.Popen([shortcut_path], shell=True)
finally:
    shutil.rmtree(temp_dir)
'''
batpynoico='''
import os
import subprocess
import winshell
import tempfile
import shutil
bat_file_path = os.path.join(os.path.dirname(__file__), 'stript.bat')
temp_dir = tempfile.mkdtemp()
shortcut_path = os.path.join(temp_dir, 'run_bat.lnk')
icon_file_path = None
with winshell.shortcut(shortcut_path) as shortcut:
    shortcut.path = bat_file_path
    shortcut.working_directory = os.path.dirname(bat_file_path)
    if icon_file_path:
        shortcut.icon_location = (icon_file_path, 0)
    shortcut.description = 'Run BAT script with custom title and icon'
try:
    subprocess.Popen([shortcut_path], shell=True)
finally:
    shutil.rmtree(temp_dir)
'''
exepy='''
import os
import subprocess
import winshell
import tempfile
import shutil
bat_file_path = os.path.join(os.path.dirname(__file__), 'stript.bat')
temp_dir = tempfile.mkdtemp()
shortcut_path = os.path.join(temp_dir, 'run_bat.lnk')
icon_file_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
with winshell.shortcut(shortcut_path) as shortcut:
    shortcut.path = bat_file_path
    shortcut.working_directory = os.path.dirname(bat_file_path)
    if icon_file_path:
        shortcut.icon_location = (icon_file_path, 0)
    shortcut.description = 'Run BAT script with custom title and icon'
try:
    subprocess.Popen([shortcut_path], shell=False)
finally:
    shutil.rmtree(temp_dir)
'''
exepynoico='''
import os
import subprocess
import winshell
import tempfile
import shutil
bat_file_path = os.path.join(os.path.dirname(__file__), 'stript.bat')
temp_dir = tempfile.mkdtemp()
shortcut_path = os.path.join(temp_dir, 'run_bat.lnk')
icon_file_path = None
with winshell.shortcut(shortcut_path) as shortcut:
    shortcut.path = bat_file_path
    shortcut.working_directory = os.path.dirname(bat_file_path)
    if icon_file_path:
        shortcut.icon_location = (icon_file_path, 0)
    shortcut.description = 'Run BAT script with custom title and icon'
try:
    subprocess.Popen([shortcut_path], shell=False)
finally:
    shutil.rmtree(temp_dir)
'''
icon=None
hidecontrol=None
file_paths=[]

root=Tk()
root.title('ZXBAT')
root.geometry('600x400')
on_save_path=None
# 获取系统中所有可用的字体
available_fonts = [f for f in font.families() if not f.startswith("@")]

# 默认字体和字号
default_font = "Arial"
default_size = 12
# 创建菜单栏
menu_bar = tk.Menu(root)

# 文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="新建", command=lambda: new_file())
file_menu.add_command(label="打开", command=lambda: open_file())
file_menu.add_command(label="保存", command=lambda: save_file())
file_menu.add_command(label="另存为", command=lambda: new_save_file())
file_menu.add_separator()
file_menu.add_command(label="退出", command=lambda:root.destroy())
menu_bar.add_cascade(label="文件", menu=file_menu)

# 编辑菜单
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="剪切", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="复制", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="粘贴", command=lambda: text_area.event_generate("<<Paste>>"))
menu_bar.add_cascade(label="编辑", menu=edit_menu)

# 字体菜单
font_menu = tk.Menu(menu_bar, tearoff=0)

# 动态更新字体
def change_font(font_name=None, font_size=None):
    if font_name:
        font_var.set(font_name)
    if font_size:
        size_var.set(font_size)
    text_area.configure(font=(font_var.get(), size_var.get()))

# 字体子菜单
font_submenu = tk.Menu(font_menu, tearoff=0)
for font_name in available_fonts:
    # 使用闭包捕获当前字体名称
    def make_font_callback(font_name):
        def callback():
            change_font(font_name=font_name)  # 明确传递关键字参数
        return callback
    font_submenu.add_command(label=font_name, command=make_font_callback(font_name))
font_menu.add_cascade(label="字体", menu=font_submenu)

# 字号子菜单
size_submenu = tk.Menu(font_menu, tearoff=0)
size_options = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 48, 56, 64, 72]
for size in size_options:
    # 使用闭包捕获当前字号
    def make_size_callback(size):
        def callback():
            change_font(font_size=size)  # 明确传递关键字参数
        return callback
    size_submenu.add_command(label=str(size), command=make_size_callback(size))
font_menu.add_cascade(label="字号", menu=size_submenu)

menu_bar.add_cascade(label="字体", menu=font_menu)

# 运行菜单
run_menu=tk.Menu(menu_bar,tearoff=0)
run_menu.add_command(label="运行",command=lambda: runbat())
menu_bar.add_cascade(label="运行", menu=run_menu)
# 转换菜单
to_menu = tk.Menu(menu_bar, tearoff=0)
to_menu.add_command(label="设置基本信息",command=lambda: settingexe())
to_menu.add_command(label="设置嵌入项目",command=lambda: settingfile())
to_menu.add_command(label="开始转换", command=lambda: toexe())
menu_bar.add_cascade(label="转换", menu=to_menu)
# 帮助菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="关于", command=lambda: about())
menu_bar.add_cascade(label="帮助", menu=help_menu)

# 将菜单栏添加到主窗口
root.config(menu=menu_bar)

# 创建文本编辑区
font_var = tk.StringVar(value=default_font)  # 当前字体
size_var = tk.IntVar(value=default_size)     # 当前字号
text_area = tk.Text(root, wrap="word", font=(font_var.get(), size_var.get()))
text_area.pack(expand=True, fill="both")

def runbat():
    save_file()
    subprocess.Popen(on_save_path)
    
# 打开文件功能
def open_file():
    global on_save_path
    file_path = filedialog.askopenfilename(filetypes=[("BAT", "*.bat"), ("CMD", "*.cmd")])
    if file_path:
        on_save_path=file_path
        root.title(on_save_path+' - ZXBAT')
        with open(file_path, "r",encoding='ANSI') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# 保存文件功能
def save_file():
    global on_save_path
    if on_save_path:
        with open(on_save_path, "w",encoding='ANSI') as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".bat", filetypes=[("BAT", "*.bat")])
        if file_path:
            on_save_path=file_path
            root.title(on_save_path+' - ZXBAT')
            with open(file_path, "w",encoding='ANSI') as file:
                file.write(text_area.get(1.0, tk.END))
def new_save_file():
    global on_save_path
    file_path = filedialog.asksaveasfilename(defaultextension=".bat", filetypes=[("BAT", "*.bat")])
    if file_path:
        on_save_path=file_path
        root.title(on_save_path+' - ZXBAT')
        with open(file_path, "w",encoding='ANSI') as file:
            file.write(text_area.get(1.0, tk.END))

def new_file():
    global on_save_path,icon,hidecontrol,file_paths
    icon=None
    hidecontrol=None
    file_paths=[]
    on_save_path=None
    root.title('ZXBAT')
    text_area.delete(1.0, tk.END)

# 关于功能
def about():
    messagebox.showinfo("关于", "ZXBAT\n当前版本号:V1.1")

def settingexe():
    global icon
    icopath=icon
    def icoset():
        icofile=filedialog.askopenfilename(filetypes=[("图标文件", "*.ico")])
        if icofile:
            iconentry.delete(0, tk.END)
            iconentry.insert(tk.END, icofile)
            iconpath=icofile
    def save_settings():
        global icon, hidecontrol
        icon = iconentry.get()
        hidecontrol = modestring.get()
        towin.destroy()
    towin=Toplevel()
    towin.title('基本信息设置')
    towin.geometry('400x240')
    towin.resizable(False,False)
    iconlabel=Label(towin,text='图标:')
    iconlabel.place(x=20,y=20)
    iconentry=Entry(towin,width=30)
    iconentry.place(x=60,y=20)
    iconbutton=Button(towin,text='浏览',command=icoset)
    iconbutton.place(x=280,y=15)
    modelabel=Label(towin,text='控制台模式:')
    modelabel.place(x=20,y=60)
    modestring=StringVar(value="1")
    tk.Radiobutton(towin, text="控制台(显示)", variable=modestring, value="1").place(x=20,y=100,anchor=tk.W)
    tk.Radiobutton(towin, text="Windows(隐藏)", variable=modestring, value="2").place(x=20,y=120,anchor=tk.W)
    tipslabel=Label(towin,text='若你看到两个选项都被选中，请手动选择一个选项，否则我们无法\n预测程序会使用哪一选项。')
    tipslabel.place(x=20,y=140)
    savebutton = Button(towin, text="保存", command=save_settings)
    savebutton.place(x=20, y=180)
    try:
        iconentry.delete(0, tk.END)
        iconentry.insert(tk.END, icon)
    except:
        pass
    towin.mainloop()
    icon=iconentry.get()
    hidecontrol=modestring.get()
def settingfile():
    global file_paths
    settings_window = Toplevel()
    settings_window.title("嵌入文件设置")
    settings_window.geometry('500x300')
    settings_window.resizable(False,False)
    
    listbox = Listbox(settings_window, width=50, height=10)
    listbox.pack(pady=10)
    
    def update_listbox():
        listbox.delete(0, tk.END)
        for path in file_paths:
            listbox.insert(tk.END, path)
    
    def add_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_path not in file_paths:
                file_paths.append(file_path)
                update_listbox()
                messagebox.showinfo("信息", f"已添加路径: {file_path}")
    
    def remove_file():
        try:
            selected_index = listbox.curselection()[0]
            removed_path = file_paths.pop(selected_index)
            update_listbox()
            messagebox.showinfo("信息", f"已移除路径: {removed_path}")
        except IndexError:
            messagebox.showwarning("警告", "请先选择一个文件路径")
    
    frame = Frame(settings_window)
    frame.pack(pady=10)

    tips=Label(settings_window,text='嵌入的文件将在运行时解压至临时目录，请在你的bat中使用"%~dp0filename"\n获取嵌入的文件的解压路径，请将示例中的filename替换成你嵌入的的文件名')
    tips.pack()
    
    add_button = Button(frame, text="添加文件", command=add_file)
    add_button.pack(side=tk.LEFT, padx=5)
    
    remove_button = Button(frame, text="移除选中文件", command=remove_file)
    remove_button.pack(side=tk.LEFT, padx=5)
    
    update_listbox()
    settings_window.mainloop()
    
def toexe():
    global icon, hidecontrol, file_paths, on_save_path
    try:
        import pyinstaller
    except:
        pass
    if not on_save_path:
        messagebox.showerror("错误", "请先保存 BAT 文件")
        return
    window=Tk()
    window.geometry('200x0')
    window.resizable(False,False)
    window.title('正在转换...')
    
    os.makedirs('C:\\zxbatstoexetemp', exist_ok=True)

    if icon:
        if hidecontrol == "1":
            script = batpy
        else:
            script = exepy
    else:
        if hidecontrol == "1":
            script = batpynoico
        else:
            script = exepynoico

    with open('C:\\zxbatstoexetemp\\stript.py', 'w', encoding='utf-8') as f:
        f.write(script)

    if icon:
        shutil.copy(icon, 'C:\\zxbatstoexetemp\\icon.ico')

    shutil.copy(on_save_path, 'C:\\zxbatstoexetemp\\stript.bat')

    for file_path in file_paths:
        shutil.copy(file_path, 'C:\\zxbatstoexetemp\\' + os.path.basename(file_path))

    pyinstaller_command = ['pyinstaller', '-F']
    if icon:
        pyinstaller_command.extend(['-i', 'icon.ico'])
    for file_path in file_paths:
        pyinstaller_command.extend(['--add-data', f'{os.path.basename(file_path)};.'])
    pyinstaller_command.append('stript.py')

    try:
        subprocess.run(pyinstaller_command, cwd='C:\\zxbatstoexetemp', check=True)
        window.destroy()
        messagebox.showinfo('转换成功', '转换成功，请选择保存路径')
        path = filedialog.asksaveasfilename(defaultextension=".exe", filetypes=[("EXE", "*.exe")])
        if path:
            shutil.copy('C:\\zxbatstoexetemp\\dist\\stript.exe', path)
    except subprocess.CalledProcessError as e:
        window.destroy()
        messagebox.showerror('转换失败', str(e))
    finally:
        shutil.rmtree('C:\\zxbatstoexetemp')
root.mainloop()
