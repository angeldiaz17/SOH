import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class SOHApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SOH - Software de Optimización de Horarios")
        self.root.geometry("400x300")
        self.root.configure(bg="#00aeff")  # Color de fondo suave

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Ingrese su ocupación:", bg="#00aeff", font=("Arial", 12), fg="#fdfdfd").pack(pady=10)
        self.occupation_entry = tk.Entry(self.root, font=("Arial", 12), bg="#ffffff", fg="#000000")
        self.occupation_entry.pack(pady=5)

        tk.Label(self.root, text="Ingrese las horas que puede trabajar (ej. 5):", bg="#00aeff", font=("Arial", 12), fg="#fdfdfd").pack(pady=10)
        self.hours_entry = tk.Entry(self.root, font=("Arial", 12), bg="#ffffff", fg="#000000")
        self.hours_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Enviar", command=self.show_recommendation, bg="#b60503", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=20)

    def show_recommendation(self):
        occupation = self.occupation_entry.get()
        try:
            available_hours = int(self.hours_entry.get())
            if available_hours <= 0:
                raise ValueError("Las horas deben ser un número positivo.")
        except ValueError as e:
            messagebox.showerror("Error", "Por favor, ingrese un número válido de horas.")
            return

        # Aquí puedes agregar lógica para determinar las mejores horas según la ocupación y horas disponibles
        recommended_hours = self.get_recommended_hours(available_hours)

        # Mostrar la segunda ventana con el gráfico
        self.show_graph(occupation, available_hours, recommended_hours)

    def get_recommended_hours(self, available_hours):
        # Lógica simple para recomendar horas (puedes personalizar esto)
        return [(9, 12), (15, 18)] if available_hours >= 5 else [(10, 12)]

    def show_graph(self, occupation, available_hours, recommended_hours):
        # Crear datos para el gráfico
        days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        demand = np.random.randint(1, 10, size=len(days))  # Simulación de demanda

        plt.figure(figsize=(10, 5))
        plt.bar(days, demand, color='skyblue')
        plt.title(f"SOH - Software de Optimización de Horarios {occupation}\nHoras Disponibles: {available_hours}", fontsize=14, color="#00796b")
        plt.xlabel("Días de la Semana", fontsize=12, color="#00796b")
        plt.ylabel("Demanda", fontsize=12, color="#00796b")
        plt.axhline(y=available_hours, color='red', linestyle='--', label='Horas Disponibles')
        plt.legend()
        plt.grid(axis='y')

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = SOHApp(root)
    root.mainloop()


