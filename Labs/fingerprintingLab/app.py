from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    print("\n========== NEW VISIT ==========")

    print("IP address :", request.remote_addr)
    print("HTTP method :", request.method)

    print("User-Agent :", request.headers.get("User-Agent"))
    print("Accept-Language :", request.headers.get("Accept-Language"))
    print("Accept :", request.headers.get("Accept"))
    print("Accept-Encoding :", request.headers.get("Accept-Encoding"))
    print("Sec-CH-UA :", request.headers.get("Sec-CH-UA"))
    print("Sec-CH-UA-Platform :", request.headers.get("Sec-CH-UA-Platform"))
    print("Sec-Fetch-Site :", request.headers.get("Sec-Fetch-Site"))
    print("Upgrade-Insecure-Requests :", request.headers.get("Upgrade-Insecure-Requests"))	
    print("================================\n")

    return render_template("index.html")
@app.route("/collect", methods=["POST"])
def collect():
    data = request.get_json()

    print("\n========== ACTIVE FEATURES ==========")
    print("Language :", data.get("language"))
    print("CPU cores :", data.get("cpuCores"))
    print("Screen resolution :", data.get("screenResolution"))
    print("Color depth :", data.get("colorDepth"))
    print("Window size :", data.get("windowSize"))
    print("Time zone :", data.get("timeZone"))
    print("Referrer :", data.get("referrer"))
    print("=====================================\n")

    return jsonify({"status": "received"})
@app.route("/collect-typing", methods=["POST"])
def collect_typing():
    data = request.get_json()

    print("\n========== TYPING BEHAVIOUR ==========")
    print("Total time :", data.get("totalTime"), "seconds")
    print("Typing speed :", data.get("typingSpeed"), "characters/second")
    print("Corrections :", data.get("corrections"))
    print("======================================\n")

    return jsonify({"status": "received"})
@app.route("/collect-fingerprint", methods=["POST"])
def collect_fingerprint():
    data = request.get_json()

    print("\n========== BROWSER FINGERPRINT ==========")
    print("Fingerprint :", data.get("fingerprint"))
    print("=========================================\n")

    return jsonify({"status": "received"})
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

