from flask import Flask, request

app = Flask(__name__)

events = []


@app.route("/collect")
def collect():
    analytics_id = request.args.get("id", "unknown")
    publisher = request.args.get("publisher", "unknown")
    page = request.args.get("page", "unknown")

    event = {
        "id": analytics_id,
        "publisher": publisher,
        "page": page
    }

    events.append(event)

    print("\n--- ANALYTICS EVENT ---")
    print("Identifier:", analytics_id)
    print("Publisher:", publisher)
    print("Page:", page)

    print("\n--- COLLECTED PROFILES ---")
    for event in events:
        print(
            event["id"],
            "|",
            event["publisher"],
            "|",
            event["page"]
        )

    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9100, debug=True)
