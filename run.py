from tkinter import *
from tkinter import filedialog,Listbox,messagebox
from tkinter.ttk import Combobox 
from PIL import Image, ImageDraw, ImageFont, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import shutil
import os



colors={"Чорний":"black","Білий":"white" ,"Жовтий":"Yellow"}
ttfs={"Calibri-Bold":"fonts\\Calibri-Bold.ttf", "Nunito":"fonts\\Nunito-VariableFont_wght.ttf", "Roboto-Bold":"fonts\\Roboto-Bold.ttf", "Roboto-ThinItalic":"fonts\\Roboto-ThinItalic.ttf"}
cords=[]
settings = {}
send={}
defont="fonts\\SometypeMono-VariableFont_wght.ttf",12
defont1="fonts\\SometypeMono-VariableFont_wght.ttf",9
defont2="fonts\\SometypeMono-VariableFont_wght.ttf",16
lines=2
drav=False
recivers=[]
pathes=[]

# Функция для открытия изображения


# Загружаем данные из файла CSV
data = []
with open('shablon.txt', encoding='utf-8') as file:
    for row in file:
        
        data.append(row)


ok=False
out = [i.strip() for i in data]
text = out[0]
n=0
#print(out)
#print(len(out))

def create_send():
    
    
    global send,message_window
    folder_path_to_clear = 'Final'
    shutil.rmtree(folder_path_to_clear)
    os.makedirs('Final', exist_ok=True)
    certificate_template = Image.open(cert_path)
    #print(lines)
    

        
    for i in range(0,len(out),lines+1):
        count=i
        cot=0
        #print(i)
        recivers.append(out[int(lines)])
        certificate = certificate_template.copy()
        draw = ImageDraw.Draw(certificate)
        
        while count<lines+i:
            name=out[count]
            #print(cords,"nnnn",cot)
            #print("count",count)
            font=ImageFont.truetype(cords[cot][1],int(cords[cot][2])*2)
        
            rect_center=cords[cot][0][0]+(cords[cot][0][2]-cords[cot][0][0])/2
            text_center=draw.textlength(name, font)/2
            moved_center=rect_center-text_center

            draw.text((moved_center , cords[cot][4]*2), name, fill=cords[cot][3],font=font)
            count+=1
            cot+=1
            
        # Сохраняем сертификат
        
        certificate_path = f'Final\\{out[i]}.png'
        pathes.append(certificate_path)
        certificate.save(certificate_path)
        
    message_window = Toplevel(root)
    message_window.title("Сертифікати збережено")

    label = Label(message_window, text="Файли збережено в папці 'Final'.")
    label.pack(padx=20, pady=20)
    send_button = Button(message_window, text="Відправити", command=Finalsend)
    send_button.pack(pady=10)
        # your password = "your password"
        

def Finalsend():
    send_button.config( text="Відправити",command=Finalsend)
    message_window.destroy()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    subtype="png"
    reciver=0
    x=False
    try:
        sender=settings["mail"]
        password=settings["mail_pass"]
        server.login(sender, password)
    except Exception:
         return messagebox.showwarning(title='Відправка не почата', message="Перевірте пошту та пароль в налаштуваннях!")
    messagebox.showinfo(title='Відправка почата', message="Відправка, зачекайте")
    for i in (pathes):
        
        try:

            msg = MIMEMultipart()
            msg["From"] = sender
            msg["To"] = recivers[reciver]
            msg["Subject"] = send[0]
            
            
            
            msg.attach(MIMEText(send[1]))
        
                
            with open(i, "rb") as f:
                file = MIMEImage(f.read(), subtype)
            
            file.add_header('content-disposition', 'attachment', filename=i)
            msg.attach(file)
        
            server.sendmail(sender, recivers[reciver], msg.as_string())
            x=True
            reciver+=1
        except Exception:
            x=False
            return messagebox.showwarning(title='Відправка не почата', message="Перевірте пошту та пароль в налаштуваннях!")
    if x==True:
        messagebox.showinfo(title='Сертифікати відправлено', message="Сертифікати відправлено!")
        
           
        
        
def open_image():
    global cert_path
    global certificate
    global image
    global cords
    global file_path,lines
    global back_number
    global drav
    #lines = settings.get('lines')
    back_number=0
    file_path= filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    cert_path= file_path
    if file_path:
        cords=[]
        certificate = Image.open(file_path)
        width, height = certificate.size
        certificate = certificate.resize((width//2, height//2))
        image = ImageTk.PhotoImage(certificate)
        label.config(image=image)
        label.image = image
        
        open_button.config(text="Повернутися\n назад",command=back,state="disabled")
        drav=True

     

def save():
    global lines
    global cords,text,n,file_path,back_number,width, height
    global cert_path, image, certificate,ok
    
    ##print(lines)
    try:
        lines=int(lines)
    except TypeError: pass
        
    if type(lines)== int:

        
        add_text_button.config(state="disabled")
        fonts= ttfs[combo_ttf.get()]
        size=combo_size.get()
        for i in range(0,len(lens)):
            lens[i]=lens[i]*2
            
        cords.append(([lens,fonts,size,color,y]))
        ###print(cords)
        ###print(cords[0][3])
       

        if len(cords)== lines:
            send_button.config(state="normal")
            name_combobox.config(state="normal")
            
            
        certificate_template = Image.open(file_path)
        certificate = certificate_template.copy()
        draw = ImageDraw.Draw(certificate)
        font=ImageFont.truetype(cords[n][1],int(cords[n][2])*2)
        
        rect_center=cords[n][0][0]+(cords[n][0][2]-cords[n][0][0])/2
        text_center=draw.textlength(text, font)/2
        moved_center=rect_center-text_center

        draw.text((moved_center , cords[n][4]*2), out[n], fill=cords[n][3],font=font)
        
        back_number+=1
        file_path = f'Cache\\Cache_certificate{back_number}.png'
        open_button.config(state="normal")
        
        #print(back_number)
        
        certificate.save(file_path)
        certificate = Image.open(file_path)
        width, height = certificate.size
        certificate = certificate.resize((width // 2, height // 2))
        image = ImageTk.PhotoImage(certificate)
        label.config(image=image)
        label.image = image
        
        n+=1
        text=out[n]
        ok=False
        #print("saved",cords)
        
        
        
        
    else:
        messagebox.showwarning(title='Помилка', message="Ви не ввели скільки записів плануєте зробити")
        open_settings()
        
    
# Функция для добавления текста
def add_text(event):
    global certificate,ok
    global image,x,y,width, height,font,lines,cords,color,rect_center,lens
    #print(event)
    try:
        lines=int(lines)
    except TypeError: pass
    if type(lines)== int :
        if len(cords) <lines and drav:
            lens=[]
            font = ImageFont.truetype(ttfs[combo_ttf.get()],int(combo_size.get()))  # Укажите путь к шрифту
            draw = ImageDraw.Draw(certificate)
            color= colors[combo_color.get()]
            
            Lens=draw.textbbox((event.x, event.y), text, font=font)

            for i in Lens:
                lens.append(i)
            lens[1]+=1
            lens[3]-=1
            lens[0]-=25
            lens[2]+=25
            rect_center=lens[0]+(lens[2]-lens[0])/2
            text_center=draw.textlength(text, font)/2
            moved_center=rect_center-text_center
            draw.rectangle((lens[0],lens[1],lens[2],lens[3]), outline='grey')
            draw.text((moved_center, event.y), text, fill=color, font=font)
                
            #print(event.x, event.y)
            x=moved_center
            y=event.y
            
            image = ImageTk.PhotoImage(certificate)
        
            label.config(image=image)
            label.image = image
            certificate = Image.open(file_path)
            width, height = certificate.size
            certificate = certificate.resize((width//2, height//2)) 
            global add_text_button
            if len(cords)< lines:
                add_text_button.config(state="normal")
            ok=True
    else:
        messagebox.showwarning(title='Помилка', message="Ви не ввели скільки записів плануєте зробити")
        open_settings()
    
def open_settings():
    settings_window = Toplevel(root,background="Light Slate Gray")
    settings_window.title("Налаштування")
    frame1_label=Label(settings_window, text="Налаштування відправки", background="Light Slate Gray", font=defont2, height=1,fg="Lavender")
    frame1_label.grid(row=0, column=1, sticky="we",pady=0)
    
    frame1 = Frame(settings_window, bd=2, relief=SUNKEN)
    frame1.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    
    number_label = Label(frame1, text="Кількість об'єктів для редагування", background="lightgrey", font=defont, height=1)
    number_label.grid(row=0, column=0, sticky="w")

    mail_label = Label(frame1, text="Ваш email", background="lightgrey", font=defont, height=1)
    mail_label.grid(row=1, column=0, sticky="w")

    password_label = Label(frame1, text="Ваш пароль від email", background="lightgrey", font=defont, height=1)
    password_label.grid(row=2, column=0, sticky="w")

    text_lines = Entry(frame1)
    text_lines.grid(row=0, column=1, padx=25, pady=10)
    mail = Entry(frame1)
    mail.grid(row=1, column=1, padx=25, pady=10)
    mail_pass = Entry(frame1)
    mail_pass.grid(row=2, column=1, padx=25, pady=10)


    # Заполняем поля данными из сохраненных настроек (если они есть)
    text_lines.insert(0, settings.get("lines", 2))
    mail.insert(0, settings.get("mail", "mail"))
    mail_pass.insert(0, settings.get("mail_pass", "password"))
    
    frame3_label=Label(settings_window, text="Налаштування листа", background="Light Slate Gray", font=defont2, height=1,fg="Lavender")
    frame3_label.grid(row=2, column=1, sticky="we",pady=0)
    frame3 = Frame(settings_window, bd=2, relief=SUNKEN)
    frame3.grid(row=3, column=1, padx=10, pady=10, sticky="n")

    zagol_label = Label(frame3, text="Заголовок для всіх листів", background="lightgrey", font=defont, height=1)
    zagol_label.grid(row=0, column=0, sticky="w")

    body_label = Label(frame3, text="Тіло листа", background="lightgrey", font=defont, height=1)
    body_label.grid(row=1, column=0, sticky="w")

    # Создаем поля для заголовка и тела
    zagol = Entry(frame3)
    zagol.grid(row=0, column=1, padx=25, pady=10)
    body = Entry(frame3)
    body.grid(row=1, column=1, padx=25, pady=10)



    # Заполняем поля данными из сохраненных настроек (если они есть)
    zagol.insert(0, send.get("zagol", " "))
    body.insert(0, send.get("body", " "))

    def save_settings():
        global lines,settings,send,out_names,name_combobox
        # Сохраняем данные в словарь settings
        settings["lines"] = int(text_lines.get())
        settings["mail"] = mail.get()
        settings["mail_pass"] = mail_pass.get()
        lines=settings["lines"]
        # Сохраняем данные в словарь send
        send[0] = zagol.get()
        send[1] = body.get()
        # Закрываем окно настроек

        ##print(send)
        # Закрываем окно настроек
        settings_window.destroy()
        ##print(settings)
        out_names=[]
        for item in range(0,len(out),lines+1):
            out_names.append(out[item])
        name_combobox.destroy()
        name_combobox = Combobox(root, values=out_names)
        name_combobox.grid(row=0, column=1, columnspan=3, sticky="wse",ipadx=2, ipady=2, padx=[5, 5], pady=50)
        name_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

    save_button = Button(settings_window, text="Зберегти", command=save_settings)
    save_button.grid(row=5, column=1, padx=5, pady=10)


def back():
    
    global file_path, cert_path, back_number, image, certificate,n,text
    
    if back_number ==1:
        file_path = cert_path
        back_number=0
        open_button.config(state="disabled")
        cords.remove(cords[-1])
        if n!=0:
            n-=1
    else:
        back_number -= 1
        file_path = f'Cache\\Cache_certificate{back_number}.png'
        cords.remove(cords[-1])
        open_button.config(state="normal")
        
        if n!=0:
            n-=1
    name_combobox.config(state="normal")
    text=out[n]
    certificate = Image.open(file_path)
    width, height = certificate.size
    certificate = certificate.resize((width // 2, height // 2))
    image = ImageTk.PhotoImage(certificate)
    label.config(image=image)
    label.image = image
    name_combobox.config(state="disabled")
    #print(back_number)
    
    
def on_combobox_select(event):
    global text,certificate,file_path

    n=0
    file_path=cert_path
    certificate = Image.open(file_path)
    width, height = certificate.size
    certificate = certificate.resize((width // 2, height // 2))
    draw = ImageDraw.Draw(certificate)
    # Проверьте, что что-то выбрано



    # Получите следующие две строки (если они существуют)
    index = out_names.index(name_combobox.get())
    next_texts = []
    index=index*(lines+1)
    
    index1=index+lines

    for i in range(index,index1):
        next_texts.append(out[i])
    #print(cords)
    for name in next_texts:
        font=ImageFont.truetype(cords[n][1],int(cords[n][2]))
            
        rect_center=cords[n][0][0]//2+(cords[n][0][2]//2-cords[n][0][0]//2)/2
        text_center=draw.textlength(name, font)/2
        moved_center=rect_center-text_center
                
        draw.text((moved_center , cords[n][4]), name, fill=cords[n][3],font=font)
        n+=1
        
        


        image = ImageTk.PhotoImage(certificate)
        label.config(image=image)
        label.image = image

def arrow(event):
    global certificate,y,ok
    font = ImageFont.truetype(ttfs[combo_ttf.get()],int(combo_size.get()))  # Укажите путь к шрифту
    draw = ImageDraw.Draw(certificate)
    if ok:
        if event.keysym == "Up":
            y-=1
            lens[3]-=1
            lens[1]-=1
            rect_center=lens[0]+(lens[2]-lens[0])/2
            text_center=draw.textlength(text, font)/2
            moved_center=rect_center-text_center
            draw.rectangle((lens[0],lens[1],lens[2],lens[3]), outline='grey')
            draw.text((moved_center, y), text, fill=color, font=font)
            
            image = ImageTk.PhotoImage(certificate)
            label.config(image=image)
            label.image = image
            certificate = Image.open(file_path)
            width, height = certificate.size
            certificate = certificate.resize((width//2, height//2)) 
        if event.keysym == "Down":
            y+=1
            lens[3]+=1
            lens[1]+=1
            rect_center=lens[0]+(lens[2]-lens[0])/2
            text_center=draw.textlength(text, font)/2
            moved_center=rect_center-text_center
            draw.rectangle((lens[0],lens[1],lens[2],lens[3]), outline='grey')
            draw.text((moved_center, y), text, fill=color, font=font)
            
            image = ImageTk.PhotoImage(certificate)
            label.config(image=image)
            label.image = image
            certificate = Image.open(file_path)
            width, height = certificate.size
            certificate = certificate.resize((width//2, height//2)) 
        if event.keysym == "Right":
            
            lens[0]+=1
            lens[2]+=1
            rect_center=lens[0]+(lens[2]-lens[0])/2
            text_center=draw.textlength(text, font)/2
            moved_center=rect_center-text_center
            draw.rectangle((lens[0],lens[1],lens[2],lens[3]), outline='grey')
            draw.text((moved_center, y), text, fill=color, font=font)
            
            image = ImageTk.PhotoImage(certificate)
            label.config(image=image)
            label.image = image
            certificate = Image.open(file_path)
            width, height = certificate.size
            certificate = certificate.resize((width//2, height//2)) 
        if event.keysym == "Left":

            lens[0]-=1
            lens[2]-=1
            rect_center=lens[0]+(lens[2]-lens[0])/2
            text_center=draw.textlength(text, font)/2
            moved_center=rect_center-text_center
            draw.rectangle((lens[0],lens[1],lens[2],lens[3]), outline='grey')
            draw.text((moved_center, y), text, fill=color, font=font)
            
            image = ImageTk.PhotoImage(certificate)
            label.config(image=image)
            label.image = image
            certificate = Image.open(file_path)
            width, height = certificate.size
            certificate = certificate.resize((width//2, height//2)) 

    
root = Tk()
root.title("Налаштування шаблону")


# Создайте изображение и объект draw, как у вас
certificate = Image.new("RGB", (800, 600), "white")

# Преобразуйте изображение в формат PhotoImage для Tkinter

image = ImageTk.PhotoImage(certificate)

# Создайте виджет Label для отображения изображения
label = Label(root, image=image)
label.grid(row=0, column=0, sticky="nsew")  # Добавьте sticky="nsew" и уберите expand=True

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)



# Создайте кнопку "Открыть"


open_button = Button(root, text="Відкрити\n шаблон", command=open_image,font=defont1)
open_button.grid(row=0, column=3, sticky="e", ipadx=6, ipady=6, padx=[3, 7], pady=4)

settings_button = Button(root, text="Налаштування", command=open_settings)
settings_button.grid(row=0, column=2, sticky="sw", ipadx=5, ipady=6,)



send_button = Button(root, text="Зберегти всі сертифікати", command=create_send,state="disabled")
send_button.grid(row=0, column=3, sticky="se", ipadx=5, ipady=6,)


add_text_button = Button(root, text="Зберегти\n розташування", command=save,font=defont1,state="disabled")
add_text_button.grid(row=0, column=2,sticky="e", ipadx=6, ipady=6, padx=[3, 7], pady=4)
# Привяжите событие щелчка мыши к функции добавления текста
label.bind("<Button-1>", add_text)
root.bind('<Up>', arrow)
root.bind('<Down>', arrow)
root.bind('<Left>', arrow)
root.bind('<Right>', arrow)


items = ["Чорний", "Білий", "Жовтий"]
ttf = ["Calibri-Bold", "Nunito", "Roboto-Bold","Roboto-ThinItalic"]
size=[80//2,70//2,60//2, 50//2, 40//2, 30//2,20//2]
# Создаем выпадающий список

combo_color = Combobox(root, values=items,font=defont1)
combo_color.set("Чорний")  
combo_color.grid(row=0, column=1, columnspan=3, sticky="n",ipadx=2, ipady=2, padx=[5, 5], pady=35)

result_label = Label(root, text="Колір",background="lightgrey",font=defont,)
result_label.grid(row=0, column=1, columnspan=3,sticky="nwne", pady=5)

result1_label = Label(root, text="Шрифт              Розмір",background="lightgrey",font=defont,)
result1_label.grid(row=0, column=1, columnspan=3,sticky="nwne", pady=90)

combo_ttf = Combobox(root, values=ttf,font=defont1,width=12)
combo_ttf.set("Calibri-Bold")  
combo_ttf.grid(row=0, column=1, columnspan=3, sticky="nw",ipadx=2, ipady=2, padx=[5, 5], pady=120)
combo_size = Combobox(root, values=size,font=defont1,width=4)
combo_size.set("30")  
combo_size.grid(row=0, column=3, columnspan=3, sticky="ne",ipadx=2, ipady=2, padx=[5, 5], pady=120)



out_names=[]
for item in range(0,len(out),lines+1):
      out_names.append(out[item])
name_combobox = Combobox(root, values=out_names,state="disabled")
name_combobox.set("Попередній перегляд")
name_combobox.grid(row=0, column=1, columnspan=3, sticky="wse",ipadx=2, ipady=2, padx=[5, 5], pady=50)
name_combobox.bind("<<ComboboxSelected>>", on_combobox_select)


root.mainloop()
