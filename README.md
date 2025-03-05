# Coffee Machine Program

This is a Python-based coffee machine simulator that allows users to order various coffee drinks, manages resources, and handles payments.

## Features

- Order coffee drinks (latte, espresso, cappuccino)
- Check resource availability before making drinks
- Process coin payments (quarters, dimes, nickels, pennies)
- Track profit and provide change
- Generate reports on remaining resources and profit

## Project Structure

The project consists of four main Python files:
- `main.py`: The main program that ties everything together
- `menu.py`: Contains `Menu` and `MenuItem` classes to manage coffee offerings
- `coffee_maker.py`: Manages coffee machine resources and drink preparation
- `money_machine.py`: Handles payment processing and profit tracking

## How to Use

1. Run the program:
   ```
   python main.py
   ```

2. Enter your drink choice when prompted, or use special commands:
   - Type a drink name (e.g., "latte", "espresso", "cappuccino")
   - Type "report" to see current resources and profit
   - Type "off" to exit the program

3. If your chosen drink is available, follow the prompts to insert coins

## Classes

- `MenuItem`: Models individual drinks with their ingredients and cost
- `Menu`: Manages the available drink options
- `CoffeeMaker`: Tracks resources and handles coffee preparation
- `MoneyMachine`: Processes payments and manages profit accounting

## Requirements

- Python 3.x

This project demonstrates object-oriented programming principles including class design, encapsulation, and object interaction.