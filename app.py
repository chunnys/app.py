from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None  # Initialize result
    if request.method == "POST":
        no1 = request.form["no1"].strip().upper()  # Normalize input
        no2 = request.form["no2"].strip().upper()  # Normalize input

        # Convert K and M to numeric values
        try:
            no1_float = convert_to_float(no1)
            no2_float = convert_to_float(no2)

            # Check for 7 digits after the decimal point
            if ('.' in no1 and len(no1.split('.')[1]) > 7) or ('.' in no2 and len(no2.split('.')[1]) > 7):
                result = "ตัวเลขต้องมีหลักหลังจุดทศนิยมไม่เกิน 7 หลัก."
            else:
                result = no1_float + no2_float
                result = f"{result:.10f}"  # Format result to show up to 10 decimal places
                
        except ValueError:
            result = "กรุณาใส่ตัวเลขที่ถูกต้อง."

    return render_template("index.html", result=result)

def convert_to_float(value):
    if value.endswith('K'):
        return float(value[:-1]) * 1_000
    elif value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    else:
        return float(value)

if __name__ == "__main__":
    app.run(debug=True)
