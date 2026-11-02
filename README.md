# Python USSD Data Purchase Simulator

A beginner-friendly Python project that simulates a USSD menu for purchasing mobile data. Users can enter a USSD code, select a mobile network, browse available data plans, choose a bundle, and confirm or cancel a simulated purchase.

> **Note:** This is an educational simulation. It does not connect to a telecom provider, process payments, deduct airtime, or purchase real data.

## Features

- USSD code validation (`*311#`, `*312#`, and `*303#`)
- SIM/network selection menu
- Glo service menu
- Daily, weekly, and monthly data plan menus
- Data bundle selection
- Purchase confirmation and cancellation
- Basic handling of invalid menu selections

## Technologies

- **Language:** Python 3
- **Interface:** Command-line / terminal

## Getting Started

### Prerequisites

Install Python 3 on your computer. You can check whether Python is available by running:

```bash
python --version
```

Depending on your system, you may need to use `python3 --version`.

### Run the project

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/python-ussd-data-simulator.git
   ```

2. Move into the project directory:

   ```bash
   cd python-ussd-data-simulator
   ```

3. Run the Python file:

   ```bash
   USSD.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 USSD.py
   ```

## How It Works

1. Enter one of the supported USSD codes.
2. Select a SIM/network option.
3. Choose a service from the menu.
4. Select **Buy Data** to view the available bundles.
5. Choose a plan category: Daily, Weekly, or Monthly.
6. Select a data bundle.
7. Confirm the purchase or cancel it.

The program displays a success message when a simulated purchase is confirmed.

## Example Menu

```text
Enter USSD *311#, *312#, or *303#:

SIM 1: GLO
SIM 2: MTN
SIM 3: Airtel

What would you like to do?
1. Voice plans
2. Buy Data
3. Check Tariff plans
4. Data Gifting
```

## Python Concepts Practised

This project provides practice with:

- `input()` and `print()` for user interaction
- Variables and strings
- Lists for storing supported USSD codes
- Conditional statements (`if`, `elif`, and `else`)
- Nested conditional logic
- Comparing user input with menu options
- Indentation and program flow
- Basic input validation

## Current Limitations

- Only the Glo data plan purchase flow is implemented.
- MTN and Airtel are displayed as network options but are not yet supported.
- Voice plans, tariff-plan details, and data gifting are placeholders.
- Only Daily, Weekly, and Monthly plan categories are implemented.
- Data purchases and balance updates are simulated; no real transaction takes place.
- The program does not yet repeat menus automatically after an action.

## Future Improvements

- Implement MTN and Airtel menu flows.
- Add the remaining plan durations.
- Add voice-plan and tariff-plan options.
- Implement data gifting.
- Use functions to make the code more modular and reusable.
- Add loops so users can perform multiple actions in one session.
- Improve input validation and error handling.
- Introduce a simulated airtime balance and transaction history.

## Project Purpose

This project was built as a practical exercise in Python programming, with a focus on conditional statements, nested logic, user input, and menu-driven applications.

## Author

**Victor**

Data Analyst | Python developer

---

If you find this project useful or have suggestions for improvement, feel free to fork the repository and contribute.
