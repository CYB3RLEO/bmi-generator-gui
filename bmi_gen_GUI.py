import tkinter as tk
from tkinter import ttk, messagebox


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Input fields
        ttk.Label(self.main_frame, text="Weight (kg):").grid(
            row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.weight_entry = ttk.Entry(self.main_frame)
        self.weight_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.main_frame, text="Height (m):").grid(
            row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.height_entry = ttk.Entry(self.main_frame)
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        # Calculate button
        self.calculate_btn = ttk.Button(
            self.main_frame, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Result display
        self.result_frame = ttk.LabelFrame(
            self.main_frame, text="Result", padding=10)
        self.result_frame.grid(
            row=3, column=0, columnspan=2, sticky=tk.EW, pady=10)

        self.bmi_label = ttk.Label(self.result_frame, text="BMI: ")
        self.bmi_label.pack(anchor=tk.W)

        self.category_label = ttk.Label(self.result_frame, text="Category: ")
        self.category_label.pack(anchor=tk.W)

        # Clear button
        self.clear_btn = ttk.Button(
            self.main_frame, text="Clear", command=self.clear_fields)
        self.clear_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror(
                    "Error", "Please enter positive values for weight and height")
                return

            bmi = weight / (height ** 2)
            category = self.get_bmi_category(bmi)

            # Update result labels
            self.bmi_label.config(text=f"BMI: {bmi:.1f}")
            self.category_label.config(text=f"Category: {category}")

            # Change category color
            color = self.get_category_color(category)
            self.category_label.config(foreground=color)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def get_category_color(self, category):
        colors = {
            "Underweight": "blue",
            "Normal weight": "green",
            "Overweight": "orange",
            "Obesity": "red"
        }
        return colors.get(category, "black")

    def clear_fields(self):
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.bmi_label.config(text="BMI: ")
        self.category_label.config(text="Category: ", foreground="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
