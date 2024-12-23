from flask import Flask, request, make_response,redirect

app = Flask(__name__);

@app.route("/")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect('/home'))
    response.set_cookie('user_ip_information',user_ip_information)
    return response

@app.route('/home')
def home():
    user_ip = request.cookies.get("user_ip_information")
    return render_template('principal.html')




app.run(host='0.0.0.0', port=81, debug=True)