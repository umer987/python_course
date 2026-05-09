import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

store = [
    {'item': 'rice', 'price': 350, 'quantity': 1000},
    {'item': 'flour', 'price': 120, 'quantity': 1000},
    {'item': 'shampoo', 'price': 1200, 'quantity': 1000},
    {'item': 'milk', 'price': 240, 'quantity': 1000},
    {'item': 'egg', 'price': 25, 'quantity': 1000},
    {'item': 'surf', 'price': 300, 'quantity': 1000},
    {'item': 'biscuit', 'price': 50, 'quantity': 1000},
    {'item': 'bread', 'price': 260, 'quantity': 1000},
    {'item': 'sugar', 'price': 55, 'quantity': 1200},
    {'item': 'salt', 'price': 20, 'quantity': 2000},
    {'item': 'cooking oil', 'price': 180, 'quantity': 800},
    {'item': 'tea', 'price': 220, 'quantity': 600},
    {'item': 'coffee', 'price': 350, 'quantity': 400},
    {'item': 'soap', 'price': 45, 'quantity': 1500},
    {'item': 'toothpaste', 'price': 85, 'quantity': 700},
    {'item': 'butter', 'price': 65, 'quantity': 500},
    {'item': 'cheese', 'price': 280, 'quantity': 300},
    {'item': 'yogurt', 'price': 40, 'quantity': 400},
    {'item': 'chicken', 'price': 220, 'quantity': 600},
    {'item': 'mutton', 'price': 650, 'quantity': 200},
    {'item': 'fish', 'price': 300, 'quantity': 350},
    {'item': 'potato', 'price': 30, 'quantity': 3000},
    {'item': 'onion', 'price': 35, 'quantity': 2800},
    {'item': 'tomato', 'price': 40, 'quantity': 2500},
    {'item': 'carrot', 'price': 45, 'quantity': 1800},
    {'item': 'cabbage', 'price': 30, 'quantity': 1500},
    {'item': 'cauliflower', 'price': 35, 'quantity': 1200},
    {'item': 'apple', 'price': 180, 'quantity': 800},
    {'item': 'banana', 'price': 60, 'quantity': 2000},
    {'item': 'orange', 'price': 120, 'quantity': 900},
    {'item': 'grapes', 'price': 100, 'quantity': 400},
    {'item': 'mango', 'price': 150, 'quantity': 600},
    {'item': 'coke', 'price': 45, 'quantity': 1500},
    {'item': 'pepsi', 'price': 45, 'quantity': 1400},
    {'item': 'juice', 'price': 120, 'quantity': 700},
    {'item': 'mineral water', 'price': 20, 'quantity': 2500},
    {'item': 'chips', 'price': 30, 'quantity': 1800},
    {'item': 'chocolate', 'price': 60, 'quantity': 1200},
    {'item': 'cake', 'price': 350, 'quantity': 200},
    {'item': 'pasta', 'price': 95, 'quantity': 500},
    {'item': 'noodles', 'price': 55, 'quantity': 800},
    {'item': 'tomato sauce', 'price': 110, 'quantity': 600},
    {'item': 'ketchup', 'price': 80, 'quantity': 700},
    {'item': 'mayonnaise', 'price': 140, 'quantity': 400},
    {'item': 'pickle', 'price': 75, 'quantity': 500},
    {'item': 'honey', 'price': 280, 'quantity': 250},
    {'item': 'jam', 'price': 120, 'quantity': 450},
    {'item': 'peanut butter', 'price': 250, 'quantity': 300},
    {'item': 'cereal', 'price': 320, 'quantity': 350},
    {'item': 'oats', 'price': 180, 'quantity': 400},
    {'item': 'cornflakes', 'price': 220, 'quantity': 380},
    {'item': 'detergent', 'price': 400, 'quantity': 500},
    {'item': 'bleach', 'price': 90, 'quantity': 600},
    {'item': 'dish soap', 'price': 60, 'quantity': 1000},
    {'item': 'sponge', 'price': 25, 'quantity': 1200},
    {'item': 'trash bag', 'price': 150, 'quantity': 700},
    {'item': 'aluminum foil', 'price': 70, 'quantity': 450},
    {'item': 'plastic wrap', 'price': 55, 'quantity': 500},
    {'item': 'battery AA', 'price': 180, 'quantity': 800},
    {'item': 'light bulb', 'price': 95, 'quantity': 600},
    {'item': 'extension cord', 'price': 350, 'quantity': 150},
    {'item': 'adapter', 'price': 220, 'quantity': 200},
    {'item': 'usb cable', 'price': 180, 'quantity': 300},
    {'item': 'notebook', 'price': 45, 'quantity': 1000},
    {'item': 'pen', 'price': 15, 'quantity': 3000},
    {'item': 'pencil', 'price': 10, 'quantity': 2500},
    {'item': 'eraser', 'price': 8, 'quantity': 2000},
    {'item': 'sharpener', 'price': 12, 'quantity': 1500},
    {'item': 'marker', 'price': 40, 'quantity': 800},
    {'item': 'highlighter', 'price': 35, 'quantity': 700},
    {'item': 'glue stick', 'price': 30, 'quantity': 600},
    {'item': 'scissors', 'price': 90, 'quantity': 400},
    {'item': 'tape', 'price': 45, 'quantity': 500},
    {'item': 'stapler', 'price': 150, 'quantity': 250},
    {'item': 'printer paper', 'price': 180, 'quantity': 400},
    {'item': 'towel', 'price': 250, 'quantity': 300},
    {'item': 'napkin', 'price': 40, 'quantity': 1200},
    {'item': 'tissue box', 'price': 65, 'quantity': 900},
    {'item': 'hand wash', 'price': 120, 'quantity': 600},
    {'item': 'body lotion', 'price': 180, 'quantity': 350},
    {'item': 'face cream', 'price': 220, 'quantity': 250},
    {'item': 'deodorant', 'price': 190, 'quantity': 400},
    {'item': 'perfume', 'price': 450, 'quantity': 150},
    {'item': 'hair oil', 'price': 160, 'quantity': 300},
    {'item': 'conditioner', 'price': 210, 'quantity': 280},
    {'item': 'face wash', 'price': 150, 'quantity': 320},
    {'item': 'shaving cream', 'price': 130, 'quantity': 350},
    {'item': 'razor', 'price': 80, 'quantity': 450},
    {'item': 'comb', 'price': 30, 'quantity': 500},
    {'item': 'hair brush', 'price': 55, 'quantity': 400},
    {'item': 'toothbrush', 'price': 45, 'quantity': 800},
    {'item': 'mouthwash', 'price': 160, 'quantity': 250},
    {'item': 'floss', 'price': 70, 'quantity': 350},
    {'item': 'baby diaper', 'price': 450, 'quantity': 400},
    {'item': 'baby oil', 'price': 200, 'quantity': 250},
    {'item': 'baby powder', 'price': 150, 'quantity': 300},
    {'item': 'pet food', 'price': 380, 'quantity': 200},
]

cart = []
status_msg = "Welcome to US Store! Quality is our priority."
WIDTH = 130  # Fixed width for the entire UI

def show_ui():
    clear_screen()
    # 1. Header Centering
    print("=" * WIDTH)
    
    # Updated name_lines to include 'R'
    name_lines = [
        " _   _   _____   _____ _____  ____  _____  ______ ",
        "| | | |/ ____| / ____|_   _|/ __ \|  __ \|  ____|",
        "| | | | (___   | (___   | | | |  | | |__) | |__   ",
        "| | | |\___ \  \___ \  | | | |  | |  _  /|  __|  ",
        "| |_| |____) | ____) | | | | |__| | | \ \| |____ ",
        " \___/|_____/ |_____/  |_|  \____/|_|  \_\______|"
    ]
        
    for line in name_lines:
        print(line.center(WIDTH))
    
    print("-" * WIDTH)
    print(f"--- OFFICIAL PRODUCT CATALOG ---".center(WIDTH))
    print("-" * WIDTH)

    # 2. Multi-column logic (15 rows)
    rows_per_page = 15
    num_items = len(store)
    
    for row in range(rows_per_page):
        line = ""
        for col_start in range(0, num_items, rows_per_page):
            idx = col_start + row
            if idx < num_items:
                p = store[idx]
                # Each column block is roughly 25-30 chars wide
                item_label = f"[{idx+1:02}] {p['item'].capitalize()[:12]:<12} Rs.{p['price']:<4}"
                line += item_label + " | "
        print(line.center(WIDTH))

    # 3. Footer
    print("=" * WIDTH)
    print(status_msg.center(WIDTH))
    print(f"Items in Cart: {len(cart)} | Running Total: Rs. {sum(i['total'] for i in cart)}".center(WIDTH))
    print("=" * WIDTH)

# Main Execution
while True:
    show_ui()
    choice = input("\nProduct name likhein (ya 'q' press karein checkout ke liye): ").lower().strip()
    
    if choice == 'q':
        break
    
    item = next((p for p in store if p['item'] == choice), None)
            
    if item:
        try:
            print(f"\n🛒 Selected: {choice.upper()} | Stock: {item['quantity']}")
            q = int(input("Quantity kitni chahiye? "))
            
            if q <= 0:
                status_msg = "⚠️ Quantity 0 se zyada honi chahiye."
            elif q <= item['quantity']:
                cost = item['price'] * q
                item['quantity'] -= q
                cart.append({"item": choice, "price": item['price'], "quantity": q, "total": cost})
                status_msg = f"✅ Success! {q} {choice} cart mein save ho gaye."
            else:
                status_msg = f"Out Of Stock! Only {item['quantity']} hain."
        except ValueError:
            status_msg = " Wrong Entry! Enter Only  Number For Quanttiy."
    else:
        status_msg = f"Sorry, '{choice}' Is Not Avalable."

# Final Receipt
clear_screen()
if cart:
    receipt_w = 50
    print("\n" + "╔" + "═"*(receipt_w-2) + "╗")
    print(f"║{'US STORE OFFICIAL RECEIPT':^48}║")
    print("╠" + "═"*(receipt_w-2) + "╣")
    print(f"║ {'ITEM':<18} {'QTY':<5} {'RATE':<8} {'TOTAL':<11}║")
    print("╟" + "─"*(receipt_w-2) + "╢")
    
    total = 0
    for c in cart:
        total += c['total']
        print(f"║ {c['item'].capitalize()[:18]:<18} {c['quantity']:<5} {c['price']:<8} {c['total']:<11}║")
    
    print("╠" + "═"*(receipt_w-2) + "╣")
    print(f"║ {'NET TOTAL:':<33} Rs. {total:<8}║")
    print("╚" + "═"*(receipt_w-2) + "╝")
    print(f"{'US STORE: Your Favoriate Palace!':^50}\n")
else:
    print("\nThanks For Visiting! Khuda Hafiz.\n")