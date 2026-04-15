from db import insert_data

def process_data(data):
    if "name" not in data or "value" not in data:
        return {"status": "error", "message": "Invalid data"}

    processed_value = data["value"] * 2

    # Save to DB
    insert_data(data["name"], processed_value)

    return {
        "status": "success",
        "data": {
            "name": data["name"],
            "value": processed_value
        }
    }