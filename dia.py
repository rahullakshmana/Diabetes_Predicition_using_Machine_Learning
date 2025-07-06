from tkinter import*
import pickle
import sklearn

dia_pred=pickle.load(open("dia.pkl","rb"))

dia=Tk()
dia.title("Diabetes Prediction")
dia.geometry("750x900")
dia.configure(background="#d446cd")
gl_input=DoubleVar()
bp_input=DoubleVar()
sk_input=DoubleVar()
ins_input=DoubleVar()
bmi_input=DoubleVar()
dpf_input=DoubleVar()
age_input=DoubleVar()


def prediction():
    gl=gl_input.get()
    bp=bp_input.get()
    sk=sk_input.get()
    ins=ins_input.get()
    bmi=bmi_input.get()
    dpf=dpf_input.get()
    age=age_input.get()
    if ((70<=gl<=350) and (80<=bp<=150) and (2<=sk<=29) and (10<=ins<=300) and (12<=bmi<=45) and (0<=dpf<=2.5) and (0<=age<=150)):
        result=dia_pred.predict([[gl,bp,sk,ins,bmi,dpf,age]])
        result_perc=dia_pred.predict_proba([[gl,bp,sk,ins,bmi,dpf,age]])
        if(result==1):
            ans=str(round(max(result_perc[0])*100))+"% You are having Diabetics"
        else:
            ans=str(round(max(result_perc[0])*100))+"% You are not having Diabetics"    
    else:    
        ans="Invalid Details"
    lb8.configure(text="Prediction: ")
    lb81.configure(text=ans)

lb1=Label(dia,text="Enter the Glucose level\t\t: ",font=('algerian',15),fg="black",bg="#d446cd")
lb1.grid(row=0,column=0,padx=(0,10),pady=10)
ent1=Entry(dia,textvariable=gl_input,font=('copperblack',15),fg="black",bg="white")
ent1.grid(row=0,column=1)

lb2=Label(dia,text="Enter the Blood pressure\t\t: ",font=('algerian',15),fg="black",bg="#d446cd")
lb2.grid(row=1,column=0,padx=(0,10),pady=10)
ent2=Entry(dia,textvariable=bp_input,font=('copperblack',15),fg="black",bg="white")
ent2.grid(row=1,column=1)

lb3=Label(dia,text="Enter the Skin thickness\t\t: ",font=('algerian',15),fg="black",bg="#d446cd")
lb3.grid(row=2,column=0,padx=(0,10),pady=10)
ent3=Entry(dia,textvariable=sk_input,font=('copperblack',15),fg="black",bg="white")
ent3.grid(row=2,column=1)

lb4=Label(dia,text="Enter the Insulin\t\t\t : ",font=('algerian',15),fg="black",bg="#d446cd")
lb4.grid(row=3,column=0,padx=(30,25),pady=10)
ent4=Entry(dia,textvariable=ins_input,font=('copperblack',15),fg="black",bg="white")
ent4.grid(row=3,column=1)

lb5=Label(dia,text="Enter the BMI value \t\t: ",font=('algerian',15),fg="black",bg="#d446cd")
lb5.grid(row=4,column=0,padx=(0,10),pady=10)
ent5=Entry(dia,textvariable=bmi_input,font=('copperblack',15),fg="black",bg="white")
ent5.grid(row=4,column=1)

lb6=Label(dia,text="Enter the Diabetes pedigree function : ",font=('algerian',15),fg="black",bg="#d446cd")
lb6.grid(row=5,column=0,padx=(20,10),pady=10)
ent6=Entry(dia,textvariable=dpf_input,font=('copperblack',15),fg="black",bg="white")
ent6.grid(row=5,column=1)

lb7=Label(dia,text="Enter the Age\t\t \t: ",font=('algerian',15),fg="black",bg="#d446cd")
lb7.grid(row=6,column=0,padx=(0,10),pady=10)
ent7=Entry(dia,textvariable=age_input,font=('copperblack',15),fg="black",bg="white")
ent7.grid(row=6,column=1)

btn=Button(dia,comman=prediction,text="PERDICT",font=('aerial',12),fg="black",bg="silver",activebackground="black",activeforeground="silver")
btn.grid(row=7,column=1,pady=(10,10))

lb8=Label(dia,font=('algerian',15),fg="black",bg="#d446cd")
lb8.grid(row=8,column=0,padx=(50,10),pady=10)
lb81=Label(dia,font=('algerian',15),fg="black",bg="#d446cd")
lb81.grid(row=8,column=1,padx=(50,10),pady=10)

dia.mainloop()
