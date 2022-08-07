# import required modules
from tkinter import *
from tkinter import ttk
import pandas as pd
import csv  
# Create an instance of tkinter frame
window = Tk()
  
# Set the size of the tkinter window
window.geometry("800x600")
window.title("label-test")
#-------------------------------------------------------------------
v_mobile = StringVar() #Search Name
v_account = StringVar() #Search Name
v_name = StringVar() #Search Name
#-------------------------------------------------------------------  

def Get_DF(in_con_name):
    # Load data from source
    #con_mobile_no = '019XX5268'
    con_name = in_con_name #'พี.เอส.พี'
    #con_cust_group_acc = in_con_name # '1040022317'
    print("in_con_name : ", in_con_name)
    df = pd.DataFrame() 
    df = pd.DataFrame(columns = ['mobile_no','cust_group_acc','pay_location','name','shift','terminal','bill_cycle','duration','new_order_no','vat_deposit','create_date','deposit_amount','refund_date','transfer_to_acc_no','first_paid','cn_ar_no','owner','current_balance','refund_no','cancel_order_no','dn_no','customer_accrual','doc_receipt_no','transfer_no','pay_type','deposit_refund_status','bank','branch','cheque_name','bank_account','cheque_no','pay_date','segment','clearing_date','remark'])


    with open("DATA_REFUND__EQ_R.csv", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="," )
        row_index = 0

        for row in csvreader:
            row_index +=1
            #if row[0] == con_mobile_no :  
            #if row[1] == con_cust_group_acc :  
            if row[3].find(con_name) >= 0 : 
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
        return df
def Event_Search():
    mobile = v_mobile.get()
    account = v_account.get()
    name = v_name.get()
    print(mobile)
    print(account)
    print(name)
    
    # Load data from source
    df = Get_DF(mobile)
    
    tree = ttk.Treeview(window, show="headings") # The first column of the table does not show 
    tree.grid(row=1, columnspan=1)
    #'mobile_no','cust_group_acc','pay_location','name','shift','terminal','bill_cycle','duration','new_order_no','vat_deposit','create_date','deposit_amount','refund_date','transfer_to_acc_no','first_paid','cn_ar_no','owner','current_balance','refund_no','cancel_order_no','dn_no','customer_accrual','doc_receipt_no','transfer_no','pay_type','deposit_refund_status','bank','branch','cheque_name','bank_account','cheque_no','pay_date','segment','clearing_date','remark'
    tree["columns"] = ('mobile_no','cust_group_acc','name','new_order_no','vat_deposit','deposit_amount','refund_date','refund_no','customer_accrual','pay_type','deposit_refund_status','remark')
    #  Set Columns , No display 
    tree.column('mobile_no', width=50, stretch=False, minwidth=50)
    tree.column('cust_group_acc', width=50, stretch=False, minwidth=50)  
    tree.column('name', width=50, stretch=False, minwidth=50) 
    tree.column('new_order_no', width=50, stretch=False, minwidth=50) 
    tree.column('vat_deposit', width=50, stretch=False, minwidth=50) 
    tree.column('deposit_amount', width=50, stretch=False, minwidth=50) 
    tree.column('refund_date', width=50, stretch=False, minwidth=50) 
    tree.column('refund_no', width=50, stretch=False, minwidth=50) 
    tree.column('customer_accrual', width=50, stretch=False, minwidth=50) 
    tree.column('pay_type', width=50, stretch=False, minwidth=50) 
    tree.column('deposit_refund_status', width=50, stretch=False, minwidth=50) 
    tree.column('remark', width=50, stretch=False, minwidth=50)  

    #  Indicator head 
    tree.heading('mobile_no', text=" mobile_no ")
    tree.heading('cust_group_acc', text=" cust_group_acc") 
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
    # Extract number of rows and columns
    n_rows = df.shape[0]
    n_cols = df.shape[1]
 
    for i in range(n_rows):
        for j in range(n_cols): 
            tree.insert("", i, text="", values=(df.loc[i][0], df.loc[i][1], df.loc[i][3], df.loc[i][8],df.loc[i][9],df.loc[i][11],df.loc[i][12],df.loc[i][18],df.loc[i][21],df.loc[i][24],df.loc[i][25],df.loc[i][34]))
    
    # ----vertical scrollbar------------
    vbar = ttk.Scrollbar(window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=vbar.set)
    #tree.grid(row=0, column=0, sticky=NSEW)
    vbar.grid(row=1, column=1, sticky=NS)

    # ----horizontal scrollbar----------
    hbar = ttk.Scrollbar(window, orient=HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=hbar.set)
    hbar.grid(row=3, column=0, sticky=EW)
       
def Event_Clear():
    v_mobile.set('')
    v_account.set('')
    v_name.set('')         
 #-------------------------------------------------------------------         
     
         
def Event_Export():
    print('do_something')
    mobile = v_mobile.get()
    account = v_account.get()
    name = v_name.get()
    print(mobile)
    print(account)
    print(name)
    # Load data from source
    df = Get_DF(mobile)
    df.to_excel("new_data.xlsx") 

v_mobile.set('พี.เอส.พี')
txt_mobile = Entry(window,textvariable=v_mobile)
txt_mobile.grid(row=1,column = 1)

search_button = Button(window, height = 2, width = 16,text ="Search",command = lambda:Event_Search())
search_button.grid(row=2,column = 0)

clear_button = Button(window, height = 2, width = 16,text ="Clear",command = lambda:Event_Clear())
clear_button.grid(row=2,column = 1)

save_button = Button(window, height = 2, width = 16,text ="Save",command = lambda:Event_Export())
save_button.grid(row=2,column = 2)
 


window.mainloop()