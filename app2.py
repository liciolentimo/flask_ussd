from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "1573ff5333f9ebd4ee4d79c0cf7195911b6e97e2379094cc1509051cd13fae74"
africastalking.initialize(username, api_key)
sms = africastalking.SMS 

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    if text == "":
        response = "CON Welcome to FutureKids. I am\n"
        response += "1. Male\n"
        response += "2. Female\n"
        response += "3. Other"

    elif text == "1":
        response = "CON What would you like to learn about?\n"
        response += "1. Consent"
        response += "2. Sexual abuse"
        response += "3. STDs"
        response += "4. Report abuse"
        response += "5. Contraception"
        response += "6. Early marriage"
        response += "0. Back"

    elif text == "2":
        response = "CON What would you like to learn about?\n"
        response += "1. Consent"
        response += "2. Sexual abuse"
        response += "3. STDs"
        response += "4. Report abuse"
        response += "5. Contraception"
        response += "6. Menstrual health"
        response += "7. Early marriage"
        response += "8. More"
        response += "0. Back"

    elif text == "3":
        response = "CON What would you like to learn about?\n"
        response += "1. Gender and Identity"
        response += "2. Sexual abuse"
        response += "3. STDs"
        response += "4. Consent"
        response += "5. Report abuse"
        response += "6. Contraception"
        response += "0. Back"

    elif text == "1*1":
        response = "Work in progress!"

    elif text == "2*1":
        response = "Work in progress!"

    elif text == "3*1":
        response = "Work in progress!"

    else:
        response = "END Invalid input. Try again."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))