import os
import random
import hashlib
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES

def encrypt_data(data, key):
    key_bytes = hashlib.sha256(key.encode('utf-8')).digest()
    nonce = b'\x00' * 8
    cipher = AES.new(key_bytes, AES.MODE_CTR, nonce=nonce)
    return cipher.encrypt(data)

def encrypt_two_files(file1, file2, key1, key2, output):
    with open(file1, 'rb') as f:
        data1 = f.read()
    with open(file2, 'rb') as f:
        data2 = f.read()

    cipher1 = encrypt_data(data1, key1)
    cipher2 = encrypt_data(data2, key2)

    len1, len2 = len(cipher1), len(cipher2)

    # 随机填充 1~2 MB
    pad_size = random.randint(1024*1024, 2*1024*1024)

    with open(output, 'wb') as f:
        f.write(len1.to_bytes(4, 'little'))
        f.write(cipher1)
        f.write(os.urandom(pad_size))
        f.write(cipher2)
        f.write(len2.to_bytes(4, 'little'))

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_mm3l4qhs = self.__tk_label_mm3l4qhs(self)
        self.tk_input_mm3ki6c6 = self.__tk_input_mm3ki6c6(self)
        self.tk_input_mm3kjyq6 = self.__tk_input_mm3kjyq6(self)
        self.tk_input_mm3l1oen = self.__tk_input_mm3l1oen(self)
        self.tk_label_mm3kk8mm = self.__tk_label_mm3kk8mm(self)
        self.tk_progressbar_mm3kz69p = self.__tk_progressbar_mm3kz69p(self)
        self.tk_label_mm3kkptz = self.__tk_label_mm3kkptz(self)
        self.tk_button_mm3kv8tw = self.__tk_button_mm3kv8tw(self)
        self.tk_label_mm3kvmbw = self.__tk_label_mm3kvmbw(self)
        self.tk_button_mm3kwr1w = self.__tk_button_mm3kwr1w(self)
        self.tk_label_mm3kxila = self.__tk_label_mm3kxila(self)
        self.tk_button_mm3ky7ho = self.__tk_button_mm3ky7ho(self)
        self.tk_button_mm3l10ni = self.__tk_button_mm3l10ni(self)

    def __win(self):
        self.title("加密")
        width, height = 201, 200
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_label_mm3l4qhs(self, parent):
        label = Label(parent, text="加密的小项目 by 颖颖", anchor="center")
        label.place(x=0, y=175, width=200, height=30)
        return label

    def __tk_input_mm3ki6c6(self, parent):
        ipt = Entry(parent)
        ipt.place(x=50, y=0, width=150, height=30)
        return ipt

    def __tk_input_mm3kjyq6(self, parent):
        ipt = Entry(parent)
        ipt.place(x=50, y=30, width=150, height=30)
        return ipt

    def __tk_input_mm3l1oen(self, parent):
        ipt = Entry(parent)
        ipt.place(x=50, y=120, width=150, height=30)
        return ipt

    def __tk_label_mm3kk8mm(self, parent):
        label = Label(parent, text="密钥1", anchor="center")
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_progressbar_mm3kz69p(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL)
        progressbar.place(x=50, y=150, width=150, height=30)
        return progressbar

    def __tk_label_mm3kkptz(self, parent):
        label = Label(parent, text="密钥2", anchor="center")
        label.place(x=0, y=30, width=50, height=30)
        return label

    def __tk_button_mm3kv8tw(self, parent):
        btn = Button(parent, text="文件1", takefocus=False)
        btn.place(x=0, y=60, width=50, height=30)
        return btn

    def __tk_label_mm3kvmbw(self, parent):
        label = Label(parent, text="未选择", anchor="center")
        label.place(x=50, y=60, width=150, height=30)
        return label

    def __tk_button_mm3kwr1w(self, parent):
        btn = Button(parent, text="文件2", takefocus=False)
        btn.place(x=0, y=90, width=50, height=30)
        return btn

    def __tk_label_mm3kxila(self, parent):
        label = Label(parent, text="未选择", anchor="center")
        label.place(x=50, y=90, width=150, height=30)
        return label

    def __tk_button_mm3ky7ho(self, parent):
        btn = Button(parent, text="执行", takefocus=False)
        btn.place(x=0, y=150, width=50, height=30)
        return btn

    def __tk_button_mm3l10ni(self, parent):
        btn = Button(parent, text="保存", takefocus=False)
        btn.place(x=0, y=120, width=50, height=30)
        return btn

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.file1_path = ""
        self.file2_path = ""
        self.output_path = ""
        self.__event_bind()

    def __event_bind(self):
        self.tk_button_mm3kv8tw.config(command=self.select_file1)
        self.tk_button_mm3kwr1w.config(command=self.select_file2)
        self.tk_button_mm3l10ni.config(command=self.select_output)
        self.tk_button_mm3ky7ho.config(command=self.do_encrypt)

    def select_file1(self):
        filename = filedialog.askopenfilename(title="选择第一个文件")
        if filename:
            self.file1_path = filename
            self.tk_label_mm3kvmbw.config(text=filename)

    def select_file2(self):
        filename = filedialog.askopenfilename(title="选择第二个文件")
        if filename:
            self.file2_path = filename
            self.tk_label_mm3kxila.config(text=filename)

    def select_output(self):
        filename = filedialog.asksaveasfilename(
            title="保存加密文件",
            defaultextension=".bin",
            filetypes=[("Binary files", "*.bin"), ("All files", "*.*")]
        )
        if filename:
            self.output_path = filename
            self.tk_input_mm3l1oen.delete(0, END)
            self.tk_input_mm3l1oen.insert(0, filename)

    def do_encrypt(self):
        key1 = self.tk_input_mm3ki6c6.get()
        key2 = self.tk_input_mm3kjyq6.get()
        output = self.tk_input_mm3l1oen.get() or self.output_path

        if not self.file1_path or not self.file2_path:
            messagebox.showerror("错误", "请选择两个文件")
            return
        if not key1 or not key2:
            messagebox.showerror("错误", "请输入两个密钥")
            return
        if not output:
            messagebox.showerror("错误", "请指定输出文件路径")
            return
            
        self.tk_progressbar_mm3kz69p.config(mode='indeterminate')
        self.tk_progressbar_mm3kz69p.start(10)
        try:
            encrypt_two_files(self.file1_path, self.file2_path, key1, key2, output)
            self.tk_progressbar_mm3kz69p.stop()
            self.tk_progressbar_mm3kz69p.config(mode='determinate', value=100)
            messagebox.showinfo("成功", f"加密完成！\n文件已保存至：\n{output}")
        except Exception as e:
            self.tk_progressbar_mm3kz69p.stop()
            self.tk_progressbar_mm3kz69p.config(mode='determinate', value=0)
            messagebox.showerror("错误", f"加密失败：{str(e)}")

if __name__ == "__main__":
    app = Win()
    app.mainloop()