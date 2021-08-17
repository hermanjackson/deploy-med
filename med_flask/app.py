import os
from twilio.rest import Client
from flask import Flask , request
from flask_cors import CORS, cross_origin




app = Flask(__name__, static_folder='medical-app/build', static_url_path="/api")


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

@app.route('/api', methods=['GET'])
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')




if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)





