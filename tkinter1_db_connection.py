from tkinter import *

t=Tk()
t.geometry('800x800')
Label(text='Name',bg='black',fg='white').place(x=10,y=10)
x=Entry()
x.place(x=55,y=12)

Label(text='Age',bg='black',fg='white').place(x=10,y=35)
ag=Entry()
ag.place(x=55,y=37)

def abcd():
    import pymysql
    y=pymysql.connect(host='localhost',user='root',password='1234',db='avodha')
    cr=y.cursor()
    n=x.get()
    a=ag.get()
    print(n)
    print(a)
    cr.execute('insert into sample values(%s,%s)',(n,a))
    y.commit()
    

    
Button(text='Submit',command=abcd).place(x=53,y=65)


Label(text='UPDATE',bg='black',fg='red',font=('arial black',20,'bold')).place(x=10,y=130)
Label(text='Enter Name to Update',bg='black',fg='white').place(x=10,y=190)
nn=Entry()
nn.place(x=155,y=190)

Label(text='Enter New Age',bg='black',fg='white').place(x=10,y=220)
nag=Entry()
nag.place(x=155,y=220)


def upd():
    import pymysql
    y=pymysql.connect(host='localhost',user='root',password='1234',db='avodha')
    cr=y.cursor()
    f=nn.get()
    g=nag.get()
    cr.execute('update sample set age=%s where name=%s',(g,f))
    y.commit()
    
Button(text='Apply',command=upd).place(x=155,y=250)

def delete():
     import pymysql
     y=pymysql.connect(host='localhost',user='root',password='1234',db='avodha')
     cr=y.cursor()
     dele=nx.get()
     cr.execute('delete from sample where name=%s',dele)
     y.commit()
    

Label(text='DELETE',bg='black',fg='red',font=('arial black',20,'bold')).place(x=10,y=330)
Label(text='Enter Name to Delete',bg='black',fg='white').place(x=10,y=380)
nx=Entry()
nx.place(x=155,y=380)

Button(text='Delete',command=delete).place(x=153,y=430)

sc=Scrollbar()
sc.pack(side=RIGHT,fill=Y)
tx=Text(height=10,width=30,yscrollcommand=sc.set)
sc.config(command=tx.yview)
tx.place(x=500,y=75)
tx.insert(INSERT,('CLICK ON VIEW DATA'))

          

def view():
    import pymysql
    y=pymysql.connect(host='localhost',user='root',password='1234',db='avodha')
    cr=y.cursor()
    cr.execute('select * from sample')
    v=cr.fetchall()
    vn=[','.join(map(str,xd))for xd in v]
    tx.delete('1.0',END)
    tx.insert(INSERT,('DATA SETS ARE :\n\n'))
    for i in vn:
            tx.insert(INSERT,('%s\n\n'%i))

Button(text='View data',bg='indigo',fg='white',command=view).place(x=500,y=250)
t.mainloop()
