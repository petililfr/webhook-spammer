import requests
import time

loop = "Y"
webhook = "https://discord.com/api/webhooks/1165572508636938330/TwRfVBqSTcacIv-qxS0lfKifnr9rDY62_jaeFPkEzGSbMIlPVeNJhCGz15BO6Tcv5aBM"

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
