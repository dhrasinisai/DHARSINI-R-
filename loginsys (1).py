from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

background = "white"
framebg = "#EDEDED"
framefg = "#141414"
button_c = '#FFFF00'


def register():
    try:
        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dhars@3010",
            database="dharsini"
        )
        mycursor = mydb.cursor()

        # Retrieve user input
        accountno = e1.get()  # Corrected line to retrieve value from the Entry widget
        username = e2.get()
        password = e3.get()
        name = e4.get()
        dob = e5.get()
        branch = e6.get()
        ifsc = e7.get()

        # Insert data into the database
        sql = "INSERT INTO user (accountno, username, password, name, dob, branch, ifsc) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (accountno, username, password, name, dob, branch, ifsc)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Registration Successful", "You have successfully registered!")
        open_login_window()  # Open login window after successful registration

    except Exception as e:
        messagebox.showerror("Error", str(e))


def login():
    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhars@3010",
        database="dharsini"
    )
    mycursor = mydb.cursor()

    # Retrieve user input
    username = e1.get()
    password = e2.get()

    # Query the database to check if the user exists
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()

    if result:
        messagebox.showinfo("Login Successful", "Welcome back, " + username + "!")
        open_user_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

def Debit():
    profile_window = Tk()
    profile_window.title('Debit Amount')

    frame = Frame(profile_window, bg='#98F5FF')
    frame.pack(fill=BOTH, expand=True)

    amount_label = Label(frame, text="Enter the amount to debit:", font=("Helvetica", 16), bg=background, fg=framefg)
    amount_label.pack(padx=20, pady=20)

    amount_entry = Entry(frame, font=("Helvetica", 16), width=30)
    amount_entry.pack(padx=20, pady=10)

    confirm_btn = Button(frame, text="Confirm", command=lambda: debit_amount(profile_window, amount_entry.get()), bg=button_c, fg=framefg, font=("Helvetica", 12),
                         width=15, height=2)
    confirm_btn.pack(padx=20, pady=10)

    profile_window.mainloop()

def debit_amount(profile_window, amount):
    # Here you can write the code to handle debit functionality
    messagebox.showinfo("Debit Successful", f"Successfully debited {amount}!")
    profile_window.destroy()


def Credits():
    credit_window = Tk()
    credit_window.title('Credit Information')

    frame = Frame(credit_window, bg='#98F5FF')
    frame.pack(fill=BOTH, expand=True)

    credit_label = Label(frame, text="Credit Information", font=("Helvetica", 16,'bold'), bg=background, fg=framefg)
    credit_label.pack(padx=20, pady=20)

    # Dummy credit information including date and creditor name
    credit_info = "Credit 1:\nDate: 2024-05-01\nCredited by: John\nAmount: ₹10000\n\n" \
                  "Credit 2:\nDate: 2024-04-30\nCredited by: Jane\nAmount: ₹25000\n\n" \
                  "Credit 3:\nDate: 2024-04-29\nCredited by: Alice\nAmount:₹5000"

    credit_info_label = Label(frame, text=credit_info, font=("Helvetica", 14), bg=background, fg=framefg, justify=LEFT)
    credit_info_label.pack(padx=20, pady=10)

    credit_window.mainloop()

def TransactionDetails():
    transaction_window = Tk()
    transaction_window.title('Transaction Details')

    frame = Frame(transaction_window, bg=background)
    frame.pack(fill=BOTH, expand=True)

    transaction_label = Label(frame, text="Transaction Details", font=("Helvetica", 16,'bold'), bg=background, fg=framefg)
    transaction_label.pack(padx=20, pady=20)

    # Dummy transaction details including date and recipient name
    transaction_info = "Transaction 1:\nDate: 2024-05-01\nRecipient: John\nAmount: ₹5000\n\n" \
                       "Transaction 2:\nDate: 2024-04-30\nRecipient: Jane\nAmount: ₹1000\n\n" \
                       "Transaction 3:\nDate: 2024-04-29\nRecipient: Alice\nAmount: ₹2000"

    transaction_info_label = Label(frame, text=transaction_info, font=("Helvetica", 14), bg=background, fg=framefg, justify=LEFT)
    transaction_info_label.pack(padx=20, pady=10)

    transaction_window.mainloop()

    
def open_user_dashboard():
    user_window=Tk()
    user_window.title('User DashBoard')

    frame=Frame(user_window, bg='#98F5FF')
    frame.pack(fill=BOTH, expand=True)


    login_prompt = Label(frame, text="User DashBoard", font=("Imprint MT Shadow", 26, "bold"), bg=background,
                         fg=framefg)
    login_prompt.pack(padx=10, pady=10, anchor=NW)

    debit_btn = Button(frame, text="Debit👆🏻", command=Debit, bg=button_c, fg=framefg, font=("Helvetica", 20,'bold'),
                       width=25, height=4)
    debit_btn.place(x=100, y=150)  # Adjust the position as needed

    credits_btn = Button(frame, text="Credits👆🏻", command=Credits, bg=button_c, fg=framefg, font=("Helvetica", 20,'bold'),
                         width=25, height=4)
    credits_btn.place(x=600, y=150)  # Adjust the position as needed

    transaction_details_btn = Button(frame, text="Transaction Details👆🏻", command=TransactionDetails, bg=button_c, fg=framefg, font=("Helvetica", 20,'bold'),
                                     width=25, height=4)
    transaction_details_btn.place(x=1100, y=150)  # Adjusting padx and pady values

    fasttag_btn = Button(frame, text="Fasttag Transaction👆🏻", command=FasttagTransactions, bg=button_c, fg=framefg, font=("Helvetica", 20,'bold'), width=25, height=4)
    fasttag_btn.place(x=350, y=350)

    feedback_btn = Button(frame, text="Feedback or Ratings👆🏻", command=open_feedback_window, bg=button_c, fg=framefg, font=("Helvetica", 20,'bold'), width=25, height=4)
    feedback_btn.place(x=850, y=350)


    user_window.mainloop()

def FasttagTransactions():
    fasttag_window = Tk()
    fasttag_window.title('Fasttag Transactions')

    frame = Frame(fasttag_window, bg='#98F5FF')
    frame.pack(fill=BOTH, expand=True)

    transaction_label = Label(frame, text="Fasttag Transactions", font=("Helvetica", 16,'bold'), bg=background, fg=framefg)
    transaction_label.pack(padx=20, pady=20)

    # Dummy Fasttag transaction details
    fasttag_info = "Stage 1: Salem to Dharmapuri\nDate: 2024-05-01\nAmount Withdrawn: ₹50\n\n" \
                   "Stage 2: Dharmapuri to Krishnagiri\nDate: 2024-05-02\nAmount Withdrawn: ₹75\n\n" \
                   "Stage 3: Krishnagiri to Vellore\nDate: 2024-05-03\nAmount Withdrawn: ₹100\n\n" \
                   "Stage 4: Vellore to Chennai\nDate: 2024-05-04\nAmount Withdrawn: ₹120"

    fasttag_info_label = Label(frame, text=fasttag_info, font=("Helvetica", 14), bg=background, fg=framefg, justify=LEFT)
    fasttag_info_label.pack(padx=20, pady=10)

    fasttag_window.mainloop()

def open_feedback_window():
    feedback_window = Tk()
    feedback_window.title('Application Feedback')

    frame = Frame(feedback_window, bg='#98F5FF')
    frame.pack(fill=BOTH, expand=True)

    feedback_label = Label(frame, text="Application Feedback", font=("Helvetica", 16), bg=background, fg=framefg)
    feedback_label.pack(padx=20, pady=20)

    # Radio buttons for feedback options
    feedback_var = StringVar()
    feedback_var.set("Excellent")  # Set default value

    feedback_options = ["Excellent", "Very Good", "Good", "Needs Improvement"]

    for option in feedback_options:
        feedback_btn = Radiobutton(frame, text=option, variable=feedback_var, value=option, font=("Helvetica", 14), bg=background, fg=framefg)
        feedback_btn.pack(pady=5)

    submit_btn = Button(frame, text="Submit", command=lambda: show_feedback_message(feedback_var.get()), bg=button_c, fg=framefg, font=("Helvetica", 14), width=15)
    submit_btn.pack(pady=10)

    feedback_window.mainloop()

def show_feedback_message(feedback):
    messagebox.showinfo("Feedback Received", f"Thank you for your valuable feedback: {feedback}")
    


def open_login_window():
    # Create Login Window
    login_window = Tk()
    login_window.title("User Login")

    frame = Frame(login_window, bg='#98F5FF')
    frame.pack(fill=BOTH, expand=True)

    bank_label = Label(frame, text="Welcome to ABC Bank 💵", font=("Imprint MT Shadow", 26, "bold"), bg=background,
                       fg=framefg)
    bank_label.pack(padx=450, pady=20, anchor=NW)

    login_prompt = Label(frame, text="Login to your account", font=("Imprint MT Shadow", 26, "bold"), bg=background,
                         fg=framefg)
    login_prompt.pack(padx=450, pady=30, anchor=NW)

    Label(frame, text='🪙Username', bg='black', fg='white', font=("Helvetica", 14)).place(x=350, y=210)
    Label(frame, text='🪙Password', bg='black', fg='white', font=("Helvetica", 14)).place(x=350, y=250)

    entry_width = 30
    entry_font = ("Helvetica", 20)

    global e1, e2
    e1 = Entry(frame, font=entry_font, width=entry_width)
    e2 = Entry(frame, show="*", font=entry_font, width=entry_width)

    e1.place(x=500, y=210)
    e2.place(x=500, y=250)

    login_btn = Button(frame, text="Login👆", command=login, bg=button_c, fg=framefg, font=("Helvetica", 12,'bold'),
                       width=15, height=2)
    login_btn.place(x=600, y=300)

    login_window.mainloop()

# Create Registration Window
root = Tk()
root.title("User Registration")

frame = Frame(root, bg=background)
frame.pack(fill=BOTH, expand=True)

welcome_label = Label(frame, text="Welcome to ABC Bank 💵", font=("Imprint MT Shadow", 26, "bold"), bg=background,
                      fg=framefg)
welcome_label.pack(padx=350, pady=20, anchor=NW)

# Images
# Load Image 1
image1 = Image.open("D:\\Image\\login.png")
photo1 = ImageTk.PhotoImage(image1)

# Calculate image 1 position (bottom left)
image1_width = image1.width
image1_height = image1.height
window_height = root.winfo_screenheight()
padding = 20  # Adjust padding as needed
x1 = 50
y1 = window_height - image1_height - padding

# Create Label for Image 1
label_image1 = Label(frame, image=photo1, bg=background)
label_image1.image = photo1  # Keep a reference to the image to prevent it from being garbage collected
label_image1.place(x=x1, y=y1)

# Load Image 2
image2 = Image.open("D:\\Image\\money.png")
photo2 = ImageTk.PhotoImage(image2)

# Calculate image 2 position (top right)
image2_width = image2.width
image2_height = image2.height
padding = 20  # Adjust padding as needed
x2 = root.winfo_screenwidth() - image2_width - padding
y2 = 50

# Create Label for Image 2
label_image2 = Label(frame, image=photo2, bg=background)
label_image2.image = photo2  # Keep a reference to the image to prevent it from being garbage collected
label_image2.place(x=x2, y=y2)

label_font = ("Helvetica", 20)  # Adjust the font size here
entry_font = ("Helvetica", 20)  # Adjust the font size here
Label(frame, text='🪙 Account No', bg='black', fg='white', font=label_font).place(x=100, y=90)
Label(frame, text='🪙 Username', bg='black', fg='white', font=label_font).place(x=100, y=130)
Label(frame, text='🪙 Password', bg='black', fg='white', font=label_font).place(x=100, y=170)
Label(frame, text='🪙 Name', bg='black', fg='white', font=label_font).place(x=100, y=210)
Label(frame, text='🪙 Date of Birth', bg='black', fg='white', font=label_font).place(x=100, y=250)
Label(frame, text='🪙 Branch', bg='black', fg='white', font=label_font).place(x=100, y=290)
Label(frame, text='🪙 IFSC Code', bg='black', fg='white', font=label_font).place(x=100, y=330)

entry_width = 30

e1 = Entry(frame, font=entry_font, width=entry_width)
e2 = Entry(frame, font=entry_font, width=entry_width)
e3 = Entry(frame, show="*", font=entry_font, width=entry_width)
e4 = Entry(frame, font=entry_font, width=entry_width)
e5 = Entry(frame, font=entry_font, width=entry_width)
e6 = Entry(frame, font=entry_font, width=entry_width)
e7 = Entry(frame, font=entry_font, width=entry_width)

e1.place(x=450, y=90)
e2.place(x=450, y=130)
e3.place(x=450, y=170)
e4.place(x=450, y=210)
e5.place(x=450, y=250)
e6.place(x=450, y=290)
e7.place(x=450, y=330)

register_btn = Button(frame, text="Register👆🏻", command=register, bg=button_c, fg=framefg, font=("Helvetica", 16),
                      width=15, height=2)
register_btn.place(x=500, y=370)

login_btn = Button(frame, text="Login👆", command=open_login_window, bg=button_c, fg=framefg, font=("Helvetica", 16),
                   width=15, height=2)
login_btn.place(x=300, y=370)

root.mainloop()
