from flask import Flask, render_template
import requests
import json

from forms import TranslateForm
from api import get_translation
from config import ConfigClass

app = Flask(__name__)
config = ConfigClass(app)

result = json.loads(
    requests.get(
        "https://api.cognitive.microsofttranslator.com/languages?api-version=3.0"
    ).content
)["translation"]

CHOICES = [(key, result[key]["nativeName"]) for key in result]


@app.route("/", methods=["GET", "POST"])
def home():
    form = TranslateForm(lang_from="pl", lang_to="en")
    form.lang_from.choices = CHOICES
    form.lang_to.choices = CHOICES

    result = ""
    if form.validate_on_submit():
        text = form.text.data
        params = {
            "api-version": "3.0",
            "from": form.lang_from.data,
            "to": form.lang_to.data,
        }

        response = get_translation(
            config.constructed_url, config.key, config.location, params, text
        )
        result = response[0]["translations"][0]["text"]

    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=config.is_debug)
