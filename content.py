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
ASSET_VERSION = 69

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
    # What a link preview (iMessage, WhatsApp, Slack) shows: title on the
    # first line, description underneath.
    "title": "E &amp; L Wedding, Save The Date",   # link previews
    "tab_title": "E &amp; L &ndash; 10.22.2027",    # the browser tab
    "description": "10.22.2027",
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
    # Spaced to match the hero and the bar. Figma has the footer tight
    # ("E&L WEDDING") on both the desktop and mobile frames; that was the
    # oversight, not this.
    "names_short": "E &amp; L Wedding",     # footer wordmark

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
    "tagline": "…more details to come. scroll down for FAQs.",
}


# ---------------------------------------------------------------------------
# Navigation (PHASE == "full" only)
# Each entry: (label, filename)
# ---------------------------------------------------------------------------
NAV = [
    ("RSVP", "home.html"),
    ("ITINERARY", "itinerary.html"),
    ("FAQs", "faqs.html"),
    ("RECOMMENDATIONS", "recommendations.html"),
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
     "all the way!), then we recommend aiming to arrive the weekend before, arriving "
     "October 15 weekend and flying out Sunday, October 24 onwards. We will be planning "
     "completely optional events throughout the week. We recommend visiting the "
     "island for at least 6 nights, but the sweet spot is 10&ndash;12 nights if you plan to "
     "island hop."],
)

_Q_AIRPORT = (
    "How do we get to the island?",
    ["Fly into Daniel K. Inouye International Airport in Honolulu, Oahu, Hawaii. This is the "
     "only airport on Oahu. You could also fly in from another island if it\u2019s more "
     "affordable and/or you\u2019d like to island hop."],
)


# --- Save the date (PHASE == "save-the-date") ------------------------------
FAQS_SHORT = [
    (
        "When will more information be shared?",
        ["We will send out official invites and more information over the coming weeks."],
    ),
    (
        "Is it safe to book our flights now?",
        ["We suggest holding off for now unless you are planning to book a specific "
         "accommodation that is already opened up for booking. Flights, hotels, and Airbnbs "
         "typically don\u2019t open up until 11 months prior (likely late November 2026). We "
         "also will share hotel and Airbnb information soon."],
    ),
    _Q_DATES,
    _Q_AIRPORT,
]


# --- FAQs page (PHASE == "phase-2") ----------------------------------------
FAQS = [
    "Wedding Day",
    (
        "How can I share my dietary restrictions?",
        ["You can indicate your dietary restrictions in the RSVP form."],
    ),
    (
        "Am I RSVP\u2019ing for my whole party?",
        ["Yes, we will only send communications to one person per party. You can RSVP for "
         "your entire party here."],
    ),
    (
        "Are children welcome?",
        ["Yes! After you enter your party code in the RSVP, you can see which guests are in "
         "your party."],
    ),
    (
        "Can I bring a plus-one?",
        ["After you enter your party code in the RSVP, you can see which guests are in your "
         "party."],
    ),
    (
        "What\u2019s the recommended attire?",
        ["Island formal. We suggest lightweight suits and dress shoes for men (ties optional) "
         "and dresses for women (whatever length is fine). Heels must have caps or be wedges "
         "due to the grass."],
    ),
    (
        "Will there be transportation on the day of?",
        ["<span class=\"k\">Getting there:</span> We recommend either a car with a designated "
         "driver (there will be parking), or scheduling a taxi or Uber in advance. We would "
         "highly suggest not waiting until the event to schedule an Uber as this can sometimes "
         "be unpredictable and the location is 40\u201360 minutes from Honolulu depending on "
         "traffic.",
         "<span class=\"k\">Getting back:</span> An optional shuttle will take guests back to "
         "Waikiki. We will message closer to the date to confirm if you would like to take the "
         "shuttle. You can also take a ride back with a designated driver or pre-schedule an "
         "Uber or Lyft if you don\u2019t prefer the shuttle or are not staying in Waikiki."],
    ),
    (
        "Where are the pickup points, and when does the last shuttle leave?",
        ["The shuttle will leave from the parking lot. There is only one shuttle since the "
         "event has a hard stop at 10 PM. It will wait until everyone is loaded in."],
    ),
    (
        "Is it outdoors? What if it rains?",
        ["The entire event will take place at one venue set against the Ko\u2019olau "
         "mountains. There will be a large tent and covered lanai so rain will not affect the "
         "event. Hawaii rain usually does not last long."],
    ),
    (
        "Is there an after afterparty?",
        ["The choice is yours after the shuttles return to Honolulu! Waikiki bars will still "
         "be open and we might join you."],
    ),

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
        ["For friends: Don\u2019t hesitate to contact either Eliza or Lucas directly.",
         "For family: For Eliza\u2019s family, contact Gala. For Lucas\u2019 family, please "
         "contact Kathy.",
         "On the wedding day, please contact our wedding coordinator (their information will "
         "be shared later).",
         "<br />".join(_CONTACTS)],
    ),
]

# --- Recommendations page (PHASE == "phase-2") -----------------------------
# Phase 1 questions here intentionally diverge from FAQS_SHORT above: the doc's
# phase-1 wording (specific dates, "international airport") is meant for this
# page, once invitations are out. FAQS_SHORT keeps the vaguer save-the-date
# wording that was deliberately trimmed while that's still the only page live.
RECOMMENDATIONS = [
    "Phase 1: Save the date",
    (
        "When will more information be shared?",
        ["We will send out official invites and more information over the coming weeks."],
    ),
    (
        "Is it safe to book travel now?",
        ["We suggest holding off for now unless you are planning to book a specific "
         "accommodation that is already opened up for booking (e.g., a larger luxury Airbnb). "
         "Flights and Airbnbs typically don\u2019t get released until 11 months prior (likely "
         "late November 2026). We also will share hotel blocks and Airbnb recommendations "
         "soon."],
    ),
    (
        "What dates do you recommend booking our trip for?",
        ["If you\u2019re planning to come for about a week (we hope you do if you\u2019re "
         "flying all the way!), then we recommend aiming to arrive the week before the "
         "wedding, arriving October 15 weekend and flying out Sunday, October 24. We will be "
         "planning completely optional events throughout October 16 through 23, including a "
         "Welcome BBQ on Wednesday, October 20 and the wedding on Friday, October 22. We "
         "recommend visiting the island for at least 6 nights, but the sweet spot is "
         "10&ndash;12 nights if you can swing some island hopping as well."],
    ),
    (
        "How do I get to the island?",
        ["Fly into Daniel K. Inouye International Airport in Honolulu, Oahu, Hawaii. This is "
         "the only international airport on Oahu. You could also fly in from another island "
         "if more affordable and you\u2019d like to island hop."],
    ),

    "Phase 2",
    (
        "Where should we stay on island?",
        ["We recommend staying in Honolulu (\u201cin town\u201d) as it\u2019s a central point "
         "to shops, dining, transportation, and more importantly, where virtually all the "
         "hotels are located. Within Honolulu, the Waikiki neighborhood is the most "
         "tourist-friendly. This is the only location with proper hotels. This is also where "
         "the wedding day return shuttle will be dropping people back off so this is our "
         "recommendation.",
         "We would not recommend staying on the North Shore (Haleiwa, Pupukea, etc.) as "
         "it\u2019s very hard to get to and from (limited transportation options). The "
         "wedding day is mostly on the east (or \u201cWindward\u201d) side, so you could stay "
         "in an Airbnb in this area (e.g., Kane\u2019ohe or Kailua), but for the rest of your "
         "trip, these areas are less central."],
    ),
    (
        "What accommodations should we stay at?",
        ["We have arranged for a 10% discount at ____ hotels, you can book here with code "
         "___. Hotels are often cheaper than Airbnbs.",
         "There are also many Airbnbs on island, we created an Airbnb shared list here.",
         "If you plan to rent a car, we recommend opting for an Airbnb in Honolulu town but "
         "not in Waikiki, as parking is tricky.",
         "If you don\u2019t plan to rent a car or get daily rentals, then you can opt for a "
         "hotel in Waikiki.",
         "<span class=\"k\">Luxury hotels:</span> The Royal Hawaiian Resort, Prince Waikiki "
         "Hotel, Hilton Hawaiian Village, Moana Surfrider (A Westin Resort &amp; Spa), Hilton "
         "Club Ka Haku Honolulu.",
         "<span class=\"k\">Boutique hotels closer to Diamond Head:</span> Kaimana Beach "
         "Hotel, Lotus Honolulu, Queen Kapi\u2019olani Hotel."],
    ),
    (
        "Do I need a rental car?",
        ["If you want freedom to explore the island, we highly recommend getting a rental car "
         "or renting daily cars, as public transportation is limited. We\u2019ve arranged a "
         "10% discount on rental cars with Paradise Rent A Car, email ___ and give code: "
         "rockpiles. Uber and Lyft are also prominent for getting around Honolulu but would be "
         "costly for longer distances across the island outside of Honolulu. We would "
         "definitely suggest not being stuck in Waikiki for your whole trip!"],
    ),
    (
        "How is parking on-island?",
        ["<span class=\"k\">If you\u2019re staying in Waikiki:</span> You\u2019ll need to pay "
         "for overnight parking at a garage (cheaper than hotel), or try your luck on "
         "Montsarrat Ave. You can usually do a couple laps and eventually find a spot.",
         "<span class=\"k\">If you\u2019re staying outside Waikiki but still in "
         "Honolulu:</span> Street parking should not be an issue, check with your host.",
         "<span class=\"k\">If you\u2019re staying outside of Honolulu:</span> Street parking "
         "should not be an issue, check with your host.",
         "Don\u2019t hesitate to message Eliza &amp; Lucas if you need advice on the parking "
         "situation near a hotel or Airbnb. Please look out for parking signs carefully as "
         "towing is very common on island.",
         "We made a shared Google Maps parking list here that you can bookmark."],
    ),
    (
        "What\u2019s the weather like, and what should guests pack?",
        ["October is an ideal time to visit O\u2019ahu because it comes after peak summer "
         "humidity and before winter rainy season. Expect warm and slightly humid with "
         "comfortable daytime highs in the 83&deg;F to 85&deg;F (28&deg;C to 29&deg;C) and "
         "daytime lows of 73&deg;F to 75&deg;F (23&deg;C to 24&deg;C). Water is warm and no "
         "wet suit is required. Rain is often brief and passing, but overall weather in "
         "Hawaii has been unpredictable for the past few years so keep this in mind."],
    ),
    (
        "Food recommendations?",
        ["We made a shared Google Maps list here that you can bookmark."],
    ),
    (
        "Beach recommendations?",
        ["For cool views and bigger waves, Makapu\u2019u Beach Park. For flat calm water and "
         "fine sand, Lanikai. For calm water and big stretches of beach, Ke\u2019iki on North "
         "Shore. For fun smaller waves and lots of space for big groups, Waimanalo.",
         "We made a shared Google Maps list here that you can bookmark."],
    ),
    (
        "Other tourism recommendations?",
        ["Take a helicopter tour or go cageless shark diving on the North Shore.",
         "ATV/Jurassic Park tours at Kualoa Ranch.",
         "Luau.",
         "Polynesian Cultural Center."],
    ),
    (
        "What passports or entry documents do international guests need?",
        ["Canadians can enter the USA on a B2 visitor visa, no pre-application required. Just "
         "state this at the border."],
    ),
    (
        "Other good things to know",
        ["<span class=\"k\">Sunscreen:</span> Hawai\u02bbi bans sunscreens containing "
         "oxybenzone and octinoxate, reef-safe sunscreen is required but easy to find.",
         "<span class=\"k\">Local etiquette:</span> Keep your distance from sea turtles and "
         "Hawaiian monk seals.",
         "<span class=\"k\">Payment:</span> Major credit cards and tap are widely accepted. "
         "Tip standard is 15&ndash;20%. Currency is USD.",
         "<span class=\"k\">Forgot something?</span> Oahu is very developed, so you can buy "
         "anything you need that you forgot (there\u2019s Costco, Target, etc.). ABC stores "
         "are all over Waikiki and sell plenty of helpful things as well (e.g., beach towels, "
         "sunscreen).",
         "<span class=\"k\">In case you are confused:</span> Honolulu is the main town. Oahu "
         "is the island. Hawaii is the state. Waikiki is an area in Honolulu (not a town)."],
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
# guest-list column. Today that is only "Friend Only Events" — a Yes there
# shows the party all three: the beach day, the sunset surf and the sunset
# cruise. If you rename that column in the sheet, change it here in the same
# sitting: a value that matches no column shows the event to nobody, silently.
# ---------------------------------------------------------------------------
ITINERARY = [
    ("Monday, October 18", [
        {
            "time": "11:00 AM \u2013 3:00 PM",
            "name": "Beach Day",
            "optional": True,
            "audience": "Friend Only Events",
            "body": "We\u2019ll have tents up at Makapu\u2019u Beach Park. Bring sunscreen, sun "
                    "protection, beach towels, and anything else you might need to have fun. Rain "
                    "permitting. Food is not easily accessed so we recommend bringing snacks and "
                    "eating before. There is also amazing poke 10 min west in Hawaii Kai at "
                    "HanaPa\u2019a Market.",
            "location": "Makapu\u2019u Beach Park, O\u2019ahu",
            "parking": "Parking should be easy on the weekday in the parking lot, otherwise "
                       "people park along the curved road and walk down.",
        },
        {
            "time": "4:00 PM \u2013 6:00 PM",
            "name": "Sunset Surf",
            "optional": True,
            "audience": "Friend Only Events",
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
            "optional": True,
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
                      "(wedge or capped heels if you feel like it). Most of the area is grass or "
                      "deck so you can also walk around barefoot.",
        },
    ]),
    ("Friday, October 22", [
        {
            "time": "3:30 \u2013 4:00 PM",
            "name": "Arrival",
            "body": "Please arrive in this time window. Because it is a working plant nursery, "
                    "guests are not permitted to arrive on the property before 3:30 on the dot.",
        },
        {
            "time": "4:00 \u2013 4:30 PM",
            "name": "Ceremony",
            "body": "Don\u2019t make us laugh! We will all paddle out to rockpiles surf break, "
                    "where we met. Just kidding. The entire event will take place at one venue "
                    "set against the Ko\u2019olau mountains.",
            "location": "The Plant Place, 41-821 Waikupanaha Street, Waimanalo, O\u2019ahu, 96795",
            "parking": "There is plenty of designated parking on-site.",
            "transportation": "Traffic can be very unpredictable and can take 40\u201360 minutes "
                              "to get to the venue from Honolulu. We recommend monitoring "
                              "traffic throughout the day. We also recommend taking a car with a "
                              "designated driver (there will be parking), or scheduling a taxi or "
                              "Uber in advance. We would highly suggest not waiting until the "
                              "event to schedule an Uber as availability can sometimes be "
                              "unpredictable. On the way back, there will be a shuttle option "
                              "for guests staying in Waikiki.",
            "directions": "After parking or being dropped off, walk down the gravel path. "
                          "You\u2019ll see a clear tent, it\u2019ll be hard to miss.",
            "attire": "Island formal. We suggest lightweight suits and dress shoes for men (ties "
                      "optional) and dresses for women (whatever length is fine). Heels must "
                      "have caps or be wedges due to the grass.",
        },
        {
            "time": "4:30 \u2013 5:30 PM",
            "name": "Champagne Hour",
            "body": "There will be champagne and time to get settled in.",
        },
        {
            "time": "5:30 \u2013 7:00 PM",
            "name": "Reception",
            "body": "There will be a few speeches accompanied by plenty of drinks and fresh "
                    "local appetizers, dinner, and desserts.",
        },
        {
            "time": "7:00 \u2013 10 PM",
            "name": "Afterparty",
            "body": "Open bar, music, and late night snacks. Because of local noise "
                    "regulations, we have a hard stop at 10 PM.",
        },
        {
            "time": "10 \u2013 11 PM",
            "name": "Shuttle Transport",
            "optional": True,
            "body": "An optional shuttle will take guests back to Waikiki. We will message "
                    "closer to the date to confirm if you would like to take the shuttle. You "
                    "can also take a ride back with a designated driver or pre-schedule an Uber "
                    "or Lyft if you don\u2019t prefer the shuttle or are not staying in Waikiki.",
        },
    ]),
    ("Saturday, October 23", [
        {
            "time": "4:30 PM \u2013 7:00 PM",
            "name": "Sunset Sail",
            "optional": True,
            "audience": "Friend Only Events",
            "body": "We will watch the sunset on the Na Hoku Waikiki Sunset Sail catamaran. "
                    "Drinks are included. Children are allowed. Check-in is from 4:30\u20135, "
                    "with a hard cutoff at 5.",
            "parking": "We recommend Uber-ing to Waikiki if you\u2019ll be drinking on the "
                       "catamaran. If you\u2019d like to drive, we recommend using paid parking "
                       "or testing your luck for free street parking on Montsarrat (15 min "
                       "walk).",
        },
    ]),
]

# The columns written to the seed file, in order.
ITINERARY_FIELDS = ["day", "time", "event", "optional", "audience", "body",
                    "location", "parking", "transportation", "directions", "attire"]

