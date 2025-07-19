from flask import Flask, render_template, request, redirect, url_for
from utils.sheet_handler import get_available_slots, save_booking
from utils.zoning import get_zone_by_postcode
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        postcode = request.form["postcode"]
        service = request.form["service"]

        zone = get_zone_by_postcode(postcode)
        duration = {
            "exterior": 1,
            "standard": 1.5,
            "full": 2.5,
            "premium": 2.5
        }.get(service, 1)

        return render_template("calendar.html", name=name, phone=phone,
                               postcode=postcode, service=service,
                               duration=duration, zone=zone,
                               slots=get_available_slots(zone, duration))
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    phone = request.form["phone"]
    postcode = request.form["postcode"]
    service = request.form["service"]
    slot = request.form["slot"]

    save_booking(name, phone, postcode, service, slot)
    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
