import xml

import vcr

from service import get_entries, handler


@vcr.use_cassette()
def test_get_entries():
    """Reads from the `test_get_entries` cassette and processes the entries. Tests that multiple
    entries get read correctly.

    """
    entries = get_entries()
    assert len(entries) == 10
    expected_entry = {
        "title": "Egypt Advanced Technologies for Onshore Exploration",
        "start_date": "2020-02-15",
        "end_date": "2020-02-28",
        "start_time": "12:09 pm",
        "end_time": "12:09 pm",
        "body": "U.S. Trade and Development Agency (USTDA) is hosting",
        "registration_title": "Egypt Advanced Technologies for Onshore Exploration",
        "cost_currency": "USD",
        "url": "https://ustda.gov/events/2020/middle-east-north-africa-europe-and-eurasia/",
        "venues": [
            {
                "venue": "Houston, TX",
                "city": "Houston, TX",
                "country_name": "Missing Country: Houston, TX",
            },
            {
                "venue": "San Francisco, CA",
                "city": "San Francisco, CA",
                "country_name": "Missing Country: San Francisco, CA",
            },
        ],
        "source_industry": ["Traditional Energy & Power"],
    }
    assert entries[0] == expected_entry


def test_handler_handles_parse_error(mocker):
    """Ensures any XML parsing issues from garbage input get ignored"""
    mocker.patch('service.get_entries', side_effect=xml.etree.ElementTree.ParseError)
    assert handler(None, None) is False
