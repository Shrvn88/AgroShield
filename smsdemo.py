from twilio.rest import Client

def smsalert(n,p):
    SID = 'AC89cfd1fa1d4f0a6694ced11146a5c2ef'
    AUTH_TOKEN = 'b94f026feb977118d3bf622c7bf9dcaf'
    img_url = "https://agroshield-aws.s3.ap-south-1.amazonaws.com/" + p

    cl = Client(SID, AUTH_TOKEN)

    cl.messages.create(body=f'Warning! {n} is detected in farm \nlink:{img_url}', from_='+12406967592', to='+917770063446')
    
