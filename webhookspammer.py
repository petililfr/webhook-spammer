import requests
import time

loop = "Y"
webhook = "" #enter your webhook here

text = input("Enter text to spam: ")

payload = {
    "content": f"{text}"
    }

loop = input("Start spamming? (Y/N): ").capitalize()

while loop =="Y":
    print("Sending", text, "to webhook.")
    response = requests.post(webhook, json=payload)
    print("Message sent successfully!")

else:
    print("Message failed to send!")
    time.sleep(3)
    exit()
