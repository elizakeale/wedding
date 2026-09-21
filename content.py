# -*- coding: utf-8 -*-
"""
E & L Wedding — all site copy and configuration.

This is the ONLY file you edit to change what the site says.
After editing, run:  python3 build.py

Everything in *.html is generated. Do not edit the HTML directly —
the next build will overwrite it.
"""

# ---------------------------------------------------------------------------
# PHASE — the one switch that decides how much of the site is live.
#
#   "save-the-date"  home.html = save-the-date hero + FAQs. No nav, no RSVP.
#                    Itinerary and recommendations are NOT generated at all,
#                    so nothing about the wedding week is discoverable.
#
#   "phase-2"        home.html = hero + nav + RSVP form, with the pinned nav
#                    bar. Itinerary, recommendations and FAQs each get their
#                    own page and the nav appears everywhere.
#
# To launch phase 2: change this to "phase-2", run build.py, commit, push.
# To look at phase 2 without launching it: python3 build.py --phase2
# ---------------------------------------------------------------------------
PHASE = "save-the-date"

# Bump this when css/wedding.css or the favicons change, so browsers don't
# serve a stale copy.
ASSET_VERSION = 7

# The page the password gate sends people to.
ENTRY_PAGE = "home.html"

# ---------------------------------------------------------------------------
# Link previews (iMessage/SMS, WhatsApp, Slack, Facebook, etc.)
#
# SITE_URL must be absolute and must be the domain people will actually be
# given, because og:image is resolved against it. Previews only work once that
# domain resolves — until lucasandeliza.com is live, a shared link will show a
# plain card with no picture.
#
# If you need previews working before the DNS switch, temporarily set this to:
#   SITE_URL = "https://elizakeale.github.io/wedding"
#
# Note: iMessage caches a preview per URL, aggressively. If someone shares the
# link before these tags are live, they may keep seeing the old blank card for
# a while even after this ships.
# ---------------------------------------------------------------------------
SITE_URL = "https://lucasandeliza.com"

META = {
    "title": "Save The Date | E &amp; L Wedding",
    "description": "02.12.2028 — Kane’ohe, O’ahu, Hawai’i",
    "image": "og-image.jpg",     # 1200x630, generated from surfing.jpg
    "image_w": "1200",
    "image_h": "630",
}


# ---------------------------------------------------------------------------
# The wedding
# ---------------------------------------------------------------------------
WEDDING = {
    "date_display": "02.12.2028",          # as shown in the hero and footer
    "date_long": "Saturday, February 12, 2028",
    "place": "Kane’ohe, O’ahu, Hawai’i",
    "names": "E &amp; L Wedding",           # hero wordmark
    "names_short": "E&amp;L Wedding",       # footer wordmark

    # TBC — not yet decided. Only appears when PHASE == "full".
    "rsvp_deadline": "TBC",
}

CONTACT = {
    "email": "elizakeale@gmail.com",
    "phone": "+1.808.452.5181",
    "phone_href": "+18084525181",
    "website": "lucasandeliza.com",
}


# ---------------------------------------------------------------------------
# Save-the-date hero (PHASE == "save-the-date" only)
# ---------------------------------------------------------------------------
SAVE_THE_DATE = {
    "label": "Save the date",
    "tagline": "…more details to come. Scroll down for FAQs.",
}


# ---------------------------------------------------------------------------
# Navigation (PHASE == "full" only)
# Each entry: (label, filename)
# ---------------------------------------------------------------------------
NAV = [
    ("RSVP", "home.html"),
    ("ITINERARY", "itinerary.html"),
    ("RECOMMENDATIONS", "recommendations.html"),
    ("FAQs", "faqs.html"),
]

# The footer nav uses a different order than the header (matches Figma).
FOOTER_NAV_ORDER = ["RSVP", "FAQs", "ITINERARY", "RECOMMENDATIONS"]


# ---------------------------------------------------------------------------
# FAQs
#
# NOTE — copy discrepancy to resolve:
# The Figma save-the-date frame now answers "Is it safe to book our flights
# now?" with "We suggest holding off for now unless you are planning to book a
# specific accommodation that is already opened up for booking..." which is the
# opposite advice to what is live below. Left as-is deliberately: changing what
# guests are told about booking flights is your call, not a build decision.
# ---------------------------------------------------------------------------
FAQS = [
    (
        "When will more information be shared?",
        ["We will send out official invites and full information over the coming months."],
    ),
    (
        "Is it safe to book our flights now?",
        ["Yes, if you know you plan to attend. Flights typically don’t get released until "
         "11 months prior (likely March 2027)."],
    ),
    (
        "When should we plan to travel?",
        ["If you’re planning to come for about a week (we hope you do if you’re flying all "
         "the way!), then we recommend aiming to arrive the week before the wedding, arriving "
         "approximately February 4 weekend and flying out Sunday or Monday February 14. We will "
         "be planning optional events throughout February 5 to 12, including the wedding on "
         "Saturday, February 12. We recommend visiting the island for at least 5 nights, but the "
         "sweet spot is 10 nights if you can swing some island hopping as well."],
    ),
    (
        "How do we get to the island?",
        ["Fly into Daniel K. Inouye International Airport in Honolulu, Oahu, Hawaii. This is the "
         "only international airport on Oahu. You could also fly in from another island if more "
         "affordable and you’d like to island hop!"],
    ),
    (
        "Where should we stay on island?",
        ["We recommend staying in Honolulu (“in town”) as it’s a central point to shops, "
         "dining, transportation and more importantly, where virtually all the hotels are located. "
         "Within Honolulu, the Waikiki neighborhood is the most tourist-friendly, though it’s "
         "also very busy. This is the only location with proper hotels. We would not recommend "
         "staying on the North Shore (Haleiwa, Pupukea, etc.) as it’s very hard to get to and "
         "from (limited transportation options). The wedding day is mostly on the east side in "
         "Kane’ohe, so you could stay in an Airbnb near here or Kailua, but for the rest of "
         "your trip, these areas are less central."],
    ),
]


# ---------------------------------------------------------------------------
# Itinerary (PHASE == "full" only — not generated while the site is dark)
#
# !! DAY LABELS ARE DERIVED, NOT CONFIRMED !!
# These were shifted from the old July 2027 schedule by the same relative
# offsets (beach day T-3, BBQ T-2, wedding day, cruise T+1) against the new
# wedding date of Saturday, February 12, 2028. Confirm before going live.
# ---------------------------------------------------------------------------
ITINERARY = [
    ("Wednesday, February 9", [
        ("11:00 AM &ndash; 3:00 PM", "Beach Day", True, [
            "We’ll have tents up at Makapu’u Beach Park. Bring sunscreen, sun protection, "
            "beach towels, and anything else you might need to have fun. Rain permitting. Food is "
            "not easily accessed so we recommend bringing snacks and eating before. There is also "
            "amazing poke 10 min west in Hawaii Kai at HanaPa’a Market.",
            "<span class=\"k\">Location:</span> Makapu’u Beach Park, O’ahu<br />"
            "<span class=\"k\">Parking:</span> Parking should be easy on the weekday in the parking "
            "lot, otherwise people park along the road.",
        ]),
        ("5:00 PM &ndash; 7:00 PM", "Sunset Surf", True, [
            "Depending on conditions, we’ll do a chill sunset surf in Waikiki. Still happening "
            "if drizzling. Beginner friendly and very unserious! Text Lucas if you have questions "
            "or need help (e.g., we’ll help people get surfboards). If you don’t want to "
            "surf, you can come and hang on the beach!",
        ]),
    ]),
    ("Thursday, February 10", [
        ("5:00 PM &ndash; 9:00 PM", "Welcome BBQ", False, [
            "We invite you to a welcome BBQ for family and close friends.",
            "<span class=\"k\">Location:</span> Kauhale Beach Cove, 45-180 Mahalani Place, "
            "Kane’ohe, O’ahu<br /><span class=\"k\">Parking:</span> There are guest parking "
            "spots as well as street parking outside the gate.",
        ]),
    ]),
    ("Saturday, February 12", [
        ("11:00 AM &ndash; 11:30 AM", "Welcome Cocktail", False, [
            "Arrive in this time window.",
        ]),
        ("11:30 AM &ndash; 2:30 PM", "Reception Lunch", False, [
            "We’re all going to paddle out to rockpiles surf break, where we met. Just kidding "
            "&mdash; the reception is a lunch with mimosas and will take place overlooking Haiku "
            "Gardens and Ko’olau mountains in Kane’ohe.",
            "<span class=\"k\">Location:</span> Hale’iwa Joe’s Haiku Gardens*, "
            "Kane’ohe, O’ahu<br /><span class=\"k\">Parking:</span> There is plenty of "
            "designated parking on-site.",
            "*not to be confused with the Haleiwa, North Shore location",
        ]),
        ("2:30 &ndash; 3:00 PM", "Shuttle Transport", False, [
            "Shuttle buses will take us from reception to Kauhale Beach Cove (still in "
            "Kane’ohe) for the day party. The ride is only 5 minutes. If you are not attending "
            "the party, there will be other buses returning people to Honolulu.",
        ]),
        ("3:00 PM &ndash; late", "Party", True, [
            "We’ll have bartenders and hangout. Feel free to bring a swimsuit for the pool or "
            "hot tub. There is also a clubhouse if you don’t want to be outside.",
        ]),
        ("8:00 &ndash; 9:00 PM", "Shuttle Transport", False, [
            "Shuttle buses will take guests back to Honolulu. You can also order an Uber or Lyft "
            "if you don’t prefer the shuttle.",
        ]),
    ]),
    ("Sunday, February 13", [
        ("5:00 PM &ndash; 9:00 PM", "Sunset Cruise", True, [
            "Purchase tickets to the Kuhio Sunset Cruise here. Totally optional. Takes off from "
            "Honolulu.",
        ]),
    ]),
]


# ---------------------------------------------------------------------------
# Recommendations (PHASE == "full" only)
# Placeholder — the Figma frame for this page is still unfinished.
# ---------------------------------------------------------------------------
RECOMMENDATIONS = [
    ("Where to stay", ["TBC"]),
    ("Getting around", ["TBC"]),
    ("Eating", ["TBC"]),
    ("Things to do", ["TBC"]),
]
