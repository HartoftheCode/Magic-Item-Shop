# Magic Item Shop – Fantasy Inventory & Trading System

A fully interactive, text-based shop simulation built in Python. Designed as a fantasy-themed game component, the **Magic Item Shop** allows players to buy and sell magical items with color-coded rarity, dynamic pricing, and a personal inventory system. Built entirely on mobile using **Pydroid 3**, this project showcases foundational Python skills including object-oriented programming, control flow, and user interaction.

---

## Features

- **Text-Based Interface**: Fully interactive shop menu via command line.
- **Color-Coded Item Rarity**:
  - **Common** – White
  - **Rare** – Blue
  - **Epic** – Purple
  - **Legendary** – Gold
- **Inventory System**:
  - Track your gold and items.
  - Items stack in inventory.
  - Clear feedback on actions.
- **Purchase & Buyback Logic**:
  - Buy items with gold.
  - Sell items back at a reduced price based on rarity:
    - Common: 40%
    - Rare: 50%
    - Epic: 60%
    - Legendary: 75%
- **Input Validation & Error Handling**:
  - Can't buy more than you can afford.
  - Can't sell more than you own.
  - Words wrap naturally to avoid broken text.
- **Built for Mobile**: Entirely written using [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3), a Python IDE for Android.

---

## Screenshots

> *(Add screenshots here of the menu, inventory, and color-coded items if available)*
> ![Screenshot_20250514_235840_Pydroid 3](https://github.com/user-attachments/assets/255940a5-c844-4a51-8890-0b905d23c55e)


![Screenshot_20250514_235813_Pydroid 3](https://github.com/user-attachments/assets/1367ed0a-f5ad-4958-90c2-c3fcdb408ca7)

![Screenshot_20250514_235912_Pydroid 3](https://github.com/user-attachments/assets/c4109a87-328e-4ea5-beea-a39689cbcf56)

![Screenshot_20250515_000021_Pydroid 3](https://github.com/user-attachments/assets/0e409a10-865a-47fb-8029-4ff85b4ec4a6)

![Screenshot_20250515_000039_Pydroid 3](https://github.com/user-attachments/assets/1431f220-cac4-40e9-9eb1-3530c4b54e28)


---

## Getting Started

### Prerequisites

Install `colorama` (for colored text output):
```bash
pip install colorama
