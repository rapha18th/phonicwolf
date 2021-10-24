from flask import Flask, request, render_template
import Bot
import wikipedia as wk
import wolframalpha

APIkey = "R62U64-JYYVGAVHHU"
wolf = wolframalpha.Client(APIkey)


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
                    try:
                        res = wolf.query(user_response)
                        response = next(res.results).text
                    except:
                        try:
                          response = wk.summary(user_response, sentences = 3)
                        except:
                          response = "May you try to refine your query, I am still learning please be patient with me"

                    return response
        else:
            flag = False
            response = "Good Bye! "
            return response

if __name__ == "__main__":
    app.run()
