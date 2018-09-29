#-*- coding: utf-8 -*-

from tkinter import Tk 
from tkinter import Menu
from tkinter import Frame
from tkinter import StringVar 
from tkinter import Button 
from tkinter import Label
from public_function.public import log

class IndexFrame(Frame):
    '''首页 + 控制页面'''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Button(self, text='关于系统', width=30, pady=7, command=self.aboutSys_frame).grid(row=0, column=0, pady=6)
        Button(self, text='关于作者', width=30, pady=7, command=self.aboutAuthor_frame).grid(row=1, column=0, pady=6)
        Button(self, text='帮助', width=30, pady=7, command=self.help_frame).grid(row=2, column=0, pady=6)

    def aboutSys_frame(self):
        self.destroy()
        mainpage = MainPage(self.root)
        return mainpage.aboutSysData()

    def aboutAuthor_frame(self):
        self.destroy()
        mainpage = MainPage(self.root)
        return mainpage.aboutAuthorData()

    def help_frame(self):
        self.destroy()
        mainpage = MainPage(self.root)
        return mainpage.helpData()


class AboutSysFrame(Frame):
    '''关于系统'''
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master  
        self.createPage() 
  
    def createPage(self):
        Label(self, text='关于系统').grid(row=0,column=0)


class AboutAuthorFrame(Frame):
    '''关于作者'''
    def __init__(self, master=None):
        Frame.__init__(self, master)  
        self.root = master  
        self.createPage() 
  
    def createPage(self):
        Label(self, text='关于作者').grid(row=0,column=0)


class HelpFrame(Frame):
    '''帮助'''
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master  
        self.createPage() 
  
    def createPage(self):
        Label(self, text='帮助').grid(row=0,column=0)


#---------------------------------------------------------------
#控制台
class MainPage(object):
    def __init__(self, master=None):  
        self.root = master 
        self.root.geometry('700x500')
        #self.root.iconbitmap('xx.ico')
        self.createPage() 
    def createPage(self):
        '''页面'''
        self.indexPage = IndexFrame(self.root)
        self.aboutSysPage = AboutSysFrame(self.root)
        self.aboutAuthorPage = AboutAuthorFrame(self.root)
        self.helpPage = HelpFrame(self.root)

        #默认显示首页界面
        self.indexPage.pack()
        #菜单
        menubar = Menu(self.root)
        menubar.add_command(label='首页', command = self.indexData)
        about = Menu(menubar, tearoff=False)
        about.add_command(label='关于系统', command = self.aboutSysData)
        about.add_command(label='关于作者', command = self.aboutAuthorData)
        menubar.add_cascade(label="关于", menu = about)
        menubar.add_command(label='帮助', command = self.helpData)
        menubar.add_command(label='退出', command = self.root.quit)
        self.root['menu'] = menubar

    def indexData(self):
        self.indexPage.pack()
        self.aboutSysPage.pack_forget()
        self.aboutAuthorPage.pack_forget()
        self.helpPage.pack_forget()
 
    def aboutSysData(self):
        self.indexPage.pack_forget() 
        self.aboutSysPage.pack()
        self.aboutAuthorPage.pack_forget()
        self.helpPage.pack_forget()

    def aboutAuthorData(self):
        self.indexPage.pack_forget() 
        self.aboutSysPage.pack_forget() 
        self.aboutAuthorPage.pack()
        self.helpPage.pack_forget()

    def helpData(self):
        self.indexPage.pack_forget() 
        self.aboutSysPage.pack_forget() 
        self.aboutAuthorPage.pack_forget()
        self.helpPage.pack()


def main():
    root = Tk()
    root.title("tk_data")
    root.resizable(False, False)
    MainPage(root)
    log('view run ok!')
    root.mainloop()
    

if __name__ == '__main__':
    main()
