


import customtkinter as ctk
import tkinter as tk
import sqlite3


ctk.set_appearance_mode("system")  
ctk.set_appearance_mode("blue")
ctk.set_appearance_mode("dark")


appWidth, appHeight = 600, 600


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Student Profile")
        self.geometry(f"{appWidth}x{appHeight}")

    
        self.conn = sqlite3.connect('student_profile_data.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        
        self.firstNameLabel = ctk.CTkLabel(self, text="First Name")
        self.firstNameLabel.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.firstNameEntry = ctk.CTkEntry(self, placeholder_text="John")
        self.firstNameEntry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        
        self.middleNameLabel = ctk.CTkLabel(self, text="Middle Name")
        self.middleNameLabel.grid(row=0, column=2, padx=20, pady=10, sticky="w")
        self.middleNameEntry = ctk.CTkEntry(self, placeholder_text="Doe")
        self.middleNameEntry.grid(row=0, column=3, padx=20, pady=10, sticky="ew")

        self.lastNameLabel = ctk.CTkLabel(self, text="Last Name")
        self.lastNameLabel.grid(row=0, column=4, padx=20, pady=10, sticky="w")
        self.lastNameEntry = ctk.CTkEntry(self, placeholder_text="Smith")
        self.lastNameEntry.grid(row=0, column=5, padx=20, pady=10, sticky="ew")

    
        self.dobLabel = ctk.CTkLabel(self, text="Date of Birth (YYYY-MM-DD)")
        self.dobLabel.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.dobEntry = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.dobEntry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")


        self.addressLabel = ctk.CTkLabel(self, text="Address")
        self.addressLabel.grid(row=1, column=2, padx=20, pady=10, sticky="w")
        self.addressEntry = ctk.CTkEntry(self, placeholder_text="123 Main St")
        self.addressEntry.grid(row=1, column=3, padx=20, pady=10, sticky="ew")

    
        self.ageLabel = ctk.CTkLabel(self, text="Age")
        self.ageLabel.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.ageEntry = ctk.CTkEntry(self, placeholder_text="18")
        self.ageEntry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        self.genderLabel = ctk.CTkLabel(self, text="Gender")
        self.genderLabel.grid(row=2, column=2, padx=20, pady=10, sticky="w")

        
        self.genderVar = tk.StringVar(value="Prefer not to say")

        self.maleRadioButton = ctk.CTkRadioButton(self, text="Male", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=2, column=3, padx=20, pady=10, sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(self, text="Female", variable=self.genderVar, value="She is")
        self.femaleRadioButton.grid(row=2, column=4, padx=20, pady=10, sticky="ew")

        
        self.applicationTypeLabel = ctk.CTkLabel(self, text="Year")
        self.applicationTypeLabel.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    
        self.applicationTypeOptionMenu = ctk.CTkOptionMenu(self, values=["1st Year", "2nd Year", "3rd Year", "4th Year"])
        self.applicationTypeOptionMenu.grid(row=3, column=1, padx=20, pady=10, columnspan=2, sticky="ew")

        
        self.admissionSemesterLabel = ctk.CTkLabel(self, text="Admission Semester")
        self.admissionSemesterLabel.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        
        self.admissionSemesterOptionMenu = ctk.CTkOptionMenu(self, values=["1st Semester", "2nd Semester"])
        self.admissionSemesterOptionMenu.grid(row=4, column=1, padx=20, pady=10, columnspan=2, sticky="ew")

       
        self.emailLabel = ctk.CTkLabel(self, text="Student Email")
        self.emailLabel.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="example@example.com")
        self.emailEntry.grid(row=5, column=1, padx=20, pady=10, sticky="ew")

        
        self.studentNumberLabel = ctk.CTkLabel(self, text="Student Number")
        self.studentNumberLabel.grid(row=5, column=2, padx=20, pady=10, sticky="w")
        self.studentNumberEntry = ctk.CTkEntry(self, placeholder_text="1234567890")
        self.studentNumberEntry.grid(row=5, column=3, padx=20, pady=10, sticky="ew")

        
        self.contactNumberLabel = ctk.CTkLabel(self, text="Contact Number")
        self.contactNumberLabel.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        self.contactNumberEntry = ctk.CTkEntry(self, placeholder_text="+1234567890")
        self.contactNumberEntry.grid(row=6, column=1, padx=20, pady=10, sticky="ew")

       
        self.departmentLabel = ctk.CTkLabel(self, text="Department")
        self.departmentLabel.grid(row=7, column=0, padx=20, pady=10, sticky="w")

       
        self.departmentOptionMenu = ctk.CTkOptionMenu(self, values=["CEIT", "CTE", "COT", "CAS"],
                                                      command=self.showCourses)
        self.departmentOptionMenu.grid(row=7, column=1, padx=20, pady=10, columnspan=2, sticky="ew")

       
        self.courseLabel = ctk.CTkLabel(self, text="Course")
        self.courseLabel.grid(row=8, column=0, padx=20, pady=10, sticky="w")
        self.courseLabel.grid_remove()  # Initially hidden

       
        self.courseOptionMenu = ctk.CTkOptionMenu(self, values=[])
        self.courseOptionMenu.grid(row=8, column=1, padx=20, pady=10, columnspan=2, sticky="ew")
        self.courseOptionMenu.grid_remove()  # Initially hidden

        
        self.submitButton = ctk.CTkButton(self, text="Student Profile Submit", command=self.StudentProfileSubmit)
        self.submitButton.grid(row=9, column=1, columnspan=2, padx=20, pady=10, sticky="ew")

        
        self.displayBox = ctk.CTkTextbox(self, width=200, height=100)
        self.displayBox.grid(row=10, column=0, columnspan=6, padx=20, pady=10, sticky="nsew")


    def submitApplication(self):
       self.insert_data()
       self.clearFields()  
       self.showSuccessMessage()

    def clearFields(self):
      self.firstNameEntry.delete(0, tk.END)
      self.middleNameEntry.delete(0, tk.END)
      self.lastNameEntry.delete(0, tk.END)
      self.ageEntry.delete(0, tk.END)
      self.addressEntry.delete(0, tk.END)
      self.dobEntry.delete(0, tk.END) 
      self.contactNumberEntry.delete(0, tk.END)
      self.emailEntry.delete(0, tk.END)  
      self.studentNumberEntry.delete(0, tk.END)  
      self.genderVar.set("Prefer not to say")
      self.departmentOptionMenu.set("Select Department") 
      self.applicationTypeOptionMenu.set("Select Year")  
      self.admissionSemesterOptionMenu.set("Select Semester")  
      self.courseOptionMenu.set("Select Course")  

         
        
    def StudentProfileSubmit(self):
        self.insert_data()
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)
        self.clearFields()
        self.showSuccessMessage()

    def showSuccessMessage(self):
        
        success_window = tk.Toplevel(self)
        success_window.title("Student Profile Success")
        success_window.geometry("300x100")
        success_label = tk.Label(success_window, text="Student Profile Submitted Successfully!")
        success_label.pack()
        
        success_window.after(3000, success_window.destroy)

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT,
                            middle_name TEXT,
                            last_name TEXT,
                            date_of_birth TEXT,
                            age INTEGER,
                            gender TEXT,
                            application_type TEXT,
                            admission_semester TEXT,
                            email TEXT,
                            student_number TEXT,
                            contact_number TEXT,
                            address TEXT,
                            department TEXT,
                            course TEXT
                            )''')
        self.conn.commit()

    def insert_data(self):
        data = (self.firstNameEntry.get(), self.middleNameEntry.get(), self.lastNameEntry.get(),
                self.dobEntry.get(), self.ageEntry.get(), self.genderVar.get(), 
                self.applicationTypeOptionMenu.get(), self.admissionSemesterOptionMenu.get(),
                self.emailEntry.get(), self.studentNumberEntry.get(), 
                self.contactNumberEntry.get(), self.addressEntry.get(), 
                self.departmentOptionMenu.get(), self.courseOptionMenu.get())
        self.cursor.execute('''INSERT INTO students 
                            (first_name, middle_name, last_name, date_of_birth, age, gender, 
                            application_type, admission_semester, email, student_number, 
                            contact_number, address, department, course)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
        self.conn.commit()


    def generateResults(self):
        self.insert_data()
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)

    
    def createText(self):
        gender = self.genderVar.get()
        text = f"Name: {self.firstNameEntry.get()} {self.middleNameEntry.get()} {self.lastNameEntry.get()}\n"
        text += f"Date of Birth: {self.dobEntry.get()}\n"
        text += f"Age: {self.ageEntry.get()} years old\n"
        text += f"Gender: {gender}\n"
        text += f"Application Type: {self.applicationTypeOptionMenu.get()}\n"
        text += f"Admission Semester: {self.admissionSemesterOptionMenu.get()}\n"
        text += f"Student Email: {self.emailEntry.get()}\n"
        text += f"Student Number: {self.studentNumberEntry.get()}\n"
        text += f"Contact Number: {self.contactNumberEntry.get()}\n"
        text += f"Address: {self.addressEntry.get()}\n"
        text += f"Department: {self.departmentOptionMenu.get()}\n"
        if self.departmentOptionMenu.get() == "CEIT":
            text += f"Course: {self.courseOptionMenu.get()}"
        return text

    
    def showCourses(self, event):
        department = self.departmentOptionMenu.get()  
        if department == "CEIT":
            self.courseLabel.grid()
            self.courseOptionMenu.grid()
            degree_programs = ["BSCE", "BSECE", "BSEE", "BSCoE", "BSIS", "BSinfoTech", "BSCS"]
            self.courseOptionMenu.configure(values=degree_programs)
        elif department == "CTE":
            self.courseLabel.grid()
            self.courseOptionMenu.grid()
            courses = ["BTVTED major in Food Services and Management",
                       "BSED major in English",
                       "BSED major in Filipino",
                       "BSED major in Mathematics",
                       "BSED major in Science",
                       "BEED",
                       "BPED"]
            self.courseOptionMenu.configure(values=courses)
        elif department == "CAS":
            self.courseLabel.grid()
            self.courseOptionMenu.grid()
            courses = ["BSES", "BS MATH", "AB-EL"]
            self.courseOptionMenu.configure(values=courses)
        elif department == "COT":
            self.courseLabel.grid()
            self.courseOptionMenu.grid()
            courses = ["BAET", "BEET", "BEXET", "BMET", "BMET-Mechanical Technology",
                       "BMET-Refrigerator and Air-Conditioning",
                       "BSIT", "BSIT major in Architectural Drafting Technology",
                       "BSIT major in Automotive Technology", "BSIT major in Electrical Technology",
                       "BSIT major in Electronics Technology", "BSIT major in Mechanical Technology",
                       "BSIT major in Welding and Fabrication Technology",
                       "BSIT major in Heating, Ventilation, Air-Conditioning and Refrigeration",
                       "BSHM", "BSTM"]
            self.courseOptionMenu.configure(values=courses)
        else:
            self.courseLabel.grid_remove()
            self.courseOptionMenu.grid_remove()   

if __name__ == "__main__": 
    app = App()
    app.mainloop()
