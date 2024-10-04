from twilio.rest import Client

def whatnoti(n, p):
    account_sid = 'AC89cfd1fa1d4f0a6694ced11146a5c2ef'
    auth_token = 'b94f026feb977118d3bf622c7bf9dcaf'
    client = Client(account_sid, auth_token)
    img_url = "https://agroshield-aws.s3.ap-south-1.amazonaws.com/" + p
    print(img_url)

    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Warning! {n} is detected in farm \nlink:{img_url}',
            to='whatsapp:+917770063446',
        )
        print(f"Twilio API response: {message}")
    except Exception as e:
        print(f"Error sending Twilio message: {e}")


