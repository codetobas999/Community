# import required modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from click import style
import pandas as pd
import csv  
import json

# Create an instance of tkinter frame
window = Tk()
frame = ttk.Frame(window)
frame.pack(pady = 5, padx = 10)

style = ttk.Style(window)
style.theme_use("clam")
style.configure(".",font=('Tohama',9))
#style.configure('Treeview.Heading', background="white" ,foreground='black' ,font=('Tohama',9,'bold'))
style.configure('Treeview.Heading' ,font=('Tohama',9,'bold'))
# Set the size of the tkinter window
window.geometry("1200x600")
window.resizable(False, False) 
window.iconbitmap('')
window.title("View & Export Data Refund")
 
 
def Get_DF(in_con_type,in_con_text):
    global df
    global cfg_data_source
    # Load data from source
    #con_mobile_no = '019XX5268'
    print('Get_DF') 
    con_text = in_con_text #'พี.เอส.พี'
    #con_cust_group_acc = in_con_name # '1040022317' 
    file_seq = 0 
    #lst_file = ['DATA_REFUND_EQ_R.csv','DATA_REFUND_NOT_R.csv']
    for cfg in cfg_data_source['config_data_source']:
        finename = cfg['path']+'/'+cfg['file_name']
        file_seq += 1 
        print("----------------- fine Name #{} = {}-----------------------".format(file_seq, finename))  
        with open(finename, encoding="utf8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter="," )
            row_index = 0 
            #if row[0] == con_mobile_no :  
            #if row[1] == con_cust_group_acc :  
            for row in csvreader:
                row_index +=1
                if in_con_type == 'mobile' :
                    index_search = 0    
                elif in_con_type == 'account' :
                    index_search = 1     
                elif in_con_type == 'name' :
                    index_search = 3 
                else :
                    index_search = -1
                if index_search >= 0 : 
                    if row[index_search].find(con_text) >= 0 : 
                        df = pd.concat([df, 
                                        pd.DataFrame({
                                                    df.columns[0]: [row[0]],
                                                    df.columns[1]: [row[1]],
                                                    df.columns[2]: [row[2]],
                                                    df.columns[3]: [row[3]],
                                                    df.columns[4]: [row[4]],
                                                    df.columns[5]: [row[5]],
                                                    df.columns[6]: [row[6]],
                                                    df.columns[7]: [row[7]],
                                                    df.columns[8]: [row[8]],
                                                    df.columns[9]: [row[9]],
                                                    df.columns[10]: [row[10]], 
                                                    df.columns[11]: [row[11]],
                                                    df.columns[12]: [row[12]],
                                                    df.columns[13]: [row[13]],
                                                    df.columns[14]: [row[14]],
                                                    df.columns[15]: [row[15]],
                                                    df.columns[16]: [row[16]],
                                                    df.columns[17]: [row[17]],
                                                    df.columns[18]: [row[18]],
                                                    df.columns[19]: [row[19]],
                                                    df.columns[20]: [row[20]],
                                                    df.columns[21]: [row[21]],
                                                    df.columns[22]: [row[22]],
                                                    df.columns[23]: [row[23]],
                                                    df.columns[24]: [row[24]],
                                                    df.columns[25]: [row[25]],
                                                    df.columns[26]: [row[26]],
                                                    df.columns[27]: [row[27]],
                                                    df.columns[28]: [row[28]],
                                                    df.columns[29]: [row[29]],
                                                    df.columns[30]: [row[30]],                                         
                                                    df.columns[31]: [row[31]],
                                                    df.columns[32]: [row[32]],
                                                    df.columns[33]: [row[33]],
                                                    df.columns[34]: [row[34]]
                                                    })
                                        ], ignore_index=True)
                else : 
                    df = pd.DataFrame()

            print('Found Data : ' , len(df))      
        csvfile.close
    return df

def Event_Search():
    global tree
    global df
    global txt_con_text
    '''
    messagebox.showinfo('information', 'Hi! You got a prompt.')
    messagebox.showerror('error', 'Something went wrong!')
    messagebox.showwarning('warning', 'accept T&C')
    messagebox.askquestion('Ask Question', 'Do you want to continue?')
    messagebox.askokcancel('Ok Cancel', 'Are You sure?')
    messagebox.askyesno('Yes|No', 'Do you want to proceed?')
    messagebox.askretrycancel('retry', 'Failed! want to try again?')
    '''
    #messagebox.showerror('error', 'Something went wrong!')
    print('Event_Search') 
    df = pd.DataFrame() 
    df = pd.DataFrame(columns = ['mobile_no','cust_group_acc','pay_location','name','shift','terminal','bill_cycle','duration','new_order_no','vat_deposit','create_date','deposit_amount','refund_date','transfer_to_acc_no','first_paid','cn_ar_no','owner','current_balance','refund_no','cancel_order_no','dn_no','customer_accrual','doc_receipt_no','transfer_no','pay_type','deposit_refund_status','bank','branch','cheque_name','bank_account','cheque_no','pay_date','segment','clearing_date','remark']) 
    tree.delete(*tree.get_children())

    v_con_type = ''
    if str(v_sel.get()) == '1' :
        v_con_type = 'mobile' 
    elif str(v_sel.get()) == '2' :
        v_con_type = 'account' 
    elif str(v_sel.get()) == '3' :
        v_con_type = 'name' 

    v_con_text = txt_con_text.get()  

    print('v_con_type : ',v_con_type)
    print('v_con_text : ',v_con_text)
    if len(v_con_type) > 0 :
        if len(v_con_text) > 0 : 
            # Load data from source
            df = Get_DF(v_con_type,v_con_text)
        
            # Extract number of rows and columns
            n_rows = df.shape[0]
            n_cols = df.shape[1]
        
            for i in range(n_rows):
                #for j in range(n_cols): 
                if i % 2 == 0 :
                    tree.insert("", i, text="", tags = ['even'], values=(i+1,df.loc[i][0], df.loc[i][1], df.loc[i][3], df.loc[i][8],df.loc[i][9],df.loc[i][11],df.loc[i][12],df.loc[i][18],df.loc[i][21],df.loc[i][24],df.loc[i][25],df.loc[i][34]))
                else :
                    tree.insert("", i, text="",   values=(i+1,df.loc[i][0], df.loc[i][1], df.loc[i][3], df.loc[i][8],df.loc[i][9],df.loc[i][11],df.loc[i][12],df.loc[i][18],df.loc[i][21],df.loc[i][24],df.loc[i][25],df.loc[i][34]))
        else :
            messagebox.showerror('error', 'Data Input wrong!')          
    else :
        messagebox.showerror('error', 'Data Type wrong!')            
        

def Event_Clear():
    global tree
    global df
    global v_con_text
    #  Set Columns , No display 
    v_con_text.set('')   
    print('Event_Clear') 
    df = pd.DataFrame() 
    df = pd.DataFrame(columns = ['mobile_no','cust_group_acc','pay_location','name','shift','terminal','bill_cycle','duration','new_order_no','vat_deposit','create_date','deposit_amount','refund_date','transfer_to_acc_no','first_paid','cn_ar_no','owner','current_balance','refund_no','cancel_order_no','dn_no','customer_accrual','doc_receipt_no','transfer_no','pay_type','deposit_refund_status','bank','branch','cheque_name','bank_account','cheque_no','pay_date','segment','clearing_date','remark']) 
    tree.delete(*tree.get_children())
 #-------------------------------------------------------------------         
     
         
def Event_Export():
    global df
    global cfg_data_source
    print('Event_Export') 
    for cfg in cfg_data_source['config_data_destination']:
        finename = cfg['path']+'/'+cfg['file_name'] 
        print("----------------- Export fine Name = {}-----------------------".format(finename))  
        df.to_excel(finename) 

def Event_SeletRadioCon():
   selection = "You selected the option " + str(v_sel.get())
   print(selection)
   #label.config(text = selection)

def Init():
    global cfg_data_source
    global v_con_text
    global v_sel
    lst_file = open('./config/lst_file.json')
    cfg_data_source = json.load(lst_file)
    lst_file.close() 
    v_con_text.set('')
    v_sel.set(1)
#---------------- Main -------------------------------------------
#-------------------------------------------------------------------
v_con_text = StringVar() #Search Text 
v_sel = IntVar() 
df = pd.DataFrame() 
df = pd.DataFrame(columns = ['mobile_no','cust_group_acc','pay_location','name','shift','terminal','bill_cycle','duration','new_order_no','vat_deposit','create_date','deposit_amount','refund_date','transfer_to_acc_no','first_paid','cn_ar_no','owner','current_balance','refund_no','cancel_order_no','dn_no','customer_accrual','doc_receipt_no','transfer_no','pay_type','deposit_refund_status','bank','branch','cheque_name','bank_account','cheque_no','pay_date','segment','clearing_date','remark']) 

#------------------------------------------------------------------- 


 

Init()

rd_con = Radiobutton(frame, text="Mobile", variable=v_sel, value=1,command=Event_SeletRadioCon)
rd_con.grid(row=1,column = 1,padx=1,pady=1, sticky=E)

rd_con = Radiobutton(frame, text="Account", variable=v_sel, value=2,command=Event_SeletRadioCon)
rd_con.grid(row=2,column = 1,padx=1,pady=1, sticky=E)

rd_con = Radiobutton(frame, text="Name", variable=v_sel, value=3,command=Event_SeletRadioCon)
rd_con.grid(row=3,column = 1,padx=1,pady=1, sticky=E)
 
txt_con_text = Entry(frame,textvariable=v_con_text,width = 50)
txt_con_text.grid(row=2,column = 2, sticky=W)
 

search_button = Button(frame , text ="Search", height = 1, width = 16 ,bg="#000", fg="#fff", activebackground="#f00", activeforeground="#fff"  , font= ('Tohama 8 bold') , command = lambda:Event_Search())
search_button.grid(row=4,column = 1, sticky=E )

clear_button = Button(frame , text ="Clear",height = 1, width = 16 ,bg="#000", fg="#fff", activebackground="#f00", activeforeground="#fff"  , font= ('Tohama 8 bold') , command = lambda:Event_Clear())
clear_button.grid(row=4,column = 2, sticky=W )
 

save_button = Button(frame , text ="Save",height = 1, width = 16 ,bg="#000", fg="#fff", activebackground="#f00", activeforeground="#fff"  , font= ('Tohama 8 bold') , command = lambda:Event_Export())
save_button.grid(row=7,column = 1, sticky=E)
 
tree = ttk.Treeview(frame, show="headings" , height=20 ,pad =5) # The first column of the table does not show 
#'mobile_no','cust_group_acc','pay_location','name','shift','terminal','bill_cycle','duration','new_order_no','vat_deposit','create_date','deposit_amount','refund_date','transfer_to_acc_no','first_paid','cn_ar_no','owner','current_balance','refund_no','cancel_order_no','dn_no','customer_accrual','doc_receipt_no','transfer_no','pay_type','deposit_refund_status','bank','branch','cheque_name','bank_account','cheque_no','pay_date','segment','clearing_date','remark'
tree["columns"] = ('no','mobile_no','cust_group_acc','name','new_order_no','vat_deposit','deposit_amount','refund_date','refund_no','customer_accrual','pay_type','deposit_refund_status','remark')
tree.grid(row=5, columnspan=4)  
tree.column('no', width=30, stretch=False, minwidth=30)
tree.column('mobile_no', width=80, stretch=False, minwidth=50)
tree.column('cust_group_acc', width=80, stretch=False, minwidth=50)  
tree.column('name', width=150, stretch=False, minwidth=50) 
tree.column('new_order_no', width=80, stretch=False, minwidth=50) 
tree.column('vat_deposit', width=80, stretch=False, minwidth=50) 
tree.column('deposit_amount', width=80, stretch=False, minwidth=50) 
tree.column('refund_date', width=80, stretch=False, minwidth=50) 
tree.column('refund_no', width=80, stretch=False, minwidth=50) 
tree.column('customer_accrual', width=80, stretch=False, minwidth=50) 
tree.column('pay_type', width=80, stretch=False, minwidth=50) 
tree.column('deposit_refund_status', width=30, stretch=False, minwidth=50) 
tree.column('remark', width=200, stretch=False, minwidth=50)  

#  Indicator head 
tree.heading('no', text=" no ")
tree.heading('mobile_no', text=" mobile_no ")
tree.heading('cust_group_acc', text=" cust_group_acc" ) 
tree.heading('name', text=" name ") 
tree.heading('new_order_no', text=" new_order_no ") 
tree.heading('vat_deposit', text=" vat_deposit ") 
tree.heading('deposit_amount', text=" deposit_amount ") 
tree.heading('refund_date', text=" refund_date ") 
tree.heading('refund_no', text=" refund_no ") 
tree.heading('customer_accrual', text=" customer_accrual ") 
tree.heading('pay_type', text=" pay_type ") 
tree.heading('deposit_refund_status', text=" deposit_refund_status ") 
tree.heading('remark', text=" remark ")  

#tree.tag_configure('t1', background = 'gray')
#tree.tag_configure('t2', background = 'white')
tree.tag_configure('even', background="#e8e8e8")

# ----vertical scrollbar------------
vbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=vbar.set,)
#tree.grid(row=0, column=0, sticky=NSEW)
vbar.grid(row=5, column=4, sticky=NS)

# ----horizontal scrollbar----------
hbar = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
tree.configure(xscrollcommand=hbar.set)
hbar.grid(row=6, columnspan=4, sticky=EW)

window.mainloop()