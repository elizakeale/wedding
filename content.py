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
ASSET_VERSION = 17

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
    "description": "10.22.2027 — Kane’ohe, O’ahu, Hawai’i",
    "image": "og-image.jpg",     # 1200x630, generated from surfing.jpg
    "image_w": "1200",
    "image_h": "630",
}


# ---------------------------------------------------------------------------
# The wedding
# ---------------------------------------------------------------------------
WEDDING = {
    "date_display": "10.22.2027",          # as shown in the hero and footer
    "date_long": "Friday, October 22, 2027",

    # NOTE: the hero and footer still say Kane’ohe, matching Figma. The
    # ceremony and reception are now at The Plant Place in WAIMANALO; only the
    # Welcome BBQ is in Kane’ohe. Worth deciding whether the site should say
    # O’ahu rather than name the wrong town.
    "place": "Kane’ohe, O’ahu, Hawai’i",
    "names": "E &amp; L Wedding",           # hero wordmark
    "names_short": "E&amp;L Wedding",       # footer wordmark

    # From Figma. Only appears when PHASE == "phase-2".
    "rsvp_deadline": "March 1, 2027",
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
# The flights answer follows Figma: hold off unless you're booking a specific
# place that's already bookable. It used to say "yes, if you know you plan to
# attend" — the opposite — so if a guest quotes that back at you, that's why.
# ---------------------------------------------------------------------------
FAQS = [
    (
        "When will more information be shared?",
        ["We will send out official invites and more information over the coming weeks."],
    ),
    (
        "Is it safe to book our flights now?",
        ["We suggest holding off for now unless you are planning to book a specific "
         "accommodation that is already opened up for booking (e.g., a larger luxury "
         "Airbnb). Flights and Airbnbs typically don’t get released until 11 months "
         "prior (likely late November 2026). We also will share hotel blocks and Airbnb "
         "recommendations soon."],
    ),
    (
        "When should we plan to travel?",
        ["If you’re planning to come for about a week (we hope you do if you’re flying all "
         "the way!), then we recommend aiming to arrive the week before the wedding, arriving "
         "October 15 weekend and flying out Sunday, October 24. We will be planning completely "
         "optional events throughout October 16 through 23, including a Welcome BBQ on "
         "Wednesday, October 20 and the wedding on Friday, October 22. We recommend visiting "
         "the island for at least 6 nights, but the sweet spot is 10&ndash;12 nights if you can "
         "swing some island hopping as well."],
    ),
    (
        "How do we get to the island?",
        ["Fly into Daniel K. Inouye International Airport in Honolulu, Oahu, Hawaii. This is the "
         "only international airport on Oahu. You could also fly in from another island if more "
         "affordable and you’d like to island hop."],
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
# Itinerary — the source of truth, taken from Figma.
#
# This list is what generates rsvp-backend/itinerary-seed.tsv on every build.
# Paste that file into the Itinerary tab of the Master Planner sheet; the Apps
# Script reads it from there and filters it per party before sending.
#
# "audience" is blank for events everyone sees, or the EXACT header of a
# guest-list column. Today that is only "Beach Day & Cruise" — a Yes there
# means the party sees both the beach day and the sunset cruise.
# ---------------------------------------------------------------------------
ITINERARY = [
    ("Monday, October 18", [
        {
            "time": "11:00 AM \u2013 3:00 PM",
            "name": "Beach Day",
            "optional": True,
            "audience": "Beach Day & Cruise",
            "body": "We\u2019ll have tents up at Makapu\u2019u Beach Park. Bring sunscreen, sun "
                    "protection, beach towels, and anything else you might need to have fun. Rain "
                    "permitting. Food is not easily accessed so we recommend bringing snacks and "
                    "eating before. There is also amazing poke 10 min west in Hawaii Kai at "
                    "HanaPa\u2019a Market.",
            "location": "Makapu\u2019u Beach Park, O\u2019ahu",
            "parking": "Parking should be easy on the weekday in the parking lot, otherwise "
                       "people park along the road.",
        },
        {
            "time": "5:00 PM \u2013 7:00 PM",
            "name": "Sunset Surf",
            "optional": True,
            "body": "Depending on conditions, we\u2019ll do a chill sunset surf in Waikiki. Still "
                    "happening if drizzling. Beginner friendly and very unserious! Text Lucas if "
                    "you have questions or need help (e.g., we\u2019ll help people get "
                    "surfboards). If you don\u2019t want to surf, you can come and hang on the "
                    "beach!",
            "location": "Will be decided closer to depending on conditions.",
            "parking": "Will be shared once break is decided.",
        },
    ]),
    ("Wednesday, October 20", [
        {
            "time": "5:00 PM \u2013 11:00 PM",
            "name": "Welcome BBQ",
            "body": "Join us at our home in Kane\u2019ohe for casual appetizers, dinner, drinks, "
                    "and our favourite local dessert. Bring a swimsuit and towel if you plan to "
                    "swim in pool/hot tub or risk it with the hammerheads.",
            "location": "Kauhale Beach Cove, 45-180 Mahalani Place, Kane\u2019ohe, O\u2019ahu, "
                        "96744",
            "parking": "There will be plenty of street parking in the neighborhood. Avoid driving "
                       "through the gates.",
            "transportation": "We recommend either driving with a designated driver, scheduling a "
                              "taxi, or taking an Uber or Lyft.",
            "directions": "After arriving, walk through the yellow gates down the hill and head "
                          "to the clubhouse.",
            "attire": "Island chic. For men, we suggest linen (white is okay!) or Hawaiian shirts "
                      "and slippahs (flip flops). For women, we suggest sundresses and sandals "
                      "(heels if you feel like it). Most of the area is grass or deck so you can "
                      "walk around barefoot.",
        },
    ]),
    ("Friday, October 22", [
        {
            "time": "3:30 \u2013 4:00 PM",
            "name": "Arrival",
            "body": "Please arrive in this time window.",
        },
        {
            "time": "4:00 \u2013 4:30 PM",
            "name": "Ceremony",
            "body": "Paddle out to rockpiles surf break, where we met. Just kidding. The entire "
                    "day will take place at one venue set against the Ko\u2019olau mountains. "
                    "There will be a tent and covered Lanai so rain will not affect the event.",
            "location": "The Plant Place, 41-821 Waikupanaha Street, Waimanalo, O\u2019ahu, 96795",
            "parking": "There is plenty of designated parking on-site.",
            "transportation": "We recommend either a car with a designated driver, or scheduling "
                              "a taxi or Uber in advance. We would highly suggest not waiting "
                              "until event to schedule an Uber as this can sometimes be "
                              "unpredictable.",
            "directions": "After parking or being dropped off, walk down the gravel path. "
                          "You\u2019ll see a clear tent, it\u2019ll be hard to miss.",
            "attire": "Island formal. We suggest lightweight suits and dress shoes for men (ties "
                      "optional) and dresses for women (whatever length is fine).",
        },
        {
            "time": "4:30 \u2013 5:30 PM",
            "name": "Champagne Hour",
            "body": "There will be champagne and time to get settled in.",
        },
        {
            "time": "5:30 \u2013 6:30 PM",
            "name": "Reception",
            "body": "There will be a few speeches accompanied by plenty of booze and fresh local "
                    "appetizers, dinner, and desserts.",
        },
        {
            "time": "6:30 \u2013 10 PM",
            "name": "Afterparty",
            "body": "Open bar, music, and hangout. We have a hard stop at 10 PM.",
        },
        {
            "time": "10 PM",
            "name": "Shuttle Transport",
            "body": "An optional shuttle bus will take guests back to Honolulu. You can also take "
                    "a ride back with a designated driver or pre-schedule an Uber or Lyft if you "
                    "don\u2019t prefer the shuttle or are not staying in Honolulu.",
        },
    ]),
    ("Saturday, October 23", [
        {
            "time": "5:00 PM \u2013 9:00 PM",
            "name": "Sunset Cruise",
            "optional": True,
            "audience": "Beach Day & Cruise",
            "body": "More information will be shared on where to buy tickets soon. Totally "
                    "optional. Takes off from Honolulu.",
        },
    ]),
]

# The columns written to the seed file, in order.
ITINERARY_FIELDS = ["day", "time", "event", "optional", "audience", "body",
                    "location", "parking", "transportation", "directions", "attire"]


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
