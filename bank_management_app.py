import sqlite3

DATABASE = "../db/bank.db"

# Database setup
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute ("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
    """)

    conn.commit()
    conn.close()

#Bank Account Class
class BankAccount():

    def __init__(self, account_number, name , username, password, balance = 0 ):
        self.account_number = account_number
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        self.record_transaction("Deposit", amount)
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.record_transaction("Withdraw", amount)
        else:
            print("Insufficient balance!")

    def record_transaction(self, transaction_type, amount):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute("""
            INSERT INTO transaction (customer_id, transaction_type, amount ) VALUES (?, ?, ?)
        """, (self.account_number, transaction_type, amount)
        )

        conn.commit()
        conn.close()

    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute("""
            SELECT transsaction_type, amount, timpestamp 
            FROM transaction
            WHERE customer_id = ?
            OREDER BY timestamp DESC
        """, (self.account_number))

        transaction_history = c.fetchall()
        conn.commit()
        conn.close()
        return transaction_history
    
# Bank Application class
class BankApplication():
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, name, username, password):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute("""
            INSERT INTO customers (name, username, password)
            VALUES (?, ?, ?)
        """, (name, username, password))

        account_number = c.lastrowid

        conn.commit()
        conn.close()

        account = BankAccount(account_number, name, username, password)
        self.accounts[account_number] = account

    def login(self, username, password):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("""
            SELECT id, name, balance
            FROM customers
            WHERE username = ? and password = ?
        """, (username, password))
        account_data = c.fetchone()
        conn.commit()
        conn.close()
        if account_data:
            account_number, name, balance = account_data
            account = BankAccount(account_number, name, username, password, balance)
            self.accounts[account_number] = account
            return account
        else:
            return None
    
    

    def get_account(self, account_number):
        return self.accounts.get(account_number) 
    
        
if __name__ == "__main__":
    initialize_database()
    customer_acc1 = BankApplication()
    customer_acc2 = BankApplication()
    customer_acc1.create_account("Chetan Vadingekar", "chetan", "pass1")
    customer_acc2.create_account("Ishan Sharma", "ishan", "pass2")
    
    
    