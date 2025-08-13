\# 📦 Amazon Price Tracker with WhatsApp Alerts



This Python script checks the price of a product on Amazon and sends you a WhatsApp message via \*\*CallMeBot\*\* when the price drops below a preset budget.



---



\## 🚀 Features

\- Tracks \*\*Amazon product title \& price\*\* in real time

\- Sends a \*\*WhatsApp alert\*\* when the price is at or below the budget

\- Simple setup — just fill in your `phone` and `apikey` in `settings.json`

\- Runs automatically at the interval you set



---



\## 📂 Project Files

.

├── main.py # Main Python script

├── settings.json # Configuration file (only edit phone \& apikey)

├── requirements.txt # Python dependencies

└── README.md # Documentation

yaml



---



\## ⚙️ Installation



1\. \*\*Download or clone\*\* this repository.

2\. Install the required packages from `requirements.txt`:

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

&nbsp;   ```

3\. 

Edit the settings.json file:

json

{

&nbsp; "url": "https://www.amazon.de/dp/B0EXAMPLE",

&nbsp; "budget": 100.00,

&nbsp; "apikey": "YOUR\_CALLMEBOT\_API\_KEY",

&nbsp; "phone": "49123456789",

&nbsp; "time\_wait": 3600

}

\- Only apikey and phone must be filled in by the user.

\- The rest is already set but can be changed.

&nbsp;

▶️ Usage

Run the script:

bash```

python main.py

```

It will:

1\. 

Check the Amazon product’s current price

2\. 

Compare it to the budget

3\. 

Send you a WhatsApp message if the price is low enough

4\. 

Wait and repeat at the set interval (time\_wait in seconds)

&nbsp;

📌 Example Output

checking price...

product is 125.99. that's too much. retrying in 3600 seconds

checking price...

price alert! Example Product is now 99.99! buy at: https://www.amazon.de/dp/B0EXAMPLE

alert sent! stopping...

&nbsp;

⚠️ Notes

\- CallMeBot Setup:

You must have an API key from CallMeBot WhatsApp API and allow messages from their number.

\- Amazon HTML changes may break the scraper — adjust selectors if needed.

\- Use a reasonable time\_wait to avoid being blocked by Amazon.

