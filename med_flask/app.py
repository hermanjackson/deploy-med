import os
from twilio.rest import Client
from flask import Flask , request
from flask_cors import CORS




app = Flask(__name__)


CORS(app)




@app.route('/', methods=['POST'])
def sendSMS():
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    text_message = request.get_json()
    print(text_message)

    # def sendTXT(): 
    message = client.messages \
                    .create(
                        body=text_message["body"],
                        from_='+19193518942',
                        to="5615029869"
                    )
    # sendTXT()                    
  
    return "hello"

@app.route('/', methods=['GET'])
def hello():
    return "hello"


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)





