import tkinter as tk
from tkinter import ttk

class MainPage:
    def __init__(self, master):
        self.master = master
        self.master.title("TkVue Test")
        self.master.geometry("900x300")

        self.label = tk.Label(master, text="Hello World!", font=("Arial", 24))
        self.label.pack(pady=50)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", font=("Arial", 14), 
                                       command=self.master.quit)
        self.cancel_button.grid(row=0, column=0, padx=10)

        self.continue_button = tk.Button(self.button_frame, text="Continue", font=("Arial", 14),
                                         command=self.open_student_info)
        self.continue_button.grid(row=0, column=1, padx=10)

    def open_student_info(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        StudentInfoGUI(self.master)

class StudentInfoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Information")
        self.master.geometry("900x400")

        # Frame for input
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(padx=10, pady=10)

        # Create entry boxes and labels in input frame
        self.name_label = tk.Label(self.input_frame, text="Name")
        self.name_label.grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, pady=2)

        self.program_label = tk.Label(self.input_frame, text="Program")
        self.program_label.grid(row=1, column=0, sticky=tk.W, pady=2)
        self.program_var = tk.StringVar(value="Computer Engineering")
        self.program_dropdown = ttk.Combobox(self.input_frame, textvariable=self.program_var, state="readonly")
        self.program_dropdown['values'] = ["Computer Engineering", "Visual Basic Programming", "Python Programming"]
        self.program_dropdown.grid(row=1, column=1, pady=2)

        self.gender_label = tk.Label(self.input_frame, text="Gender")
        self.gender_label.grid(row=2, column=0, sticky=tk.W, pady=2)
        self.gender_var = tk.StringVar(value="Male")
        self.gender_male = tk.Radiobutton(self.input_frame, text="Male", variable=self.gender_var, value="Male")
        self.gender_male.grid(row=2, column=1, sticky=tk.W, pady=2)
        self.gender_female = tk.Radiobutton(self.input_frame, text="Female", variable=self.gender_var, value="Female")
        self.gender_female.grid(row=2, column=2, sticky=tk.W, pady=2)

        self.birth_date_label = tk.Label(self.input_frame, text="Birth Date")
        self.birth_date_label.grid(row=3, column=0, sticky=tk.W, pady=2)
        self.month_var = tk.StringVar(value="Month")
        self.month_dropdown = ttk.Combobox(self.input_frame, textvariable=self.month_var, state="readonly")
        self.month_dropdown['values'] = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                                         "October", "November", "December"]
        self.month_dropdown.grid(row=3, column=1, pady=2)
        self.day_var = tk.StringVar(value="Day")
        self.day_dropdown = ttk.Combobox(self.input_frame, textvariable=self.day_var, state="readonly")
        self.day_dropdown['values'] = [str(i) for i in range(1, 32)]
        self.day_dropdown.grid(row=3, column=2, pady=2)
        self.year_var = tk.StringVar(value="Year")
        self.year_dropdown = ttk.Combobox(self.input_frame, textvariable=self.year_var, state="readonly")
        self.year_dropdown['values'] = [str(i) for i in range(1900, 2025)]
        self.year_dropdown.grid(row=3, column=3, pady=2)

        # Create submit and clear buttons in input frame
        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.submit_info)
        self.submit_button.grid(row=4, column=0, pady=10)
        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_info)
        self.clear_button.grid(row=4, column=1, pady=10)

        # Create display area
        self.display_area = tk.Text(master, width=50, height=10)
        self.display_area.pack(padx=10, pady=10)

    def submit_info(self):
        name = self.name_entry.get()
        program = self.program_var.get()
        gender = self.gender_var.get()
        month = self.month_var.get()
        day = self.day_var.get()
        year = self.year_var.get()

        info = f"Name: {name}\nProgram: {program}\nGender: {gender}\nBirth Date: {month} {day}, {year}\n\n"
        self.display_area.insert(tk.END, info)

    def clear_info(self):
        self.name_entry.delete(0, tk.END)
        self.program_var.set("Computer Engineering")
        self.gender_var.set("Male")
        self.month_var.set("Month")
        self.day_var.set("Day")
        self.year_var.set("Year")
        self.display_area.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(root)
    root.mainloop()


