from twilio.rest import Client

# Function to send SMS
def send_sms(phonenumber, stock_data, stock_symbol):
    # Twilio credentials (set these securely)
    twilio_sid = ''
    auth_token = ''
    from_phone_number = ''

    message = f"Stock Report for {stock_symbol}:\n"
    message += f"Latest Closing Price: {stock_data['Close'].iloc[-1]}\n"
    message += f"Moving Average: {stock_data['Moving_Avg'].iloc[-1]}\n"
    message += f"RSI: {stock_data['RSI'].iloc[-1]}\n"

    client = Client(twilio_sid, auth_token)

    try:
        sms = client.messages.create(
            body=message,
            from_=from_phone_number,
            to=phonenumber
        )
        return f"SMS sent successfully! SID: {sms.sid}"
    except Exception as e:
        raise Exception(f"Failed to send SMS: {str(e)}")
