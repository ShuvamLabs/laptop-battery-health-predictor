from flask import Flask, render_template, request
from src.predict import predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    pred = None

    if request.method == "POST":

        input_data = {
            "Battery Age": float(request.form["battery_age"]),
            "Daily Usage Hours": float(request.form["daily_usage_hours"]),
            "Gaming User": int(request.form["gaming_user"]),
            "Cycle Count": float(request.form["cycle_count"]),
            "CPU Usage": float(request.form["cpu_usage"]),
            "GPU Usage": float(request.form["gpu_usage"]),
            "Power Consumption": float(request.form["power_consumption"]),
            "Average Temperature": float(request.form["average_temperature"])
        }

        pred = predict(input_data)

    return render_template(
        "index.html",
        prediction=pred
    )


if __name__ == "__main__":
    app.run(debug=True)