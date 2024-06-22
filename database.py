import pymysql
import cryptography
import bcrypt



def create_conn():
    try:
        conn = pymysql.connect(
             host = 'localhost',
            user = 'root',
            password ='Prajwal1!' ,
            db = 'bitebox',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit =True
        )
        return conn

    except pymysql.Error as e:
        print("Connection Failed error :%d :%s" %(e.args[0],e.args[1]))
        print("Connection Failed : {0}".format(e))
        exit()

# Create User
def create_user(user):
    connection = create_conn()
    hashed_password = bcrypt.hashpw(user['password'].encode(), bcrypt.gensalt())
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO user (firstname, lastname, email, phone, username, password, role) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user['firstname'], user['lastname'], user['email'], user['phone'], user['username'], hashed_password, user['role']))
        connection.commit()
    finally:
        connection.close()

# Read User
def read_user_by_id(userid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE userid=%s"
            cursor.execute(sql, (userid,))
            return cursor.fetchone()
    finally:
        connection.close()

#Update user
def update_user(user):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE user SET firstname=%s, lastname=%s, email=%s, phone=%s, username=%s, password=%s, role=%s WHERE userid=%s"
            cursor.execute(sql, (user['firstname'], user['lastname'], user['email'], user['phone'], user['username'], user['password'], user['role'], user['userid']))
        connection.commit()
    finally:
        connection.close()

#Delete User
def delete_user(userid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM user WHERE userid=%s"
            cursor.execute(sql, (userid,))
        connection.commit()
    finally:
        connection.close()


#UserID
def get_last_inserted_user_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user ORDER BY userid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['userid']
    finally:
        connection.close()


#create customer
def create_customer(userid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO customer (userid) VALUES (%s)"
            cursor.execute(sql, (userid['userid']))
        connection.commit()
    finally:
        connection.close()


# Read customer
def read_customer_by_userid(userid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM customer WHERE userid=%s"
            cursor.execute(sql, (userid,))
            return cursor.fetchone()
    finally:
        connection.close()


#update customer
def update_CUSTOMER(customer):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE customer SET userid=%s WHERE customerid=%s"
            cursor.execute(sql, (customer['userid'], customer['customerid']))
        connection.commit()
    finally:
        connection.close()

#Delete customer
def delete_customer(customerid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Customer WHERE customerid=%s"
            cursor.execute(sql, (customerid,))
        connection.commit()
    finally:
        connection.close()



#CustomerID
def get_last_inserted_customer_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM customer ORDER BY customerid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['customerid']
    finally:
        connection.close()


# Create owner
def create_owner(userid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO owner (userid) VALUES (%s)"
            cursor.execute(sql, (userid,))
        connection.commit()
    finally:
        connection.close()

# Read owner
def read_owner_by_id(ownerid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM owner WHERE ownerid=%s"
            cursor.execute(sql, (ownerid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update owner
def update_owner(owner):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE owner SET userid=%s WHERE ownerid=%s"
            cursor.execute(sql, (owner['userid'], owner['ownerid']))
        connection.commit()
    finally:
        connection.close()

# Delete owner
def delete_owner(ownerid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM owner WHERE ownerid=%s"
            cursor.execute(sql, (ownerid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted owner id
def get_last_inserted_owner_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM owner ORDER BY ownerid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['ownerid']
    finally:
        connection.close()


# Create user address
def create_user_address(address):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO useraddress (street, city, state, pin, customerid) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (address['street'], address['city'], address['state'], address['pin'], address['customerid']))
        connection.commit()
    finally:
        connection.close()

# Read user address by id
def read_user_address_by_id(addressid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM useraddress WHERE addressid=%s"
            cursor.execute(sql, (addressid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update user address
def update_user_address(address):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE useraddress SET street=%s, city=%s, state=%s, pin=%s, customerid=%s WHERE addressid=%s"
            cursor.execute(sql, (address['street'], address['city'], address['state'], address['pin'], address['customerid'], address['addressid']))
        connection.commit()
    finally:
        connection.close()

# Delete user address
def delete_user_address(addressid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM useraddress WHERE addressid=%s"
            cursor.execute(sql, (addressid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted user address id
def get_last_inserted_user_address_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM useraddress ORDER BY addressid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['addressid']
    finally:
        connection.close()



# Create restaurant address
def create_restaurant_address(address):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO restaurantaddress (street, city, state, pin) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (address['street'], address['city'], address['state'], address['pin']))
        connection.commit()
    finally:
        connection.close()

# Read restaurant address by id
def read_restaurant_address_by_id(addressid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurantaddress WHERE addressid=%s"
            cursor.execute(sql, (addressid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update restaurant address
def update_restaurant_address(address):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE restaurantaddress SET street=%s, city=%s, state=%s, pin=%s WHERE addressid=%s"
            cursor.execute(sql, (address['street'], address['city'], address['state'], address['pin'], address['addressid']))
        connection.commit()
    finally:
        connection.close()

# Delete restaurant address
def delete_restaurant_address(addressid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM restaurantaddress WHERE addressid=%s"
            cursor.execute(sql, (addressid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted restaurant address id
def get_last_inserted_restaurant_address_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurantaddress ORDER BY addressid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['addressid']
    finally:
        connection.close()


# Create restaurant
def create_restaurant(restaurant):
    connection = create_conn()
    cursor = connection.cursor()
    try:
        
        cursor.execute("INSERT INTO RestaurantAddress (street, city, state, pin) VALUES (%s, %s, %s, %s)",
                       (restaurant["street"], restaurant["city"], restaurant["state"], restaurant["pin"]))
        connection.commit()
        address_id = cursor.lastrowid

       
        cursor.execute("INSERT INTO Restaurant (restaurantname, email, phone, addressid, ownerid) VALUES (%s, %s, %s, %s, %s)",
                       (restaurant["restaurantname"], restaurant["email"], restaurant["phone"], address_id, restaurant["ownerid"]))
        connection.commit()
    finally:
        cursor.close()
        connection.close()

# Read restaurant by id
def read_restaurant_by_id(restaurantid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurant WHERE restaurantid=%s"
            cursor.execute(sql, (restaurantid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update restaurant
def update_restaurant(restaurant):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
           
            sql = "UPDATE Restaurant SET restaurantname=%s, phone=%s WHERE restaurantid=%s"
            cursor.execute(sql, (restaurant['name'], restaurant['phone'], restaurant['restaurantid']))

            
            sql = """UPDATE RestaurantAddress AS a
                     JOIN Restaurant AS r ON a.addressid = r.addressid
                     SET a.street=%s, a.city=%s, a.state=%s, a.pin=%s
                     WHERE r.restaurantid=%s"""
            cursor.execute(sql, (restaurant['street'], restaurant['city'], restaurant['state'], restaurant['pin'], restaurant['restaurantid']))

        connection.commit()
    finally:
        connection.close()

# Delete restaurant
def delete_restaurant(restaurantid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM restaurant WHERE restaurantid=%s"
            cursor.execute(sql, (restaurantid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted restaurant id
def get_last_inserted_restaurant_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurant ORDER BY restaurantid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['restaurantid']
    finally:
        connection.close()


# Create menu
def create_menu(menu):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO menu (restaurantid) VALUES (%s)"
            cursor.execute(sql, (menu['restaurantid'],))
        connection.commit()
    finally:
        connection.close()

# Read menu by id
def read_menu_by_id(menuid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM menu WHERE menuid=%s"
            cursor.execute(sql, (menuid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update menu
def update_menu(menu):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE menu SET restaurantid=%s WHERE menuid=%s"
            cursor.execute(sql, (menu['restaurantid'], menu['menuid']))
        connection.commit()
    finally:
        connection.close()

# Delete menu
def delete_menu(menuid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM menu WHERE menuid=%s"
            cursor.execute(sql, (menuid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted menu id
def get_last_menu_id():
    connection = create_conn()
    menu_id = None
    try:
        with connection.cursor() as cursor:
            sql = "SELECT menuid FROM Menu ORDER BY menuid DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                menu_id = result['menuid']
    finally:
        connection.close()
    return menu_id



# Create menu item
def create_menu_item(item):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO MenuItems (nameofthedish, description, price, menuid) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (item['nameofthedish'], item['description'], item['price'], item['menuid']))
        connection.commit()
    finally:
        connection.close()

# Read menu item by id
def read_menu_item_by_id(itemid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM menuitems WHERE itemid=%s"
            cursor.execute(sql, (itemid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update menu item
def update_menu_item(item):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE menuitems SET nameofthedish=%s, description=%s, price=%s, menuid=%s WHERE itemid=%s"
            cursor.execute(sql, (item['nameofthedish'], item['description'], item['price'], item['menuid'], item['itemid']))
        connection.commit()
    finally:
        connection.close()

# Delete menu item
def delete_menu_item(itemid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM menuitems WHERE itemid=%s"
            cursor.execute(sql, (itemid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted menu item id
def get_last_inserted_menu_item_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM menuitems ORDER BY itemid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['itemid']
    finally:
        connection.close()

# Create delivery driver
def create_delivery_driver(driver):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO deliverydriver (firstname, lastname, phone, email, userid) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (driver['firstname'], driver['lastname'], driver['phone'], driver['email'], driver['userid']))
        connection.commit()
    finally:
        connection.close()

# Read delivery driver by id
def read_delivery_driver_by_id(driverid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM deliverydriver WHERE delivery_driver_id=%s"
            cursor.execute(sql, (driverid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update delivery driver
def update_delivery_driver(driver):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE deliverydriver SET firstname=%s, lastname=%s, phone=%s, email=%s, userid=%s WHERE delivery_driver_id=%s"
            cursor.execute(sql, (driver['firstname'], driver['lastname'], driver['phone'], driver['email'], driver['userid'], driver['delivery_driver_id']))
        connection.commit()
    finally:
        connection.close()

# Delete delivery driver
def delete_delivery_driver(driverid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM deliverydriver WHERE delivery_driver_id=%s"
            cursor.execute(sql, (driverid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted delivery driver id
def get_last_inserted_delivery_driver_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM deliverydriver ORDER BY delivery_driver_id DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['delivery_driver_id']
    finally:
        connection.close()


# Create order
def create_order(order):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO orders (orderdate, totalamount, specialinstructions, orderstatus, addressid, userid, delivery_driver_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (order['orderdate'], order['totalamount'], order['specialinstructions'], order['orderstatus'], order['addressid'], order['userid'], order['delivery_driver_id']))
        connection.commit()
    finally:
        connection.close()

# Read order by id
def read_order_by_id(orderid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM orders WHERE orderid=%s"
            cursor.execute(sql, (orderid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update order
def update_order(order):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE orders SET orderdate=%s, totalamount=%s, specialinstructions=%s, orderstatus=%s, addressid=%s, userid=%s, delivery_driver_id=%s WHERE orderid=%s"
            cursor.execute(sql, (order['orderdate'], order['totalamount'], order['specialinstructions'], order['orderstatus'], order['addressid'], order['userid'], order['delivery_driver_id'], order['orderid']))
        connection.commit()
    finally:
        connection.close()

# Delete order
def delete_order(orderid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM orders WHERE orderid=%s"
            cursor.execute(sql, (orderid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted order id
def get_last_inserted_order_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM orders ORDER BY orderid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['orderid']
    finally:
        connection.close()


# Create order item
def create_order_item(order_item):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO orderitems (amount, quantity, totalamount, itemid, orderid) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (order_item['amount'], order_item['quantity'], order_item['totalamount'], order_item['itemid'], order_item['orderid']))
        connection.commit()
    finally:
        connection.close()

# Read order item by id
def read_order_item_by_id(detailid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM orderitems WHERE detailid=%s"
            cursor.execute(sql, (detailid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update order item
def update_order_item(order_item):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE orderitems SET amount=%s, quantity=%s, totalamount=%s, itemid=%s, orderid=%s WHERE detailid=%s"
            cursor.execute(sql, (order_item['amount'], order_item['quantity'], order_item['totalamount'], order_item['itemid'], order_item['orderid'], order_item['detailid']))
        connection.commit()
    finally:
        connection.close()

# Delete order item
def delete_order_item(detailid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM orderitems WHERE detailid=%s"
            cursor.execute(sql, (detailid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted order item id
def get_last_inserted_order_item_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM orderitems ORDER BY detailid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['detailid']
    finally:
        connection.close()


# Create payment
def create_payment(payment):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO payment (amount, date, cardnumber, expdate, cvv, orderid, customerid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (payment['amount'], payment['date'], payment['cardnumber'], payment['expdate'], payment['cvv'], payment['orderid'], payment['customerid']))
        connection.commit()
    finally:
        connection.close()

# Read payment by id
def read_payment_by_id(paymentid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM payment WHERE paymentid=%s"
            cursor.execute(sql, (paymentid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update payment
def update_payment(payment):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE payment SET amount=%s, date=%s, cardnumber=%s, expdate=%s, cvv=%s, orderid=%s, customerid=%s WHERE paymentid=%s"
            cursor.execute(sql, (payment['amount'], payment['date'], payment['cardnumber'], payment['expdate'], payment['cvv'], payment['orderid'], payment['customerid'], payment['paymentid']))
        connection.commit()
    finally:
        connection.close()

# Delete payment
def delete_payment(paymentid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM payment WHERE paymentid=%s"
            cursor.execute(sql, (paymentid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted payment id
def get_last_inserted_payment_id():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM payment ORDER BY paymentid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['paymentid']
    finally:
        connection.close()


# Create rating
def create_rating(rating):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO rating (noofstars, description, userid, restaurantid) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (rating['noofstars'], rating['description'], rating['userid'], rating['restaurantid']))
        connection.commit()
    finally:
        connection.close()

# Read rating by id
def read_rating_by_id(ratingid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM rating WHERE ratingid=%s"
            cursor.execute(sql, (ratingid,))
            return cursor.fetchone()
    finally:
        connection.close()

# Update rating
def update_rating(rating):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE rating SET noofstars=%s, description=%s, userid=%s, restaurantid=%s WHERE ratingid=%s"
            cursor.execute(sql, (rating['noofstars'], rating['description'], rating['userid'], rating['restaurantid'], rating['ratingid']))
        connection.commit()
    finally:
        connection.close()

# Delete rating
def delete_rating(ratingid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM rating WHERE ratingid=%s"
            cursor.execute(sql, (ratingid,))
        connection.commit()
    finally:
        connection.close()

# Get last inserted rating id
def get_last_inserted_rating_id(): 
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM rating ORDER BY ratingid DESC LIMIT 1"
            cursor.execute(sql)
            return cursor.fetchone()['ratingid']
    finally:
        connection.close()

def verify_user_credentials(username, password):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            return cursor.fetchone()
    finally:
        connection.close()


def read_user_role(user_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT role_name FROM role WHERE userid=%s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            return result['role_name'] if result else None
    finally:
        connection.close()

def fetch_all_restaurants():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurant"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

def fetch_menu_items(restaurant_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = """SELECT menu_items.*
                     FROM menu_items
                     JOIN menu ON menu_items.menuid = menu.menuid
                     WHERE menu.restaurantid = %s"""
            cursor.execute(sql, (restaurant_id,))
            return cursor.fetchall()
    finally:
        connection.close()


def validate_user(username, password):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE username=%s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
                return user
            else:
                return None
    finally:
        connection.close()


def get_all_restaurants():
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM restaurant"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

def get_menu_items(restaurant_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = """SELECT mi.*
                FROM menuitems mi
                JOIN menu m ON m.menuid = mi.menuid
                JOIN restaurant r ON r.restaurantid = m.restaurantid
                WHERE r.restaurantid = %s"""
            cursor.execute(sql, (restaurant_id,))
            return cursor.fetchall()
    finally:
        connection.close()


def add_order_item(order_item):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO orderitems (orderid, itemid, quantity) VALUES (%s, %s, %s)"
            cursor.execute(sql, (order_item['orderid'], order_item['itemid'], order_item['quantity']))
        connection.commit()
    finally:
        connection.close()

def remove_order_item(order_item_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM orderitems WHERE detailid = %s"
            cursor.execute(sql, (order_item_id,))
        connection.commit()
    finally:
        connection.close()


def read_restaurant_by_owner_id(owner_id):
    connection = create_conn()
    print(owner_id)
    try:
        with connection.cursor() as cursor:
            sql = """SELECT r.restaurantid, r.restaurantname, r.phone, r.ownerid, 
                     a.street, a.city, a.state, a.pin 
                     FROM Restaurant r
                     JOIN RestaurantAddress a ON r.addressid = a.addressid
                     WHERE r.ownerid = %s"""
            cursor.execute(sql, (owner_id,))
            restaurant = cursor.fetchone()
    finally:
        connection.close()
    return restaurant

def get_ownerId_from_user(user_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = """SELECT ownerid
                     FROM owner
                     WHERE userid = %s"""
            cursor.execute(sql, (user_id,))
            owner = cursor.fetchone()
    finally:
        connection.close()
    return owner['ownerid']
    
def get_or_create_order_id(customerid, special_instructions=None):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            # Try to get the existing order ID for the current customer
            sql = "SELECT orderid FROM orders WHERE customerid = %s"
            cursor.execute(sql, (customerid,))
            order = cursor.fetchone()
            if order:
                order_id = order['orderid']
                # Update the special instructions for the existing order
                sql = "UPDATE orders SET specialinstructions = %s WHERE orderid = %s"
                cursor.execute(sql, (special_instructions, order_id))
                connection.commit()
                return order_id

            # If no existing order found, create a new order with an initial status and return the new order ID
            initial_status = "Received"  # Change this to a valid status for your application
            sql = "INSERT INTO orders (customerid, orderstatus, specialinstructions) VALUES (%s, %s, %s)"
            cursor.execute(sql, (customerid, initial_status, special_instructions))
            connection.commit()
            return cursor.lastrowid
    finally:
        connection.close()

def customer_exists(customerid):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT customerid FROM customer WHERE customerid = %s"
            cursor.execute(sql, (customerid,))
            return cursor.fetchone() is not None
    finally:
        connection.close()

def create_owner_user(owner_user):
    connection = create_conn()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO owner (userid) VALUES (%s)", (owner_user["userid"],))
        connection.commit()
        ownerid = cursor.lastrowid
    finally:
        cursor.close()
        connection.close()
    return ownerid


def select_random_driver():
    connection = create_conn()
    try:
        with connection.cursor(DictCursor) as cursor:
            sql = "SELECT * FROM deliverydriver"
            cursor.execute(sql)
            drivers = cursor.fetchall()
            if drivers:
                random_driver = random.choice(drivers)
                return {
                    "delivery_driver_id": random_driver["delivery_driver_id"],
                    "firstname": random_driver["firstname"],
                    "phone": random_driver["phone"]
                }
            else:
                return None
    finally:
        connection.close()


def set_driver_for_order(order_id, driver_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE orders SET delivery_driver_id = %s WHERE orderid = %s"
            cursor.execute(sql, (driver_id, order_id))
            connection.commit()
    finally:
        connection.close()


def get_driver_by_order_id(order_id):
    connection = create_conn()
    try:
        with connection.cursor(DictCursor) as cursor:
            sql = """SELECT d.delivery_driver_id, d.firstname, d.phone
                     FROM deliverydriver AS d
                     JOIN orders AS o ON d.delivery_driver_id = o.delivery_driver_id
                     WHERE o.orderid = %s"""
            cursor.execute(sql, (order_id,))
            driver = cursor.fetchone()
            if driver:
                return {
                    "delivery_driver_id": driver["delivery_driver_id"],
                    "firstname": driver["firstname"],
                    "phone": driver["phone"]
                }
            else:
                return None
    finally:
        connection.close()

def assign_driver(order_id):
    driver = select_random_driver()
    if driver:
        set_driver_for_order(order_id, driver["delivery_driver_id"])
    else:
        print("No available drivers")


def update_order_total_amount(order_id, amount):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE orders SET totalamount = totalamount + %s WHERE orderid = %s"
            cursor.execute(sql, (amount, order_id))
            connection.commit()
    finally:
        connection.close()


def get_menu_item_by_id(item_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM menuitems WHERE itemid = %s"
            cursor.execute(sql, (item_id,))
            menu_item = cursor.fetchone()
            return menu_item
    finally:
        connection.close()



def update_special_instructions(order_id, special_instructions):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE orders SET specialinstructions = %s WHERE orderid = %s"
            cursor.execute(sql, (special_instructions, order_id))
            connection.commit()
    finally:
        connection.close()


def get_order_items_by_order_id(order_id):
    conn = create_conn()
    items = []
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT itemid, quantity
                FROM orderitems
                WHERE orderid = %s
            """
            cursor.execute(sql, (order_id,))
            result = cursor.fetchall()
            if result:
                for item in result:
                    items.append({
                        'itemid': item['itemid'],
                        'quantity': item['quantity']
                    })
    finally:
        conn.close()
    return items


def get_order_items_with_prices(order_id):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            query = f"""
                SELECT oi.detailid, oi.itemid, mi.price, oi.quantity
                FROM orderitems AS oi
                JOIN menuitems AS mi ON oi.itemid = mi.itemid
                WHERE oi.orderid = %s
            """
            cursor.execute(query, (order_id,))
            result = cursor.fetchall()
            order_items_with_prices = [dict(row) for row in result]
    finally:
        connection.close()
    return order_items_with_prices


def update_order_status(order_id, new_status):
    connection = create_conn()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE orders SET orderstatus = %s WHERE orderid = %s"
            cursor.execute(sql, (new_status, order_id))
            connection.commit()
    finally:
        connection.close()