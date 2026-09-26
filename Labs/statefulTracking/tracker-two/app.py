from flask import Flask, render_template, request, make_response
import secrets

app = Flask(__name__)

# Store the relationships learned during cookie syncing
sync_mappings = []


def get_tracker2_id():
    tracker2_id = request.cookies.get("tracker2_id")
    is_new = tracker2_id is None

    if is_new:
        tracker2_id = secrets.token_hex(8)

    return tracker2_id, is_new


@app.route("/")
def tracker():
    tracker2_id, is_new = get_tracker2_id()

    print("\n--- TRACKER TWO REQUEST ---")
    print("Tracker 2 ID:", tracker2_id)

    response = make_response(
        render_template(
            "tracker.html",
            tracker2_id=tracker2_id
        )
    )

    if is_new:
        response.set_cookie(
            key="tracker2_id",
            value=tracker2_id,
            max_age=86400,
            samesite="None",
            secure=True
        )

    return response


@app.route("/sync")
def sync():
    # Tracker 1 sends its identifier in the URL
    tracker1_id = request.args.get("tracker1_id", "unknown")

    # Tracker 2 reads its own cookie
    tracker2_id, is_new = get_tracker2_id()

    mapping = {
        "tracker1_id": tracker1_id,
        "tracker2_id": tracker2_id
    }

    if mapping not in sync_mappings:
        sync_mappings.append(mapping)

    print("\n--- COOKIE SYNC ---")
    print("Tracker 1 ID:", tracker1_id)
    print("Tracker 2 ID:", tracker2_id)

    print("\n--- SYNCED IDENTIFIERS ---")
    for item in sync_mappings:
        print(
            item["tracker1_id"],
            "<-->",
            item["tracker2_id"]
        )

    response = make_response("Cookie sync completed", 200)

    if is_new:
        response.set_cookie(
            key="tracker2_id",
            value=tracker2_id,
            max_age=86400,
            samesite="None",
            secure=True
        )

    return response


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=9200,
        debug=True,
        ssl_context="adhoc"
    )
