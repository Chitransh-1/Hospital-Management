import mysql.connector
from tkinter import messagebox

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Hospital_Management_System"
)
mycursor = conn.cursor()

def delete():
    myquery = "DROP TABLE IF EXISTS Hospital_Data"
    mycursor.execute(myquery)

def creat_table():
    myquery = """
    CREATE TABLE IF NOT EXISTS Hospital_Data (
        Name_Of_Tablets VARCHAR(45) NOT NULL,
        Referrence_No VARCHAR(45) NOT NULL,
        Dose VARCHAR(45) NULL,
        NumberOfTablets VARCHAR(45) NULL,
        Lot VARCHAR(45) NULL,
        IssueDate VARCHAR(45) NULL,
        ExpDate VARCHAR(45) NULL,
        DailyDose VARCHAR(45) NULL,
        Storage VARCHAR(45) NULL,
        NHS_Number VARCHAR(45) NULL,
        PatientName VARCHAR(45) NULL,
        DOB VARCHAR(45) NULL,
        PatientAddress VARCHAR(45) NULL,
        UNIQUE(Referrence_No)
    );
    """
    mycursor.execute(myquery)

# Create table if it does not exist
creat_table()

def insert_Data(nameoftablet, textReference, Dose, NumberOfTablets, Lot, IssueDate, ExpDate, DailyDose, Storage, NHSNumber, PatientName, DateOfBirth, PatientAddress):
    myquery = """
    INSERT INTO Hospital_Data (Name_Of_Tablets, Referrence_No, Dose, NumberOfTablets, Lot, IssueDate, ExpDate, DailyDose, Storage, NHS_Number, PatientName, DOB, PatientAddress) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    mycursor.execute(
        myquery, (
            nameoftablet,
            textReference,
            Dose,
            NumberOfTablets,
            Lot,
            IssueDate,
            ExpDate,
            DailyDose,
            Storage,
            NHSNumber,
            PatientName,
            DateOfBirth,
            PatientAddress
        )
    )
    conn.commit()
    messagebox.showinfo("Success", "Your Record has been Inserted")

def Fetch_Data():
    myquery = "SELECT * FROM Hospital_Data"
    mycursor.execute(myquery)
    datta = mycursor.fetchall()
    return datta

def Update_Data(nameoftablet, textReference, Dose, NumberOfTablets, Lot, IssueDate, ExpDate, DailyDose, Storage, NHSNumber, PatientName, DateOfBirth, PatientAddress):
    myquery = """
    UPDATE Hospital_Data SET
        Name_Of_Tablets = %s,
        Dose = %s,
        NumberOfTablets = %s,
        Lot = %s,
        IssueDate = %s,
        ExpDate = %s,
        DailyDose = %s,
        Storage = %s,
        NHS_Number = %s,
        PatientName = %s,
        DOB = %s,
        PatientAddress = %s
    WHERE Referrence_No = %s
    """
    mycursor.execute(
        myquery, (
            nameoftablet,
            Dose,
            NumberOfTablets,
            Lot,
            IssueDate,
            ExpDate,
            DailyDose,
            Storage,
            NHSNumber,
            PatientName,
            DateOfBirth,
            PatientAddress,
            textReference
        )
    )
    conn.commit()
    messagebox.showinfo("Changed", "Your Record has been Changed")

def Delete_Data(textReference):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Hospital_Management_System"
    )
    mycursorr = conn.cursor()
    myqurry = "DELETE FROM hospital_data WHERE Referrence_No = %s"
    value = (textReference,)
    mycursorr.execute(myqurry, value)

    conn.commit()
    Fetch_Data()
    messagebox.showinfo("Deleted", "Your Record has been Deleted")
    conn.close()

def close_connection():
    mycursor.close()
    conn.close()