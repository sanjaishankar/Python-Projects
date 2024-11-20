from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

# Functionality part

def clear():
    bathSoapEntry.delete(0,END)
    faceCreamEntry.delete(0, END)
    faceWashEntry.delete(0, END)
    hairOilEntry.delete(0, END)
    powderEntry.delete(0, END)
    bodyLotionEntry.delete(0, END)
    lipsticksEntry.delete(0, END)

    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    dallEntry.delete(0, END)
    teaEntry.delete(0, END)
    wheatEntry.delete(0, END)
    chillPowerEntry.delete(0, END)

    fantaEntry.delete(0, END)
    redBullEntry.delete(0, END)
    maazaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    spritEntry.delete(0, END)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    coolDrinkstaxEntry.delete(0,END)

    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    coolDrinkspriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneeEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)

    bathSoapEntry.insert(0, 0)
    faceCreamEntry.insert(0, 0)
    faceWashEntry.insert(0, 0)
    hairOilEntry.insert(0, 0)
    powderEntry.insert(0, 0)
    bodyLotionEntry.insert(0, 0)
    lipsticksEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    dallEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    chillPowerEntry.insert(0, 0)
    oilEntry.insert(0, 0)

    pepsiEntry.insert(0, 0)
    spritEntry.insert(0, 0)
    redBullEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    fantaEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),receiverEntry.get())
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent',parent=root1)
            root1.destroy()

        except:
            messagebox.showerror('Error','Something went wrong, pleasse try again')
    if textarea.get(1.0,END)=='\n':
            messagebox.showerror('Error','Bill is empty')
    else:
        if textarea.get(1.0, END) == '\n':
            messagebox.showerror('Error', 'Bill is empty')
        else:
            root1 = Toplevel()
            root1.grab_set()
            root1.title('Send Gmail')
            root1.config(bg='gray20')
            root1.resizable(0, 0)

            senderFrame = LabelFrame(root1, text="SENDER", font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
            senderFrame.grid(row=0, column=0, padx=40, pady=20)

            senderlabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'), bg='gray20', fg='white')
            senderlabel.grid(row=0, column=0, padx=10, pady=8)

            senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
            senderEntry.grid(row=0, column=1, padx=10, pady=8)

            passwordlabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
            passwordlabel.grid(row=1, column=0, padx=10, pady=8)

            passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
            passwordEntry.grid(row=1, column=1, padx=10, pady=8)

            recipientFrame = LabelFrame(root1, text="RECIPEINT", font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
            recipientFrame.grid(row=1, column=0, padx=40, pady=20)

            receiverlabel = Label(recipientFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
            receiverlabel.grid(row=0, column=0, padx=10, pady=8)

            receiverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
            receiverEntry.grid(row=1, column=1, padx=10, pady=8)

            messagelabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
            messagelabel.grid(row=1, column=0, padx=10, pady=8)

            email_textarea = Text(recipientFrame, font=('arial', 16, 'bold'), bd=2, relief=SUNKEN, width=42, height=11)
            email_textarea.grid(row=0, column=0, columnspan=2)
            email_textarea.delete(1.0, END)
            email_textarea.insert(END, textarea.get(1.0, END).replace('=','').replace('-','').replace('\t\t\t','\t\t '))

            sendButton = Button(root1, text='SEND', font=('arial', 14, 'bold'), width=15,command=send_gmail)
            sendButton.grid(row=2, column=0, pady=20)

        root1.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file= tempfile.mktemp('.txt')
        open(file,'a').write(textarea.get(1.0,END))
        os.startfile(file,'Print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')
    
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the Bill')
    if result:
        bill_content = textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        # while i  in range(billnumber):
            # i=0
            # if i >=0
            # i+=1
        billnumber=random.randint(1,1000)

billnumber = random.randint(1,1000)
def bill_area():
    if nameEntry.get()=='' or phoneeEntry.get()=='':
        messagebox.showerror('Error', 'Customer Details are Required')
    elif cosmeticpriceEntry.get()=='' or grocerypriceEntry.get()=='' or coolDrinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are Selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and coolDrinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No Products are Selected')   
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneeEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'Products\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        # for billing cosmetics items if needed
        if bathSoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathSoapEntry.get()}\t\t\t{soapprice} Rs')
        if faceCreamEntry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{faceCreamEntry.get()}\t\t\t{faceCreamprice} Rs')
        if faceWashEntry.get() != '0':
         textarea.insert(END, f'\nFace Wash\t\t\t{faceWashEntry.get()}\t\t\t{faceWashprice} Rs')
        if hairOilEntry.get() != '0':
            textarea.insert(END, f'\nHair Oil\t\t\t{hairOilEntry.get()}\t\t\t{hairOilprice} Rs')
        if powderEntry.get() != '0':
            textarea.insert(END, f'\nPowder\t\t\t{powderEntry.get()}\t\t\t{powderprice} Rs')
        if bodyLotionEntry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodyLotionEntry.get()}\t\t\t{bodyLotionprice} Rs')
        if lipsticksEntry.get() != '0':
            textarea.insert(END, f'\nLipstick\t\t\t{lipsticksEntry.get()}\t\t\t{lipsticksprice} Rs')

       # for grocety item for billing if needed
        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if dallEntry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{dallEntry.get()}\t\t\t{dallprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if chillPowerEntry.get() != '0':
            textarea.insert(END, f'\nChilli Powder\t\t\t{chillPowerEntry.get()}\t\t\t{chillprice} Rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')

        # for grocery item for billing if needed
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{Pepsiprice} Rs')
        if spritEntry.get() != '0':
            textarea.insert(END, f'\nSprit\t\t\t{spritEntry.get()}\t\t\t{spritprice} Rs')
        if fantaEntry.get() != '0':
            textarea.insert(END, f'\nFanta\t\t\t{fantaEntry.get()}\t\t\t{fantaprice} Rs')
        if redBullEntry.get() != '0':
            textarea.insert(END, f'\nRed Bull\t\t\t{redBullEntry.get()}\t\t\t{redbullprice} Rs')
        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if cocacolaEntry.get() != '0':
            textarea.insert(END, f'\nCocacola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')

        textarea.insert(END, '\n-------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t{cosmetictaxEntry.get()}')

        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery  Tax\t\t\t{grocerytaxEntry.get()}')

        if coolDrinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCool Drinks Tax\t\t\t{coolDrinkstaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t{totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')

        save_bill()

def total():
    global soapprice, faceCreamprice, faceWashprice, hairOilprice, powderprice, bodyLotionprice, lipsticksprice
    global riceprice, oilprice, dallprice, wheatprice, teaprice, chillprice
    global Pepsiprice, spritprice, redbullprice, fantaprice, cocacolaprice, maazaprice
    global totalbill
    # Cosmetic price calculation
    soapprice = int(bathSoapEntry.get())*20
    faceCreamprice = int(faceCreamEntry.get())*50
    faceWashprice = int(faceWashEntry.get()) * 80
    hairOilprice = int(hairOilEntry.get()) * 90
    powderprice = int(powderEntry.get()) * 30
    bodyLotionprice = int(bodyLotionEntry.get()) * 100
    lipsticksprice = int(lipsticksEntry.get()) * 50

    totalcosmeticprice = soapprice + faceWashprice + faceCreamprice+ hairOilprice + powderprice + bodyLotionprice + lipsticksprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0, f"{totalcosmeticprice} Rs")
    cosmetictax = totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax) +' Rs')

    # grocery price calculations

    riceprice=int(riceEntry.get())*200
    oilprice = int(oilEntry.get()) * 130
    dallprice = int(dallEntry.get()) * 80
    wheatprice = int(wheatEntry.get()) * 90
    teaprice = int(teaEntry.get()) * 120
    chillprice = int(chillPowerEntry.get()) * 30

    totalgroceryprice= riceprice + oilprice + dallprice + wheatprice + chillprice + teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0,f"{totalgroceryprice} Rs")
    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax)  + ' Rs')


    # cool drink price calculations

    Pepsiprice = int(riceEntry.get()) * 40
    spritprice = int(spritEntry.get()) * 40
    redbullprice = int(redBullEntry.get()) * 110
    fantaprice = int(fantaEntry.get()) * 40
    cocacolaprice = int(cocacolaEntry.get()) * 40
    maazaprice = int(maazaEntry.get()) * 40

    totalcooldrinkprice = Pepsiprice + spritprice + redbullprice + fantaprice + cocacolaprice + maazaprice
    coolDrinkspriceEntry.delete(0, END)
    coolDrinkspriceEntry.insert(0, f"{totalcooldrinkprice} Rs")
    coolDrinkstax = totalcooldrinkprice * 0.08
    coolDrinkstaxEntry.delete(0, END)
    coolDrinkstaxEntry.insert(0, str(coolDrinkstax) + ' Rs')

    totalbill= totalcosmeticprice + totalgroceryprice + totalcooldrinkprice + cosmetictax + grocerytax + coolDrinkstax

root = Tk()

root.title("Retail Billing System")  # name of the Window

root.geometry("1270x685")  # dimention of the window

root.iconbitmap('bill-icon.ico') # favicon of the window

headingLabel = Label(root, text= "Retail Billing System", font= ('Garamond',30,'bold'), bg= 'gray20', fg= 'Gold', bd=12, relief=GROOVE)   # fg-forground (text-color), bg- background, bd-border

headingLabel.pack(fill=X)  # fills the border linearlly

# Customer Details Frame 
customer_details_frame = LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'), fg='Gold', bd=8, relief=GROOVE, bg='gray20' )
customer_details_frame.pack(fill=X)

# Customer Name Details
nameLabel = Label(customer_details_frame, text= "Name",font=('times new roman',15,'bold'), bg='gray20', fg='white')
nameLabel.grid(row=0,column=0,padx=20)

# Entering the name in the field(box)
nameEntry = Entry(customer_details_frame, font=('Arial',15), bd = 7, width = 18) # typing-box
nameEntry.grid(row=0,column=1,padx=20)    # position of the box

# Customer Phone Number Details
phoneLabel = Label(customer_details_frame, text= "Phone No",font=('times new roman',15,'bold'), bg='gray20', fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

# Customer entering the phone number in this box
phoneeEntry = Entry(customer_details_frame, font=('Arial',15), bd = 7, width = 18) # entering the number-box
phoneeEntry.grid(row=0,column=3,padx=20,pady=2)    # position of the box

# Bill Number
billnumberLabel = Label(customer_details_frame, text= "Bill Number",font=('times new roman',15,'bold'), bg='gray20', fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)


# Entering the bill number in this box
billnumberEntry = Entry(customer_details_frame, font=('Arial',15), bd = 7, width = 18) # entering the number-box
billnumberEntry.grid(row=0,column=5,padx=20,pady=2)    # position of the box

# Search button
searchButton = Button(customer_details_frame, text='SEARCH',font=('arial',12,'bold'),bd=7, width=10,command=search_bill)  # box
searchButton.grid(row=0,column=6, padx=20, pady=8)

# Product Frame
productFrame = Frame(root)
productFrame.pack()

# Cosmetics Frame
cosmeticsFrame = LabelFrame(productFrame, text='Cosmetics',font=('times new roman',15,'bold'), fg='Gold', bd=8, relief=GROOVE, bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

# Cosmetics Products frame

#  ---------->>>> product 1
bathSoapLabel = Label(cosmeticsFrame,text='Bath Soap', font=('times new roman',15,'bold'), bg='gray20', fg='white')
bathSoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

#box
bathSoapEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
bathSoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathSoapEntry.insert(0,0)

#  ---------->>>> product 2
faceCreamLabel = Label(cosmeticsFrame,text='Face Cream', font=('times new roman',15,'bold'), bg='gray20', fg='white')
faceCreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

#box
faceCreamEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
faceCreamEntry.grid(row=1,column=1,pady=9,padx=10)
faceCreamEntry.insert(0,0)

#  ---------->>>> product 3
faceWashLabel = Label(cosmeticsFrame,text='Face Wash', font=('times new roman',15,'bold'), bg='gray20', fg='white')
faceWashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

#box
faceWashEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
faceWashEntry.grid(row=2,column=1,pady=9,padx=10)
faceWashEntry.insert(0,0)

#  ---------->>>> product 4
hairOilLabel = Label(cosmeticsFrame,text='HairOil', font=('times new roman',15,'bold'), bg='gray20', fg='white')
hairOilLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

#box
hairOilEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
hairOilEntry.grid(row=3,column=1,pady=9,padx=10)
hairOilEntry.insert(0,0)

#  ---------->>>> product 5
powderLabel = Label(cosmeticsFrame,text='Powder', font=('times new roman',15,'bold'), bg='gray20', fg='white')
powderLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

#box
powderEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
powderEntry.grid(row=4,column=1,pady=9,padx=10)
powderEntry.insert(0,0)

#  ---------->>>> product 6
bodyLotionLabel = Label(cosmeticsFrame,text='Body Lotion', font=('times new roman',15,'bold'), bg='gray20', fg='white')
bodyLotionLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

#box
bodyLotionEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
bodyLotionEntry.grid(row=4,column=1,pady=9,padx=10)
bodyLotionEntry.insert(0,0)

#  ---------->>>> product 7
lipsticksLabel = Label(cosmeticsFrame,text='Lip-Sticks', font=('times new roman',15,'bold'), bg='gray20', fg='white')
lipsticksLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

#box
lipsticksEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'), width=10, bd=5)
lipsticksEntry.grid(row=5,column=1,pady=9,padx=10)
lipsticksEntry.insert(0,0)

# Groceries Frame
groceryFrame = LabelFrame(productFrame, text='Groceries',font=('times new roman',15,'bold'), fg='Gold', bd=8, relief=GROOVE, bg='gray20')
groceryFrame.grid(row=0,column=1)

# Groceries Products frame

#  ---------->>>> product 1
riceLabel = Label(groceryFrame,text='Rice', font=('times new roman',15,'bold'), bg='gray20', fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

#box
riceEntry = Entry(groceryFrame,font=('times new roman',15,'bold'), width=10, bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)


#  ---------->>>> product 2
oilLabel = Label(groceryFrame,text='Oil', font=('times new roman',15,'bold'), bg='gray20', fg='white')
oilLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

#box
oilEntry = Entry(groceryFrame,font=('times new roman',15,'bold'), width=10, bd=5)
oilEntry.grid(row=2,column=1,pady=9,padx=10)
oilEntry.insert(0,0)


#  ---------->>>> product 3
daalLabel = Label(groceryFrame,text='Daal', font=('times new roman',15,'bold'), bg='gray20', fg='white')
daalLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

#box
dallEntry = Entry(groceryFrame,font=('times new roman',15,'bold'), width=10, bd=5)
dallEntry.grid(row=3,column=1,pady=9,padx=10)
dallEntry.insert(0,0)

#  ---------->>>> product 4
wheatLabel = Label(groceryFrame,text='Wheat', font=('times new roman',15,'bold'), bg='gray20', fg='white')
wheatLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

#box
wheatEntry = Entry(groceryFrame,font=('times new roman',15,'bold'), width=10, bd=5)
wheatEntry.grid(row=4,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

#----------->>product 5
teaLabel = Label(groceryFrame,text='Tea', font=('times new roman',15,'bold'), bg='gray20', fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry = Entry(groceryFrame,font=('times new roman',14,'bold'), width=10, bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

#  ---------->>>> product 6
chilliPowerLabel = Label(groceryFrame,text='Chilli-Powder', font=('times new roman',14,'bold'), bg='gray20', fg='white')
chilliPowerLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')

#box
chillPowerEntry = Entry(groceryFrame,font=('times new roman',14,'bold'), width=10, bd=5)
chillPowerEntry.grid(row=6,column=1,pady=9,padx=10)
chillPowerEntry.insert(0,0)

# Cool Drinks Frame
coolDrinksFrame = LabelFrame(productFrame, text='Cool Drinks',font=('times new roman',14,'bold'), fg='Gold', bd=8, relief=GROOVE, bg='gray20')
coolDrinksFrame.grid(row=0,column=2)

# Cool Drinks Products frame

#  ---------->>>> product 1
pepsiLabel = Label(coolDrinksFrame,text='Pepsi', font=('times new roman',14,'bold'), bg='gray20', fg='white')
pepsiLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

pepsiEntry = Entry(coolDrinksFrame,font=('times new roman',14,'bold'), width=10, bd=5)
pepsiEntry.grid(row=0,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

#  ---------->>>> product 2
spritLabel = Label(coolDrinksFrame,text='Sprit', font=('times new roman',14,'bold'), bg='gray20', fg='white')
spritLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

spritEntry = Entry(coolDrinksFrame,font=('times new roman',14,'bold'), width=10, bd=5)
spritEntry.grid(row=1,column=1,pady=9,padx=10)
spritEntry.insert(0,0)

#  ---------->>>> product 3
redBullLabel = Label(coolDrinksFrame,text='Red Bull', font=('times new roman',15,'bold'), bg='gray20', fg='white')
redBullLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

redBullEntry = Entry(coolDrinksFrame,font=('times new roman',14,'bold'), width=10, bd=5)
redBullEntry.grid(row=2,column=1,pady=9,padx=10)
redBullEntry.insert(0,0)

#  ---------->>>> product 4
fantaLabel = Label(coolDrinksFrame,text='Fanta', font=('times new roman',14,'bold'), bg='gray20', fg='white')
fantaLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

fantaEntry = Entry(coolDrinksFrame,font=('times new roman',14,'bold'), width=10, bd=5)
fantaEntry.grid(row=3,column=1,pady=9,padx=10)
fantaEntry.insert(0,0)

#  ---------->>>> product 5
cocacolaLabel = Label(coolDrinksFrame,text='Coca-Cola', font=('times new roman',15,'bold'), bg='gray20', fg='white')
cocacolaLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry = Entry(coolDrinksFrame,font=('times new roman',14,'bold'), width=10, bd=5)
cocacolaEntry.grid(row=4,column=1,pady=9,padx=10)
cocacolaEntry.insert(0,0)

#  ---------->>>> product 6
maazaLabel = Label(coolDrinksFrame,text='Maaza', font=('times new roman',14,'bold'), bg='gray20', fg='white')
maazaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

maazaEntry = Entry(coolDrinksFrame,font=('times new roman',14,'bold'), width=10, bd=5)
maazaEntry.grid(row=5,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

# bill frame
billframe = Frame(productFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel = Label(billframe,text='Bill Area',font=('times new roman',14,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

# scrollbar functionalities
scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea = Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# Bill Menu Frame
billmenuFrame = LabelFrame(root, text='Bill-Menu',font=('times new roman',14,'bold'), fg='Gold', bd=8, relief=GROOVE, bg='gray20',padx=2)
billmenuFrame.pack()

#  Total Cosmetics Price
cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price', font=('times new roman',15,'bold'), bg='gray20', fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=8,padx=10,sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=8,padx=10)

#  Total Groceries Price
grocerypriceLabel = Label(billmenuFrame,text='Grocery Price', font=('times new roman',13,'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=8,padx=10,sticky='w')

grocerypriceEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=8,padx=10)


#  Total Cool Drinks Price
coolDrinkspriceLabel = Label(billmenuFrame,text='Cool Drinks Price', font=('times new roman',13,'bold'), bg='gray20', fg='white')
coolDrinkspriceLabel.grid(row=2,column=0,pady=8,padx=10,sticky='w')

coolDrinkspriceEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'), width=10, bd=5)
coolDrinkspriceEntry.grid(row=2,column=1,pady=8,padx=10)

#  Total Cosmetics Tax
cosmetictaxLabel = Label(billmenuFrame,text='Cosmetic Tax', font=('times new roman',15,'bold'), bg='gray20', fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

#  Total Groceries tax
grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax', font=('times new roman',13,'bold'), bg='gray20', fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)


#  Total Cool Drinks Price
coolDrinkstaxLabel = Label(billmenuFrame,text='Cool Drinks Tax', font=('times new roman',13,'bold'), bg='gray20', fg='white')
coolDrinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

coolDrinkstaxEntry = Entry(billmenuFrame,font=('times new roman',13,'bold'), width=10, bd=5)
coolDrinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)

# button-frame

buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton= Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

# bill button
billButton= Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

# Email button
emailButton= Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

# Print button
printButton= Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

# Clear button
clearButton= Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()  # opens a window