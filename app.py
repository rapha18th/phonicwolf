from flask import Flask, request, render_template
import Bot
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def chat():
    flag = True
    while (flag == True):
        user_response = request.args.get('msg')

        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                response = "You are welcome.."
                return response
            else:
                if (Bot.greeting(user_response) != None):
                    response = Bot.greeting(user_response)
                    return response
                else:

                    response = Bot.response(user_response)
                    Bot.sent_tokens.remove(user_response)
                    return response
        else:
            flag = False
            response = "Bye! take care, and if you want to say anything more you can leave a voice note"
            return response

if __name__ == "__main__":
    app.run()
