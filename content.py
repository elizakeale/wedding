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
ASSET_VERSION = 20

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
    "rsvp_deadline": "June 1, 2027",
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
# FAQs and Recommendations
#
# SOURCE OF TRUTH: the Google doc, not Figma.
#   docs.google.com/document/d/1D7eX9xFn12uT4U-fPNNcf1_s-rUC_rsKL-V4OuG-mSs
# (The itinerary is the other way round — Figma is its source.)
#
# A bare string in these lists is a group heading; a tuple is a question and
# its answer paragraphs.
#
# FAQS_SHORT is the save-the-date page: the doc's "Phase 1" questions, which
# are the only ones that can be answered honestly before invitations go out.
# FAQS and RECOMMENDATIONS are the phase-2 pages.
# ---------------------------------------------------------------------------

_CONTACTS = [
    "Eliza: +1.808.452.5181 | elizakeale@gmail.com",
    "Lucas: +1.206.316.6192 | lucasweyand@gmail.com",
    "Gala: +1.647.261.3943 | vedamom155@gmail.com",
    "Kathy: +1.206.380.6098 | kathleenkweyand@gmail.com",
]

_Q_DATES = (
    "What dates do you recommend booking our trip for?",
    ["If you\u2019re planning to come for about a week (we hope you do if you\u2019re flying "
     "all the way!), then we recommend aiming to arrive the week before the wedding, arriving "
     "October 15 weekend and flying out Sunday, October 24. We will be planning completely "
     "optional events throughout October 16 through 23, including a Welcome BBQ on Wednesday, "
     "October 20 and the wedding on Friday, October 22. We recommend visiting the island for at "
     "least 6 nights, but the sweet spot is 10&ndash;12 nights if you can swing some island "
     "hopping as well."],
)

_Q_AIRPORT = (
    "How do I get to the island?",
    ["Fly into Daniel K. Inouye International Airport in Honolulu, Oahu, Hawaii. This is the "
     "only international airport on Oahu. You could also fly in from another island if more "
     "affordable and you\u2019d like to island hop."],
)


# --- Save the date (PHASE == "save-the-date") ------------------------------
FAQS_SHORT = [
    (
        "When will more information be shared?",
        ["We will send out official invites and more information over the coming weeks."],
    ),
    (
        "Is it safe to book travel now?",
        ["We suggest holding off for now unless you are planning to book a specific "
         "accommodation that is already opened up for booking (e.g., a larger luxury Airbnb). "
         "Flights and Airbnbs typically don\u2019t get released until 11 months prior (likely "
         "late November 2026). We also will share hotel blocks and Airbnb recommendations soon."],
    ),
    _Q_DATES,
    _Q_AIRPORT,
]


# --- FAQs page (PHASE == "phase-2") ----------------------------------------
FAQS = [
    "General",
    (
        "When is the RSVP deadline? What if I need to change my RSVP?",
        ["We kindly ask you to RSVP by June 1, 2027. If you need to change your RSVP, please "
         "email Eliza and Lucas at "
         "<a href=\"mailto:elizakeale@gmail.com\">elizakeale@gmail.com</a>."],
    ),
    (
        "What if we cannot make it?",
        ["Hawaii is the most isolated land mass on earth, so we will not be offended if you "
         "cannot make it!"],
    ),
    (
        "Do you have a registry?",
        ["We are genuinely so grateful that you travelled all the way to join us in Hawaii and "
         "your presence is the only gift we need! We are so excited about this big group "
         "vacation and for you to experience the island. If you feel like you absolutely must "
         "contribute, we have a honeymoon fund you can contribute to here."],
    ),
    (
        "Who should guests contact with questions?",
        ["For friends: Don\u2019t hesitate to contact either Eliza or Lucas directly!",
         "For family: For Eliza\u2019s family, contact Gala. For Lucas\u2019 family, please "
         "contact Kathy.",
         "On the wedding day, please contact the wedding coordinator (their information to be "
         "updated later).",
         "<br />".join(_CONTACTS)],
    ),

    "Wedding Day",
    (
        "Can guests bring a plus-one?",
        ["After you enter your party code in the RSVP, you can see which guests you can RSVP "
         "for."],
    ),
    (
        "Are children welcome?",
        ["Yes! After you enter your party code in the RSVP, you can see which guests you can "
         "RSVP for."],
    ),
    (
        "Do you need meal choices or dietary restrictions?",
        ["You can indicate your dietary restrictions in the RSVP form."],
    ),
    (
        "What\u2019s the wedding dress code?",
        ["Island formal. We suggest lightweight suits and dress shoes for men (ties optional) "
         "and dresses for women (whatever length is fine). There will be grass so we suggest "
         "heel caps or wedges."],
    ),
    (
        "Will there be transportation on the day of?",
        ["<span class=\"k\">Getting there:</span> We recommend either a car with a designated "
         "driver (there will be parking), or scheduling a taxi or Uber in advance. We would "
         "highly suggest not waiting until the event to schedule an Uber as this can sometimes "
         "be unpredictable.",
         "<span class=\"k\">Getting back:</span> An optional shuttle bus will take guests back "
         "to Honolulu. You can also take a ride back with a designated driver or pre-schedule an "
         "Uber or Lyft if you don\u2019t prefer the shuttle or are not staying in Honolulu."],
    ),
    (
        "Where are the pickup points, and when does the last shuttle leave?",
        ["The shuttle will leave from the parking lot. There is only one shuttle since the event "
         "has a hard stop at 10 PM. It will wait until everyone is loaded in."],
    ),
    (
        "Is it outdoors? What if it rains?",
        ["The entire day will take place at one venue set against the Ko\u2019olau mountains. "
         "There will be a large tent and covered Lanai so rain will not affect the event. Hawaii "
         "rain usually does not last long."],
    ),
    (
        "Is there an after afterparty?",
        ["The choice is yours after the shuttles return to Honolulu! Waikiki bars will still be "
         "open and we might join you."],
    ),
]

FAQS_NOTE = ('Other trip-related recommendations can be found on the '
             '<a href="recommendations.html">recommendations</a> page.')


# --- Recommendations page (PHASE == "phase-2") -----------------------------
RECOMMENDATIONS = [
    "General Travel",
    _Q_DATES,
    _Q_AIRPORT,
    (
        "Where should we stay on island?",
        ["We recommend staying in Honolulu (\u201cin town\u201d) as it\u2019s a central point "
         "to shops, dining, transportation, and more importantly, where virtually all the hotels "
         "are located. Within Honolulu, the Waikiki neighborhood is the most tourist-friendly, "
         "though it\u2019s also very busy. This is the only location with proper hotels. This is "
         "also where the wedding day return shuttle will be dropping people back off.",
         "We would not recommend staying on the North Shore (Haleiwa, Pupukea, etc.) as it\u2019s "
         "very hard to get to and from (limited transportation options). The wedding day is "
         "mostly on the east (or \u201cWindward\u201d) side, so you could stay in an Airbnb in "
         "this area (e.g., Kane\u2019ohe or Kailua), but for the rest of your trip, these areas "
         "are less central."],
    ),
    (
        "What accommodations should we stay at?",
        ["We have arranged for a XX% discount at ____ hotels, you can book here with code ___. "
         "Hotels are often cheaper than Airbnbs.",
         "There are also many Airbnbs on island, we created an Airbnb shared list here.",
         "If you plan to rent a car, we recommend opting for an Airbnb in Honolulu but not in "
         "Waikiki, as parking is tricky.",
         "If you don\u2019t plan to rent a car or get daily rentals, then you can opt for a "
         "hotel in Waikiki."],
    ),
    (
        "Do I need a rental car?",
        ["If you want freedom to explore the island, we highly recommend getting a rental car or "
         "renting daily cars, as public transportation is limited. We\u2019ve arranged a 10% "
         "discount on rental cars with Paradise Rent A Car, email ___ and give code: rockpiles. "
         "Uber and Lyft are also prominent for getting around Honolulu but would be costly for "
         "longer distances across the island outside of Honolulu."],
    ),
    (
        "How is parking on-island?",
        ["Street parking is tricky unless you have an Airbnb outside of Waikiki or are willing "
         "to pay for overnight parking at a garage in Waikiki. We recommend asking your Airbnb "
         "host about the parking situation (usually an Airbnb in Honolulu but not in Waikiki "
         "will have street parking). Don\u2019t hesitate to message Eliza &amp; Lucas if you "
         "need advice on the parking situation near a hotel or Airbnb. For accommodations in "
         "Waikiki, there is very limited overnight and even daytime street parking except on "
         "Montsarrat, which can be hit or miss and very stressful."],
    ),
    (
        "What\u2019s the weather like, and what should we pack?",
        ["October is an ideal time to visit Oahu because it comes after peak summer humidity and "
         "before winter rainy season. Expect warm and slightly humid with comfortable daytime "
         "highs in the 83&deg;F to 85&deg;F (28&deg;C to 29&deg;C) and daytime lows of 73&deg;F "
         "to 75&deg;F (23&deg;C to 24&deg;C). Water is warm and no wet suit is required."],
    ),
    (
        "Food recommendations?",
        ["We made a shared Google Maps list here that you can bookmark."],
    ),
    (
        "Beach recommendations?",
        ["For cool views and bigger waves, Makapu\u2019u. For flat calm water and fine sand, "
         "Lanikai. For calm water and big stretches of beach, Ke\u2019iki on North Shore. For "
         "fun smaller waves and lots of space, Waimanalo.",
         "We made a shared Google Maps list here that you can bookmark."],
    ),
    (
        "Other tourism recommendations?",
        ["Take a helicopter tour or go cageless shark diving on North Shore.",
         "ATV/Jurassic Park tours at Kualoa Ranch."],
    ),
    (
        "Other good things to know",
        ["<span class=\"k\">Sunscreen:</span> Hawai\u02bbi bans sunscreens containing "
         "oxybenzone and octinoxate, use reef-safe sunscreen.",
         "<span class=\"k\">Local etiquette:</span> Keep your distance from sea turtles and "
         "Hawaiian monk seals.",
         "<span class=\"k\">Payment:</span> Major credit cards and tap are widely accepted. "
         "Tip standard is 18&ndash;20%. Currency is USD.",
         "<span class=\"k\">Forgot something?</span> Oahu is very developed, so you can buy "
         "anything you need that you forgot (there\u2019s Costco, Target, etc.). ABC stores are "
         "all over Waikiki and sell plenty of helpful things as well (e.g., beach towels, "
         "sunscreen).",
         "<span class=\"k\">In case you are confused:</span> Honolulu is the main town. Oahu "
         "is the island. Hawaii is the state. Waikiki is an area in Honolulu (not a town)."],
    ),
    (
        "What passports or entry documents do international guests need?",
        ["Canadians can enter the USA on a B2 visitor visa, no pre-application required. Just "
         "state this at border."],
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
