import vcr

from service import get_entries


@vcr.use_cassette()
def test_get_entries():
    """Reads from the `test_get_entries` cassette and processes the entries. Tests that multiple
    entries get read correctly.

    """
    entries = get_entries()
    assert len(entries) == 10
    expected_entry = {
        "title": "Egypt Advanced Technologies for Onshore Exploration and Production Reverse Trade Mission",
        "start_date": "2020-02-15",
        "end_date": "2020-02-28",
        "start_time": "12:09 pm",
        "end_time": "12:09 pm",
        "body": "U.S. Trade and Development Agency (USTDA) is hosting the Egypt Advanced Technologies for Onshore Exploration and Production Reverse Trade Mission, bringing senior decision-makers from Egypt to the United States to meet with leading U.S. suppliers of oil and gas exploration and production technologies.  The delegation will include high-ranking officials from Egypt’s Ministry of Petroleum and Mineral Resources and state-owned enterprises in the petroleum sector.\n\nAs part of the itinerary, USTDA will host a business briefing for U.S. companies to learn about upcoming project opportunities on February 20th in Houston, Texas. .U.S. companies will showcase their technologies and expertise to the delegation as Egypt moves forward on its plans to modernize its oil and gas sector. \n\nKoeppen, Elliott & Associates, Ltd. is organizing this visit on behalf of USTDA.  For further information regarding registration and/or to arrange for a private meeting with the delegation, please contact  David Elliott, davidelliott@kealtd.com; or by text or phone at (757) 342-2149. \n\nClick here for the event flyer.",
        "registration_title": "Egypt Advanced Technologies for Onshore Exploration and Production Reverse Trade Mission",
        "cost_currency": "USD",
        "url": "https://ustda.gov/events/2020/middle-east-north-africa-europe-and-eurasia/egypt-advanced-technologies-onshore",
        "venues": [
            {
                "venue": "Houston, TX",
                "city": "Houston, TX",
                "country_name": "Missing Country: Houston, TX"},
            {
                "venue": "San Francisco, CA",
                "city": "San Francisco, CA",
                "country_name": "Missing Country: San Francisco, CA",
            },
        ],
        "source_industry": ["Traditional Energy & Power"],
    }
    assert entries[0] == expected_entry
