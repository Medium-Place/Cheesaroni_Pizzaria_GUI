# This application is intended to allow users to place an order
# from the GUI

import tkinter as tk
from tkinter import messagebox


class PizzaPalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cheesaroni Pizzeria")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Welcome message
        self.welcomeLabel = tk.Label(self.root, text="Welcome to Cheesaroni Pizzeria!", font=("Arial", 16), padx=10,
                                     pady=10)
        self.welcomeLabel.pack()

        self.introLabel = tk.Label(self.root, text="Order your favorite pizza with ease!", font=("Arial", 12), padx=10,
                                   pady=5)
        self.introLabel.pack()

        # Buttons to navigate to different sections
        self.newOrderButton = tk.Button(self.root, text="Start a New Order", font=("Arial", 12),
                                        command=self.start_new_order)
        self.newOrderButton.pack(pady=10)

        self.viewOrdersButton = tk.Button(self.root, text="View Existing Orders", font=("Arial", 12),
                                          command=self.view_existing_orders)
        self.viewOrdersButton.pack(pady=10)

        self.quitButton = tk.Button(self.root, text="Quit", font=("Arial", 12), command=self.quit_app)
        self.quitButton.pack(pady=10)

    def start_new_order(self):
        # Simulate starting a new order (can be later expanded with actual order logic)
        messagebox.showinfo("New Order", "You can now start a new pizza order!")

    def view_existing_orders(self):
        # Simulate viewing existing orders (will be expanded with actual order history logic)
        messagebox.showinfo("Existing Orders", "Here is a list of your previous orders.")

    def quit_app(self):
        # Quit the application
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPalApp(root)
    root.mainloop()
