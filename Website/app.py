from flask import Flask, request, render_template
from query_llm import query_llm, query, QA_LLM

app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            answer = query(QA_LLM, question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
