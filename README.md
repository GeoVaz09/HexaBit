# 🔷 HexaBit - 6-Bit LED MicroApp System

**HexaBit** is a compact Raspberry Pi Pico project utilizing **6 LEDs** (bits) to run various minimal yet functional applications. Designed to be simple, hackable, and educational, HexaBit demonstrates how much you can achieve with just a few GPIO pins and some clever coding. 

Whether you're learning embedded systems or just want a cool multi-functional LED device, HexaBit is for you!

---

## 🚀 Features

- Built on **Raspberry Pi Pico**
- Uses **6 LEDs** for binary output
- Expandable with buttons, buzzers, etc.
- Written in **MicroPython**
- Modular app system for different use cases

---

## 🔧 Hardware Requirements

- Raspberry Pi Pico
- 6 LEDs (any color)
- 6 Resistors (e.g., 220Ω)
- Breadboard or PCB
- Push buttons for user input

---

## 🧠 Apps for HexaBit

| App # | Name                  | Description                                 |
|-------|-----------------------|---------------------------------------------|
| 1️⃣   | **Stopwatch**          | Binary stopwatch that counts seconds        |
| 2️⃣   | **Counter**            | Increment/decrement using input buttons     |
| 3️⃣   | **1-Minute Timer**     | Countdown from 60 seconds (binary format)   |
| 4️⃣   | **1-Hour Timer**       | Countdown from 3600 seconds                 |
| 5️⃣   | **Clock**              | Real-time binary clock (HH:MM approx.)   |

- Each app is loaded separately via MicroPython script. 
- Keep in mind apps 3&4 are in one file,so one of the two has to be deleted.
- I have videos explaining the apps (Recomandation: see the videos in the order mentioned above)
---

## 🛠️ Setup Instructions

1. Connect your Raspberry Pi Pico to your PC.
2. Flash it with MicroPython (if not already done).
3. Clone this repo and upload files using [Thonny](https://thonny.org/).
4. Modify `main.py` to choose the app you want to run.
5. Power up and enjoy your blinking bits!

---

## 💡 Ideas for Expansion

- Add buzzer feedback for timers
- Add rotary encoder for input
- Use RGB LEDs for extra state feedback
- Add app switcher via long-press button logic

---

## Disclaimer!

This readme file is a product of AI use.
