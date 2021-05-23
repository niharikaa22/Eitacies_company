from flask import Flask
app = Flask(__name__)

@app.route("/home/<name>")


def hello(name):
	return "hello %s!" % name





@app.route("/id/<int:nid>")

def n_id(nid):
	return "id : %d" % nid
	
if __name__ == "__main__":
	app.run(debug = True)