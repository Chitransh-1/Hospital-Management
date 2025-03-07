from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import SqlQueries as sqll

class Hospital:
    def show_data(self):
        rows = sqll.Fetch_Data()
        for row in rows:
            self.hospital_table.insert("", END, values=row)
    def Iprescription(self):
        if self.NameOfTablets.get() == "" or self.textReferrence.get() =="":
            messagebox.showerror("Error", "All Fields are required")
        else:
            sqll.insert_Data(
                self.NameOfTablets.get(),
                self.textReferrence.get(),
                self.Dose.get(),
                self.NumberOfTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.Storage.get(),
                self.NHSNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            )
            self.show_data()

    def Iupdate(self):
        sqll.Update_Data(
            self.NameOfTablets.get(),
            self.textReferrence.get(),
            self.Dose.get(),
            self.NumberOfTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.Storage.get(),
            self.NHSNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get()
        )
        self.show_data()

    def Idelete(self):
        sqll.Delete_Data(self.textReferrence.get())
        

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets = StringVar()
        self.textReferrence = StringVar()
        self.Dose = StringVar()
        self.NumberOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffects = StringVar()
        self.FurtherInfomation = StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientID = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        label_title = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        label_title.pack(side=TOP, fill=X)

        #===================================================================================================---FRAMES---===============================================================================================================

        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame,bd=10, relief=RIDGE,padx=10,font = ("arial", 12, "bold"), text = "Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame,bd=10, relief=RIDGE,padx=10,font = ("arial", 12, "bold"), text = "Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        #==================================================================================================---BUTTONSFRAMES---===============================================================================================================

        ButtonFrames = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrames.place(x=0, y=530, width=1530, height=70)

        #===================================================================================================---DETAILSFRAMES---===============================================================================================================

        DetailFrames = Frame(self.root, bd=20, relief=RIDGE)
        DetailFrames.place(x=0, y=600, width=1530, height=190)

        #===================================================================================================---DATAFRAMES__LABELS__LEFT---===============================================================================================================
        
        LabelNameTablet = Label(DataFrameLeft, text="Names Of Tablet :", font=("times of roman", 12, "bold"), padx=2, pady=6)
        LabelNameTablet.grid(row=0, column=0)

        ComboNameTablet = ttk.Combobox(DataFrameLeft, textvariable=self.NameOfTablets , state="readonly", font=("times of roman", 12, "bold"), width=33)
        ComboNameTablet["values"]= ("Nice", "Corona Vaccine", "Acetaminophen", "Amlodipine", "Ativan")
        ComboNameTablet.grid(row=0, column=1)

        LabelRef = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No. :", padx=2)
        LabelRef.grid(row=1, column=0, sticky=W)
        TextRef = Entry(DataFrameLeft, textvariable=self.textReferrence, font=("arial", 12, "bold"), width=35)
        TextRef.grid(row=1, column=1)

        LabelDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose :", padx=2, pady=4)
        LabelDose.grid(row=2, column=0, sticky=W)
        TextDose = Entry(DataFrameLeft, textvariable=self.Dose, font=("arial", 12, "bold"), width=35)
        TextDose.grid(row=2, column=1)

        LabelNoTablet = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No. Of Tablets :", padx=2, pady=5)
        LabelNoTablet.grid(row=3, column=0, sticky=W)
        TextNoTablet = Entry(DataFrameLeft, textvariable=self.NumberOfTablets, font=("arial", 12, "bold"), width=35)
        TextNoTablet.grid(row=3, column=1)

        labelLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot :", padx=2, pady=6)
        labelLot.grid(row=4, column=0, sticky=W)
        TextLot = Entry(DataFrameLeft, textvariable=self.Lot ,font=("arial", 12, "bold"), width=35)
        TextLot.grid(row=4, column=1)

        LabelIssueData = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Data. :", padx=2, pady=6)
        LabelIssueData.grid(row=5, column=0, sticky=W)
        TextIssueData = Entry(DataFrameLeft, textvariable=self.IssueDate, font=("arial", 12, "bold"), width=35)
        TextIssueData.grid(row=5, column=1)

        LabelExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date. :", padx=2, pady=6)
        LabelExpDate.grid(row=6, column=0, sticky=W)
        TextExpDate = Entry(DataFrameLeft, textvariable=self.ExpDate, font=("arial", 12, "bold"), width=35)
        TextExpDate.grid(row=6, column=1)

        LabelDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose :", padx=2, pady=4)
        LabelDailyDose.grid(row=7, column=0, sticky=W)
        TextDailyDose = Entry(DataFrameLeft, textvariable=self.DailyDose, font=("arial", 12, "bold"), width=35)
        TextDailyDose.grid(row=7, column=1)

        LabelSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effects :", padx=2, pady=6)
        LabelSideEffect.grid(row=8, column=0, sticky=W)
        TextSideEffect = Entry(DataFrameLeft, textvariable=self.SideEffects, font=("arial", 12, "bold"), width=35)
        TextSideEffect.grid(row=8, column=1)

        LabelFurtherInfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information :", padx=2)
        LabelFurtherInfo.grid(row=0, column=2, sticky=W)
        TextFurtherInfo = Entry(DataFrameLeft, textvariable=self.FurtherInfomation, font=("arial", 12, "bold"), width=35)
        TextFurtherInfo.grid(row=0, column=3)

        LabelBloodPressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure :", padx=2, pady=6)
        LabelBloodPressure.grid(row=1, column=2, sticky=W)
        TextBloodPressure = Entry(DataFrameLeft, textvariable=self.BloodPressure, font=("arial", 12, "bold"), width=35)
        TextBloodPressure.grid(row=1, column=3)

        LabelStorageAdvice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice :", padx=2, pady=6)
        LabelStorageAdvice.grid(row=2, column=2, sticky=W)
        TextStorageAdvice = Entry(DataFrameLeft, textvariable=self.Storage, font=("arial", 12, "bold"), width=35)
        TextStorageAdvice.grid(row=2, column=3)

        LabelMedication = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication :", padx=2, pady=6)
        LabelMedication.grid(row=3, column=2, sticky=W)
        TextMedication = Entry(DataFrameLeft, textvariable=self.HowToUseMedication, font=("arial", 12, "bold"), width=35)
        TextMedication.grid(row=3, column=3)

        LabelPatientID= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient ID :", padx=2, pady=6)
        LabelPatientID.grid(row=4, column=2, sticky=W)
        TextPatientID= Entry(DataFrameLeft, textvariable=self.PatientID, font=("arial", 12, "bold"), width=35)
        TextPatientID.grid(row=4, column=3)

        LabelNHSNumber= Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number :", padx=2, pady=6)
        LabelNHSNumber.grid(row=5, column=2, sticky=W)
        TextNHSNumber= Entry(DataFrameLeft, textvariable=self.NHSNumber, font=("arial", 12, "bold"), width=35)
        TextNHSNumber.grid(row=5, column=3)

        LabelPatientName= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name :", padx=2, pady=6)
        LabelPatientName.grid(row=6, column=2, sticky=W)
        TextPatientName= Entry(DataFrameLeft, textvariable=self.PatientName, font=("arial", 12, "bold"), width=35)
        TextPatientName.grid(row=6, column=3)

        LabelDateOfBirth= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth :", padx=2, pady=6)
        LabelDateOfBirth.grid(row=7, column=2, sticky=W)
        TextDateOfBirth= Entry(DataFrameLeft, textvariable=self.DateOfBirth, font=("arial", 12, "bold"), width=35)
        TextDateOfBirth.grid(row=7, column=3)

        LabelPatientAddress= Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address :", padx=2, pady=6)
        LabelPatientAddress.grid(row=8, column=2, sticky=W)
        TextPatientAddress= Entry(DataFrameLeft, textvariable=self.PatientAddress, font=("arial", 12, "bold"), width=35)
        TextPatientAddress.grid(row=8, column=3)

        #===================================================================================================---DATAFRAMES__LABELS__RIGHT---===============================================================================================================

        self.textPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=47, height=16, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0)

        #===================================================================================================---BUTTONS---===============================================================================================================

        prescriptionButton = Button(ButtonFrames, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.Iprescription)
        prescriptionButton.grid(row=0, column=0)

        PrescriptionDataButton = Button(ButtonFrames, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.Iprectioption)
        PrescriptionDataButton.grid(row=0, column=1)
        
        UpdateButton = Button(ButtonFrames, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.Iupdate)
        UpdateButton.grid(row=0, column=2)

        DeleteButton = Button(ButtonFrames, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.Idelete)
        DeleteButton.grid(row=0, column=3)

        ClearButton = Button(ButtonFrames, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.clear)
        ClearButton.grid(row=0, column=4)

        ExitButton = Button(ButtonFrames, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, command=self.exist)
        ExitButton.grid(row=0, column=5)

        #===================================================================================================---SCROLL BAR---===============================================================================================================
        
        ScrollbarX_axis = ttk.Scrollbar(DetailFrames, orient=HORIZONTAL)
        ScrollbarY_axis = ttk.Scrollbar(DetailFrames, orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailFrames, column=("NameOfTable", "Ref", "Dose", "nooftable", "lot", "issuedata",
                                                           "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=ScrollbarX_axis.set, yscrollcommand=ScrollbarY_axis.set)

        ScrollbarX_axis.pack(side=BOTTOM, fill=X)
        ScrollbarY_axis.pack(side=RIGHT, fill=Y)
        ScrollbarX_axis = ttk.Scrollbar(command=self.hospital_table.xview)
        ScrollbarY_axis = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("NameOfTable", text="Name of Table")
        self.hospital_table.heading("Ref", text="Reference No.")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("nooftable", text="No. of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedata", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("NameOfTable", width=100, anchor=CENTER)
        self.hospital_table.column("Ref", width=100, anchor=CENTER)
        self.hospital_table.column("Dose", width=100, anchor=CENTER)
        self.hospital_table.column("nooftable", width=100, anchor=CENTER)
        self.hospital_table.column("lot", width=100, anchor=CENTER)
        self.hospital_table.column("issuedata", width=100, anchor=CENTER)
        self.hospital_table.column("expdate", width=100, anchor=CENTER)
        self.hospital_table.column("dailydose", width=100, anchor=CENTER)
        self.hospital_table.column("storage", width=100, anchor=CENTER)
        self.hospital_table.column("nhsnumber", width=100, anchor=CENTER)
        self.hospital_table.column("pname", width=100, anchor=CENTER)
        self.hospital_table.column("dob", width=100, anchor=CENTER)
        self.hospital_table.column("address", width=100, anchor=CENTER)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.show_data()
        self.hospital_table.bind("<ButtonRelease-1>" ,self.get_cursor)
    
        
    def get_cursor(self, event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        print(row)
        self.NameOfTablets.set(row[0])
        self.textReferrence.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Storage.set(row[8])
        self.NHSNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def Iprectioption(self):
        self.textPrescription.insert(END, "Name of tablets\t\t\t" + self.NameOfTablets.get() + "\n")
        self.textPrescription.insert(END, "Referrence No.\t\t\t" + self.textReferrence.get() + "\n")
        self.textPrescription.insert(END, "Dose\t\t\t" + self.Dose.get() + "\n")
        self.textPrescription.insert(END, "Number of Tablets\t\t\t" + self.NumberOfTablets.get() + "\n")
        self.textPrescription.insert(END, "Lot\t\t\t" + self.Lot.get() + "\n")
        self.textPrescription.insert(END, "Issue Date\t\t\t" + self.IssueDate.get() + "\n")
        self.textPrescription.insert(END, "Exp Date\t\t\t" + self.ExpDate.get() + "\n")
        self.textPrescription.insert(END, "Daily Dose\t\t\t" + self.DailyDose.get() + "\n")
        self.textPrescription.insert(END, "Side Effect\t\t\t" + self.SideEffects.get() + "\n")
        self.textPrescription.insert(END, "Further Information\t\t\t" + self.FurtherInfomation.get() + "\n")
        self.textPrescription.insert(END, "DrivingUsingMAchine\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.textPrescription.insert(END, "PatientNAme\t\t\t" + self.PatientID.get() + "\n")
        self.textPrescription.insert(END, "DateOfBirth\t\t\t" + self.DateOfBirth.get() + "\n")
        self.textPrescription.insert(END, "PatientAddress\t\t\t" + self.PatientAddress.get() + "\n")

    def clear(self):
        self.NameOfTablets.set("")
        self.textReferrence.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffects.set("")
        self.FurtherInfomation.set("")
        self.Storage.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientID.set("")
        self.NHSNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.textPrescription.delete("1.0",END)

    def exist(self):
        iExist = messagebox.askyesno("Hospital Management System", "Confirm you wnat to Exit")
        if iExist>0:
            root.destroy()
            return

root = Tk()
app = Hospital(root)
root.mainloop()