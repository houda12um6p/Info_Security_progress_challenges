from flask import Flask, render_template, request, make_response
import secrets
from datetime import datetime

app = Flask(__name__)

# Store the visits received by the tracker
visits = []


@app.route("/")
def tracker():
    # Identify which publisher/page loaded the tracker
    publisher = request.args.get("publisher", "unknown")
    page = request.args.get("page", "unknown")

    # Check whether this browser already has a tracker identifier
    tracker_id = request.cookies.get("tracker_id")
    is_new = tracker_id is None

    # Create a new identifier if no cookie was received
    if is_new:
        tracker_id = secrets.token_hex(8)

    # Record this visit
    visit = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "tracker_id": tracker_id,
        "publisher": publisher,
        "page": page
    }

    visits.append(visit)

    # Display the current request
    print("\n--- TRACKER REQUEST ---")
    print("Identifier:", tracker_id)
    print("Publisher:", publisher)
    print("Page:", page)

    # Display the reconstructed profile
    print("\n--- RECONSTRUCTED PROFILE ---")
    for visit in visits:
        print(
            visit["time"],
            "|",
            visit["tracker_id"],
            "|",
            visit["publisher"],
            "|",
            visit["page"]
        )

    # Create the tracker response
    response = make_response(
        render_template(
            "tracker.html",
            tracker_id=tracker_id,
            publisher=publisher,
            page=page
        )
    )

    # Create a persistent tracker cookie for a new browser
    if is_new:
        response.set_cookie(
            key="tracker_id",
            value=tracker_id,
            max_age=86400,
            samesite="None",
            secure=True
        )

    return response


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=9000,
        debug=True,
        ssl_context="adhoc"
    )
