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
- Keep in mind apps 3 and 4 are in one file, so one of the two has to be deleted.
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

## 🎬 Demo Videos

Experience HexaBit in action! Watch the videos below to see each app and feature demonstrated on real hardware.

| Title | Description | Watch |
|-------|-------------|-------|
| 🧭 **Introduction** | Overview of the HexaBit project and its capabilities. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/a8d303478983ad42c770b58a8853164f75be95bb_introduction.mp4) |
| ⏱️ **Stopwatch** | See the binary stopwatch counting seconds. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/90e5a23981201ba161b6cd162c83b12a36da6e44_stopwatch.mp4) |
| 🔢 **Counter with Buttons** | Increment/decrement the counter using button input. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/66531f7de94bc00e98d94bc6f1dca76859121da3_counter.mp4) |
| ⏲️ **Timers (Part 1)** | Demonstrates the 1-minute and 1-hour timer logic. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/43e7cd0f3bc0b1ed154fc84b6dc3d3625192933d_timers_part1.mp4) |
| ⏲️ **Timers (Part 2)** | Continuation of timer apps and extra behavior. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b4bd8ca74b0d6686c3fbc84d6f72c52944103967_timer_part2.mp4) |
| 🕒 **Clock** | Real-time binary clock display using LEDs. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/266be22194b9b4084d841a01661ef5349219d142_clock.mp4) |
| 💡 **Ideas for Expansion** | Explore creative future possibilities with HexaBit. | [Watch Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/31a12bb31827b07beabea2949b3585878a92547f_ideas_for_expansion.mp4) |

> 🎥 Thanks to [@George Vazakas](https://github.com/) for capturing the demos!

---

## Disclaimer!

This readme file is a product of AI use.
