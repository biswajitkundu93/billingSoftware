from tkinter import *
from tkinter import messagebox
import math,random,string,os


class Bill_App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Billing Software")
        self.root.geometry("1350x768+0+0")
        self.root.configure(bg="Black")
        
        backgroundcolor = "#074463"
        foregroundcolor = "White"
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=backgroundcolor,fg="gold", font=("times new roman",30,"bold")).pack(fill=X)
        
        #===========veriables===============
        #=====cosmatic==========
        self.soap = StringVar()
        self.face_creeam = StringVar()
        self.face_wash = StringVar()
        self.spray = StringVar()
        self.gell = StringVar()
        self.loshan = StringVar()
        #======grocery==========
        self.rice = StringVar()
        self.food_oil = StringVar()
        self.daal = StringVar()
        self.wheat = StringVar()
        self.sugar = StringVar()
        self.tea = StringVar()
        #======cold drinks======
        self.maza = StringVar()
        self.cock = StringVar()
        self.frooti = StringVar()
        self.thumbsup = StringVar()
        self.limca = StringVar()
        self.sprite = StringVar()
        #=Total product and Tax=
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        #=====Customer==========
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()

        # self.bill_no.set(str(random.randint(1000,9999)))

        #==============customer==============
        f1 = LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE, font=("times new roman",15),fg="gold",bg=backgroundcolor)
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(f1,text="Customer Name",bg=backgroundcolor,fg=foregroundcolor,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(f1,width=15,bd=7,textvariable=self.c_name, relief=SUNKEN,font="arial 15",).grid(row=0,column=1,padx=20,pady=5)

        cphn_lbl = Label(f1,text="Phone No.",bg=backgroundcolor,fg=foregroundcolor,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(f1,width=15,bd=7,relief=SUNKEN,textvariable=self.c_phone,font="arial 15",).grid(row=0,column=3,padx=20,pady=5)

        c_bill_lbl = Label(f1,text="Bill No.",bg=backgroundcolor,fg=foregroundcolor,font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt = Entry(f1,width=15,bd=7,relief=SUNKEN,textvariable=self.bill_no,font="arial 15",).grid(row=0,column=5,padx=20,pady=5)

        bill_btn = Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #====================Cosmatics==============
        f2 = LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE, font=("times new roman",15),fg="gold",bg=backgroundcolor)
        f2.place(x=0,y=190,width=335)

        bath_lbl = Label(f2,text="Bath Shop",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=5,sticky='w')
        bath_txt = Entry(f2,width=10,textvariable=self.soap,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        face_cream_lbl = Label(f2,text="Face Cream ",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=1,column=0,padx=5,pady=10,sticky='w')
        face_cream_txt = Entry(f2,width=10,textvariable=self.face_creeam,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        face_w_lbl = Label(f2,text="Face Wash",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=5,sticky='w')
        face_w_txt = Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        hair_s_lbl = Label(f2,text="Hair Spray",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=5,sticky='w')
        hair_s_txt = Entry(f2,width=10,textvariable=self.spray,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)

        hair_g_lbl = Label(f2,text="Hair Gell",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=5,sticky='w')
        hair_g_txt = Entry(f2,width=10,textvariable=self.gell,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)

        body_lbl = Label(f2,text="Body Loshan",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=5,sticky='w')
        body_txt = Entry(f2,width=10,textvariable=self.loshan,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #====================Grocery==============
        f3 = LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE, font=("times new roman",15),fg="gold",bg=backgroundcolor)
        f3.place(x=340,y=190,width=325)

        g1_lbl = Label(f3,text="Rice",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=5,sticky='w')
        g1_txt = Entry(f3,width=10,textvariable=self.rice,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        g2_lbl = Label(f3,text="Food Oil",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=5,sticky='w')
        g2_txt = Entry(f3,width=10,textvariable=self.food_oil,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        g3_lbl = Label(f3,text="Daal",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=5,sticky='w')
        g3_txt = Entry(f3,width=10,textvariable=self.daal,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        g4_lbl = Label(f3,text="Wheat",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=5,sticky='w')
        g4_txt = Entry(f3,width=10,textvariable=self.wheat,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)

        g5_lbl = Label(f3,text="Suger",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=5,sticky='w')
        g5_txt = Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)

        g6_lbl = Label(f3,text="Tea",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=5,sticky='w')
        g6_txt = Entry(f3,width=10,textvariable=self.tea,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #====================Cold Drinks==============
        f4 = LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE, font=("times new roman",15),fg="gold",bg=backgroundcolor)
        f4.place(x=670,y=190,width=332)

        c1_lbl = Label(f4,text="Mazza",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=5,sticky='w')
        c1_txt = Entry(f4,width=10,textvariable=self.maza,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        c2_lbl = Label(f4,text="cock",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=1,column=0,padx=10,pady=5,sticky='w')
        c2_txt = Entry(f4,width=10,textvariable=self.cock,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        c3_lbl = Label(f4,text="Frooti",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=2,column=0,padx=10,pady=5,sticky='w')
        c3_txt = Entry(f4,width=10,textvariable=self.frooti,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=5)

        c4_lbl = Label(f4,text="Thumbs Up",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=3,column=0,padx=10,pady=5,sticky='w')
        c4_txt = Entry(f4,width=10,textvariable=self.thumbsup,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=5)

        c5_lbl = Label(f4,text="Limca",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=4,column=0,padx=10,pady=5,sticky='w')
        c5_txt = Entry(f4,width=10,textvariable=self.limca,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=5)

        c6_lbl = Label(f4,text="Sprite",font=("times new roman",18,"bold"),bg=backgroundcolor,fg="lightgreen").grid(row=5,column=0,padx=10,pady=5,sticky='w')
        c6_txt = Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",18,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=5)

        #==========Bill area=========
        f5 = LabelFrame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1010,y=190,width=350,height=348)

        bill_title = Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(f5,orient=VERTICAL)
        self.textarea = Text(f5,yscrollcommand=scrol_y.set,state="normal")
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #==============Button fram =============
        f6 = LabelFrame(self.root,text="Bill Manu",bd=10,relief=GROOVE, font=("times new roman",15),fg="gold",bg=backgroundcolor)
        f6.place(x=0,y=545,relwidth=1)

        m1_lbl = Label(f6,text="Total Cosmetic Price",bg=backgroundcolor,fg="white",font=("times new roman ",14,"bold")).grid(row=0,column=0,padx=20,pady=3,sticky='w')
        m1_txt = Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=3)

        m2_lbl = Label(f6,text="Total Grocery Price",bg=backgroundcolor,fg="white",font=("times new roman ",14,"bold")).grid(row=1,column=0,padx=20,pady=3,sticky='w')
        m2_txt = Entry(f6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=20,pady=3)
        
        m3_lbl = Label(f6,text="Total cold Drinks Price",bg=backgroundcolor,fg="white",font=("times new roman ",14,"bold")).grid(row=2,column=0,padx=20,pady=3,sticky='w')
        m3_txt = Entry(f6,width=18,textvariable=self.cold_drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=20,pady=3)
        
        c1_lbl = Label(f6,text="Cosmetic Tax",bg=backgroundcolor,fg="white",font=("times new roman ",14,"bold")).grid(row=0,column=2,padx=20,pady=3,sticky='w')
        c1_txt = Entry(f6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=3)

        c2_lbl = Label(f6,text="Grocery Tax",bg=backgroundcolor,fg="white",font=("times new roman ",14,"bold")).grid(row=1,column=2,padx=20,pady=3,sticky='w')
        c2_txt = Entry(f6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=20,pady=3)
        
        c3_lbl = Label(f6,text="Cold Drinks Tax",bg=backgroundcolor,fg="white",font=("times new roman ",14,"bold")).grid(row=2,column=2,padx=20,pady=3,sticky='w')
        c3_txt = Entry(f6,width=18,textvariable=self.cold_drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=20,pady=3)

        btn_f = Frame(f6,bd=6,relief=GROOVE,bg="dark green")
        btn_f.place(x=760,width=572,height=120)
        total_btn = Button(btn_f,text="Total\n",bg="cadetblue",fg="black",pady=15,width=9,font="arial 15 bold",command=self.totaal_fun).grid(row=0,column=0,padx=10,pady=15)
        clear_btn = Button(btn_f,text="Clear\n",bg="cadetblue",fg="black",pady=15,width=9,font="arial 15 bold",command=self.clear_fun).grid(row=0,column=2,padx=5,pady=15)
        gbill_btn = Button(btn_f,text="Genarete\nBill",bg="cadetblue",fg="black",pady=15,width=9,font="arial 15 bold",command=self.bill_area).grid(row=0,column=1,padx=5,pady=15)
        exit_btn = Button(btn_f,text="Exit\n",bg="cadetblue",fg="black",pady=15,width=9,font="arial 15 bold",command=self.exit_fun).grid(row=0,column=3,padx=5,pady=15)
        self.clear_fun()
        self.welcome_bill()
        self.root.mainloop()


    def totaal_fun(self):
        try:
            self.c_s_p = int(self.soap.get())*40
            self.c_fc_p = int(self.face_creeam.get())*120 
            self.c_fw_p = int(self.face_wash.get())*60
            self.c_hs_p = int(self.spray.get())*180
            self.c_hg_p = int(self.gell.get())*150
            self.c_hl_p = int(self.loshan.get())*180
            self.total_cosmetic_price = float(
                                            self.c_s_p+
                                            self.c_fc_p+
                                            self.c_fw_p+
                                            self.c_hs_p+
                                            self.c_hg_p+
                                            self.c_hl_p
                                            )   
            self.g_r_p = int(self.rice.get())*80
            self.g_f_p = int(self.food_oil.get())*180
            self.g_d_p = int(self.daal.get())*60
            self.g_w_p = int(self.sugar.get())*150
            self.g_s_p = int(self.tea.get())*150
            self.g_t_p = int(self.wheat.get())*240
            self.total_grocery_price = float(
                                            self.g_r_p+
                                            self.g_f_p+
                                            self.g_d_p+
                                            self.g_w_p+
                                            self.g_s_p+
                                            self.g_t_p
                                            )

            self.d_m_p = int(self.maza.get())*60
            self.d_c_p = int(self.cock.get())*60
            self.d_f_p = int(self.frooti.get())*50
            self.d_t_p = int(self.thumbsup.get())*45
            self.d_l_p = int(self.limca.get())*40
            self.d_s_p = int(self.sprite.get())*60
            self.total_cold_drinks_price = float(
                                            self.d_m_p+
                                            self.d_c_p+
                                            self.d_f_p+
                                            self.d_t_p+
                                            self.d_l_p+
                                            self.d_s_p
                                            )
        except:
            messagebox.showerror("Error","Enter number only")
        else:
            self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
            self.cosmetic_tax.set("Rs. "+str(round(self.total_cosmetic_price*0.05,2)))

            self.grocery_price.set("Rs. "+str(self.total_grocery_price))
            self.grocery_tax.set("Rs. "+str(round(self.total_grocery_price*0.1,2)))

            self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
            self.cold_drinks_tax.set("Rs. "+str(round(self.total_cold_drinks_price*0.05,2)))

    def clear_fun(self):
        #=====cosmatic==========
        self.soap.set("0")
        self.face_creeam.set("0")
        self.face_wash.set("0")
        self.spray.set("0")
        self.gell.set("0")
        self.loshan.set("0")
        #======grocery==========
        self.rice.set("0")
        self.food_oil.set("0")
        self.daal.set("0")
        self.wheat.set("0")
        self.sugar.set("0")
        self.tea.set("0")
        #======cold drinks======
        self.maza.set("0")
        self.cock.set("0")
        self.frooti.set("0")
        self.thumbsup.set("0")
        self.limca.set("0")
        self.sprite.set("0")
        #=Total product and Tax=
        self.cosmetic_price.set("0")
        self.grocery_price.set("0")
        self.cold_drinks_price.set("0")
        
        self.cosmetic_tax.set("0")
        self.grocery_tax.set("0")
        self.cold_drinks_tax.set("0")
        #=====Customer==========
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no,set("")
        self.search_bill.set("")

        self.welcome_bill()

        
    def bill_no_genaretor(self):
        alpha = list(string.ascii_uppercase)
        digits = list(string.digits)
        g_bill_no = random.choices(alpha)[0]+"-"+random.choices(alpha)[0]+random.choices(digits)[0]+"-"+str(random.randint(1000,9999))
        return g_bill_no


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "-"*38+"\n")
        self.textarea.insert(END,"\t   Welcome Reatil shop\n")
        self.textarea.insert(END, "-"*38+"\n")
        self.bill_no.set(self.bill_no_genaretor())
        self.textarea.insert(END,f"\n Bill No. : {self.bill_no.get()}")
        if str(self.c_name.get()).isdigit():
            messagebox.showerror("Error","The invalid customer name ")
            self.textarea.delete('1.0',END)
            return False
        elif str(self.c_phone.get()).isalpha() or 10<len(str(self.c_phone.get())) or 0<len(str(self.c_phone.get()))<10 :
            messagebox.showerror("Error","The invalid customar phone number ")
            self.textarea.delete('1.0',END)
            return False
        else:
            self.textarea.insert(END,f"\n Customar Name : {self.c_name.get()}")
            self.textarea.insert(END,f"\n Phone Nn. : {self.c_phone.get()}\n")
        self.textarea.insert(END, "="*38+"\n")
        self.textarea.insert(END, "Products\t\tQuantity\t    price \n")
        self.textarea.insert(END, "="*38)
        return True

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details is missing !!!")
            return
        elif float(self.cosmetic_price.get().split()[1]) == 0.0 and float(self.grocery_price.get().split()[1]) == 0.0 and float(self.cold_drinks_price.get().split()[1]) == 0.0:
            messagebox.showerror("Error", "All fill are emety !!!")
            return            
        else:
            if self.welcome_bill():
                try:
                    if int(self.soap.get()) != 0 :
                        self.textarea.insert(END, f"\nBath Shop\t\t{self.soap.get()}\t    {float(self.c_s_p)} ")
                    if int(self.face_creeam.get()) != 0 :
                        self.textarea.insert(END, f"\nFace Cream\t\t{self.face_creeam.get()}\t    {float(self.c_fc_p)} ")
                    if int(self.face_wash.get()) != 0 :
                        self.textarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t    {float(self.c_fw_p)} ")
                    if int(self.spray.get()) != 0 :
                        self.textarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t    {float(self.c_hs_p)} ")
                    if int(self.gell.get()) != 0 :
                        self.textarea.insert(END, f"\nHair Gell\t\t{self.gell.get()}\t    {float(self.c_hg_p)} ")
                    if int(self.loshan.get()) != 0 :
                        self.textarea.insert(END, f"\nBody Loshan\t\t{self.loshan.get()}\t    {float(self.c_hl_p)} ")
                    
                    if int(self.rice.get()) != 0 :
                        self.textarea.insert(END, f"\nRice\t\t{self.rice.get()}\t    {float(self.g_r_p)} ")
                    if int(self.food_oil.get()) != 0 :
                        self.textarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t    {float(self.g_f_p)} ")
                    if int(self.daal.get()) != 0 :
                        self.textarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t    {float(self.g_d_p)} ")
                    if int(self.wheat.get()) != 0 :
                        self.textarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t    {float(self.g_w_p)} ")
                    if int(self.sugar.get()) != 0 :
                        self.textarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t    {float(self.g_s_p)} ")
                    if int(self.tea.get()) != 0 :
                        self.textarea.insert(END, f"\nTea\t\t{self.tea.get()}\t    {float(self.g_t_p)} ")
                    
                    if int(self.maza.get()) != 0 :
                        self.textarea.insert(END, f"\nMaza\t\t{self.maza.get()}\t    {float(self.d_m_p)} ")
                    if int(self.cock.get()) != 0 :
                        self.textarea.insert(END, f"\nCock\t\t{self.cock.get()}\t    {float(self.d_c_p)} ")
                    if int(self.frooti.get()) != 0 :
                        self.textarea.insert(END, f"\nFrooti\t\t{self.frooti.get()}\t    {float(self.d_f_p)} ")
                    if int(self.thumbsup.get()) != 0 :
                        self.textarea.insert(END, f"\nThumbs up\t\t{self.thumbsup.get()}\t    {float(self.d_t_p)} ")
                    if int(self.limca.get()) != 0 :
                        self.textarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t    {float(self.d_l_p)} ")
                    if int(self.sprite.get()) != 0 :
                        self.textarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t    {float(self.d_s_p)} ")
                    self.textarea.insert(END, "\n"+"-"*38)
                    if self.cosmetic_tax.get().split()[1] != '0.0':
                        self.textarea.insert(END, f"\nCosmetic Tax\t\t\t Rs. {self.cosmetic_tax.get().split()[1]} ")
                    if self.grocery_tax.get().split()[1] != '0.0':
                        self.textarea.insert(END, f"\nGrocery Tax\t\t\t Rs. {self.grocery_tax.get().split()[1]} ")
                    if self.cold_drinks_tax.get().split()[1] != '0.0':
                        self.textarea.insert(END, f"\nCold Drinks Tax\t\t\t Rs. {self.cold_drinks_tax.get().split()[1]} ")
                    self.textarea.insert(END, "\n"+"-"*38)
                    total_amount = (
                                    float(self.cosmetic_tax.get().split()[1])+
                                    float(self.grocery_tax.get().split()[1])+
                                    float(self.cold_drinks_tax.get().split()[1])+
                                    float(self.cosmetic_price.get().split()[1])+
                                    float(self.grocery_price.get().split()[1])+
                                    float(self.cold_drinks_price.get().split()[1])
                                    )
                    self.textarea.insert(END, f"\nTotal Amount\t\t\t Rs. {total_amount} \n")
                    self.save_bill()

                except AttributeError :
                    messagebox.showerror("Error","Fisrt click 'Total' after 'Genarate bill'")
    def exit_fun(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit...!!! ")
        if option > 0:
            self.root.destroy()
        else:
            return
    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op > 0:
            bill_data = self.textarea.get("1.0",END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(bill_data)
            f1.close()
            messagebox.showinfo("Save",f"Bill no : {self.bill_no.get()}\nhas been saved!!!")
        else:
            return
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.bill_no.get():
                f2 = open(f"bills/{i}",'r')
                self.textarea.delete("1.0",END)
                for j in f2:
                    self.textarea.insert(END,j)
                f2.close()
                present = "yes"
        if present == 'no':
            messagebox.showerror("Error","Invalid bill no")
        

  

