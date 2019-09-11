from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "f5b47ca7f37d37eab589b2ec1425211c53b373b7f8cec2a4e64ca653b49ee40b"
africastalking.initialize(username, api_key)

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId",None)
    service_code = request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    print(phone_number)
    text = request.values.get("text","default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    if text == "":
        response = "CON What would you like to do?\n"
        response += "1. Check account details\n"
        response += "2. Check phone number\n"
        response += "3. Send me a message"

    elif text == "1":
        response = "CON What would you like to check on your account?\n"
        response += "1. Account number"
        response += "2. Account balance"

    elif text == "2":
        response = "END Your phone number is {}".format(phone_number)

    elif text == "3":
        try:
            sms_response = sms.send("Thank you for your response", sms_phone_number)
            print(sms_response)
        except Exception as e:
            print(f"Licio, we have a problem: {e}")

    elif text == "1*1":
        account_number = "1243324376742"
        response = "END Your account number is {}".format(account_number)

    elif text == "1*2":
        account_balance = "100,000"
        response = "END Your account balance is KES {}".format(account_balance)

    else:
        response = "END Invalid input. Try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))                                        