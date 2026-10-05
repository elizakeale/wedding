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
ASSET_VERSION = 77

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
    ("TRAVEL", "travel.html"),
    ("RECOMMENDATIONS", "recommendations.html"),
    ("REGISTRY", "registry.html"),
]

# The footer nav uses a different order than the header (matches Figma): it
# reads across in pairs, RSVP/ITINERARY, TRAVEL/REGISTRY, FAQs/RECOMMENDATIONS.
FOOTER_NAV_ORDER = ["RSVP", "ITINERARY", "TRAVEL", "REGISTRY", "FAQs", "RECOMMENDATIONS"]


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
# Mirrors the doc's FAQS tab exactly: General, Wedding Day, Other.
FAQS = [
    "General",
    (
        "When is the RSVP deadline? What if I need to change my RSVP?",
        ["We kindly ask you to RSVP by June 1, 2027. If you need to change your RSVP, please "
         "email Eliza and Lucas at "
         "<a href=\"mailto:elizakeale@gmail.com\">elizakeale@gmail.com</a>."],
    ),
    (
        "Is it safe to book travel now?",
        ["You can, flights and Airbnbs typically don’t get released until 11 months prior "
         "so they should be starting to open up now. We suggest setting flight alerts on "
         "pricing as it fluctuates quite a bit and prices may be higher since it is further "
         "away. We also will share hotel blocks and Airbnb recommendations soon."],
    ),
    (
        "What if we cannot make it?",
        ["Hawaii is the most isolated land mass on earth, so we will not be offended if you "
         "cannot make it!"],
    ),
    (
        "How can I share my dietary restrictions?",
        ["You can indicate your dietary restrictions in the RSVP form."],
    ),
    (
        "Am I RSVP’ing for my whole party?",
        ["Yes, we will only send communications to one person per party. You can RSVP for "
         "your entire party here."],
    ),
    (
        "Are children welcome?",
        ["Yes! After you enter your party code in the RSVP, you can see which guests are in "
         "your party."],
    ),
    (
        "Can I bring a +1?",
        ["After you enter your party code in the RSVP, you can see which guests are in your "
         "party."],
    ),

    "Wedding Day",
    (
        "What’s the recommended attire?",
        ["Island formal. We suggest lightweight suits and dress shoes for men (ties optional) "
         "and dresses for women (whatever length is fine). The venue requires that heels have "
         "caps or be wedges due to the grass."],
    ),
    (
        "Will there be transportation on the day of?",
        ["<span class=\"k\">Getting there:</span> We recommend either a car with a designated "
         "driver (there will be parking), or scheduling a taxi or Uber in advance. We would "
         "highly suggest not waiting until the event to schedule an Uber as this can sometimes "
         "be unpredictable and the location is 40–60 minutes from Honolulu depending on "
         "traffic.",
         "<span class=\"k\">Getting back:</span> An optional shuttle will take guests back to "
         "Waikiki. We will message closer to the date to confirm if you would like to take the "
         "shuttle. You can also take a ride back with a designated driver or pre-schedule an "
         "Uber or Lyft if you don’t prefer the shuttle or are not staying in Waikiki."],
    ),
    (
        "Where are the pickup points, and when does the last shuttle leave?",
        ["The shuttle will leave from the parking lot. There is only one shuttle since the "
         "event has a hard stop at 10 PM. It will wait until everyone is loaded in!"],
    ),
    (
        "Is it outdoors? What if it rains?",
        ["The entire event will take place at one venue set against the Ko’olau "
         "mountains. There will be a large tent and covered lanai so rain will not affect the "
         "event. Hawaii rain usually does not last long!"],
    ),

    "Other",
    (
        "When will more information be shared?",
        ["This website has the most up to date information. We will send updates over the "
         "coming year as more information comes in or if we need information from you on "
         "your preferences post-RSVP."],
    ),
    (
        "Who should guests contact with questions?",
        ["For friends: Don’t hesitate to contact either Eliza or Lucas directly.",
         "For family: For Eliza’s family, contact Gala. For Lucas’ family, please "
         "contact Kathleen.",
         "On the wedding day, please contact our wedding coordinator (their information will "
         "be shared later).",
         "<br />".join(_CONTACTS),
         "Note: Other trip-related recommendations can be found "
         "<a href=\"../recommendations/\">here</a>."],
    ),
]

# --- Recommendations page (PHASE == "phase-2") -----------------------------
# The doc's "Phase 1" questions now live on the Travel page and in the FAQs, so
# this page is the doc's Phase 2 set only.
_MAPS = "We made a shared Google Maps list here that you can bookmark."

RECOMMENDATIONS = [
    (
        "Can you share food recommendations?",
        ["Yes! Hawaii has amazing seafood, poke, and asian food. " + _MAPS,
         "<span class=\"k\">Our must hit cheap eats are:</span> HanaPa’a Market for "
         "Poke, Pioneer Saloon for quality plate lunch, Rainbow Inn for the classic plate "
         "lunch, Leonard’s for Malasadas donuts, fresh poke + rice at Foodland grocery "
         "stores.",
         "<span class=\"k\">Our top restaurants in Honolulu are:</span> Akasaka Sushi near "
         "Waikiki, Pig &amp; The Lady in Chinatown, Izakaya Nonbei off Kapahulu.",
         "<span class=\"k\">Our top restaurants with views are:</span> Roy’s Hawaii Kai "
         "and Haleiwa Joe’s Haiku Gardens in Kane’ohe."],
    ),
    (
        "Can you share beach recommendations?",
        [("ul", ["For cool views and bigger waves, Makapu’u Beach Park.",
                 "For flat calm water and fine sand, Lanikai.",
                 "For calm water and big stretches of beach, Ke’iki on North Shore.",
                 "For fun smaller waves and lots of space for big groups, Waimanalo."]),
         _MAPS],
    ),
    (
        "Other tourism recommendations?",
        [("ul", [
            "Day trip to North Shore for Dole whip, garlic shrimp, shave ice, Acai bowls, and "
            "large stretch beaches",
            "Day trip to east side and hit Spitting Caves and Makapu’u Tide Pools, the "
            "drive itself is beautiful and winding",
            "Hike Wiliwilinui (our favourite hike, can be done in a few hours and easy to "
            "access, not too dangerous and awesome cliff payoff)",
            "Surf! We recommend RV’s Ocean Sports for lessons.",
            "Snorkel, though you’ll mostly see fish and turtles, not reef unless you take "
            "a boat further out.",
            "Visit Pearl Harbor",
            "Take a helicopter tour (list <a href=\"https://www.tripadvisor.com/"
            "Attraction_Products-g29222-t12026-zfg11864-a_contentId.195810255825+23840390061-"
            "Oahu_Hawaii.html\">here</a>)",
            "Go cage-free shark diving on the North Shore (list <a href=\"https://www."
            "tripadvisor.com/Attraction_Products-g29222-t12061-zfg12023-a_contentId."
            "195810255585+23840390061-Oahu_Hawaii.html\">here</a>)",
            "ATV/Jurassic Park tours at Kualoa Ranch",
            "Airbnb experiences run by locals, like a luau",
            "Get a sunset drink at a nice hotel",
            "Brewery in Kaka’ako",
            "Visit the shops at SALT Kaka’ako",
            "Trendier local shops and cafes in Kaimuki, in Honolulu",
            "For a more lowkey activity, we suggest the Thursday and Sunday Kailua "
            "Farmer’s Market, or the Saturday Kaka’ako Farmer’s Market in "
            "Honolulu. They have tons of local food vendors, not just produce."]),
         "Message Eliza &amp; Lucas if you need more recommendations!"],
    ),
    (
        "Other good things to know",
        ["<span class=\"k\">Sunscreen:</span> Hawaiʻi bans sunscreens containing "
         "oxybenzone and octinoxate, reef-safe sunscreen is required but easy to find.",
         "<span class=\"k\">Payment:</span> Major credit cards and tap are widely accepted. "
         "Standard tip is 15&ndash;20%. Currency is USD.",
         "<span class=\"k\">Forgot something?</span> Oahu is very developed, so you can buy "
         "anything you need that you forgot (there’s Costco, Target, etc.). ABC stores "
         "are all over Waikiki and sell plenty of helpful things as well (e.g., beach towels, "
         "sunscreen).",
         "<span class=\"k\">In case you are confused:</span> Honolulu is the main town. Oahu "
         "is the island. Hawaii is the state. Waikiki is an area in Honolulu (not a town in "
         "itself).",
         "Please contact Eliza &amp; Lucas should you have any other questions!"],
    ),
]

# --- Travel page (PHASE == "phase-2") ---------------------------------------
# SOURCE OF TRUTH: the same Google doc, TRAVEL tab (tab t.tdz7w2dumvxd).
# The doc still has blanks ("____ hotels", "code ___", "email ___") — they are
# carried over as written so they are impossible to miss; fill them in the doc.
TRAVEL = [
    (
        "How do I get to the island?",
        ["Fly into Daniel K. Inouye International Airport in Honolulu, Oahu, Hawaii. This is "
         "the only international airport on Oahu. You could also fly in from another island "
         "if more affordable and you’d like to island hop."],
    ),
    (
        "What dates do you recommend booking our trip for?",
        ["If you’re planning to come for about a week (we hope you do if you’re "
         "flying all the way!), then we recommend aiming to arrive the week before the "
         "wedding, arriving October 15 weekend and flying out Sunday, October 24. We will be "
         "planning completely optional events throughout October 16 through 23, including a "
         "Welcome BBQ on Wednesday, October 20 and the wedding on Friday, October 22. We "
         "recommend visiting the island for at least 6 nights, but the sweet spot is "
         "10&ndash;12 nights if you can swing some island hopping as well."],
    ),
    (
        "Where should we stay on island?",
        ["We recommend staying in Honolulu (“in town”) as it’s a central point "
         "to shops, dining, transportation, and more importantly, where virtually all the "
         "hotels are located. Within Honolulu, the Waikiki neighborhood is the most "
         "tourist-friendly. This is the only location with proper hotels. This is also where "
         "the wedding day return shuttle will be dropping people back off so this is our "
         "recommendation.",
         "We would not recommend staying on the North Shore (Haleiwa, Pupukea, etc.) as "
         "it’s very hard to get to and from (limited transportation options). The "
         "wedding day is mostly on the east (or “Windward”) side, so you could stay "
         "in an Airbnb in this area (e.g., Kane’ohe or Kailua), but for the rest of your "
         "trip, these areas are less central."],
    ),
    (
        "What accommodations should we stay at?",
        ["We have arranged for a 10% discount at ____ hotels, you can book here with code "
         "___. Hotels are often cheaper than Airbnbs.",
         "There are also many Airbnbs on island, we created an Airbnb shared list here.",
         "If you plan to rent a car, we recommend opting for an Airbnb in Honolulu town but "
         "not in Waikiki, as parking is tricky.",
         "If you don’t plan to rent a car or get daily rentals, then you can opt for a "
         "hotel in Waikiki.",
         "<span class=\"k\">Luxury hotels:</span><br />The Royal Hawaiian Resort<br />Prince "
         "Waikiki Hotel<br />Hilton Hawaiian Village<br />Moana Surfrider, A Westin Resort "
         "&amp; Spa<br />Hilton Club Ka Haku Honolulu",
         "<span class=\"k\">Boutique hotels closer to Diamond Head:</span><br />Kaimana "
         "Beach Hotel<br />Lotus Honolulu<br />Queen Kapi’olani Hotel"],
    ),
    (
        "Do I need a rental car?",
        ["If you want freedom to explore the island, we highly recommend getting a rental car "
         "or renting daily cars, as public transportation is limited. We’ve arranged a "
         "10% discount on rental cars with Paradise Rent A Car, email ___ and give code: "
         "rockpiles. Uber and Lyft are also prominent for getting around Honolulu but would be "
         "costly for longer distances across the island outside of Honolulu. We would "
         "definitely suggest not being stuck in Waikiki for your whole trip!"],
    ),
    (
        "How is parking on-island?",
        ["<span class=\"k\">If you’re staying in Waikiki:</span> You’ll need to pay "
         "for overnight parking at a garage (cheaper than hotel), or try your luck on "
         "Montsarrat Ave. You can usually do a couple laps and eventually find a spot.",
         "<span class=\"k\">If you’re staying outside Waikiki but still in "
         "Honolulu:</span> Street parking should not be an issue, check with your host.",
         "<span class=\"k\">If you’re staying outside of Honolulu:</span> Street parking "
         "should not be an issue, check with your host.",
         "Don’t hesitate to message Eliza &amp; Lucas if you need advice on the parking "
         "situation near a hotel or Airbnb. Please look out for parking signs carefully as "
         "towing is very common on island.",
         "We made a shared Google Maps parking list here that you can bookmark."],
    ),
    (
        "What’s the weather like, and what should guests pack?",
        ["October is an ideal time to visit O’ahu because it comes after peak summer "
         "humidity and before winter rainy season. Expect warm and slightly humid with "
         "comfortable daytime highs in the 83&deg;F to 85&deg;F (28&deg;C to 29&deg;C) and "
         "daytime lows of 73&deg;F to 75&deg;F (23&deg;C to 24&deg;C). Water is warm and no "
         "wet suit is required. Rain is often brief and passing, but overall weather in "
         "Hawaii has been unpredictable for the past few years so keep this in mind."],
    ),
    (
        "What passports or entry documents do international guests need?",
        ["Canadians can enter the USA on a B2 visitor visa, no pre-application required. Just "
         "state this at the border."],
    ),
]

# --- Registry page (PHASE == "phase-2") -------------------------------------
# SOURCE OF TRUTH: Figma ("Registry" frame), not the Google doc. The row has no
# heading in the design, just the rule and the copy, then "Visit: ->".
# REGISTRY_URL is the honeymoon-fund link; it isn't in Figma, so it is blank
# until Eliza supplies it.
REGISTRY_URL = ""
REGISTRY = [
    (
        None,
        ["We are so grateful that you’re taking the time, resources, and effort to "
         "travel to Hawaii to celebrate with us. Having our friends and family together is "
         "all we need, and we can’t wait to see you. If you would still like to gift, "
         "you’re welcome to do so here.",
         "VISIT_LINK"],
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
    ("Tuesday, October 19", [
        {
            "time": "4:00 PM \u2013 10:00 PM",
            "name": "Tea Ceremony & Dinner",
            "optional": True,
            "audience": "Family Only Events",
            "body": "We'll have a tea ceremony and dinner.",
            "location": "To be confirmed.",
            "parking": "Will be shared once location is confirmed.",
            "transportation": "Will be shared once location is confirmed.",
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

