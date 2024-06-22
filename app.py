import cmd
import getpass
from database import *
from cryptography.fernet import Fernet
import datetime


class FoodDeliveryCLI(cmd.Cmd):
    intro = "Welcome to the BiteBox. Type 'help' or '?' to list commands.\n"
    prompt = "> "


    def preloop(self):
        self.userid = None
        self.role = None

    def do_register(self, arg):
        print("Enter your registration information")
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        role = input("Role (customer/owner): ")

        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "username": username,
            "password": password,
            "role": role
        }
        create_user(user)
        userid = get_last_inserted_user_id()
        if role == "customer":
            create_customer({"userid": userid})
        elif role == "owner":
            ownerid = create_owner_user({"userid": userid})
            print("Enter your restaurant information")
            restaurant_name = input("Restaurant Name: ")
            street = input("Street: ")
            city = input("City: ")
            state = input("State: ")
            pin = input("PIN: ")
            restaurant_phone = input("Restaurant Phone: ")

            restaurant = {
                "restaurantname": restaurant_name,
                "email": email,
                "phone": restaurant_phone,
                "ownerid": ownerid,
                "street": street,
                "city": city,
                "state": state,
                "pin": pin
            }
            create_restaurant(restaurant)
            create_menu({"restaurantid": get_last_inserted_restaurant_id()})
            print("Add menu items")
            print("Enter menu item details (or type 'finish')")

            
            while True:
                menu_item = {'menuid': get_last_menu_id()} 
                menu_item['nameofthedish'] = input("Item Name: ")
                if menu_item['nameofthedish'].lower() == 'finish':
                    break
                menu_item['description'] = input("Description: ")
                menu_item['price'] = float(input("Price: "))

                create_menu_item(menu_item)
                print(f"Added {menu_item['nameofthedish']}")

            print("Menu items have been added.")


        print("Registration successful")


    def do_login(self, arg):
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        user = validate_user(username, password)
        if user:
            print(f"Welcome, {user['firstname']} {user['lastname']}!")
            self.userid = user["userid"]
            self.role = user["role"]
        else:
            print("Invalid username or password")

    def do_update(self, arg):
        if self.role not in ["customer", "owner"]:
            print("Please log in first.")
            return

        print("Enter the updated information (leave blank to keep the current value)")
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        user = read_user_by_id(self.userid)
        updated_user = {
            "userid": self.userid,
            "firstname": firstname or user["firstname"],
            "lastname": lastname or user["lastname"],
            "email": email or user["email"],
            "phone": phone or user["phone"],
            "username": username or user["username"],
            "password": bcrypt.hashpw(password.encode(), bcrypt.gensalt()) if password else user["password"],
            "role": user["role"],
        }
        update_user(updated_user)
        print("User information updated successfully")


    def do_delete(self, arg):
        if self.role not in ["customer", "owner"]:
            print("Please log in first.")
            return

        confirmation = input("Are you sure you want to delete your account? (yes/no): ")
        if confirmation.lower() == "yes":
            if self.role == "customer":
                customer = read_customer_by_userid(self.userid)
                if customer:
                    delete_customer(customer["customerid"])
            delete_user(self.userid)
            print("Your account has been deleted successfully.")
            self.userid = None
            self.role = None
        else:
            print("Account deletion cancelled.")


    def do_show_restaurants(self, arg):
        if self.role != "customer":
            print("This action is allowed only for customers.")
            return

        restaurants = get_all_restaurants()
        for restaurant in restaurants:
            print(f"{restaurant['restaurantid']} - {restaurant['restaurantname']}")


    def do_view_menu(self, arg):
        if self.role != "customer":
            print("This action is allowed only for customers.")
            return

        try:
            restaurant_id = int(arg)
        except ValueError:
            print("Invalid restaurant ID")
            return

        menu_items = get_menu_items(restaurant_id)
        for item in menu_items:
            print(f"{item['itemid']} - {item['nameofthedish']} - ${item['price']}")

    def do_add_to_order(self, arg):
        if self.role != "customer":
            print("This action is allowed only for customers.")
            return
        customer = read_customer_by_userid(self.userid)
        if not customer:
            print("Invalid customer ID.")
            return

        order_id = get_or_create_order_id(customer['customerid'])

        while True:
            try:
                item_id, quantity = map(int, input("Enter item ID and quantity (or type 'finish'): ").split())
            except ValueError:
                break

            order_item = {
                "orderid": order_id,
                "itemid": item_id,
                "quantity": quantity
            }

            add_order_item(order_item)
            print(f"Added {quantity} of item {item_id} to your order.")

        special_instructions = input("Special Instructions: ")
        update_special_instructions(order_id, special_instructions)

        order = read_order_by_id(order_id)
        assign_driver(order_id)
        driver = get_driver_by_order_id(order_id)

        order_items = get_order_items_with_prices(order_id)
        total_amount = sum(item['price'] * item['quantity'] for item in order_items)

        print(f"Order ID: {order['orderid']}")
        print(f"Order Date: {order['orderdate']}")
        print(f"Total Amount: ${total_amount}")
        print(f"Special Instructions: {order['specialinstructions']}")
        print(f"Order Status: {order['orderstatus']}")
        print(f"Delivery Driver: {driver['firstname']}")
        print(f"Driver Phone: {driver['phone']}")

        self.do_payment(total_amount)

    def assign_driver(self, order_id):
        driver = select_random_driver()
        set_driver_for_order(order_id, driver['driverid'])

    def do_remove_from_order(self, arg):
        if self.role != "customer":
            print("This action is allowed only for customers.")
            return

        try:
            order_item_id = int(arg)
        except ValueError:
            print("Invalid input format. Usage: remove_from_order <order_item_id>")
            return

        remove_order_item(order_item_id)
        print(f"Removed item {order_item_id} from your order.")


     # Owner-related methods
    def do_update_restaurant(self, arg):
        if self.role != "owner":
            print("This action is allowed only for owners.")
            return
        print("Enter the updated information (leave blank to keep the current value)")
        name = input("Restaurant Name: ")
        street = input("Street: ")
        city = input("City: ")
        state = input("State: ")
        pin = input("PIN: ")
        phone = input("Phone: ")
        ownerId = get_ownerId_from_user(self.userid)
        restaurant = read_restaurant_by_owner_id(ownerId)
        
        if not restaurant:
            print("No restaurant found for the given owner ID.")
            return

        updated_restaurant = {
            "restaurantid": restaurant["restaurantid"],
            "name": name or restaurant["name"],
            "street": street or restaurant["street"],
            "city": city or restaurant["city"],
            "state": state or restaurant["state"],
            "pin": pin or restaurant["pin"],
            "phone": phone or restaurant["phone"],
            "ownerid": self.userid,
        }
        update_restaurant(updated_restaurant)
        print("Restaurant information updated successfully")


    def do_delete_restaurant(self, arg):
        if self.role != "owner":
            print("Only restaurant owners can delete their restaurants.")
            return

        confirmation = input("Are you sure you want to delete your restaurant? (yes/no): ")
        if confirmation.lower() == "yes":
            ownerId = get_ownerId_from_user(self.userid)
            restaurant = read_restaurant_by_owner_id(ownerId)
            delete_restaurant(restaurant["restaurantid"])
            print("Your restaurant has been deleted successfully.")
        else:
            print("Restaurant deletion cancelled.")

        

    def do_create_menu_item(self, arg):
        if self.role != "owner":
            print("Please log in as an owner.")
            return

        menu_id = input("Enter the menu ID: ")
        item_name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = input("Enter the item price: ")

        menu_item = {
            "menuid": menu_id,
            "nameofdish": item_name,
            "description": description,
            "price": price
        }
        create_menu_item(menu_item)
        print("Menu item created successfully.")

    def do_update_menu_item(self, arg):
        if self.role != "owner":
            print("Please log in as an owner.")
            return

        item_id = input("Enter the item ID to update: ")
        menu_id = input("Enter the menu ID for this item: ")
        item_name = input("Enter the new item name: ")
        description = input("Enter the new item description: ")
        price = input("Enter the new item price: ")

        menu_item = {
            "itemid": item_id,
            "menuid": menu_id,
            "nameofthedish": item_name,
            "description": description,
            "price": price
        }
        update_menu_item(menu_item)
        print("Menu item updated successfully.")

    def do_quit(self, arg):
        """Exit the CLI"""
        print("Bye!")
        return True
    
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_data(data, key):
        f = Fernet(key)
        return f.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt_data(data, key):
        f = Fernet(key)
        return f.decrypt(data.encode()).decode()
    
    def do_payment(self, amount):
        print("Payment details")
        card_number = input("Enter your credit card number: ")
        card_exp_date = input("Enter the card expiration date (MM/YY): ")
        card_cvv = input("Enter the CVV: ")

        encryption_key = self.generate_key()
        encrypted_cvv = self.encrypt_data(card_cvv, encryption_key)

        customer = read_customer_by_userid(self.userid)
        order_id = get_or_create_order_id(customer['customerid'])


        payment_info = {
        "customerid":customer['customerid'],
        "orderid": order_id,
        "cardnumber": card_number,
        "expdate": card_exp_date,
        "cvv": encrypted_cvv,
        "encryption_key": encryption_key.decode(),  # Storing the key as a string
        "amount": amount,
        "date": datetime.datetime.now()
        }
        create_payment(payment_info)
        payment_successful = True
        if payment_successful:
            print("Payment successful")
            update_order_status(order_id, "Preparing")
        else:
            print("Payment failed")

if __name__ == "__main__":
    FoodDeliveryCLI().cmdloop()