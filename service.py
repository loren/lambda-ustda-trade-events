# -*- coding: utf-8 -*-
import datetime as dt
import json
import logging
import re

import boto3
import requests
from botocore.exceptions import ClientError
import xml.etree.ElementTree as ET

JSON = "application/json"
BUCKET = "trade-events"
KEY = "ustda.json"
XML_ENDPOINT = "https://www.ustda.gov/api/events/xml"
RSS_ENDPOINT = "https://www.ustda.gov/events/feed"
S3_CLIENT = boto3.client("s3")


def handler(event, context):
    response = True
    try:
        entries = get_entries()
        S3_CLIENT.put_object(
            Bucket=BUCKET, Key=KEY, Body=json.dumps(entries), ContentType=JSON
        )
        print(f"✅ Uploaded {KEY} file with {len(entries)} locations")
    except (ClientError, ET.ParseError) as e:
        logging.error(e)
        response = False
    return response


def get_entries():
    title_link_dict = get_items()
    print("Fetching XML feed of items...")
    response = requests.get(XML_ENDPOINT)
    root = ET.fromstring(response.text.encode("utf-8"))
    nodes = root.findall("node")
    entries = [get_entry(node, title_link_dict) for node in nodes]
    print(f"Found {len(entries)} entries")
    return entries


def get_entry(node, title_link_dict):
    entry = {
        kid.tag.lower().replace("-", "_"): kid.text.strip()
        for kid in node
        if kid.text and len(kid.text) > 0
    }
    entry["title"] = re.sub(r"[^a-zA-Z -]+", "", entry["title"])
    entry["url"] = title_link_dict.get(entry["title"], None)
    entry["end_date"] = normalize_date(entry["end_date"])
    entry["start_date"] = (
        normalize_date(entry["start_date"]) if "start_date" in entry else entry["end_date"]
    )
    venues = get_venues(entry)
    if venues:
        entry["venues"] = venues
    entry["source_industry"] = [entry.pop("industry")]
    return entry


def get_venues(entry):
    venues = []
    for x in range(1, 4):
        venue_val = entry.pop(f"venue_{x}", None)
        if venue_val:
            venue = {
                "venue": venue_val,
                "city": entry.pop(f"city_{x}", venue_val),
                "country_name": f"Missing Country: {venue_val}",
            }
            venues.append(venue)
    return venues


def normalize_date(entry_date):
    return dt.datetime.strptime(entry_date, "%m/%d/%Y").strftime("%Y-%m-%d")


def get_items():
    print("Fetching RSS feed of items...")
    response = requests.get(RSS_ENDPOINT)
    root = ET.fromstring(response.text.encode("utf-8"))
    items = root.findall("./channel/item")
    title_link_dict = {item.find("title").text.strip(): item.find("link").text for item in items}
    print(f"Found {len(title_link_dict)} items")
    return title_link_dict
