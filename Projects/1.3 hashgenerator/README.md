# Exercise 1.3 - Hash Generator Application

A containerized Node.js application that generates a random hash string upon startup and continues to log it to the console alongside a current timestamp every 5 seconds.

---

## 🚀 Application Logic

The script initializes a random unique identifier when the container boots up, and uses an infinite loop to log messages dynamically:

* **Frequency:** Every 5,000 milliseconds (5 seconds)
* **Output Format:** `[YYYY-MM-DDTHH:mm:ss.sssZ] - <random-hash-string>`

---

## 🛠 Local Development & Testing

### 1. Run the script locally
Make sure you have Node.js installed, then run:
```bash
node index.js
