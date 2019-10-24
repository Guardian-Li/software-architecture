from tkinter import *
import figure


def show_circle(r,label):

    circle = figure.circle((float)(r))
    area = circle.area()
    girth = circle.girth()
    label["text"] = "面积："+(str)(area) + "\n" + "周长： "+(str)(girth)

def show_rect(s,label):
    ''' 
    s string 用空格分隔的字符串数据
    '''
    x = s.split()
    rect = figure.rectangle(float(x[0]),float(x[1]))
    area=rect.area()
    girth=rect.girth()
    label["text"] = "面积："+(str)(area) + "\n" + "周长： "+(str)(girth)

def show_triangle(s,label):
    x = s.split()
    triangle = figure.triangle(float(x[0]),float(x[1]),float(x[2]))
    area=triangle.area()
    girth=triangle.girth()
    label["text"] = "面积："+(str)(area) + "\n" + "周长： "+(str)(girth)



def show_ellipse(s,label):
    x = s.split()
    e = figure.ellipse(float(x[0]),float(x[1]))
    area = e.area()
    girth = e.girth()
    label["text"] = "面积："+(str)(area) + "\n" + "周长： "+(str)(girth)


def main():
    root = Tk()
    root.title("图形计算器")
    root.geometry("400x300")
    frame = Frame(root)
    frame_top = Frame(frame)
    tip = Label(frame_top,text="请输入数据")
    tip.grid(row = 0 , column = 0)
    entry = Entry(frame_top)
    entry.grid(row = 0, column=1)
    frame_top.pack()

    frame_res = Frame(frame)
    res = Label(frame_res,text= "")
    res.pack()
    frame_res.pack()


    frame_mid = Frame(frame)
    b1 = Button(frame_mid, text="triangle",command = lambda: show_triangle(entry.get(),res))
    b2 = Button(frame_mid, text="rectangle",command = lambda:show_rect(entry.get(),res))
    b3 = Button(frame_mid, text="circle",command = lambda: show_circle(entry.get(),res))
    b4 = Button(frame_mid, text="ellipse",command=lambda:show_ellipse(entry.get(),res))
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=4)
    frame_mid.pack()    
    frame_tip = Frame(frame)
    Label(frame_tip,text= "输入数据以空格分开").grid(row = 0)
    Label(frame_tip,text= "圆：一个浮点数，代表半径").grid(row = 1)
    Label(frame_tip,text= "椭圆：两个浮点数，代表长轴和短轴").grid(row = 2)
    Label(frame_tip,text= "长方形：两个浮点数，代表长和宽").grid(row = 3)
    Label(frame_tip,text= "三角形：三个浮点数，代表三条边").grid(row = 4)
    frame_tip.pack()
    frame.pack()
    root.mainloop()



if __name__ == '__main__':
    main()