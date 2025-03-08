# This application is intended to allow users to place an order
# from the GUI

""" This application is intended to allow users to place pizza orders on the application
Author: Jordan Henry
Assignment: Final Project """

import tkinter as tk
from tkinter import messagebox


class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cheesaroni Pizzeria")
        self.root.geometry("600x500")

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
        # Open the Order Form
        self.order_form = OrderForm(self.root)

    def view_existing_orders(self):
        # Simulate viewing existing orders (will be expanded with actual order history logic)
        messagebox.showinfo("Existing Orders", "Here is a list of your previous orders.")

    def quit_app(self):
        # Quit the application
        self.root.quit()


class OrderForm:
    def __init__(self, parent):
        self.parent = parent
        self.new_order_window = tk.Toplevel(self.parent)
        self.new_order_window.title("New Order Form")
        self.new_order_window.geometry("500x500")

        self.pizzas = []  # List to hold pizza selections
        self.sides = []  # List to hold side selections

        self.create_order_form()

    def create_order_form(self):
        # Pizza customization options
        self.pizza_frame = tk.Frame(self.new_order_window)
        self.pizza_frame.pack(pady=10)

        tk.Label(self.pizza_frame, text="Select Pizza Size:", font=("Arial", 12)).grid(row=0, column=0, pady=5)
        self.size_var = tk.StringVar()
        size_menu = tk.OptionMenu(self.pizza_frame, self.size_var, "Small", "Medium", "Large")
        size_menu.grid(row=0, column=1, pady=5)

        tk.Label(self.pizza_frame, text="Select Crust Type:", font=("Arial", 12)).grid(row=1, column=0, pady=5)
        self.crust_var = tk.StringVar()
        crust_menu = tk.OptionMenu(self.pizza_frame, self.crust_var, "Thin", "Thick", "Stuffed")
        crust_menu.grid(row=1, column=1, pady=5)

        tk.Label(self.pizza_frame, text="Select Sauce Type:", font=("Arial", 12)).grid(row=2, column=0, pady=5)
        self.sauce_var = tk.StringVar()
        sauce_menu = tk.OptionMenu(self.pizza_frame, self.sauce_var, "Tomato", "Pesto", "Alfredo")
        sauce_menu.grid(row=2, column=1, pady=5)

        tk.Label(self.pizza_frame, text="Select Toppings:", font=("Arial", 12)).grid(row=3, column=0, pady=5)
        self.topping_var = tk.StringVar()
        topping_menu = tk.OptionMenu(self.pizza_frame, self.topping_var, "Cheese", "Pepperoni", "Mushrooms", "Olives",
                                     "Onions", "Peppers")
        topping_menu.grid(row=3, column=1, pady=5)

        # Button to add pizza
        self.add_pizza_button = tk.Button(self.pizza_frame, text="Add Pizza", font=("Arial", 12),
                                          command=self.add_pizza)
        self.add_pizza_button.grid(row=4, columnspan=2, pady=10)

        # Button to add side
        self.add_side_button = tk.Button(self.new_order_window, text="Add Side", font=("Arial", 12),
                                         command=self.add_side)
        self.add_side_button.pack(pady=10)

        # Button to proceed to checkout
        self.checkout_button = tk.Button(self.new_order_window, text="Proceed to Checkout", font=("Arial", 12),
                                         command=self.checkout_window)
        self.checkout_button.pack(pady=10)

        # Frame to display the current order summary (pizzas and sides added)
        self.order_summary_frame = tk.Frame(self.new_order_window)
        self.order_summary_frame.pack(pady=10)

        self.update_order_summary()

    def add_pizza(self):
        pizza_order = {
            'size': self.size_var.get(),
            'crust': self.crust_var.get(),
            'sauce': self.sauce_var.get(),
            'topping': self.topping_var.get()
        }
        self.pizzas.append(pizza_order)
        self.clear_pizza_form()
        messagebox.showinfo("Pizza Added", "A pizza has been added to your order!")
        self.update_order_summary()

    def add_side(self):
        side_window = SideSelectionWindow(self.parent, self)
        side_window.create_side_selection_form()

    def clear_pizza_form(self):
        # Reset pizza options for adding new pizzas
        self.size_var.set("")
        self.crust_var.set("")
        self.sauce_var.set("")
        self.topping_var.set("")

    def update_order_summary(self):
        # Clear previous order summary
        for widget in self.order_summary_frame.winfo_children():
            widget.destroy()

        order_summary = "Pizzas:\n"
        for pizza in self.pizzas:
            order_summary += f"Size: {pizza['size']}, Crust: {pizza['crust']}, Sauce: {pizza['sauce']}, Topping: {pizza['topping']}\n"

        order_summary += "\nSides:\n"
        for side in self.sides:
            order_summary += f"{side}\n"

        # Display the order summary
        tk.Label(self.order_summary_frame, text=order_summary, font=("Arial", 12)).pack()

    def checkout_window(self):
        # Open the Checkout window
        self.checkout_win = CheckoutWindow(self.parent, self.pizzas, self.sides)
        self.new_order_window.destroy()


class SideSelectionWindow:
    def __init__(self, parent, order_form):
        self.parent = parent
        self.order_form = order_form
        self.side_window = tk.Toplevel(self.parent)
        self.side_window.title("Select Side Dishes")
        self.side_window.geometry("400x300")

    def create_side_selection_form(self):
        tk.Label(self.side_window, text="Select Side Dish:", font=("Arial", 12)).pack(pady=10)

        self.side_var = tk.StringVar()
        side_menu = tk.OptionMenu(self.side_window, self.side_var, "Garlic Bread", "Wings", "Salad")
        side_menu.pack(pady=5)

        # Button to add side dish
        self.add_side_button = tk.Button(self.side_window, text="Add Side", font=("Arial", 12), command=self.add_side)
        self.add_side_button.pack(pady=10)

        # Button to proceed to checkout
        self.checkout_button = tk.Button(self.side_window, text="Proceed to Checkout", font=("Arial", 12),
                                         command=self.checkout_window)
        self.checkout_button.pack(pady=10)

    def add_side(self):
        side_order = self.side_var.get()
        self.order_form.sides.append(side_order)
        self.side_window.destroy()
        messagebox.showinfo("Side Added", f"{side_order} has been added to your order!")
        self.order_form.update_order_summary()

    def checkout_window(self):
        # Open the Checkout window
        self.checkout_win = CheckoutWindow(self.parent, self.order_form.pizzas, self.order_form.sides)
        self.side_window.destroy()


class CheckoutWindow:
    def __init__(self, parent, pizzas, sides=None):
        self.parent = parent
        self.checkout_win = tk.Toplevel(self.parent)
        self.checkout_win.title("Checkout")
        self.checkout_win.geometry("500x500")

        self.pizzas = pizzas
        self.sides = sides if sides is not None else []

        self.create_checkout_form()

    def create_checkout_form(self):
        # Order Summary
        order_summary = "Pizzas:\n"
        for pizza in self.pizzas:
            order_summary += f"Size: {pizza['size']}, Crust: {pizza['crust']}, Sauce: {pizza['sauce']}, Topping: {pizza['topping']}\n"

        order_summary += "\nSides:\n"
        for side in self.sides:
            order_summary += f"{side}\n"

        tk.Label(self.checkout_win, text="Order Summary:", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.checkout_win, text=order_summary, font=("Arial", 12)).pack(pady=5)

        # Customer details
        tk.Label(self.checkout_win, text="Name:", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(self.checkout_win, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(self.checkout_win, text="Address:", font=("Arial", 12)).pack(pady=5)
        self.address_entry = tk.Entry(self.checkout_win, font=("Arial", 12))
        self.address_entry.pack(pady=5)

        tk.Label(self.checkout_win, text="Credit Card Information:", font=("Arial", 12)).pack(pady=5)
        self.credit_card_entry = tk.Entry(self.checkout_win, font=("Arial", 12))
        self.credit_card_entry.pack(pady=5)

        # Button to place the order
        self.place_order_button = tk.Button(self.checkout_win, text="Place Order", font=("Arial", 12),
                                            command=self.place_order)
        self.place_order_button.pack(pady=10)

        # Button to go back to modify order
        self.modify_order_button = tk.Button(self.checkout_win, text="Modify Order", font=("Arial", 12),
                                             command=self.modify_order)
        self.modify_order_button.pack(pady=5)

    def place_order(self):
        # Place the order (in a real app, this would involve backend integration)
        self.checkout_win.destroy()
        self.show_confirmation_window()

    def modify_order(self):
        # Close checkout window and reopen order form to modify
        self.checkout_win.destroy()
        OrderForm(self.parent)

    def show_confirmation_window(self):
        confirmation_win = tk.Toplevel(self.parent)
        confirmation_win.title("Order Confirmation")
        confirmation_win.geometry("400x200")

        confirmation_message = "We have received your order!\nEstimated delivery time 30-45 minutes.\nHave a wonderful day!"

        tk.Label(confirmation_win, text=confirmation_message, font=("Arial", 12), padx=20, pady=20).pack()
        tk.Button(confirmation_win, text="Close", font=("Arial", 12), command=confirmation_win.destroy).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaApp(root)
    root.mainloop()
