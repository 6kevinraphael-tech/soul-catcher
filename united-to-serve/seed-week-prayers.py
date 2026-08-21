#!/usr/bin/env python3
"""Replace the united-to-serve prayer chain with this week's prayer points."""

import json
import secrets
import time
import urllib.error
import urllib.request

DOC_URL = (
    "https://firestore.googleapis.com/v1/projects/united-to-serve-prayer"
    "/databases/(default)/documents/prayerChains/united-to-serve"
)

POINTS = [
    ("World / Community", "Unity, peace, and economic stability in the world"),
    ("World / Community", "Pray for neighbors"),
    ("Career", "Jeya – full-time job"),
    ("Career", "Richard – startup and promotion"),
    ("Career", "Monica – hire a believer for day care and enroll more kids"),
    ("Career", "Sullaiman, Monas’ brother – next steps for his career"),
    ("Visa", "Jeya – visa extension"),
    ("Visa", "Raijo – visa and wife to rejoin him"),
    ("Visa", "Alfred and Aanish – visa"),
    ("Healing", "Cendrine’s mom / Kathy – healing from cancer and kidney infection"),
    ("Healing", "Scott’s mom, Barbara – healing"),
    ("Healing", "Jeevan – eczema"),
    ("Healing", "Monas, cousin’s wife – recovering from heart attack"),
    ("Healing", "Monica’s mom – knee healing without surgery"),
    ("Healing", "Berta’s friends – healing"),
    ("Healing", "Marlyn, Monica’s sister – healing"),
    ("Healing", "Monica cousin’s son – healing from virus in the brain"),
    ("Healing", "Jeya’s niece – healing"),
    ("Healing", "Adora – healing"),
    ("Travel", "Giby’s stay in India"),
    ("Travel", "Giby’s Missionary Journey starts Wednesday 22nd"),
    ("Travel", "Andrey to SFO"),
    ("Relationships", "All small group families"),
    ("Relationships", "Andrew’s family"),
    ("Relationships", "Scott – relationship between siblings and mom"),
    ("Relationships", "Monica – relationship between her sisters"),
    ("Relationships", "Monica – pregnancy"),
    ("Relationships", "Jeya’s friend – miscarriage / loss of baby"),
    ("Kids", "Jeevan – soccer selection"),
    ("Kids", "All kids – summer vacation and graduation"),
    ("Spiritual Deliverance", "Monica’s client Surya – to receive God"),
    ("Spiritual Deliverance", "Surya’s son Ved – deliverance from attacks from the enemy"),
]


def make_id():
    return secrets.token_hex(4) + secrets.token_hex(3)


def main():
    base = int(time.time() * 1000)
    requests = []
    for i, (name, text) in enumerate(POINTS):
        requests.append(
            {
                "mapValue": {
                    "fields": {
                        "id": {"stringValue": make_id()},
                        "name": {"stringValue": name},
                        "text": {"stringValue": text},
                        "createdAt": {"integerValue": str(base + i)},
                    }
                }
            }
        )

    body = {
        "fields": {
            "requests": {"arrayValue": {"values": requests}},
            "marks": {"mapValue": {"fields": {}}},
            "weekKey": {"stringValue": "2026-07-13"},
            "updatedAt": {
                "timestampValue": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            },
        }
    }

    params = "&".join(
        [
            "updateMask.fieldPaths=requests",
            "updateMask.fieldPaths=marks",
            "updateMask.fieldPaths=weekKey",
            "updateMask.fieldPaths=updatedAt",
        ]
    )
    url = DOC_URL + "?" + params
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        method="PATCH",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.load(resp)
    except urllib.error.HTTPError as e:
        print("ERROR", e.code, e.read().decode())
        raise

    values = (
        result.get("fields", {})
        .get("requests", {})
        .get("arrayValue", {})
        .get("values", [])
    )
    print(f"Updated successfully. Requests now: {len(values)}")
    for v in values[:3]:
        f = v["mapValue"]["fields"]
        print("-", f["name"]["stringValue"] + ":", f["text"]["stringValue"])
    print("...")
    last = values[-1]["mapValue"]["fields"]
    print("-", last["name"]["stringValue"] + ":", last["text"]["stringValue"])


if __name__ == "__main__":
    main()
