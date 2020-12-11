from twilio.rest import Client 
 
account_sid = 'ACd9d936be69223c796a8ab84f9a5f980c' 
auth_token = '790bc55ee9e20d0c746f1ab94cd3c40b' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12515128401', 
                              body ='para este trabajo hare este trabajo por $5000000,mi vida es hermosa mi amor',     
                              to='+2348171202603' 
                          ) 
 
print(message.sid)