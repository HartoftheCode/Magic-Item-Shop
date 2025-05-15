from colorama import Fore, Style, init
init(autoreset=True)

# Define color mappings
RARITY_COLORS = {
    "Common": Fore.WHITE,
    "Rare": Fore.BLUE,
    "Epic": Fore.MAGENTA,
    "Legendary": Fore.YELLOW
}

class Item:
    def __init__(self, name, price, description, rarity, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.rarity = rarity
        self.quantity = quantity

class Shop:
    inventory = [
        Item("Potion of Healing", 10, "Restores health.", "Common", 7),
        Item("Invisibility Cloak", 50, "Makes you invisible for a short time.", "Rare", 2),
        Item("Fire Sword", 75, "Deals extra fire damage.", "Epic", 1),
        Item("Ring of Teleportation", 100, "Teleports you to a safe location.", "Legendary", 1)
    ]

    @classmethod
    def show_items(cls):
        print("\n--- Shop Inventory ---")
        for item in cls.inventory:
            color = RARITY_COLORS[item.rarity]
            print(color + f"{item.name} - {item.price} gold (Qty: {item.quantity}) Rarity: {item.rarity}")

    @staticmethod
    def item_details(item_name):
        for item in Shop.inventory:
            if item.name.lower() == item_name.lower():
                color = RARITY_COLORS[item.rarity]
                print(color + f"\n--- {item.name} ---")
                print(color + f"Price: {item.price} gold")
                print(color + f"Description: {item.description}")
                print(color + f"Rarity: {item.rarity}")
                print(color + f"Quantity in stock: {item.quantity}")
                return
        print("Item not found.")

    def purchase_item(self, player, item_name, amount):
        for item in Shop.inventory:
            if item.name.lower() == item_name.lower():
                if item.quantity <= 0:
                    print(f"{item.name} is out of stock.")
                    return
                if item.quantity < amount:
                    print(f"Not enough stock. Only {item.quantity} available.")
                    return
                total_price = item.price * amount
                if player.gold < total_price:
                    print(f"Not enough gold. You need {total_price}, but have {player.gold}.")
                    return
                item.quantity -= amount
                player.gold -= total_price
                for _ in range(amount):
                    purchased_item = Item(item.name, item.price, item.description, item.rarity, 1)
                    player.inventory.append(purchased_item)
                color = RARITY_COLORS[item.rarity]
                print(color + f"You bought {amount} x {item.name} for {total_price} gold!")
                return
        print("Item not found.")

    def sell_item(self, player, item_name, amount):
        matched_items = [i for i in player.inventory if i.name.lower() == item_name.lower()]
        if not matched_items:
            print("You don't have that item.")
            return

        item = matched_items[0]
        if len(matched_items) < amount:
            print("You don't have that many!")
            return

        rarity = item.rarity
        percent = {"Common": 0.4, "Rare": 0.5, "Epic": 0.6, "Legendary": 0.75}[rarity]
        sell_price = int(item.price * percent) * amount
        player.gold += sell_price

        for _ in range(amount):
            player.inventory.remove(item)

        color = RARITY_COLORS[rarity]
        print(color + f"You sold {amount} x {item.name} for {sell_price} gold.")

class Player:
    def __init__(self, name, gold=100):
        self.name = name
        self.gold = gold
        self.inventory = []

    def show_inventory(self):
        print("\n--- Your Inventory ---")
        print(f"Gold: {self.gold}")
        if not self.inventory:
            print("Empty.")
            return

        item_counts = {}
        for item in self.inventory:
            key = (item.name, item.rarity)
            item_counts[key] = item_counts.get(key, 0) + 1

        for (name, rarity), count in item_counts.items():
            color = RARITY_COLORS[rarity]
            print(color + f"{name} ({rarity}) x{count}")

def main():
    print("Welcome to the Magic Item Shop!")
    name = input("Enter your name: ")
    player = Player(name)
    shop = Shop()

    while True:
        print("\nWhat would you like to do?")
        print("1. View items")
        print("2. Inspect item")
        print("3. Buy item")
        print("4. Sell item")
        print("5. View inventory")
        print("6. Exit")
        choice = input("Choose an option (1–6): ")

        if choice == "1":
            Shop.show_items()
        elif choice == "2":
            item_name = input("Enter item name: ")
            Shop.item_details(item_name)
        elif choice == "3":
            item_name = input("Enter item name to buy: ")
            amount = input("How many would you like to buy? ")
            if amount.isdigit():
                shop.purchase_item(player, item_name, int(amount))
            else:
                print("Invalid amount.")
        elif choice == "4":
            item_name = input("Enter item name to sell: ")
            amount = input("How many would you like to sell? ")
            if amount.isdigit():
                shop.sell_item(player, item_name, int(amount))
            else:
                print("Invalid amount.")
        elif choice == "5":
            player.show_inventory()
        elif choice == "6":
            print("Thanks for visiting!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()