import os
import sys
import hashlib
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util import Counter

# ================== 界面布局类 ==================
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_mm3ltnr0 = self.__tk_label_mm3ltnr0(self)
        self.tk_input_mm3lk4xz = self.__tk_input_mm3lk4xz(self)
        self.tk_label_mm3lk7p3 = self.__tk_label_mm3lk7p3(self)
        self.tk_button_mm3lmi2x = self.__tk_button_mm3lmi2x(self)
        self.tk_progressbar_mm3lo469 = self.__tk_progressbar_mm3lo469(self)
        self.tk_label_mm3lof2y = self.__tk_label_mm3lof2y(self)
        self.tk_label_mm3lzk0m = self.__tk_label_mm3lzk0m(self)
        self.tk_button_mm3m8voq = self.__tk_button_mm3m8voq(self)
        self.tk_input_mm3m9gw2 = self.__tk_input_mm3m9gw2(self)
        self.tk_label_mm3m9mky = self.__tk_label_mm3m9mky(self)

    def __win(self):
        self.title("Time Gift Decryption Tool")
        width = 371
        height = 120
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_input_mm3lk4xz(self, parent):
        ipt = Entry(parent)
        ipt.place(x=0, y=0, width=298, height=30)
        return ipt

    def __tk_label_mm3lk7p3(self, parent):
        label = Label(parent, text="YOUkey", anchor="center")
        label.place(x=307, y=0, width=63, height=30)
        return label

    def __tk_button_mm3lmi2x(self, parent):
        btn = Button(parent, text="yes", takefocus=False)
        btn.place(x=0, y=70, width=55, height=30)
        return btn

    def __tk_progressbar_mm3lo469(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL)
        progressbar.place(x=60, y=70, width=238, height=30)
        return progressbar

    def __tk_label_mm3lof2y(self, parent):
        label = Label(parent, text="None%", anchor="center")
        label.place(x=307, y=70, width=63, height=30)
        return label

    def __tk_label_mm3ltnr0(self, parent):
        label = Label(parent, text="You might need a key to unlock him.", anchor="center")
        label.place(x=0, y=94, width=220, height=30)
        return label

    def __tk_label_mm3lzk0m(self, parent):
        label = Label(parent, text="by CeryCN", anchor="center")
        label.place(x=300, y=94, width=76, height=30)
        return label

    def __tk_button_mm3m8voq(self, parent):
        btn = Button(parent, text="file", takefocus=False)
        btn.place(x=0, y=37, width=55, height=30)
        return btn

    def __tk_input_mm3m9gw2(self, parent):
        ipt = Entry(parent)
        ipt.place(x=60, y=37, width=238, height=30)
        return ipt

    def __tk_label_mm3m9mky(self, parent):
        label = Label(parent, text="bin file", anchor="center")
        label.place(x=307, y=37, width=63, height=30)
        return label


# ================== 业务逻辑类 ==================
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        self.__style_config()
        # 初始化进度条
        self.tk_progressbar_mm3lo469['value'] = 0
        self.tk_progressbar_mm3lo469['mode'] = 'determinate'

    def __event_bind(self):
        self.tk_button_mm3m8voq.config(command=self.select_file)
        self.tk_button_mm3lmi2x.config(command=self.start_decrypt)

    def __style_config(self):
        pass

    # 选择文件
    def select_file(self):
        file_path = filedialog.askopenfilename(title="选择加密文件")
        if file_path:
            self.tk_input_mm3m9gw2.delete(0, END)
            self.tk_input_mm3m9gw2.insert(0, file_path)

    # 启动解密（主线程执行，模拟进度）
    def start_decrypt(self):
        key = self.tk_input_mm3lk4xz.get().strip()
        infile = self.tk_input_mm3m9gw2.get().strip()

        if not key or not infile:
            messagebox.showerror("错误", "请填写密钥和文件路径")
            return
        if not os.path.isfile(infile):
            messagebox.showerror("错误", "文件不存在")
            return

        # 生成输出文件名
        base, ext = os.path.splitext(infile)
        outfile = base + "_decrypted" + ext

        # 禁用按钮
        self.tk_button_mm3lmi2x.config(state=DISABLED)
        self.tk_button_mm3m8voq.config(state=DISABLED)

        # 进度条归零
        self.tk_progressbar_mm3lo469['value'] = 0
        self.tk_label_mm3lof2y.config(text="0%")
        self.update_idletasks()

        try:
            # 模拟进度50%
            self.tk_progressbar_mm3lo469['value'] = 50
            self.tk_label_mm3lof2y.config(text="50%")
            self.update_idletasks()

            # 执行实际解密
            self.real_decrypt(infile, key, outfile)

            # 完成
            self.tk_progressbar_mm3lo469['value'] = 100
            self.tk_label_mm3lof2y.config(text="100%")
            self.update_idletasks()
            messagebox.showinfo("成功", f"解密完成，文件已保存至:\n{outfile}")

        except Exception as e:
            self.tk_progressbar_mm3lo469['value'] = 0
            self.tk_label_mm3lof2y.config(text="错误")
            self.update_idletasks()
            messagebox.showerror("解密失败", str(e))

        finally:
            self.tk_button_mm3lmi2x.config(state=NORMAL)
            self.tk_button_mm3m8voq.config(state=NORMAL)

    # 实际解密逻辑（改编自原 main 函数）
    def real_decrypt(self, infile, key, outfile):
        with open(infile, 'rb') as f:
            data = f.read()

        filesize = len(data)
        if filesize < 8:
            raise ValueError("文件太短，无法解密")

        # 尝试第一个区域
        len_a = int.from_bytes(data[0:4], 'little')
        if 4 + len_a <= filesize:
            cipher_a = data[4:4+len_a]
            plain_a = self.decrypt_data(cipher_a, key)

            if plain_a.startswith(b'PK\x03\x04'):  # ZIP文件头
                with open(outfile, 'wb') as f:
                    f.write(plain_a)
                return
            else:
                # 尝试第二个区域
                len_b = int.from_bytes(data[-4:], 'little')
                if len_b <= filesize - 4:
                    start_b = filesize - 4 - len_b
                    cipher_b = data[start_b:start_b+len_b]
                    plain_b = self.decrypt_data(cipher_b, key)
                    with open(outfile, 'wb') as f:
                        f.write(plain_b)
                    return
                else:
                    raise ValueError("第二个区域长度无效")
        else:
            raise ValueError("第一个区域长度无效")

    # AES-256-CTR 解密
    def decrypt_data(self, ciphertext, key):
        key_bytes = hashlib.sha256(key.encode('utf-8')).digest()
        nonce = b'\x00' * 8
        cipher = AES.new(key_bytes, AES.MODE_CTR, nonce=nonce)
        return cipher.decrypt(ciphertext)


# ================== 程序入口 ==================
if __name__ == "__main__":
    app = Win()
    app.mainloop()