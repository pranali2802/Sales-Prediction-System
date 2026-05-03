import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_sales():
    try:
        tv = float(entry_tv.get())
        radio = float(entry_radio.get())
        news = float(entry_news.get())

        prediction = model.predict([[tv, radio, news]])
        result_var.set(f"Predicted Sales: {prediction[0]:.2f}")

    except:
        messagebox.showerror("Error", "Please enter valid numeric values")

# Clear inputs
def clear_fields():
    entry_tv.delete(0, 'end')
    entry_radio.delete(0, 'end')
    entry_news.delete(0, 'end')
    result_var.set("")

# Show graph
def show_graph():
    plt.figure()
    plt.scatter(data['TV'], y)
    plt.xlabel("TV Budget")
    plt.ylabel("Sales")
    plt.title("Sales vs TV Budget")
    plt.show()

# Main window
app = tb.Window(themename="superhero")   # Try: darkly, cosmo, flatly
app.title("Sales Prediction System")
app.geometry("450x450")

# Title
tb.Label(
    app,
    text="📊 Sales Prediction System",
    font=("Helvetica", 18, "bold"),
    bootstyle="info"
).pack(pady=15)

# Input Frame
frame = tb.Frame(app)
frame.pack(pady=10)

tb.Label(frame, text="TV Budget").grid(row=0, column=0, padx=10, pady=8)
entry_tv = tb.Entry(frame, bootstyle="primary")
entry_tv.grid(row=0, column=1)

tb.Label(frame, text="Radio Budget").grid(row=1, column=0, padx=10, pady=8)
entry_radio = tb.Entry(frame, bootstyle="primary")
entry_radio.grid(row=1, column=1)

tb.Label(frame, text="Newspaper Budget").grid(row=2, column=0, padx=10, pady=8)
entry_news = tb.Entry(frame, bootstyle="primary")
entry_news.grid(row=2, column=1)

# Buttons
btn_frame = tb.Frame(app)
btn_frame.pack(pady=15)

tb.Button(
    btn_frame,
    text="Predict",
    bootstyle="success",
    command=predict_sales
).grid(row=0, column=0, padx=8)

tb.Button(
    btn_frame,
    text="Clear",
    bootstyle="warning",
    command=clear_fields
).grid(row=0, column=1, padx=8)

tb.Button(
    btn_frame,
    text="Show Graph",
    bootstyle="info",
    command=show_graph
).grid(row=0, column=2, padx=8)

# Result Display
result_var = tb.StringVar()
tb.Label(
    app,
    textvariable=result_var,
    font=("Arial", 14),
    bootstyle="light"
).pack(pady=20)

# Footer
tb.Label(
    app,
    text="Machine Learning Project | Linear Regression",
    font=("Arial", 9),
    bootstyle="secondary"
).pack(side="bottom", pady=10)

app.mainloop()