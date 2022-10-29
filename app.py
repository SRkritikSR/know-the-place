from flask import Flask, render_template

app = Flask(__name__)
##Name the folder containing html as templates not template as it creates some problems.

@app.route("/")
def Hello_World():
  return render_template('index.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
