import pandas as pd
import csv

tracks = [
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1",
    "pollyear": 1996,
    "position": 1,
    "releaseyear": "1996",
    "track": "Buy Me a Pony"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "2",
    "pollyear": 1996,
    "position": 2,
    "releaseyear": "1996",
    "track": "Stinkfist"
    },
    {
    "alltime": False,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "3",
    "pollyear": 1996,
    "position": 3,
    "releaseyear": "1996",
    "track": "Underground"
    },
    {
    "alltime": False,
    "artist": "Butthole Surfers",
    "country": "USA",
    "id": "4",
    "pollyear": 1996,
    "position": 4,
    "releaseyear": "1996",
    "track": "Pepper"
    },
    {
    "alltime": False,
    "artist": "Bush",
    "country": "UK",
    "id": "5",
    "pollyear": 1996,
    "position": 5,
    "releaseyear": "1996",
    "track": "Glycerine"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "6",
    "pollyear": 1996,
    "position": 6,
    "releaseyear": "1996",
    "track": "Pick You Up"
    },
    {
    "alltime": False,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "7",
    "pollyear": 1996,
    "position": 7,
    "releaseyear": "1996",
    "track": "Breathe"
    },
    {
    "alltime": False,
    "artist": "Allen Ginsberg",
    "country": "USA",
    "id": "8",
    "pollyear": 1996,
    "position": 8,
    "releaseyear": "1996",
    "track": "Ballad of the Skeletons"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "9",
    "pollyear": 1996,
    "position": 9,
    "releaseyear": "1996",
    "track": "El Scorcho"
    },
    {
    "alltime": False,
    "artist": "311",
    "country": "USA",
    "id": "10",
    "pollyear": 1996,
    "position": 11,
    "releaseyear": "1996",
    "track": "Down"
    },
    {
    "alltime": False,
    "artist": "Underworld",
    "country": "UK",
    "id": "11",
    "pollyear": 1996,
    "position": 12,
    "releaseyear": "1996",
    "track": "Born Slippy"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "12",
    "pollyear": 1996,
    "position": 13,
    "releaseyear": "1996",
    "track": "1979"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "13",
    "pollyear": 1996,
    "position": 15,
    "releaseyear": "1996",
    "track": "Kong Foo Sing"
    },
    {
    "alltime": False,
    "artist": "Babylon Zoo",
    "country": "UK",
    "id": "14",
    "pollyear": 1996,
    "position": 16,
    "releaseyear": "1996",
    "track": "Spaceman"
    },
    {
    "alltime": False,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "15",
    "pollyear": 1996,
    "position": 17,
    "releaseyear": "1996",
    "track": "Firestarter"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "16",
    "pollyear": 1996,
    "position": 18,
    "releaseyear": "1996",
    "track": "D.A.F."
    },
    {
    "alltime": False,
    "artist": "Bush",
    "country": "UK",
    "id": "17",
    "pollyear": 1996,
    "position": 19,
    "releaseyear": "1996",
    "track": "Swallowed"
    },
    {
    "alltime": False,
    "artist": "The Fauves",
    "country": "Australia",
    "id": "18",
    "pollyear": 1996,
    "position": 20,
    "releaseyear": "1996",
    "track": "Dogs Are the Best People"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "19",
    "pollyear": 1996,
    "position": 21,
    "releaseyear": "1996",
    "track": "Down in the Park"
    },
    {
    "alltime": False,
    "artist": "Ash",
    "country": "Ireland",
    "id": "20",
    "pollyear": 1996,
    "position": 22,
    "releaseyear": "1996",
    "track": "Oh Yeah"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "21",
    "pollyear": 1996,
    "position": 23,
    "releaseyear": "1996",
    "track": "I Sucked a Lot of Cock to Get Where I Am"
    },
    {
    "alltime": False,
    "artist": "Everclear",
    "country": "USA",
    "id": "22",
    "pollyear": 1996,
    "position": 24,
    "releaseyear": "1996",
    "track": "Santa Monica"
    },
    {
    "alltime": False,
    "artist": "No Doubt",
    "country": "USA",
    "id": "23",
    "pollyear": 1996,
    "position": 25,
    "releaseyear": "1996",
    "track": "Just a Girl"
    },
    {
    "alltime": False,
    "artist": "Chemical Brothers",
    "country": "UK",
    "id": "24",
    "pollyear": 1996,
    "position": 26,
    "releaseyear": "1996",
    "track": "Setting Sun"
    },
    {
    "alltime": False,
    "artist": "Cake",
    "country": "USA",
    "id": "25",
    "pollyear": 1996,
    "position": 27,
    "releaseyear": "1996",
    "track": "The Distance"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "26",
    "pollyear": 1996,
    "position": 28,
    "releaseyear": "1996",
    "track": "Zero"
    },
    {
    "alltime": False,
    "artist": "The Fauves",
    "country": "Australia",
    "id": "27",
    "pollyear": 1996,
    "position": 30,
    "releaseyear": "1996",
    "track": "Self Abuser"
    },
    {
    "alltime": False,
    "artist": "Skin",
    "country": "UK",
    "id": "28",
    "pollyear": 1996,
    "position": 31,
    "releaseyear": "1996",
    "track": "Mah Na Mah Na"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "29",
    "pollyear": 1996,
    "position": 32,
    "releaseyear": "1996",
    "track": "Living Type"
    },
    {
    "alltime": False,
    "artist": "2Pac",
    "country": "USA",
    "id": "30",
    "pollyear": 1996,
    "position": 33,
    "releaseyear": "1996",
    "track": "California Love"
    },
    {
    "alltime": False,
    "artist": "Tracy Bonham",
    "country": "USA",
    "id": "31",
    "pollyear": 1996,
    "position": 34,
    "releaseyear": "1996",
    "track": "Mother Mother"
    },
    {
    "alltime": False,
    "artist": "Fugees",
    "country": "USA",
    "id": "32",
    "pollyear": 1996,
    "position": 35,
    "releaseyear": "1996",
    "track": "Killing Me Softly"
    },
    {
    "alltime": False,
    "artist": "Primitive Radio Gods",
    "country": "USA",
    "id": "33",
    "pollyear": 1996,
    "position": 36,
    "releaseyear": "1996",
    "track": "Standing Outside a Broken Phone Booth with Money in My Hand"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "34",
    "pollyear": 1996,
    "position": 37,
    "releaseyear": "1996",
    "track": "Virtual Insanity"
    },
    {
    "alltime": False,
    "artist": "Bush",
    "country": "UK",
    "id": "35",
    "pollyear": 1996,
    "position": 38,
    "releaseyear": "1996",
    "track": "Comedown"
    },
    {
    "alltime": False,
    "artist": "The Eels",
    "country": "USA",
    "id": "36",
    "pollyear": 1996,
    "position": 39,
    "releaseyear": "1996",
    "track": "Novocaine for the Soul"
    },
    {
    "alltime": False,
    "artist": "Tricky/Garbage",
    "country": "UK",
    "id": "37",
    "pollyear": 1996,
    "position": 40,
    "releaseyear": "1996",
    "track": "Milk"
    },
    {
    "alltime": False,
    "artist": "Geggy Tah",
    "country": "USA",
    "id": "38",
    "pollyear": 1996,
    "position": 41,
    "releaseyear": "1996",
    "track": "Whoever You Are"
    },
    {
    "alltime": False,
    "artist": "Fini Scad",
    "country": "Australia",
    "id": "39",
    "pollyear": 1996,
    "position": 42,
    "releaseyear": "1996",
    "track": "Coppertone"
    },
    {
    "alltime": False,
    "artist": "The Cranberries",
    "country": "Ireland",
    "id": "40",
    "pollyear": 1996,
    "position": 44,
    "releaseyear": "1996",
    "track": "Salvation"
    },
    {
    "alltime": False,
    "artist": "Nirvana",
    "country": "USA",
    "id": "41",
    "pollyear": 1996,
    "position": 45,
    "releaseyear": "1996",
    "track": "Aneurysm {Muddy Banks of the Wishka live version}"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "42",
    "pollyear": 1996,
    "position": 46,
    "releaseyear": "1996",
    "track": "Bulls on Parade"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "43",
    "pollyear": 1996,
    "position": 47,
    "releaseyear": "1996",
    "track": "Hail, Hail"
    },
    {
    "alltime": False,
    "artist": "Nada Surf",
    "country": "USA",
    "id": "44",
    "pollyear": 1996,
    "position": 48,
    "releaseyear": "1996",
    "track": "Popular"
    },
    {
    "alltime": False,
    "artist": "Definition of Sound",
    "country": "UK",
    "id": "45",
    "pollyear": 1996,
    "position": 49,
    "releaseyear": "1996",
    "track": "Pass the Vibes"
    },
    {
    "alltime": False,
    "artist": "The Presidents of the USA",
    "country": "USA",
    "id": "46",
    "pollyear": 1996,
    "position": 50,
    "releaseyear": "1996",
    "track": "Mach 5"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "47",
    "pollyear": 1996,
    "position": 51,
    "releaseyear": "1996",
    "track": "Only Happy When It Rains"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "48",
    "pollyear": 1996,
    "position": 52,
    "releaseyear": "1996",
    "track": "Until It Sleeps"
    },
    {
    "alltime": False,
    "artist": "Bjork",
    "country": "Iceland",
    "id": "49",
    "pollyear": 1996,
    "position": 53,
    "releaseyear": "1996",
    "track": "Hyperballad"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "50",
    "pollyear": 1996,
    "position": 55,
    "releaseyear": "1996",
    "track": "Tonight, Tonight"
    },
    {
    "alltime": False,
    "artist": "Everclear",
    "country": "USA",
    "id": "51",
    "pollyear": 1996,
    "position": 58,
    "releaseyear": "1996",
    "track": "Heartspark Dollarsign"
    },
    {
    "alltime": False,
    "artist": "Tumbleweed",
    "country": "Australia",
    "id": "52",
    "pollyear": 1996,
    "position": 59,
    "releaseyear": "1996",
    "track": "Silver Lizard"
    },
    {
    "alltime": False,
    "artist": "Kula Shaker",
    "country": "UK",
    "id": "53",
    "pollyear": 1996,
    "position": 60,
    "releaseyear": "1996",
    "track": "Hey Dude"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "54",
    "pollyear": 1996,
    "position": 62,
    "releaseyear": "1996",
    "track": "Hero of the Day"
    },
    {
    "alltime": False,
    "artist": "Bad Religion",
    "country": "USA",
    "id": "55",
    "pollyear": 1996,
    "position": 63,
    "releaseyear": "1996",
    "track": "Punk Rock Song"
    },
    {
    "alltime": False,
    "artist": "Angelique Kidjo",
    "country": "Benin",
    "id": "56",
    "pollyear": 1996,
    "position": 64,
    "releaseyear": "1996",
    "track": "Wombo Lombo"
    },
    {
    "alltime": False,
    "artist": "Goldfinger",
    "country": "USA",
    "id": "57",
    "pollyear": 1996,
    "position": 65,
    "releaseyear": "1996",
    "track": "Here in Your Bedroom"
    },
    {
    "alltime": False,
    "artist": "Crowded House",
    "country": "Australia",
    "id": "58",
    "pollyear": 1996,
    "position": 67,
    "releaseyear": "1996",
    "track": "Everything Is Good for You"
    },
    {
    "alltime": False,
    "artist": "Mullen/Clayton",
    "country": "Ireland",
    "id": "59",
    "pollyear": 1996,
    "position": 68,
    "releaseyear": "1996",
    "track": "Mission Impossible"
    },
    {
    "alltime": False,
    "artist": "Insurge",
    "country": "Australia",
    "id": "60",
    "pollyear": 1996,
    "position": 69,
    "releaseyear": "1996",
    "track": "Speculator"
    },
    {
    "alltime": False,
    "artist": "Pulp",
    "country": "UK",
    "id": "61",
    "pollyear": 1996,
    "position": 71,
    "releaseyear": "1996",
    "track": "Disco 2000"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "62",
    "pollyear": 1996,
    "position": 72,
    "releaseyear": "1996",
    "track": "Punch in the Face"
    },
    {
    "alltime": False,
    "artist": "Hole",
    "country": "USA",
    "id": "63",
    "pollyear": 1996,
    "position": 73,
    "releaseyear": "1996",
    "track": "Gold Dust Woman"
    },
    {
    "alltime": False,
    "artist": "Ministry",
    "country": "USA",
    "id": "64",
    "pollyear": 1996,
    "position": 74,
    "releaseyear": "1996",
    "track": "Lay Lady Lay"
    },
    {
    "alltime": False,
    "artist": "Spacehog",
    "country": "UK",
    "id": "65",
    "pollyear": 1996,
    "position": 76,
    "releaseyear": "1996",
    "track": "In the Meantime"
    },
    {
    "alltime": False,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "66",
    "pollyear": 1996,
    "position": 77,
    "releaseyear": "1996",
    "track": "Burden in My Hand"
    },
    {
    "alltime": False,
    "artist": "OMC",
    "country": "New Zealand",
    "id": "67",
    "pollyear": 1996,
    "position": 78,
    "releaseyear": "1996",
    "track": "How Bizarre"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "68",
    "pollyear": 1996,
    "position": 79,
    "releaseyear": "1996",
    "track": "I Make Hamburgers"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "69",
    "pollyear": 1996,
    "position": 80,
    "releaseyear": "1996",
    "track": "Soldiers"
    },
    {
    "alltime": False,
    "artist": "The Superjesus",
    "country": "Australia",
    "id": "70",
    "pollyear": 1996,
    "position": 81,
    "releaseyear": "1996",
    "track": "Shut My Eyes"
    },
    {
    "alltime": False,
    "artist": "Luscious Jackson",
    "country": "USA",
    "id": "71",
    "pollyear": 1996,
    "position": 82,
    "releaseyear": "1996",
    "track": "Naked Eye"
    },
    {
    "alltime": False,
    "artist": "Hoodoo Gurus",
    "country": "Australia",
    "id": "72",
    "pollyear": 1996,
    "position": 83,
    "releaseyear": "1996",
    "track": "Waking Up Tired"
    },
    {
    "alltime": False,
    "artist": "Ash",
    "country": "UK",
    "id": "73",
    "pollyear": 1996,
    "position": 85,
    "releaseyear": "1996",
    "track": "Goldfinger"
    },
    {
    "alltime": False,
    "artist": "Neneh Cherry",
    "country": "Sweden",
    "id": "74",
    "pollyear": 1996,
    "position": 86,
    "releaseyear": "1996",
    "track": "Woman"
    },
    {
    "alltime": False,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "75",
    "pollyear": 1996,
    "position": 87,
    "releaseyear": "1996",
    "track": "E-Bow the Letter"
    },
    {
    "alltime": False,
    "artist": "Hunting Party",
    "country": "Australia",
    "id": "76",
    "pollyear": 1996,
    "position": 88,
    "releaseyear": "1996",
    "track": "Grooving"
    },
    {
    "alltime": False,
    "artist": "Snout",
    "country": "Australia",
    "id": "77",
    "pollyear": 1996,
    "position": 89,
    "releaseyear": "1996",
    "track": "Cromagnon Man"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "78",
    "pollyear": 1996,
    "position": 90,
    "releaseyear": "1996",
    "track": "Leaving Here"
    },
    {
    "alltime": False,
    "artist": "Barry Adamson",
    "country": "UK",
    "id": "79",
    "pollyear": 1996,
    "position": 91,
    "releaseyear": "1996",
    "track": "Set the Controls"
    },
    {
    "alltime": False,
    "artist": "Skunk Anansie",
    "country": "UK",
    "id": "80",
    "pollyear": 1996,
    "position": 93,
    "releaseyear": "1996",
    "track": "All I Want"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "81",
    "pollyear": 1996,
    "position": 94,
    "releaseyear": "1996",
    "track": "Mankind"
    },
    {
    "alltime": False,
    "artist": "Frank Bennett",
    "country": "Australia",
    "id": "82",
    "pollyear": 1996,
    "position": 95,
    "releaseyear": "1996",
    "track": "Creep"
    },
    {
    "alltime": False,
    "artist": "AC/DC",
    "country": "Australia",
    "id": "83",
    "pollyear": 1996,
    "position": 97,
    "releaseyear": "1996",
    "track": "Hail Caesar"
    },
    {
    "alltime": False,
    "artist": "Tori Amos",
    "country": "USA",
    "id": "84",
    "pollyear": 1996,
    "position": 98,
    "releaseyear": "1996",
    "track": "Professional Widow"
    },
    {
    "alltime": False,
    "artist": "Republica",
    "country": "UK",
    "id": "85",
    "pollyear": 1996,
    "position": 99,
    "releaseyear": "1996",
    "track": "Ready to Go"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "86",
    "pollyear": 1996,
    "position": 100,
    "releaseyear": "1996",
    "track": "Gold to Me"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "87",
    "pollyear": 1991,
    "position": 1,
    "releaseyear": "1991",
    "track": "Smells Like Teen Spirit"
    },
    {
    "alltime": True,
    "artist": "Joy Division",
    "country": "UK",
    "id": "88",
    "pollyear": 1991,
    "position": 2,
    "releaseyear": "1979",
    "track": "Love Will Tear Us Apart"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "89",
    "pollyear": 1991,
    "position": 3,
    "releaseyear": "1991",
    "track": "Lithium"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "90",
    "pollyear": 1991,
    "position": 4,
    "releaseyear": "1985",
    "track": "Throw Your Arms Around Me"
    },
    {
    "alltime": True,
    "artist": "Andy Prieboy",
    "country": "USA",
    "id": "91",
    "pollyear": 1991,
    "position": 5,
    "releaseyear": "1990",
    "track": "Tomorrow Wendy"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "92",
    "pollyear": 1991,
    "position": 6,
    "releaseyear": "1984",
    "track": "How Soon Is Now?"
    },
    {
    "alltime": True,
    "artist": "The Stone Roses",
    "country": "UK",
    "id": "93",
    "pollyear": 1991,
    "position": 7,
    "releaseyear": "1989",
    "track": "Fools Gold"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "94",
    "pollyear": 1991,
    "position": 8,
    "releaseyear": "1980",
    "track": "A Forest"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "95",
    "pollyear": 1991,
    "position": 9,
    "releaseyear": "1982",
    "track": "Blister In The Sun"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "96",
    "pollyear": 1991,
    "position": 10,
    "releaseyear": "1983",
    "track": "Blue Monday"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "97",
    "pollyear": 1991,
    "position": 11,
    "releaseyear": "1987",
    "track": "Just Like Heaven"
    },
    {
    "alltime": True,
    "artist": "The The",
    "country": "UK",
    "id": "98",
    "pollyear": 1991,
    "position": 13,
    "releaseyear": "1983",
    "track": "Uncertain Smile"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "99",
    "pollyear": 1991,
    "position": 14,
    "releaseyear": "1990",
    "track": "The Ship Song"
    },
    {
    "alltime": True,
    "artist": "The Cult",
    "country": "UK",
    "id": "100",
    "pollyear": 1991,
    "position": 16,
    "releaseyear": "1985",
    "track": "She Sells Sanctuary"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "101",
    "pollyear": 1991,
    "position": 18,
    "releaseyear": "1982",
    "track": "Add It Up"
    },
    {
    "alltime": True,
    "artist": "Kate Bush",
    "country": "UK",
    "id": "102",
    "pollyear": 1991,
    "position": 19,
    "releaseyear": "1978",
    "track": "Wuthering Heights"
    },
    {
    "alltime": True,
    "artist": "Falling Joys",
    "country": "Australia",
    "id": "103",
    "pollyear": 1991,
    "position": 20,
    "releaseyear": "1990",
    "track": "Lock It"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "104",
    "pollyear": 1991,
    "position": 21,
    "releaseyear": "1983",
    "track": "Kiss Off"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "105",
    "pollyear": 1991,
    "position": 22,
    "releaseyear": "1991",
    "track": "Sexuality"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "106",
    "pollyear": 1991,
    "position": 24,
    "releaseyear": "1986",
    "track": "Bizarre Love Triangle"
    },
    {
    "alltime": True,
    "artist": "Sex Pistols",
    "country": "UK",
    "id": "107",
    "pollyear": 1991,
    "position": 25,
    "releaseyear": "1976",
    "track": "Anarchy in the U.K."
    },
    {
    "alltime": True,
    "artist": "Dead Kennedys",
    "country": "USA",
    "id": "108",
    "pollyear": 1991,
    "position": 26,
    "releaseyear": "1980",
    "track": "Holiday in Cambodia"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "109",
    "pollyear": 1991,
    "position": 28,
    "releaseyear": "1989",
    "track": "Debaser"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "110",
    "pollyear": 1991,
    "position": 29,
    "releaseyear": "1983",
    "track": "This Charming Man"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "111",
    "pollyear": 1991,
    "position": 30,
    "releaseyear": "1971",
    "track": "Stairway to Heaven"
    },
    {
    "alltime": True,
    "artist": "The Church",
    "country": "Australia",
    "id": "112",
    "pollyear": 1991,
    "position": 31,
    "releaseyear": "1988",
    "track": "Under the Milky Way"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "113",
    "pollyear": 1991,
    "position": 32,
    "releaseyear": "1991",
    "track": "Losing My Religion"
    },
    {
    "alltime": True,
    "artist": "Clouds",
    "country": "Australia",
    "id": "114",
    "pollyear": 1991,
    "position": 33,
    "releaseyear": "1991",
    "track": "Hieronymus"
    },
    {
    "alltime": True,
    "artist": "Died Pretty",
    "country": "Australia",
    "id": "115",
    "pollyear": 1991,
    "position": 34,
    "releaseyear": "1991",
    "track": "DC"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "116",
    "pollyear": 1991,
    "position": 35,
    "releaseyear": "1981",
    "track": "Primary"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "117",
    "pollyear": 1991,
    "position": 36,
    "releaseyear": "1986",
    "track": "There Is a Light That Never Goes Out"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "118",
    "pollyear": 1991,
    "position": 37,
    "releaseyear": "1985",
    "track": "Close to Me"
    },
    {
    "alltime": True,
    "artist": "Boys Next Door",
    "country": "Australia",
    "id": "119",
    "pollyear": 1991,
    "position": 38,
    "releaseyear": "1978",
    "track": "Shivers"
    },
    {
    "alltime": True,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "120",
    "pollyear": 1991,
    "position": 39,
    "releaseyear": "1991",
    "track": "Give It Away"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "121",
    "pollyear": 1991,
    "position": 40,
    "releaseyear": "1987",
    "track": "The One I Love"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "122",
    "pollyear": 1991,
    "position": 44,
    "releaseyear": "1989",
    "track": "Lullaby"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "123",
    "pollyear": 1991,
    "position": 45,
    "releaseyear": "1982",
    "track": "Talking to a Stranger"
    },
    {
    "alltime": True,
    "artist": "They Might Be Giants",
    "country": "USA",
    "id": "124",
    "pollyear": 1991,
    "position": 46,
    "releaseyear": "1990",
    "track": "Birdhouse in Your Soul"
    },
    {
    "alltime": True,
    "artist": "Radio Birdman",
    "country": "Australia",
    "id": "125",
    "pollyear": 1991,
    "position": 47,
    "releaseyear": "1978",
    "track": "Aloha Steve and Danno"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "126",
    "pollyear": 1991,
    "position": 48,
    "releaseyear": "1985",
    "track": "In Between Days"
    },
    {
    "alltime": True,
    "artist": "Queen",
    "country": "UK",
    "id": "127",
    "pollyear": 1991,
    "position": 49,
    "releaseyear": "1975",
    "track": "Bohemian Rhapsody"
    },
    {
    "alltime": True,
    "artist": "This Mortal Coil",
    "country": "UK",
    "id": "128",
    "pollyear": 1991,
    "position": 50,
    "releaseyear": "1983",
    "track": "Song to the Siren"
    },
    {
    "alltime": True,
    "artist": "Tall Tales and True",
    "country": "Australia",
    "id": "129",
    "pollyear": 1991,
    "position": 51,
    "releaseyear": "1989",
    "track": "Trust"
    },
    {
    "alltime": True,
    "artist": "The Triffids",
    "country": "Australia",
    "id": "130",
    "pollyear": 1991,
    "position": 52,
    "releaseyear": "1986",
    "track": "Wide Open Road"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "131",
    "pollyear": 1991,
    "position": 53,
    "releaseyear": "1984",
    "track": "The Slab"
    },
    {
    "alltime": True,
    "artist": "Soft Cell",
    "country": "UK",
    "id": "132",
    "pollyear": 1991,
    "position": 54,
    "releaseyear": "1981",
    "track": "Tainted Love"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "133",
    "pollyear": 1991,
    "position": 55,
    "releaseyear": "1987",
    "track": "True Faith"
    },
    {
    "alltime": True,
    "artist": "Sonic Youth",
    "country": "USA",
    "id": "134",
    "pollyear": 1991,
    "position": 56,
    "releaseyear": "1990",
    "track": "Kool Thing"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "135",
    "pollyear": 1991,
    "position": 57,
    "releaseyear": "1988",
    "track": "Waiting for the Great Leap Forward"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "136",
    "pollyear": 1991,
    "position": 58,
    "releaseyear": "1975",
    "track": "Wish You Were Here"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "137",
    "pollyear": 1991,
    "position": 59,
    "releaseyear": "1967",
    "track": "The End"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "138",
    "pollyear": 1991,
    "position": 60,
    "releaseyear": "1991",
    "track": "Enter Sandman"
    },
    {
    "alltime": True,
    "artist": "The Jimi Hendrix Experience",
    "country": "USA",
    "id": "139",
    "pollyear": 1991,
    "position": 61,
    "releaseyear": "1968",
    "track": "All Along the Watchtower"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "140",
    "pollyear": 1991,
    "position": 62,
    "releaseyear": "1988",
    "track": "Orange Crush"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "141",
    "pollyear": 1991,
    "position": 63,
    "releaseyear": "1991",
    "track": "The Unforgiven"
    },
    {
    "alltime": True,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "142",
    "pollyear": 1991,
    "position": 64,
    "releaseyear": "1991",
    "track": "Unfinished Sympathy"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "143",
    "pollyear": 1991,
    "position": 65,
    "releaseyear": "1986",
    "track": "Fall On Me"
    },
    {
    "alltime": True,
    "artist": "Straitjacket Fits",
    "country": "New Zealand",
    "id": "144",
    "pollyear": 1991,
    "position": 66,
    "releaseyear": "1990",
    "track": "Down in Splendour"
    },
    {
    "alltime": True,
    "artist": "Clouds",
    "country": "Australia",
    "id": "145",
    "pollyear": 1991,
    "position": 67,
    "releaseyear": "1991",
    "track": "4 PM"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "146",
    "pollyear": 1991,
    "position": 68,
    "releaseyear": "1989",
    "track": "Pictures of You"
    },
    {
    "alltime": True,
    "artist": "Frente!",
    "country": "Australia",
    "id": "147",
    "pollyear": 1991,
    "position": 69,
    "releaseyear": "1991",
    "track": "Labour of Love"
    },
    {
    "alltime": True,
    "artist": "The Church",
    "country": "Australia",
    "id": "148",
    "pollyear": 1991,
    "position": 70,
    "releaseyear": "1981",
    "track": "The Unguarded Moment"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "149",
    "pollyear": 1991,
    "position": 72,
    "releaseyear": "1986",
    "track": "Bigmouth Strikes Again"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "150",
    "pollyear": 1991,
    "position": 73,
    "releaseyear": "1979",
    "track": "Comfortably Numb"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "151",
    "pollyear": 1991,
    "position": 74,
    "releaseyear": "1983",
    "track": "The Lovecats"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "152",
    "pollyear": 1991,
    "position": 75,
    "releaseyear": "1986",
    "track": "Levi Stubbs Tears"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "153",
    "pollyear": 1991,
    "position": 76,
    "releaseyear": "1991",
    "track": "Come As You Are"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "154",
    "pollyear": 1991,
    "position": 78,
    "releaseyear": "1971",
    "track": "L.A Woman"
    },
    {
    "alltime": True,
    "artist": "Dinosaur Jr",
    "country": "USA",
    "id": "155",
    "pollyear": 1991,
    "position": 79,
    "releaseyear": "1988",
    "track": "Freak Scene"
    },
    {
    "alltime": True,
    "artist": "Def FX",
    "country": "Australia",
    "id": "156",
    "pollyear": 1991,
    "position": 80,
    "releaseyear": "1990",
    "track": "Surfers of the Mind"
    },
    {
    "alltime": True,
    "artist": "The Stone Roses",
    "country": "UK",
    "id": "157",
    "pollyear": 1991,
    "position": 81,
    "releaseyear": "1989",
    "track": "She Bangs The Drums"
    },
    {
    "alltime": True,
    "artist": "Ride",
    "country": "UK",
    "id": "158",
    "pollyear": 1991,
    "position": 82,
    "releaseyear": "1991",
    "track": "Vapour Trail"
    },
    {
    "alltime": True,
    "artist": "Yothu Yindi",
    "country": "Australia",
    "id": "159",
    "pollyear": 1991,
    "position": 83,
    "releaseyear": "1991",
    "track": "Treaty"
    },
    {
    "alltime": True,
    "artist": "The Only Ones",
    "country": "UK",
    "id": "160",
    "pollyear": 1991,
    "position": 84,
    "releaseyear": "1978",
    "track": "Another Girl, Another Planet"
    },
    {
    "alltime": True,
    "artist": "The Wonder Stuff",
    "country": "UK",
    "id": "161",
    "pollyear": 1991,
    "position": 86,
    "releaseyear": "1991",
    "track": "The Size of a Cow"
    },
    {
    "alltime": True,
    "artist": "The Rolling Stones",
    "country": "UK",
    "id": "162",
    "pollyear": 1991,
    "position": 87,
    "releaseyear": "1968",
    "track": "Sympathy for the Devil"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "163",
    "pollyear": 1991,
    "position": 88,
    "releaseyear": "1988",
    "track": "Mercy Seat"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "164",
    "pollyear": 1991,
    "position": 89,
    "releaseyear": "1989",
    "track": "One"
    },
    {
    "alltime": True,
    "artist": "My Bloody Valentine",
    "country": "Ireland",
    "id": "165",
    "pollyear": 1991,
    "position": 90,
    "releaseyear": "1991",
    "track": "Soon"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "166",
    "pollyear": 1991,
    "position": 91,
    "releaseyear": "1989",
    "track": "Monkey Gone to Heaven"
    },
    {
    "alltime": True,
    "artist": "Public Enemy",
    "country": "USA",
    "id": "167",
    "pollyear": 1991,
    "position": 92,
    "releaseyear": "1987",
    "track": "Bring the Noise"
    },
    {
    "alltime": True,
    "artist": "XTC",
    "country": "UK",
    "id": "168",
    "pollyear": 1991,
    "position": 93,
    "releaseyear": "1986",
    "track": "Dear God"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "169",
    "pollyear": 1991,
    "position": 94,
    "releaseyear": "1989",
    "track": "Wave Of Mutilation"
    },
    {
    "alltime": True,
    "artist": "Jesus Jones",
    "country": "UK",
    "id": "170",
    "pollyear": 1991,
    "position": 95,
    "releaseyear": "1989",
    "track": "Info Freako"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "171",
    "pollyear": 1991,
    "position": 96,
    "releaseyear": "1983",
    "track": "Cattle and Cane"
    },
    {
    "alltime": True,
    "artist": "The Clash",
    "country": "UK",
    "id": "172",
    "pollyear": 1991,
    "position": 97,
    "releaseyear": "1979",
    "track": "London Calling"
    },
    {
    "alltime": True,
    "artist": "U2",
    "country": "Ireland",
    "id": "173",
    "pollyear": 1991,
    "position": 98,
    "releaseyear": "1984",
    "track": "Bad"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "174",
    "pollyear": 1991,
    "position": 99,
    "releaseyear": "1988",
    "track": "Deanna"
    },
    {
    "alltime": True,
    "artist": "Prince",
    "country": "USA",
    "id": "175",
    "pollyear": 1991,
    "position": 100,
    "releaseyear": "1991",
    "track": "Cream"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "176",
    "pollyear": 2002,
    "position": 1,
    "releaseyear": "2002",
    "track": "No One Knows"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "177",
    "pollyear": 2002,
    "position": 2,
    "releaseyear": "2002",
    "track": "Chemical Heart"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "178",
    "pollyear": 2002,
    "position": 3,
    "releaseyear": "2002",
    "track": "London Still"
    },
    {
    "alltime": False,
    "artist": "1200 Techniques",
    "country": "Australia",
    "id": "179",
    "pollyear": 2002,
    "position": 4,
    "releaseyear": "2002",
    "track": "Karma"
    },
    {
    "alltime": False,
    "artist": "The Vines",
    "country": "Australia",
    "id": "180",
    "pollyear": 2002,
    "position": 5,
    "releaseyear": "2002",
    "track": "Get Free"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "181",
    "pollyear": 2002,
    "position": 6,
    "releaseyear": "2002",
    "track": "Rollercoaster"
    },
    {
    "alltime": False,
    "artist": "Eminem",
    "country": "USA",
    "id": "182",
    "pollyear": 2002,
    "position": 7,
    "releaseyear": "2002",
    "track": "Lose Yourself"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "183",
    "pollyear": 2002,
    "position": 8,
    "releaseyear": "2002",
    "track": "Pussytown"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "184",
    "pollyear": 2002,
    "position": 9,
    "releaseyear": "2002",
    "track": "By the Way"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "185",
    "pollyear": 2002,
    "position": 10,
    "releaseyear": "2002",
    "track": "The Greatest View"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "186",
    "pollyear": 2002,
    "position": 11,
    "releaseyear": "2002",
    "track": "The One"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "187",
    "pollyear": 2002,
    "position": 13,
    "releaseyear": "2002",
    "track": "All My Life"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "188",
    "pollyear": 2002,
    "position": 14,
    "releaseyear": "2002",
    "track": "Lost Control"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "189",
    "pollyear": 2002,
    "position": 15,
    "releaseyear": "2002",
    "track": "No Reason"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "190",
    "pollyear": 2002,
    "position": 16,
    "releaseyear": "2002",
    "track": "The Zephyr Song"
    },
    {
    "alltime": False,
    "artist": "Eminem",
    "country": "USA",
    "id": "191",
    "pollyear": 2002,
    "position": 17,
    "releaseyear": "2002",
    "track": "Without Me"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "192",
    "pollyear": 2002,
    "position": 18,
    "releaseyear": "2002",
    "track": "Toxicity"
    },
    {
    "alltime": False,
    "artist": "The Vines",
    "country": "Australia",
    "id": "193",
    "pollyear": 2002,
    "position": 19,
    "releaseyear": "2002",
    "track": "Highly Evolved"
    },
    {
    "alltime": False,
    "artist": "Audioslave",
    "country": "USA",
    "id": "194",
    "pollyear": 2002,
    "position": 20,
    "releaseyear": "2002",
    "track": "Cochise"
    },
    {
    "alltime": False,
    "artist": "The Vines",
    "country": "Australia",
    "id": "195",
    "pollyear": 2002,
    "position": 21,
    "releaseyear": "2002",
    "track": "Outtathaway!!"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "196",
    "pollyear": 2002,
    "position": 22,
    "releaseyear": "2002",
    "track": "Something Borrowed, Something Blue"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "197",
    "pollyear": 2002,
    "position": 23,
    "releaseyear": "2002",
    "track": "Times Like These"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "198",
    "pollyear": 2002,
    "position": 25,
    "releaseyear": "2002",
    "track": "Without You"
    },
    {
    "alltime": False,
    "artist": "Salmon Hater",
    "country": "Australia",
    "id": "199",
    "pollyear": 2002,
    "position": 26,
    "releaseyear": "2002",
    "track": "6.66"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "200",
    "pollyear": 2002,
    "position": 27,
    "releaseyear": "2002",
    "track": "Home Is Where the Heart Is"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "201",
    "pollyear": 2002,
    "position": 28,
    "releaseyear": "2002",
    "track": "I Am Mine"
    },
    {
    "alltime": False,
    "artist": "Motor Ace",
    "country": "Australia",
    "id": "202",
    "pollyear": 2002,
    "position": 29,
    "releaseyear": "2002",
    "track": "Carry On"
    },
    {
    "alltime": False,
    "artist": "The Vines",
    "country": "Australia",
    "id": "203",
    "pollyear": 2002,
    "position": 30,
    "releaseyear": "2002",
    "track": "Ms. Jackson"
    },
    {
    "alltime": False,
    "artist": "Bodyjar",
    "country": "Australia",
    "id": "204",
    "pollyear": 2002,
    "position": 31,
    "releaseyear": "2002",
    "track": "One in a Million"
    },
    {
    "alltime": False,
    "artist": "George",
    "country": "Australia",
    "id": "205",
    "pollyear": 2002,
    "position": 32,
    "releaseyear": "2002",
    "track": "Release"
    },
    {
    "alltime": False,
    "artist": "The Hives",
    "country": "Sweden",
    "id": "206",
    "pollyear": 2002,
    "position": 33,
    "releaseyear": "2002",
    "track": "Hate to Say I Told You So"
    },
    {
    "alltime": False,
    "artist": "Pacifier",
    "country": "New Zealand",
    "id": "207",
    "pollyear": 2002,
    "position": 34,
    "releaseyear": "2002",
    "track": "Comfort Me"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "208",
    "pollyear": 2002,
    "position": 35,
    "releaseyear": "2002",
    "track": "Luv Your Life"
    },
    {
    "alltime": False,
    "artist": "Waikiki",
    "country": "Australia",
    "id": "209",
    "pollyear": 2002,
    "position": 36,
    "releaseyear": "2002",
    "track": "Here Comes September"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "210",
    "pollyear": 2002,
    "position": 37,
    "releaseyear": "2002",
    "track": "Aerials"
    },
    {
    "alltime": False,
    "artist": "The Drugs",
    "country": "Australia",
    "id": "211",
    "pollyear": 2002,
    "position": 38,
    "releaseyear": "2002",
    "track": "The Bold and the Beautiful"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "212",
    "pollyear": 2002,
    "position": 39,
    "releaseyear": "2002",
    "track": "In My Place"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "213",
    "pollyear": 2002,
    "position": 40,
    "releaseyear": "2002",
    "track": "Fall For You"
    },
    {
    "alltime": False,
    "artist": "George",
    "country": "Australia",
    "id": "214",
    "pollyear": 2002,
    "position": 43,
    "releaseyear": "2002",
    "track": "Breaking It Slowly"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "215",
    "pollyear": 2002,
    "position": 44,
    "releaseyear": "2002",
    "track": "God is in the Radio"
    },
    {
    "alltime": False,
    "artist": "N.E.R.D",
    "country": "USA",
    "id": "216",
    "pollyear": 2002,
    "position": 46,
    "releaseyear": "2002",
    "track": "Rock Star"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "217",
    "pollyear": 2002,
    "position": 47,
    "releaseyear": "2002",
    "track": "1000 Miles"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "218",
    "pollyear": 2002,
    "position": 48,
    "releaseyear": "2002",
    "track": "Go with the Flow"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "219",
    "pollyear": 2002,
    "position": 50,
    "releaseyear": "2002",
    "track": "You Give Me Something"
    },
    {
    "alltime": False,
    "artist": "Wilcannia Mob",
    "country": "Australia",
    "id": "220",
    "pollyear": 2002,
    "position": 51,
    "releaseyear": "2002",
    "track": "Down River"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "221",
    "pollyear": 2002,
    "position": 52,
    "releaseyear": "2002",
    "track": "One Said to the Other"
    },
    {
    "alltime": False,
    "artist": "Basement Jaxx",
    "country": "UK",
    "id": "222",
    "pollyear": 2002,
    "position": 53,
    "releaseyear": "2002",
    "track": "Get Me Off"
    },
    {
    "alltime": False,
    "artist": "The Androids",
    "country": "Australia",
    "id": "223",
    "pollyear": 2002,
    "position": 54,
    "releaseyear": "2002",
    "track": "Do it With Madonna"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "224",
    "pollyear": 2002,
    "position": 55,
    "releaseyear": "2002",
    "track": "Disenchanted Lullaby"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "225",
    "pollyear": 2002,
    "position": 56,
    "releaseyear": "2002",
    "track": "First It Giveth"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "226",
    "pollyear": 2002,
    "position": 57,
    "releaseyear": "2002",
    "track": "Love Foolosphy"
    },
    {
    "alltime": False,
    "artist": "PJ Harvey and Gordon Gano",
    "country": "UK",
    "id": "227",
    "pollyear": 2002,
    "position": 58,
    "releaseyear": "2002",
    "track": "Hitting the Ground"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "228",
    "pollyear": 2002,
    "position": 59,
    "releaseyear": "2002",
    "track": "Take It Slow"
    },
    {
    "alltime": False,
    "artist": "JXL vs Elvis Presley",
    "country": "Netherlands",
    "id": "229",
    "pollyear": 2002,
    "position": 60,
    "releaseyear": "2002",
    "track": "A Little Less Conversation"
    },
    {
    "alltime": False,
    "artist": "Moby",
    "country": "USA",
    "id": "230",
    "pollyear": 2002,
    "position": 61,
    "releaseyear": "2002",
    "track": "We Are All Made of Stars"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "231",
    "pollyear": 2002,
    "position": 62,
    "releaseyear": "2002",
    "track": "Across the Night"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "232",
    "pollyear": 2002,
    "position": 63,
    "releaseyear": "2002",
    "track": "Say Something"
    },
    {
    "alltime": False,
    "artist": "Gomez",
    "country": "UK",
    "id": "233",
    "pollyear": 2002,
    "position": 64,
    "releaseyear": "2002",
    "track": "Shot Shot"
    },
    {
    "alltime": False,
    "artist": "Area-7",
    "country": "Australia",
    "id": "234",
    "pollyear": 2002,
    "position": 65,
    "releaseyear": "2002",
    "track": "Nobody Likes a Bogan"
    },
    {
    "alltime": False,
    "artist": "Augie March",
    "country": "Australia",
    "id": "235",
    "pollyear": 2002,
    "position": 66,
    "releaseyear": "2002",
    "track": "This Train Will Be Taking No Passengers"
    },
    {
    "alltime": False,
    "artist": "Waikiki",
    "country": "Australia",
    "id": "236",
    "pollyear": 2002,
    "position": 67,
    "releaseyear": "2002",
    "track": "New Technology"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "237",
    "pollyear": 2002,
    "position": 69,
    "releaseyear": "2002",
    "track": "Clocks"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "238",
    "pollyear": 2002,
    "position": 70,
    "releaseyear": "2002",
    "track": "Bucket Bong"
    },
    {
    "alltime": False,
    "artist": "Basement Jaxx",
    "country": "UK",
    "id": "239",
    "pollyear": 2002,
    "position": 71,
    "releaseyear": "2002",
    "track": "Do Your Thing"
    },
    {
    "alltime": False,
    "artist": "Audioslave",
    "country": "USA",
    "id": "240",
    "pollyear": 2002,
    "position": 72,
    "releaseyear": "2002",
    "track": "Show Me How to Live"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "241",
    "pollyear": 2002,
    "position": 73,
    "releaseyear": "2002",
    "track": "Dope Nose"
    },
    {
    "alltime": False,
    "artist": "Ms. Dynamite",
    "country": "UK",
    "id": "242",
    "pollyear": 2002,
    "position": 75,
    "releaseyear": "2002",
    "track": "Dy-na-mi-tee"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "243",
    "pollyear": 2002,
    "position": 76,
    "releaseyear": "2002",
    "track": "World Upon Your Shoulders"
    },
    {
    "alltime": False,
    "artist": "The Streets",
    "country": "UK",
    "id": "244",
    "pollyear": 2002,
    "position": 77,
    "releaseyear": "2002",
    "track": "Has it Come to This?"
    },
    {
    "alltime": False,
    "artist": "Badly Drawn Boy",
    "country": "UK",
    "id": "245",
    "pollyear": 2002,
    "position": 78,
    "releaseyear": "2002",
    "track": "Something to Talk About"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "246",
    "pollyear": 2002,
    "position": 79,
    "releaseyear": "2002",
    "track": "Who Put the Devil in You"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "247",
    "pollyear": 2002,
    "position": 80,
    "releaseyear": "2002",
    "track": "Highway One"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "248",
    "pollyear": 2002,
    "position": 82,
    "releaseyear": "2002",
    "track": "Strawberry Fields Forever"
    },
    {
    "alltime": False,
    "artist": "28 Days",
    "country": "Australia",
    "id": "249",
    "pollyear": 2002,
    "position": 83,
    "releaseyear": "2002",
    "track": "Take Me Away"
    },
    {
    "alltime": False,
    "artist": "Oasis",
    "country": "UK",
    "id": "250",
    "pollyear": 2002,
    "position": 84,
    "releaseyear": "2002",
    "track": "Little By Little"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "251",
    "pollyear": 2002,
    "position": 85,
    "releaseyear": "2002",
    "track": "Star Guitar"
    },
    {
    "alltime": False,
    "artist": "Eminem",
    "country": "USA",
    "id": "252",
    "pollyear": 2002,
    "position": 86,
    "releaseyear": "2002",
    "track": "Cleaning Out My Closet"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "253",
    "pollyear": 2002,
    "position": 87,
    "releaseyear": "2002",
    "track": "Innervision"
    },
    {
    "alltime": False,
    "artist": "Groove Armada",
    "country": "UK",
    "id": "254",
    "pollyear": 2002,
    "position": 89,
    "releaseyear": "2002",
    "track": "Purple Haze"
    },
    {
    "alltime": False,
    "artist": "Badly Drawn Boy",
    "country": "UK",
    "id": "255",
    "pollyear": 2002,
    "position": 90,
    "releaseyear": "2002",
    "track": "Silent Sigh"
    },
    {
    "alltime": False,
    "artist": "Rocket Science",
    "country": "Australia",
    "id": "256",
    "pollyear": 2002,
    "position": 91,
    "releaseyear": "2002",
    "track": "Being Followed"
    },
    {
    "alltime": False,
    "artist": "Antiskeptic",
    "country": "Australia",
    "id": "257",
    "pollyear": 2002,
    "position": 92,
    "releaseyear": "2002",
    "track": "Called"
    },
    {
    "alltime": False,
    "artist": "Tori Amos",
    "country": "USA",
    "id": "258",
    "pollyear": 2002,
    "position": 93,
    "releaseyear": "2002",
    "track": "A Sorta Fairytale"
    },
    {
    "alltime": False,
    "artist": "Machine Translations",
    "country": "Australia",
    "id": "259",
    "pollyear": 2002,
    "position": 95,
    "releaseyear": "2002",
    "track": "She Wears a Mask"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "260",
    "pollyear": 2002,
    "position": 96,
    "releaseyear": "2002",
    "track": "Lies"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "261",
    "pollyear": 2002,
    "position": 97,
    "releaseyear": "2002",
    "track": "Electrical Storm"
    },
    {
    "alltime": False,
    "artist": "Cartman",
    "country": "Australia",
    "id": "262",
    "pollyear": 2002,
    "position": 98,
    "releaseyear": "2002",
    "track": "Shock (Living Without You)"
    },
    {
    "alltime": False,
    "artist": "Bodyjar",
    "country": "Australia",
    "id": "263",
    "pollyear": 2002,
    "position": 99,
    "releaseyear": "2002",
    "track": "Too Drunk to Drive"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "264",
    "pollyear": 2002,
    "position": 100,
    "releaseyear": "2002",
    "track": "A Rush of Blood to the Head"
    },
    {
    "alltime": False,
    "artist": "Mumford & Sons",
    "country": "UK",
    "id": "265",
    "pollyear": 2009,
    "position": 1,
    "releaseyear": "2009",
    "track": "Little Lion Man"
    },
    {
    "alltime": False,
    "artist": "Art vs Science",
    "country": "Australia",
    "id": "266",
    "pollyear": 2009,
    "position": 2,
    "releaseyear": "2009",
    "track": "Parlez Vous Francais?"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "267",
    "pollyear": 2009,
    "position": 3,
    "releaseyear": "2009",
    "track": "Chase That Feeling"
    },
    {
    "alltime": False,
    "artist": "Phoenix",
    "country": "France",
    "id": "268",
    "pollyear": 2009,
    "position": 4,
    "releaseyear": "2009",
    "track": "Lisztomania"
    },
    {
    "alltime": False,
    "artist": "Bluejuice",
    "country": "Australia",
    "id": "269",
    "pollyear": 2009,
    "position": 5,
    "releaseyear": "2009",
    "track": "Broken Leg"
    },
    {
    "alltime": False,
    "artist": "La Roux",
    "country": "UK",
    "id": "270",
    "pollyear": 2009,
    "position": 6,
    "releaseyear": "2009",
    "track": "Bulletproof"
    },
    {
    "alltime": False,
    "artist": "Lisa Mitchell",
    "country": "Australia",
    "id": "271",
    "pollyear": 2009,
    "position": 7,
    "releaseyear": "2009",
    "track": "Coin Laundry"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "272",
    "pollyear": 2009,
    "position": 8,
    "releaseyear": "2009",
    "track": "Not Fair"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "273",
    "pollyear": 2009,
    "position": 9,
    "releaseyear": "2009",
    "track": "Uprising"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "274",
    "pollyear": 2009,
    "position": 10,
    "releaseyear": "2009",
    "track": "Dog Days Are Over"
    },
    {
    "alltime": False,
    "artist": "Yeah Yeah Yeahs",
    "country": "USA",
    "id": "275",
    "pollyear": 2009,
    "position": 11,
    "releaseyear": "2009",
    "track": "Heads Will Roll"
    },
    {
    "alltime": False,
    "artist": "Dizzee Rascal and Armand Van Helden",
    "country": "UK",
    "id": "276",
    "pollyear": 2009,
    "position": 12,
    "releaseyear": "2009",
    "track": "Bonkers"
    },
    {
    "alltime": False,
    "artist": "Phoenix",
    "country": "France",
    "id": "277",
    "pollyear": 2009,
    "position": 13,
    "releaseyear": "2009",
    "track": "1901"
    },
    {
    "alltime": False,
    "artist": "Edward Sharpe and the Magnetic Zeros",
    "country": "USA",
    "id": "278",
    "pollyear": 2009,
    "position": 15,
    "releaseyear": "2009",
    "track": "Home"
    },
    {
    "alltime": False,
    "artist": "Gossip",
    "country": "USA",
    "id": "279",
    "pollyear": 2009,
    "position": 16,
    "releaseyear": "2009",
    "track": "Heavy Cross"
    },
    {
    "alltime": False,
    "artist": "Kasabian",
    "country": "UK",
    "id": "280",
    "pollyear": 2009,
    "position": 17,
    "releaseyear": "2009",
    "track": "Fire"
    },
    {
    "alltime": False,
    "artist": "Bag Raiders",
    "country": "Australia",
    "id": "281",
    "pollyear": 2009,
    "position": 18,
    "releaseyear": "2009",
    "track": "Shooting Stars"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "282",
    "pollyear": 2009,
    "position": 19,
    "releaseyear": "2009",
    "track": "Undisclosed Desires"
    },
    {
    "alltime": False,
    "artist": "Passion Pit",
    "country": "USA",
    "id": "283",
    "pollyear": 2009,
    "position": 20,
    "releaseyear": "2009",
    "track": "Sleepyhead"
    },
    {
    "alltime": False,
    "artist": "The Temper Trap",
    "country": "Australia",
    "id": "284",
    "pollyear": 2009,
    "position": 21,
    "releaseyear": "2009",
    "track": "Fader"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "285",
    "pollyear": 2009,
    "position": 22,
    "releaseyear": "2009",
    "track": "Cousins"
    },
    {
    "alltime": False,
    "artist": "The Bloody Beetroots",
    "country": "Italy",
    "id": "286",
    "pollyear": 2009,
    "position": 23,
    "releaseyear": "2009",
    "track": "Warp 1.9 {ft. Steve Aoki}"
    },
    {
    "alltime": False,
    "artist": "Flight of the Conchords",
    "country": "New Zealand",
    "id": "287",
    "pollyear": 2009,
    "position": 24,
    "releaseyear": "2009",
    "track": "Carol Brown"
    },
    {
    "alltime": False,
    "artist": "Yeah Yeah Yeahs",
    "country": "USA",
    "id": "288",
    "pollyear": 2009,
    "position": 25,
    "releaseyear": "2009",
    "track": "Zero"
    },
    {
    "alltime": False,
    "artist": "La Roux",
    "country": "UK",
    "id": "289",
    "pollyear": 2009,
    "position": 27,
    "releaseyear": "2009",
    "track": "In for the Kill"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "290",
    "pollyear": 2009,
    "position": 29,
    "releaseyear": "2009",
    "track": "All I Want"
    },
    {
    "alltime": False,
    "artist": "Flight of the Conchords",
    "country": "New Zealand",
    "id": "291",
    "pollyear": 2009,
    "position": 30,
    "releaseyear": "2009",
    "track": "Hurt Feelings"
    },
    {
    "alltime": False,
    "artist": "Seth Sentry",
    "country": "Australia",
    "id": "292",
    "pollyear": 2009,
    "position": 31,
    "releaseyear": "2009",
    "track": "The Waitress Song"
    },
    {
    "alltime": False,
    "artist": "Paul Dempsey",
    "country": "Australia",
    "id": "293",
    "pollyear": 2009,
    "position": 32,
    "releaseyear": "2009",
    "track": "Ramona Was a Waitress"
    },
    {
    "alltime": False,
    "artist": "Kid Cudi",
    "country": "USA",
    "id": "294",
    "pollyear": 2009,
    "position": 33,
    "releaseyear": "2009",
    "track": "Pursuit of Happiness {ft. MGMT & Ratatat}"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "295",
    "pollyear": 2009,
    "position": 34,
    "releaseyear": "2009",
    "track": "Brother"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "296",
    "pollyear": 2009,
    "position": 35,
    "releaseyear": "2009",
    "track": "Resistance"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "297",
    "pollyear": 2009,
    "position": 37,
    "releaseyear": "2009",
    "track": "Still Standing"
    },
    {
    "alltime": False,
    "artist": "Passion Pit",
    "country": "USA",
    "id": "298",
    "pollyear": 2009,
    "position": 38,
    "releaseyear": "2009",
    "track": "Little Secrets"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "299",
    "pollyear": 2009,
    "position": 39,
    "releaseyear": "2009",
    "track": "One Way Road"
    },
    {
    "alltime": False,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "300",
    "pollyear": 2009,
    "position": 40,
    "releaseyear": "2009",
    "track": "And the Boys"
    },
    {
    "alltime": False,
    "artist": "Simian Mobile Disco",
    "country": "UK",
    "id": "301",
    "pollyear": 2009,
    "position": 41,
    "releaseyear": "2009",
    "track": "Audacity of Huge {ft. Chris Keating}"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "302",
    "pollyear": 2009,
    "position": 42,
    "releaseyear": "2009",
    "track": "Vanilla"
    },
    {
    "alltime": False,
    "artist": "The Bloody Beetroots",
    "country": "Italy",
    "id": "303",
    "pollyear": 2009,
    "position": 43,
    "releaseyear": "2009",
    "track": "Awesome {ft. The Cool Kids}"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "304",
    "pollyear": 2009,
    "position": 44,
    "releaseyear": "2009",
    "track": "Rabbit Heart (Raise It Up)"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "305",
    "pollyear": 2009,
    "position": 45,
    "releaseyear": "2009",
    "track": "Drumming Song"
    },
    {
    "alltime": False,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "306",
    "pollyear": 2009,
    "position": 46,
    "releaseyear": "2009",
    "track": "Blood Bank"
    },
    {
    "alltime": False,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "307",
    "pollyear": 2009,
    "position": 47,
    "releaseyear": "2009",
    "track": "Set Fire to the Hive"
    },
    {
    "alltime": False,
    "artist": "The Temper Trap",
    "country": "Australia",
    "id": "308",
    "pollyear": 2009,
    "position": 48,
    "releaseyear": "2009",
    "track": "Science of Fear"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "309",
    "pollyear": 2009,
    "position": 49,
    "releaseyear": "2009",
    "track": "All of the Dreamers"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "310",
    "pollyear": 2009,
    "position": 50,
    "releaseyear": "2009",
    "track": "Buttons {CSS Remix}"
    },
    {
    "alltime": False,
    "artist": "Kasabian",
    "country": "UK",
    "id": "311",
    "pollyear": 2009,
    "position": 51,
    "releaseyear": "2009",
    "track": "Where Did All the Love Go?"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "312",
    "pollyear": 2009,
    "position": 52,
    "releaseyear": "2009",
    "track": "Horchata"
    },
    {
    "alltime": False,
    "artist": "Miike Snow",
    "country": "Sweden",
    "id": "313",
    "pollyear": 2009,
    "position": 53,
    "releaseyear": "2009",
    "track": "Animal"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "314",
    "pollyear": 2009,
    "position": 54,
    "releaseyear": "2009",
    "track": "Crying Lightning"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "315",
    "pollyear": 2009,
    "position": 55,
    "releaseyear": "2009",
    "track": "No You Girls"
    },
    {
    "alltime": False,
    "artist": "The xx",
    "country": "UK",
    "id": "316",
    "pollyear": 2009,
    "position": 56,
    "releaseyear": "2009",
    "track": "Islands"
    },
    {
    "alltime": False,
    "artist": "Philadelphia Grand Jury",
    "country": "Australia",
    "id": "317",
    "pollyear": 2009,
    "position": 57,
    "releaseyear": "2009",
    "track": "The Good News"
    },
    {
    "alltime": False,
    "artist": "The Temper Trap",
    "country": "Australia",
    "id": "318",
    "pollyear": 2009,
    "position": 58,
    "releaseyear": "2009",
    "track": "Love Lost"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "319",
    "pollyear": 2009,
    "position": 60,
    "releaseyear": "2009",
    "track": "22"
    },
    {
    "alltime": False,
    "artist": "Grizzly Bear",
    "country": "USA",
    "id": "320",
    "pollyear": 2009,
    "position": 61,
    "releaseyear": "2009",
    "track": "Two Weeks"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "321",
    "pollyear": 2009,
    "position": 62,
    "releaseyear": "2009",
    "track": "One More Chance"
    },
    {
    "alltime": False,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "322",
    "pollyear": 2009,
    "position": 63,
    "releaseyear": "2009",
    "track": "All I Know"
    },
    {
    "alltime": False,
    "artist": "The Middle East",
    "country": "Australia",
    "id": "323",
    "pollyear": 2009,
    "position": 64,
    "releaseyear": "2009",
    "track": "Blood"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "324",
    "pollyear": 2009,
    "position": 65,
    "releaseyear": "2009",
    "track": "Foreign Land"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "325",
    "pollyear": 2009,
    "position": 66,
    "releaseyear": "2009",
    "track": "Pictures"
    },
    {
    "alltime": False,
    "artist": "Washington",
    "country": "Australia",
    "id": "326",
    "pollyear": 2009,
    "position": 67,
    "releaseyear": "2009",
    "track": "Cement"
    },
    {
    "alltime": False,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "327",
    "pollyear": 2009,
    "position": 68,
    "releaseyear": "2009",
    "track": "Omen"
    },
    {
    "alltime": False,
    "artist": "Death Cab for Cutie",
    "country": "USA",
    "id": "328",
    "pollyear": 2009,
    "position": 69,
    "releaseyear": "2009",
    "track": "Meet Me on the Equinox"
    },
    {
    "alltime": False,
    "artist": "Animal Collective",
    "country": "USA",
    "id": "329",
    "pollyear": 2009,
    "position": 70,
    "releaseyear": "2009",
    "track": "My Girls"
    },
    {
    "alltime": False,
    "artist": "Bertie Blackman",
    "country": "Australia",
    "id": "330",
    "pollyear": 2009,
    "position": 71,
    "releaseyear": "2009",
    "track": "Byrds of Prey"
    },
    {
    "alltime": False,
    "artist": "MSTRKRFT",
    "country": "Canada",
    "id": "331",
    "pollyear": 2009,
    "position": 73,
    "releaseyear": "2009",
    "track": "Heartbreaker {ft. John Legend}"
    },
    {
    "alltime": False,
    "artist": "Art vs Science",
    "country": "Australia",
    "id": "332",
    "pollyear": 2009,
    "position": 74,
    "releaseyear": "2009",
    "track": "Friend in the Field"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "333",
    "pollyear": 2009,
    "position": 75,
    "releaseyear": "2009",
    "track": "New Moon Rising"
    },
    {
    "alltime": False,
    "artist": "Julian Casablancas",
    "country": "USA",
    "id": "334",
    "pollyear": 2009,
    "position": 76,
    "releaseyear": "2009",
    "track": "11th Dimension"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "335",
    "pollyear": 2009,
    "position": 78,
    "releaseyear": "2009",
    "track": "Remember Me"
    },
    {
    "alltime": False,
    "artist": "Yves Klein Blue",
    "country": "Australia",
    "id": "336",
    "pollyear": 2009,
    "position": 79,
    "releaseyear": "2009",
    "track": "Getting Wise"
    },
    {
    "alltime": False,
    "artist": "Dizzee Rascal",
    "country": "UK",
    "id": "337",
    "pollyear": 2009,
    "position": 80,
    "releaseyear": "2009",
    "track": "Holiday"
    },
    {
    "alltime": False,
    "artist": "Mumford & Sons",
    "country": "UK",
    "id": "338",
    "pollyear": 2009,
    "position": 81,
    "releaseyear": "2009",
    "track": "The Cave"
    },
    {
    "alltime": False,
    "artist": "Miami Horror",
    "country": "Australia",
    "id": "339",
    "pollyear": 2009,
    "position": 82,
    "releaseyear": "2009",
    "track": "Sometimes"
    },
    {
    "alltime": False,
    "artist": "Basement Jaxx",
    "country": "UK",
    "id": "340",
    "pollyear": 2009,
    "position": 83,
    "releaseyear": "2009",
    "track": "Raindrops"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "341",
    "pollyear": 2009,
    "position": 84,
    "releaseyear": "2009",
    "track": "United States of Eurasia"
    },
    {
    "alltime": False,
    "artist": "Kasabian",
    "country": "UK",
    "id": "342",
    "pollyear": 2009,
    "position": 85,
    "releaseyear": "2009",
    "track": "Underdog"
    },
    {
    "alltime": False,
    "artist": "Flight of the Conchords",
    "country": "New Zealand",
    "id": "343",
    "pollyear": 2009,
    "position": 86,
    "releaseyear": "2009",
    "track": "Too Many Dicks (On the Dance Floor)"
    },
    {
    "alltime": False,
    "artist": "The Middle East",
    "country": "Australia",
    "id": "344",
    "pollyear": 2009,
    "position": 87,
    "releaseyear": "2009",
    "track": "The Darkest Side"
    },
    {
    "alltime": False,
    "artist": "NOFX",
    "country": "USA",
    "id": "345",
    "pollyear": 2009,
    "position": 88,
    "releaseyear": "2009",
    "track": "Creeping Out Sara"
    },
    {
    "alltime": False,
    "artist": "Jay-Z",
    "country": "USA",
    "id": "346",
    "pollyear": 2009,
    "position": 89,
    "releaseyear": "2009",
    "track": "D.O.A. (Death of Auto-Tune)"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "347",
    "pollyear": 2009,
    "position": 90,
    "releaseyear": "2009",
    "track": "Kiss with a Fist"
    },
    {
    "alltime": False,
    "artist": "Friendly Fires",
    "country": "UK",
    "id": "348",
    "pollyear": 2009,
    "position": 92,
    "releaseyear": "2009",
    "track": "Skeleton Boy"
    },
    {
    "alltime": False,
    "artist": "Bertie Blackman",
    "country": "Australia",
    "id": "349",
    "pollyear": 2009,
    "position": 93,
    "releaseyear": "2009",
    "track": "Thump"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "350",
    "pollyear": 2009,
    "position": 94,
    "releaseyear": "2009",
    "track": "Blue Lips"
    },
    {
    "alltime": False,
    "artist": "Silversun Pickups",
    "country": "USA",
    "id": "351",
    "pollyear": 2009,
    "position": 95,
    "releaseyear": "2009",
    "track": "Panic Switch"
    },
    {
    "alltime": False,
    "artist": "Deadmau5",
    "country": "Canada",
    "id": "352",
    "pollyear": 2009,
    "position": 96,
    "releaseyear": "2009",
    "track": "Ghosts N Stuff"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "353",
    "pollyear": 2009,
    "position": 97,
    "releaseyear": "2009",
    "track": "Laughing With"
    },
    {
    "alltime": False,
    "artist": "Them Crooked Vultures",
    "country": "USA",
    "id": "354",
    "pollyear": 2009,
    "position": 98,
    "releaseyear": "2009",
    "track": "New Fang"
    },
    {
    "alltime": False,
    "artist": "Tegan and Sara",
    "country": "Canada",
    "id": "355",
    "pollyear": 2009,
    "position": 99,
    "releaseyear": "2009",
    "track": "Hell"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "356",
    "pollyear": 2009,
    "position": 100,
    "releaseyear": "2009",
    "track": "Wheels"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "357",
    "pollyear": 2009,
    "position": 1,
    "releaseyear": "1991",
    "track": "Smells Like Teen Spirit"
    },
    {
    "alltime": True,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "358",
    "pollyear": 2009,
    "position": 2,
    "releaseyear": "1992",
    "track": "Killing in the Name"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "359",
    "pollyear": 2009,
    "position": 3,
    "releaseyear": "1994",
    "track": "Hallelujah"
    },
    {
    "alltime": True,
    "artist": "Joy Division",
    "country": "UK",
    "id": "360",
    "pollyear": 2009,
    "position": 4,
    "releaseyear": "1980",
    "track": "Love Will Tear Us Apart"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "361",
    "pollyear": 2009,
    "position": 5,
    "releaseyear": "1997",
    "track": "Paranoid Android"
    },
    {
    "alltime": True,
    "artist": "Queen",
    "country": "UK",
    "id": "362",
    "pollyear": 2009,
    "position": 6,
    "releaseyear": "1975",
    "track": "Bohemian Rhapsody"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "363",
    "pollyear": 2009,
    "position": 7,
    "releaseyear": "1994",
    "track": "Last Goodbye"
    },
    {
    "alltime": True,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "364",
    "pollyear": 2009,
    "position": 8,
    "releaseyear": "1991",
    "track": "Under the Bridge"
    },
    {
    "alltime": True,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "365",
    "pollyear": 2009,
    "position": 9,
    "releaseyear": "1997",
    "track": "Everlong"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "366",
    "pollyear": 2009,
    "position": 10,
    "releaseyear": "1971",
    "track": "Stairway to Heaven"
    },
    {
    "alltime": True,
    "artist": "John Lennon",
    "country": "UK",
    "id": "367",
    "pollyear": 2009,
    "position": 11,
    "releaseyear": "1971",
    "track": "Imagine"
    },
    {
    "alltime": True,
    "artist": "Oasis",
    "country": "UK",
    "id": "368",
    "pollyear": 2009,
    "position": 12,
    "releaseyear": "1995",
    "track": "Wonderwall"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "369",
    "pollyear": 2009,
    "position": 13,
    "releaseyear": "1992",
    "track": "Creep"
    },
    {
    "alltime": True,
    "artist": "The Verve",
    "country": "UK",
    "id": "370",
    "pollyear": 2009,
    "position": 14,
    "releaseyear": "1997",
    "track": "Bitter Sweet Symphony"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "371",
    "pollyear": 2009,
    "position": 15,
    "releaseyear": "1997",
    "track": "Karma Police"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "372",
    "pollyear": 2009,
    "position": 16,
    "releaseyear": "1975",
    "track": "Wish You Were Here"
    },
    {
    "alltime": True,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "373",
    "pollyear": 2009,
    "position": 17,
    "releaseyear": "2003",
    "track": "The Nosebleed Section"
    },
    {
    "alltime": True,
    "artist": "Muse",
    "country": "UK",
    "id": "374",
    "pollyear": 2009,
    "position": 18,
    "releaseyear": "2006",
    "track": "Knights of Cydonia"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "375",
    "pollyear": 2009,
    "position": 19,
    "releaseyear": "1988",
    "track": "One"
    },
    {
    "alltime": True,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "376",
    "pollyear": 2009,
    "position": 20,
    "releaseyear": "2003",
    "track": "Seven Nation Army"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "377",
    "pollyear": 2009,
    "position": 21,
    "releaseyear": "2000",
    "track": "These Days"
    },
    {
    "alltime": True,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "378",
    "pollyear": 2009,
    "position": 22,
    "releaseyear": "1998",
    "track": "Teardrop"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "379",
    "pollyear": 2009,
    "position": 23,
    "releaseyear": "1985",
    "track": "Throw Your Arms Around Me"
    },
    {
    "alltime": True,
    "artist": "The Beatles",
    "country": "UK",
    "id": "380",
    "pollyear": 2009,
    "position": 24,
    "releaseyear": "1967",
    "track": "A Day in the Life"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "381",
    "pollyear": 2009,
    "position": 25,
    "releaseyear": "1991",
    "track": "Alive"
    },
    {
    "alltime": True,
    "artist": "Michael Jackson",
    "country": "USA",
    "id": "382",
    "pollyear": 2009,
    "position": 26,
    "releaseyear": "1984",
    "track": "Thriller"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "383",
    "pollyear": 2009,
    "position": 27,
    "releaseyear": "2000",
    "track": "My Happiness"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "384",
    "pollyear": 2009,
    "position": 28,
    "releaseyear": "1995",
    "track": "Fake Plastic Trees"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "385",
    "pollyear": 2009,
    "position": 29,
    "releaseyear": "1988",
    "track": "Where Is My Mind?"
    },
    {
    "alltime": True,
    "artist": "The Jimi Hendrix Experience",
    "country": "USA",
    "id": "386",
    "pollyear": 2009,
    "position": 30,
    "releaseyear": "1968",
    "track": "All Along the Watchtower"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "387",
    "pollyear": 2009,
    "position": 31,
    "releaseyear": "1991",
    "track": "Enter Sandman"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "388",
    "pollyear": 2009,
    "position": 32,
    "releaseyear": "1983",
    "track": "Blue Monday"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "389",
    "pollyear": 2009,
    "position": 33,
    "releaseyear": "1994",
    "track": "Tomorrow"
    },
    {
    "alltime": True,
    "artist": "The Living End",
    "country": "Australia",
    "id": "390",
    "pollyear": 2009,
    "position": 34,
    "releaseyear": "1997",
    "track": "Prisoner of Society"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "391",
    "pollyear": 2009,
    "position": 35,
    "releaseyear": "1996",
    "track": "1979"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "392",
    "pollyear": 2009,
    "position": 36,
    "releaseyear": "1997",
    "track": "Into My Arms"
    },
    {
    "alltime": True,
    "artist": "Tool",
    "country": "USA",
    "id": "393",
    "pollyear": 2009,
    "position": 37,
    "releaseyear": "1996",
    "track": "Stinkfist"
    },
    {
    "alltime": True,
    "artist": "The Killers",
    "country": "USA",
    "id": "394",
    "pollyear": 2009,
    "position": 38,
    "releaseyear": "2004",
    "track": "Mr. Brightside"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "395",
    "pollyear": 2009,
    "position": 39,
    "releaseyear": "1994",
    "track": "Better Man"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "396",
    "pollyear": 2009,
    "position": 40,
    "releaseyear": "1991",
    "track": "Come as You Are"
    },
    {
    "alltime": True,
    "artist": "Michael Jackson",
    "country": "USA",
    "id": "397",
    "pollyear": 2009,
    "position": 41,
    "releaseyear": "1983",
    "track": "Billie Jean"
    },
    {
    "alltime": True,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "398",
    "pollyear": 2009,
    "position": 42,
    "releaseyear": "2005",
    "track": "Banquet"
    },
    {
    "alltime": True,
    "artist": "The Beach Boys",
    "country": "USA",
    "id": "399",
    "pollyear": 2009,
    "position": 43,
    "releaseyear": "1966",
    "track": "God Only Knows"
    },
    {
    "alltime": True,
    "artist": "The Beatles",
    "country": "UK",
    "id": "400",
    "pollyear": 2009,
    "position": 44,
    "releaseyear": "1968",
    "track": "Hey Jude"
    },
    {
    "alltime": True,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "401",
    "pollyear": 2009,
    "position": 45,
    "releaseyear": "2002",
    "track": "No One Knows"
    },
    {
    "alltime": True,
    "artist": "Faith No More",
    "country": "USA",
    "id": "402",
    "pollyear": 2009,
    "position": 46,
    "releaseyear": "1990",
    "track": "Epic"
    },
    {
    "alltime": True,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "403",
    "pollyear": 2009,
    "position": 47,
    "releaseyear": "2001",
    "track": "Betterman"
    },
    {
    "alltime": True,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "404",
    "pollyear": 2009,
    "position": 48,
    "releaseyear": "1994",
    "track": "Sabotage"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "405",
    "pollyear": 2009,
    "position": 51,
    "releaseyear": "1995",
    "track": "Bullet with Butterfly Wings"
    },
    {
    "alltime": True,
    "artist": "You Am I",
    "country": "Australia",
    "id": "406",
    "pollyear": 2009,
    "position": 52,
    "releaseyear": "1994",
    "track": "Berlin Chair"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "407",
    "pollyear": 2009,
    "position": 53,
    "releaseyear": "1979",
    "track": "Comfortably Numb"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "408",
    "pollyear": 2009,
    "position": 54,
    "releaseyear": "1985",
    "track": "Close to Me"
    },
    {
    "alltime": True,
    "artist": "Bob Dylan",
    "country": "USA",
    "id": "409",
    "pollyear": 2009,
    "position": 55,
    "releaseyear": "1965",
    "track": "Like a Rolling Stone"
    },
    {
    "alltime": True,
    "artist": "Tool",
    "country": "USA",
    "id": "410",
    "pollyear": 2009,
    "position": 57,
    "releaseyear": "1997",
    "track": "Forty-Six & 2"
    },
    {
    "alltime": True,
    "artist": "Daft Punk",
    "country": "France",
    "id": "411",
    "pollyear": 2009,
    "position": 58,
    "releaseyear": "1997",
    "track": "Around the World"
    },
    {
    "alltime": True,
    "artist": "Augie March",
    "country": "Australia",
    "id": "412",
    "pollyear": 2009,
    "position": 59,
    "releaseyear": "2006",
    "track": "One Crowded Hour"
    },
    {
    "alltime": True,
    "artist": "Johnny Cash",
    "country": "USA",
    "id": "413",
    "pollyear": 2009,
    "position": 60,
    "releaseyear": "2003",
    "track": "Hurt"
    },
    {
    "alltime": True,
    "artist": "Blur",
    "country": "UK",
    "id": "414",
    "pollyear": 2009,
    "position": 61,
    "releaseyear": "1997",
    "track": "Song 2"
    },
    {
    "alltime": True,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "415",
    "pollyear": 2009,
    "position": 62,
    "releaseyear": "1994",
    "track": "Closer"
    },
    {
    "alltime": True,
    "artist": "AC/DC",
    "country": "Australia",
    "id": "416",
    "pollyear": 2009,
    "position": 63,
    "releaseyear": "1990",
    "track": "Thunderstruck"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "417",
    "pollyear": 2009,
    "position": 64,
    "releaseyear": "1982",
    "track": "Blister in the Sun"
    },
    {
    "alltime": True,
    "artist": "Underworld",
    "country": "UK",
    "id": "418",
    "pollyear": 2009,
    "position": 65,
    "releaseyear": "1995",
    "track": "Born Slippy .NUXX"
    },
    {
    "alltime": True,
    "artist": "Elton John",
    "country": "UK",
    "id": "419",
    "pollyear": 2009,
    "position": 66,
    "releaseyear": "1971",
    "track": "Tiny Dancer"
    },
    {
    "alltime": True,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "420",
    "pollyear": 2009,
    "position": 67,
    "releaseyear": "1997",
    "track": "Brick"
    },
    {
    "alltime": True,
    "artist": "Blink-182",
    "country": "USA",
    "id": "421",
    "pollyear": 2009,
    "position": 68,
    "releaseyear": "1997",
    "track": "Dammit (Growing Up)"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "422",
    "pollyear": 2009,
    "position": 69,
    "releaseyear": "1994",
    "track": "Grace"
    },
    {
    "alltime": True,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "423",
    "pollyear": 2009,
    "position": 70,
    "releaseyear": "1996",
    "track": "Breathe"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "424",
    "pollyear": 2009,
    "position": 71,
    "releaseyear": "1984",
    "track": "How Soon Is Now?"
    },
    {
    "alltime": True,
    "artist": "The Shins",
    "country": "USA",
    "id": "425",
    "pollyear": 2009,
    "position": 72,
    "releaseyear": "2001",
    "track": "New Slang"
    },
    {
    "alltime": True,
    "artist": "The Clash",
    "country": "UK",
    "id": "426",
    "pollyear": 2009,
    "position": 73,
    "releaseyear": "1979",
    "track": "London Calling"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "427",
    "pollyear": 2009,
    "position": 74,
    "releaseyear": "1991",
    "track": "Lithium"
    },
    {
    "alltime": True,
    "artist": "Green Day",
    "country": "USA",
    "id": "428",
    "pollyear": 2009,
    "position": 75,
    "releaseyear": "1997",
    "track": "Good Riddance (Time of Your Life)"
    },
    {
    "alltime": True,
    "artist": "The Stone Roses",
    "country": "UK",
    "id": "429",
    "pollyear": 2009,
    "position": 76,
    "releaseyear": "1989",
    "track": "Fools Gold"
    },
    {
    "alltime": True,
    "artist": "Gotye",
    "country": "Australia",
    "id": "430",
    "pollyear": 2009,
    "position": 77,
    "releaseyear": "2006",
    "track": "Hearts a Mess"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "431",
    "pollyear": 2009,
    "position": 78,
    "releaseyear": "1993",
    "track": "Today"
    },
    {
    "alltime": True,
    "artist": "David Bowie",
    "country": "UK",
    "id": "432",
    "pollyear": 2009,
    "position": 79,
    "releaseyear": "1971",
    "track": "Life on Mars?"
    },
    {
    "alltime": True,
    "artist": "The Rolling Stones",
    "country": "UK",
    "id": "433",
    "pollyear": 2009,
    "position": 80,
    "releaseyear": "1966",
    "track": "Paint It, Black"
    },
    {
    "alltime": True,
    "artist": "Pulp",
    "country": "UK",
    "id": "434",
    "pollyear": 2009,
    "position": 81,
    "releaseyear": "1995",
    "track": "Common People"
    },
    {
    "alltime": True,
    "artist": "System of a Down",
    "country": "USA",
    "id": "435",
    "pollyear": 2009,
    "position": 82,
    "releaseyear": "2001",
    "track": "Chop Suey!"
    },
    {
    "alltime": True,
    "artist": "Placebo",
    "country": "UK",
    "id": "436",
    "pollyear": 2009,
    "position": 83,
    "releaseyear": "1999",
    "track": "Every You Every Me"
    },
    {
    "alltime": True,
    "artist": "Bob Marley & The Wailers",
    "country": "Jamaica",
    "id": "437",
    "pollyear": 2009,
    "position": 84,
    "releaseyear": "1974",
    "track": "No Woman, No Cry"
    },
    {
    "alltime": True,
    "artist": "The Dandy Warhols",
    "country": "USA",
    "id": "438",
    "pollyear": 2009,
    "position": 85,
    "releaseyear": "2000",
    "track": "Bohemian Like You"
    },
    {
    "alltime": True,
    "artist": "The Beatles",
    "country": "UK",
    "id": "439",
    "pollyear": 2009,
    "position": 86,
    "releaseyear": "1969",
    "track": "Come Together"
    },
    {
    "alltime": True,
    "artist": "Coldplay",
    "country": "UK",
    "id": "440",
    "pollyear": 2009,
    "position": 87,
    "releaseyear": "2000",
    "track": "Yellow"
    },
    {
    "alltime": True,
    "artist": "The Rolling Stones",
    "country": "UK",
    "id": "441",
    "pollyear": 2009,
    "position": 88,
    "releaseyear": "1969",
    "track": "Gimme Shelter"
    },
    {
    "alltime": True,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "442",
    "pollyear": 2009,
    "position": 89,
    "releaseyear": "1996",
    "track": "Bulls on Parade"
    },
    {
    "alltime": True,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "443",
    "pollyear": 2009,
    "position": 90,
    "releaseyear": "2008",
    "track": "Sex on Fire"
    },
    {
    "alltime": True,
    "artist": "AC/DC",
    "country": "Australia",
    "id": "444",
    "pollyear": 2009,
    "position": 91,
    "releaseyear": "1980",
    "track": "Back in Black"
    },
    {
    "alltime": True,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "445",
    "pollyear": 2009,
    "position": 92,
    "releaseyear": "2008",
    "track": "Skinny Love"
    },
    {
    "alltime": True,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "446",
    "pollyear": 2009,
    "position": 93,
    "releaseyear": "1991",
    "track": "Unfinished Sympathy"
    },
    {
    "alltime": True,
    "artist": "Modest Mouse",
    "country": "USA",
    "id": "447",
    "pollyear": 2009,
    "position": 94,
    "releaseyear": "2004",
    "track": "Float On"
    },
    {
    "alltime": True,
    "artist": "Stevie Wonder",
    "country": "USA",
    "id": "448",
    "pollyear": 2009,
    "position": 95,
    "releaseyear": "1972",
    "track": "Superstition"
    },
    {
    "alltime": True,
    "artist": "Daft Punk",
    "country": "France",
    "id": "449",
    "pollyear": 2009,
    "position": 96,
    "releaseyear": "2000",
    "track": "One More Time"
    },
    {
    "alltime": True,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "450",
    "pollyear": 2009,
    "position": 97,
    "releaseyear": "1987",
    "track": "Beds Are Burning"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "451",
    "pollyear": 2009,
    "position": 98,
    "releaseyear": "1975",
    "track": "Kashmir"
    },
    {
    "alltime": True,
    "artist": "TV on the Radio",
    "country": "USA",
    "id": "452",
    "pollyear": 2009,
    "position": 99,
    "releaseyear": "2006",
    "track": "Wolf Like Me"
    },
    {
    "alltime": True,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "453",
    "pollyear": 2009,
    "position": 100,
    "releaseyear": "2004",
    "track": "Take Me Out"
    },
    {
    "alltime": False,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "454",
    "pollyear": 2010,
    "position": 1,
    "releaseyear": "2010",
    "track": "Big Jet Plane"
    },
    {
    "alltime": False,
    "artist": "Little Red",
    "country": "Australia",
    "id": "455",
    "pollyear": 2010,
    "position": 2,
    "releaseyear": "2010",
    "track": "Rock It"
    },
    {
    "alltime": False,
    "artist": "Ou Est Le Swimming Pool",
    "country": "UK",
    "id": "456",
    "pollyear": 2010,
    "position": 3,
    "releaseyear": "2010",
    "track": "Dance the Way I Feel"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "457",
    "pollyear": 2010,
    "position": 4,
    "releaseyear": "2010",
    "track": "Plans"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "458",
    "pollyear": 2010,
    "position": 5,
    "releaseyear": "2010",
    "track": "Fall at Your Feet"
    },
    {
    "alltime": False,
    "artist": "Adrian Lux",
    "country": "Sweden",
    "id": "459",
    "pollyear": 2010,
    "position": 6,
    "releaseyear": "2010",
    "track": "Teenage Crime"
    },
    {
    "alltime": False,
    "artist": "Cee-Lo Green",
    "country": "USA",
    "id": "460",
    "pollyear": 2010,
    "position": 7,
    "releaseyear": "2010",
    "track": "Fuck You!"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "461",
    "pollyear": 2010,
    "position": 8,
    "releaseyear": "2010",
    "track": "Tokyo (Vampires & Wolves)"
    },
    {
    "alltime": False,
    "artist": "Art vs Science",
    "country": "Australia",
    "id": "462",
    "pollyear": 2010,
    "position": 9,
    "releaseyear": "2010",
    "track": "Magic Fountain"
    },
    {
    "alltime": False,
    "artist": "Mark Ronson & The Business Intl.",
    "country": "UK",
    "id": "463",
    "pollyear": 2010,
    "position": 10,
    "releaseyear": "2010",
    "track": "Somebody to Love Me {ft. Boy George & Andrew Wyatt}"
    },
    {
    "alltime": False,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "464",
    "pollyear": 2010,
    "position": 11,
    "releaseyear": "2010",
    "track": "ABC News Theme Remix"
    },
    {
    "alltime": False,
    "artist": "Drapht",
    "country": "Australia",
    "id": "465",
    "pollyear": 2010,
    "position": 12,
    "releaseyear": "2010",
    "track": "Rapunzel"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "466",
    "pollyear": 2010,
    "position": 13,
    "releaseyear": "2010",
    "track": "Clap Your Hands"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "467",
    "pollyear": 2010,
    "position": 14,
    "releaseyear": "2010",
    "track": "Runaway {ft. Pusha T}"
    },
    {
    "alltime": False,
    "artist": "Duck Sauce",
    "country": "USA",
    "id": "468",
    "pollyear": 2010,
    "position": 15,
    "releaseyear": "2010",
    "track": "Barbra Streisand"
    },
    {
    "alltime": False,
    "artist": "The Jezabels",
    "country": "Australia",
    "id": "469",
    "pollyear": 2010,
    "position": 16,
    "releaseyear": "2010",
    "track": "Mace Spray"
    },
    {
    "alltime": False,
    "artist": "Mark Ronson & The Business Intl.",
    "country": "UK",
    "id": "470",
    "pollyear": 2010,
    "position": 17,
    "releaseyear": "2010",
    "track": "Bang Bang Bang {ft. Q-Tip & MNDR}"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "471",
    "pollyear": 2010,
    "position": 19,
    "releaseyear": "2010",
    "track": "Crave You {ft. Giselle}"
    },
    {
    "alltime": False,
    "artist": "Washington",
    "country": "Australia",
    "id": "472",
    "pollyear": 2010,
    "position": 20,
    "releaseyear": "2010",
    "track": "Sunday Best"
    },
    {
    "alltime": False,
    "artist": "Two Door Cinema Club",
    "country": "UK",
    "id": "473",
    "pollyear": 2010,
    "position": 21,
    "releaseyear": "2010",
    "track": "Undercover Martyn"
    },
    {
    "alltime": False,
    "artist": "Children Collide",
    "country": "Australia",
    "id": "474",
    "pollyear": 2010,
    "position": 22,
    "releaseyear": "2010",
    "track": "Jellylegs"
    },
    {
    "alltime": False,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "475",
    "pollyear": 2010,
    "position": 23,
    "releaseyear": "2010",
    "track": "Addicted"
    },
    {
    "alltime": False,
    "artist": "Gotye",
    "country": "Australia",
    "id": "476",
    "pollyear": 2010,
    "position": 25,
    "releaseyear": "2010",
    "track": "Eyes Wide Open"
    },
    {
    "alltime": False,
    "artist": "Crystal Castles",
    "country": "Canada",
    "id": "477",
    "pollyear": 2010,
    "position": 26,
    "releaseyear": "2010",
    "track": "Not in Love {ft. Robert Smith}"
    },
    {
    "alltime": False,
    "artist": "Dizzee Rascal & Florence and the Machine",
    "country": "UK",
    "id": "478",
    "pollyear": 2010,
    "position": 27,
    "releaseyear": "2010",
    "track": "You Got the Dirtee Love"
    },
    {
    "alltime": False,
    "artist": "Darwin Deez",
    "country": "USA",
    "id": "479",
    "pollyear": 2010,
    "position": 28,
    "releaseyear": "2010",
    "track": "Radar Detector"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "480",
    "pollyear": 2010,
    "position": 29,
    "releaseyear": "2010",
    "track": "It Can Wait"
    },
    {
    "alltime": False,
    "artist": "Yeasayer",
    "country": "USA",
    "id": "481",
    "pollyear": 2010,
    "position": 30,
    "releaseyear": "2010",
    "track": "O.N.E."
    },
    {
    "alltime": False,
    "artist": "The National",
    "country": "USA",
    "id": "482",
    "pollyear": 2010,
    "position": 31,
    "releaseyear": "2010",
    "track": "Bloodbuzz Ohio"
    },
    {
    "alltime": False,
    "artist": "Foster the People",
    "country": "USA",
    "id": "483",
    "pollyear": 2010,
    "position": 32,
    "releaseyear": "2010",
    "track": "Pumped Up Kicks"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "484",
    "pollyear": 2010,
    "position": 33,
    "releaseyear": "2010",
    "track": "Solitude Is Bliss"
    },
    {
    "alltime": False,
    "artist": "The Naked and Famous",
    "country": "New Zealand",
    "id": "485",
    "pollyear": 2010,
    "position": 34,
    "releaseyear": "2010",
    "track": "Punching in a Dream"
    },
    {
    "alltime": False,
    "artist": "Mark Ronson & The Business Intl.",
    "country": "UK",
    "id": "486",
    "pollyear": 2010,
    "position": 35,
    "releaseyear": "2010",
    "track": "The Bike Song {ft. Kyle Falconer & Spank Rock}"
    },
    {
    "alltime": False,
    "artist": "Chiddy Bang",
    "country": "USA",
    "id": "487",
    "pollyear": 2010,
    "position": 36,
    "releaseyear": "2010",
    "track": "Opposite of Adults"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "488",
    "pollyear": 2010,
    "position": 37,
    "releaseyear": "2010",
    "track": "Doncamatic {ft. Daley}"
    },
    {
    "alltime": False,
    "artist": "The Naked and Famous",
    "country": "New Zealand",
    "id": "489",
    "pollyear": 2010,
    "position": 38,
    "releaseyear": "2010",
    "track": "Young Blood"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "490",
    "pollyear": 2010,
    "position": 39,
    "releaseyear": "2010",
    "track": "Revolution"
    },
    {
    "alltime": False,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "491",
    "pollyear": 2010,
    "position": 41,
    "releaseyear": "2010",
    "track": "Down by the River"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "492",
    "pollyear": 2010,
    "position": 42,
    "releaseyear": "2010",
    "track": "On Melancholy Hill"
    },
    {
    "alltime": False,
    "artist": "Yolanda Be Cool & DCUP",
    "country": "Australia",
    "id": "493",
    "pollyear": 2010,
    "position": 43,
    "releaseyear": "2010",
    "track": "We No Speak Americano"
    },
    {
    "alltime": False,
    "artist": "Crystal Castles",
    "country": "Canada",
    "id": "494",
    "pollyear": 2010,
    "position": 44,
    "releaseyear": "2010",
    "track": "Baptism"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "495",
    "pollyear": 2010,
    "position": 45,
    "releaseyear": "2010",
    "track": "Rabbit Song"
    },
    {
    "alltime": False,
    "artist": "Bag Raiders",
    "country": "Australia",
    "id": "496",
    "pollyear": 2010,
    "position": 46,
    "releaseyear": "2010",
    "track": "Way Back Home"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "497",
    "pollyear": 2010,
    "position": 47,
    "releaseyear": "2010",
    "track": "Wild at Heart"
    },
    {
    "alltime": False,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "498",
    "pollyear": 2010,
    "position": 48,
    "releaseyear": "2010",
    "track": "Witchcraft"
    },
    {
    "alltime": False,
    "artist": "The Jezabels",
    "country": "Australia",
    "id": "499",
    "pollyear": 2010,
    "position": 49,
    "releaseyear": "2010",
    "track": "Easy to Love"
    },
    {
    "alltime": False,
    "artist": "Hot Chip",
    "country": "UK",
    "id": "500",
    "pollyear": 2010,
    "position": 50,
    "releaseyear": "2010",
    "track": "One Life Stand"
    },
    {
    "alltime": False,
    "artist": "Yeasayer",
    "country": "USA",
    "id": "501",
    "pollyear": 2010,
    "position": 51,
    "releaseyear": "2010",
    "track": "Ambling Alp"
    },
    {
    "alltime": False,
    "artist": "The John Steel Singers",
    "country": "Australia",
    "id": "502",
    "pollyear": 2010,
    "position": 52,
    "releaseyear": "2010",
    "track": "Overpass"
    },
    {
    "alltime": False,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "503",
    "pollyear": 2010,
    "position": 53,
    "releaseyear": "2010",
    "track": "Reflections"
    },
    {
    "alltime": False,
    "artist": "Miami Horror",
    "country": "Australia",
    "id": "504",
    "pollyear": 2010,
    "position": 54,
    "releaseyear": "2010",
    "track": "Holidays"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "505",
    "pollyear": 2010,
    "position": 55,
    "releaseyear": "2010",
    "track": "Giving Up the Gun"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "506",
    "pollyear": 2010,
    "position": 56,
    "releaseyear": "2010",
    "track": "Bring Night"
    },
    {
    "alltime": False,
    "artist": "Example",
    "country": "UK",
    "id": "507",
    "pollyear": 2010,
    "position": 57,
    "releaseyear": "2010",
    "track": "Kickstarts"
    },
    {
    "alltime": False,
    "artist": "Arcade Fire",
    "country": "Canada",
    "id": "508",
    "pollyear": 2010,
    "position": 58,
    "releaseyear": "2010",
    "track": "The Suburbs"
    },
    {
    "alltime": False,
    "artist": "Washington",
    "country": "Australia",
    "id": "509",
    "pollyear": 2010,
    "position": 59,
    "releaseyear": "2010",
    "track": "Rich Kids"
    },
    {
    "alltime": False,
    "artist": "Children Collide",
    "country": "Australia",
    "id": "510",
    "pollyear": 2010,
    "position": 60,
    "releaseyear": "2010",
    "track": "My Eagle"
    },
    {
    "alltime": False,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "511",
    "pollyear": 2010,
    "position": 62,
    "releaseyear": "2010",
    "track": "Hold On"
    },
    {
    "alltime": False,
    "artist": "Arcade Fire",
    "country": "Canada",
    "id": "512",
    "pollyear": 2010,
    "position": 63,
    "releaseyear": "2010",
    "track": "Ready to Start"
    },
    {
    "alltime": False,
    "artist": "Gypsy & the Cat",
    "country": "Australia",
    "id": "513",
    "pollyear": 2010,
    "position": 64,
    "releaseyear": "2010",
    "track": "Jona Vark"
    },
    {
    "alltime": False,
    "artist": "Dead Letter Circus",
    "country": "Australia",
    "id": "514",
    "pollyear": 2010,
    "position": 65,
    "releaseyear": "2010",
    "track": "One Step"
    },
    {
    "alltime": False,
    "artist": "Cold War Kids",
    "country": "USA",
    "id": "515",
    "pollyear": 2010,
    "position": 66,
    "releaseyear": "2010",
    "track": "Audience"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "516",
    "pollyear": 2010,
    "position": 67,
    "releaseyear": "2010",
    "track": "Holiday"
    },
    {
    "alltime": False,
    "artist": "Andy Bull",
    "country": "Australia",
    "id": "517",
    "pollyear": 2010,
    "position": 68,
    "releaseyear": "2010",
    "track": "Dog {ft. Lisa Mitchell}"
    },
    {
    "alltime": False,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "518",
    "pollyear": 2010,
    "position": 69,
    "releaseyear": "2010",
    "track": "Watercolour"
    },
    {
    "alltime": False,
    "artist": "Groove Armada",
    "country": "UK",
    "id": "519",
    "pollyear": 2010,
    "position": 70,
    "releaseyear": "2010",
    "track": "Paper Romance"
    },
    {
    "alltime": False,
    "artist": "Two Door Cinema Club",
    "country": "UK",
    "id": "520",
    "pollyear": 2010,
    "position": 72,
    "releaseyear": "2010",
    "track": "I Can Talk"
    },
    {
    "alltime": False,
    "artist": "Gypsy & the Cat",
    "country": "Australia",
    "id": "521",
    "pollyear": 2010,
    "position": 73,
    "releaseyear": "2010",
    "track": "Time to Wander"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "522",
    "pollyear": 2010,
    "position": 74,
    "releaseyear": "2010",
    "track": "Lucidity"
    },
    {
    "alltime": False,
    "artist": "Hungry Kids of Hungary",
    "country": "Australia",
    "id": "523",
    "pollyear": 2010,
    "position": 75,
    "releaseyear": "2010",
    "track": "Coming Around"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "524",
    "pollyear": 2010,
    "position": 76,
    "releaseyear": "2010",
    "track": "Radioactive"
    },
    {
    "alltime": False,
    "artist": "Big Boi",
    "country": "USA",
    "id": "525",
    "pollyear": 2010,
    "position": 77,
    "releaseyear": "2010",
    "track": "Shutterbugg"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "526",
    "pollyear": 2010,
    "position": 78,
    "releaseyear": "2010",
    "track": "Stylo"
    },
    {
    "alltime": False,
    "artist": "Little Red",
    "country": "Australia",
    "id": "527",
    "pollyear": 2010,
    "position": 79,
    "releaseyear": "2010",
    "track": "Slow Motion"
    },
    {
    "alltime": False,
    "artist": "Klaxons",
    "country": "UK",
    "id": "528",
    "pollyear": 2010,
    "position": 81,
    "releaseyear": "2010",
    "track": "Echoes"
    },
    {
    "alltime": False,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "529",
    "pollyear": 2010,
    "position": 82,
    "releaseyear": "2010",
    "track": "Tighten Up"
    },
    {
    "alltime": False,
    "artist": "Arcade Fire",
    "country": "Canada",
    "id": "530",
    "pollyear": 2010,
    "position": 83,
    "releaseyear": "2010",
    "track": "Modern Man"
    },
    {
    "alltime": False,
    "artist": "Washington",
    "country": "Australia",
    "id": "531",
    "pollyear": 2010,
    "position": 84,
    "releaseyear": "2010",
    "track": "The Hardest Part"
    },
    {
    "alltime": False,
    "artist": "Hot Chip",
    "country": "UK",
    "id": "532",
    "pollyear": 2010,
    "position": 85,
    "releaseyear": "2010",
    "track": "I Feel Better"
    },
    {
    "alltime": False,
    "artist": "Evil Eddie",
    "country": "Australia",
    "id": "533",
    "pollyear": 2010,
    "position": 86,
    "releaseyear": "2010",
    "track": "Queensland"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "534",
    "pollyear": 2010,
    "position": 87,
    "releaseyear": "2010",
    "track": "The Saddest Thing I Know"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "535",
    "pollyear": 2010,
    "position": 88,
    "releaseyear": "2010",
    "track": "Monster {ft. Jay-Z, Rick Ross, Nicki Minaj & Bon Iver}"
    },
    {
    "alltime": False,
    "artist": "Interpol",
    "country": "USA",
    "id": "536",
    "pollyear": 2010,
    "position": 89,
    "releaseyear": "2010",
    "track": "Barricade"
    },
    {
    "alltime": False,
    "artist": "Art vs Science",
    "country": "Australia",
    "id": "537",
    "pollyear": 2010,
    "position": 90,
    "releaseyear": "2010",
    "track": "Finally See Our Way"
    },
    {
    "alltime": False,
    "artist": "The Bedroom Philosopher",
    "country": "Australia",
    "id": "538",
    "pollyear": 2010,
    "position": 91,
    "releaseyear": "2010",
    "track": "Northcote (So Hungover)"
    },
    {
    "alltime": False,
    "artist": "LCD Soundsystem",
    "country": "USA",
    "id": "539",
    "pollyear": 2010,
    "position": 92,
    "releaseyear": "2010",
    "track": "I Can Change"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "540",
    "pollyear": 2010,
    "position": 94,
    "releaseyear": "2010",
    "track": "Time to Smile"
    },
    {
    "alltime": False,
    "artist": "Broken Bells",
    "country": "USA",
    "id": "541",
    "pollyear": 2010,
    "position": 95,
    "releaseyear": "2010",
    "track": "The High Road"
    },
    {
    "alltime": False,
    "artist": "Jonsi",
    "country": "Iceland",
    "id": "542",
    "pollyear": 2010,
    "position": 96,
    "releaseyear": "2010",
    "track": "Go Do"
    },
    {
    "alltime": False,
    "artist": "Parkway Drive",
    "country": "Australia",
    "id": "543",
    "pollyear": 2010,
    "position": 97,
    "releaseyear": "2010",
    "track": "Sleepwalker"
    },
    {
    "alltime": False,
    "artist": "Foals",
    "country": "UK",
    "id": "544",
    "pollyear": 2010,
    "position": 98,
    "releaseyear": "2010",
    "track": "Spanish Sahara"
    },
    {
    "alltime": False,
    "artist": "Dead Letter Circus",
    "country": "Australia",
    "id": "545",
    "pollyear": 2010,
    "position": 99,
    "releaseyear": "2010",
    "track": "Big"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "546",
    "pollyear": 2010,
    "position": 100,
    "releaseyear": "2010",
    "track": "Neutron Star Collision (Love Is Forever)"
    },
    {
    "alltime": False,
    "artist": "Denis Leary",
    "country": "USA",
    "id": "547",
    "pollyear": 1993,
    "position": 1,
    "releaseyear": "1993",
    "track": "Asshole"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "548",
    "pollyear": 1993,
    "position": 2,
    "releaseyear": "1993",
    "track": "Creep"
    },
    {
    "alltime": False,
    "artist": "The Cranberries",
    "country": "Ireland",
    "id": "549",
    "pollyear": 1993,
    "position": 3,
    "releaseyear": "1993",
    "track": "Linger"
    },
    {
    "alltime": False,
    "artist": "Blind Melon",
    "country": "USA",
    "id": "550",
    "pollyear": 1993,
    "position": 4,
    "releaseyear": "1993",
    "track": "No Rain"
    },
    {
    "alltime": False,
    "artist": "The Breeders",
    "country": "USA",
    "id": "551",
    "pollyear": 1993,
    "position": 5,
    "releaseyear": "1993",
    "track": "Cannonball"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "552",
    "pollyear": 1993,
    "position": 6,
    "releaseyear": "1993",
    "track": "Killing in the Name"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "553",
    "pollyear": 1993,
    "position": 7,
    "releaseyear": "1993",
    "track": "Lemon"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "554",
    "pollyear": 1993,
    "position": 8,
    "releaseyear": "1993",
    "track": "Go"
    },
    {
    "alltime": False,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "555",
    "pollyear": 1993,
    "position": 9,
    "releaseyear": "1993",
    "track": "The Honeymoon Is Over"
    },
    {
    "alltime": False,
    "artist": "Atomic Swing",
    "country": "Sweden",
    "id": "556",
    "pollyear": 1993,
    "position": 10,
    "releaseyear": "1993",
    "track": "Stone Me into the Groove"
    },
    {
    "alltime": False,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "557",
    "pollyear": 1993,
    "position": 11,
    "releaseyear": "1993",
    "track": "Everybody Hurts"
    },
    {
    "alltime": False,
    "artist": "Stone Temple Pilots",
    "country": "USA",
    "id": "558",
    "pollyear": 1993,
    "position": 12,
    "releaseyear": "1993",
    "track": "Plush"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "559",
    "pollyear": 1993,
    "position": 13,
    "releaseyear": "1993",
    "track": "Soul to Squeeze"
    },
    {
    "alltime": False,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "560",
    "pollyear": 1993,
    "position": 14,
    "releaseyear": "1993",
    "track": "I Held Her in My Arms"
    },
    {
    "alltime": False,
    "artist": "Iggy Pop",
    "country": "USA",
    "id": "561",
    "pollyear": 1993,
    "position": 15,
    "releaseyear": "1993",
    "track": "Wild America"
    },
    {
    "alltime": False,
    "artist": "Urge Overkill",
    "country": "USA",
    "id": "562",
    "pollyear": 1993,
    "position": 16,
    "releaseyear": "1993",
    "track": "Sister Havana"
    },
    {
    "alltime": False,
    "artist": "Cypress Hill",
    "country": "USA",
    "id": "563",
    "pollyear": 1993,
    "position": 17,
    "releaseyear": "1993",
    "track": "Hits From the Bong"
    },
    {
    "alltime": False,
    "artist": "Pet Shop Boys",
    "country": "UK",
    "id": "564",
    "pollyear": 1993,
    "position": 18,
    "releaseyear": "1993",
    "track": "Go West"
    },
    {
    "alltime": False,
    "artist": "Neneh Cherry & Michael Stipe",
    "country": "USA",
    "id": "565",
    "pollyear": 1993,
    "position": 19,
    "releaseyear": "1993",
    "track": "Trout"
    },
    {
    "alltime": False,
    "artist": "Nirvana",
    "country": "USA",
    "id": "566",
    "pollyear": 1993,
    "position": 20,
    "releaseyear": "1993",
    "track": "Heart-Shaped Box"
    },
    {
    "alltime": False,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "567",
    "pollyear": 1993,
    "position": 21,
    "releaseyear": "1993",
    "track": "Black Stick"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "568",
    "pollyear": 1993,
    "position": 22,
    "releaseyear": "1993",
    "track": "The Ship Song"
    },
    {
    "alltime": False,
    "artist": "Bjork",
    "country": "Iceland",
    "id": "569",
    "pollyear": 1993,
    "position": 23,
    "releaseyear": "1993",
    "track": "Human Behaviour"
    },
    {
    "alltime": False,
    "artist": "Belly",
    "country": "USA",
    "id": "570",
    "pollyear": 1993,
    "position": 25,
    "releaseyear": "1993",
    "track": "Feed the Tree"
    },
    {
    "alltime": False,
    "artist": "Efua",
    "country": "UK",
    "id": "571",
    "pollyear": 1993,
    "position": 26,
    "releaseyear": "1993",
    "track": "Somewhere"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "572",
    "pollyear": 1993,
    "position": 27,
    "releaseyear": "1993",
    "track": "Sober"
    },
    {
    "alltime": False,
    "artist": "Lenny Kravitz",
    "country": "USA",
    "id": "573",
    "pollyear": 1993,
    "position": 28,
    "releaseyear": "1993",
    "track": "Are You Gonna Go My Way"
    },
    {
    "alltime": False,
    "artist": "Ace of Base",
    "country": "Sweden",
    "id": "574",
    "pollyear": 1993,
    "position": 29,
    "releaseyear": "1993",
    "track": "All That She Wants"
    },
    {
    "alltime": False,
    "artist": "k.d. lang",
    "country": "Canada",
    "id": "575",
    "pollyear": 1993,
    "position": 30,
    "releaseyear": "1993",
    "track": "Constant Craving"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "576",
    "pollyear": 1993,
    "position": 31,
    "releaseyear": "1993",
    "track": "Numb"
    },
    {
    "alltime": False,
    "artist": "Paw",
    "country": "USA",
    "id": "577",
    "pollyear": 1993,
    "position": 32,
    "releaseyear": "1993",
    "track": "Jessie"
    },
    {
    "alltime": False,
    "artist": "Porno for Pyros",
    "country": "USA",
    "id": "578",
    "pollyear": 1993,
    "position": 33,
    "releaseyear": "1993",
    "track": "Pets"
    },
    {
    "alltime": False,
    "artist": "US3",
    "country": "UK",
    "id": "579",
    "pollyear": 1993,
    "position": 34,
    "releaseyear": "1993",
    "track": "Cantaloop"
    },
    {
    "alltime": False,
    "artist": "Salt-N-Pepa",
    "country": "USA",
    "id": "580",
    "pollyear": 1993,
    "position": 35,
    "releaseyear": "1993",
    "track": "Shoop"
    },
    {
    "alltime": False,
    "artist": "Hoodoo Gurus",
    "country": "Australia",
    "id": "581",
    "pollyear": 1993,
    "position": 36,
    "releaseyear": "1993",
    "track": "The Right Time"
    },
    {
    "alltime": False,
    "artist": "Juliana Hatfield",
    "country": "USA",
    "id": "582",
    "pollyear": 1993,
    "position": 37,
    "releaseyear": "1993",
    "track": "My Sister"
    },
    {
    "alltime": False,
    "artist": "Dinosaur Jr.",
    "country": "USA",
    "id": "583",
    "pollyear": 1993,
    "position": 38,
    "releaseyear": "1993",
    "track": "Get Me"
    },
    {
    "alltime": False,
    "artist": "Yothu Yindi",
    "country": "Australia",
    "id": "584",
    "pollyear": 1993,
    "position": 41,
    "releaseyear": "1993",
    "track": "World Turning"
    },
    {
    "alltime": False,
    "artist": "Gabrielle",
    "country": "UK",
    "id": "585",
    "pollyear": 1993,
    "position": 42,
    "releaseyear": "1993",
    "track": "Dreams"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "586",
    "pollyear": 1993,
    "position": 43,
    "releaseyear": "1993",
    "track": "Cherub Rock"
    },
    {
    "alltime": False,
    "artist": "Headless Chickens",
    "country": "New Zealand",
    "id": "587",
    "pollyear": 1993,
    "position": 44,
    "releaseyear": "1993",
    "track": "Juice"
    },
    {
    "alltime": False,
    "artist": "Dinosaur Jr.",
    "country": "USA",
    "id": "588",
    "pollyear": 1993,
    "position": 45,
    "releaseyear": "1993",
    "track": "Start Choppin"
    },
    {
    "alltime": False,
    "artist": "King Missile",
    "country": "USA",
    "id": "589",
    "pollyear": 1993,
    "position": 46,
    "releaseyear": "1993",
    "track": "Detachable Penis"
    },
    {
    "alltime": False,
    "artist": "Chaka Demus & Pliers",
    "country": "Jamaica",
    "id": "590",
    "pollyear": 1993,
    "position": 47,
    "releaseyear": "1993",
    "track": "Tease Me"
    },
    {
    "alltime": False,
    "artist": "Living Colour",
    "country": "USA",
    "id": "591",
    "pollyear": 1993,
    "position": 49,
    "releaseyear": "1993",
    "track": "Bi"
    },
    {
    "alltime": False,
    "artist": "Alice in Chains",
    "country": "USA",
    "id": "592",
    "pollyear": 1993,
    "position": 51,
    "releaseyear": "1993",
    "track": "Would?"
    },
    {
    "alltime": False,
    "artist": "Soul Asylum",
    "country": "USA",
    "id": "593",
    "pollyear": 1993,
    "position": 52,
    "releaseyear": "1993",
    "track": "Runaway Train"
    },
    {
    "alltime": False,
    "artist": "Buffalo Tom",
    "country": "USA",
    "id": "594",
    "pollyear": 1993,
    "position": 53,
    "releaseyear": "1993",
    "track": "Taillights Fade"
    },
    {
    "alltime": False,
    "artist": "Hunters and Collectors",
    "country": "Australia",
    "id": "595",
    "pollyear": 1993,
    "position": 54,
    "releaseyear": "1993",
    "track": "Holy Grail"
    },
    {
    "alltime": False,
    "artist": "Deborah Conway",
    "country": "Australia",
    "id": "596",
    "pollyear": 1993,
    "position": 55,
    "releaseyear": "1993",
    "track": "Alive and Brilliant"
    },
    {
    "alltime": False,
    "artist": "Pet Shop Boys",
    "country": "UK",
    "id": "597",
    "pollyear": 1993,
    "position": 56,
    "releaseyear": "1993",
    "track": "Can You Forgive Her?"
    },
    {
    "alltime": False,
    "artist": "Headless Chickens",
    "country": "New Zealand",
    "id": "598",
    "pollyear": 1993,
    "position": 57,
    "releaseyear": "1993",
    "track": "Choppers"
    },
    {
    "alltime": False,
    "artist": "King Missile",
    "country": "USA",
    "id": "599",
    "pollyear": 1993,
    "position": 58,
    "releaseyear": "1993",
    "track": "Jesus Was Way Cool"
    },
    {
    "alltime": False,
    "artist": "Crowded House",
    "country": "Australia",
    "id": "600",
    "pollyear": 1993,
    "position": 60,
    "releaseyear": "1993",
    "track": "Distant Sun"
    },
    {
    "alltime": False,
    "artist": "Christine Anu & Paul Kelly",
    "country": "Australia",
    "id": "601",
    "pollyear": 1993,
    "position": 61,
    "releaseyear": "1993",
    "track": "Last Train"
    },
    {
    "alltime": False,
    "artist": "Faith No More",
    "country": "USA",
    "id": "602",
    "pollyear": 1993,
    "position": 62,
    "releaseyear": "1993",
    "track": "Easy"
    },
    {
    "alltime": False,
    "artist": "The Sharp",
    "country": "Australia",
    "id": "603",
    "pollyear": 1993,
    "position": 63,
    "releaseyear": "1993",
    "track": "Scratch My Back"
    },
    {
    "alltime": False,
    "artist": "Screaming Trees",
    "country": "USA",
    "id": "604",
    "pollyear": 1993,
    "position": 64,
    "releaseyear": "1993",
    "track": "Nearly Lost You"
    },
    {
    "alltime": False,
    "artist": "New Order",
    "country": "UK",
    "id": "605",
    "pollyear": 1993,
    "position": 65,
    "releaseyear": "1993",
    "track": "Regret"
    },
    {
    "alltime": False,
    "artist": "Utah Saints",
    "country": "UK",
    "id": "606",
    "pollyear": 1993,
    "position": 66,
    "releaseyear": "1993",
    "track": "Something Good"
    },
    {
    "alltime": False,
    "artist": "Apache Indian",
    "country": "UK",
    "id": "607",
    "pollyear": 1993,
    "position": 67,
    "releaseyear": "1993",
    "track": "Boom Shack-A-Lak"
    },
    {
    "alltime": False,
    "artist": "Culture Beat",
    "country": "Germany",
    "id": "608",
    "pollyear": 1993,
    "position": 68,
    "releaseyear": "1993",
    "track": "Mr Vain"
    },
    {
    "alltime": False,
    "artist": "Suede",
    "country": "UK",
    "id": "609",
    "pollyear": 1993,
    "position": 69,
    "releaseyear": "1993",
    "track": "Animal Nitrate"
    },
    {
    "alltime": False,
    "artist": "Ed Kuepper",
    "country": "Australia",
    "id": "610",
    "pollyear": 1993,
    "position": 70,
    "releaseyear": "1993",
    "track": "Sleepy Head"
    },
    {
    "alltime": False,
    "artist": "Living Colour",
    "country": "USA",
    "id": "611",
    "pollyear": 1993,
    "position": 71,
    "releaseyear": "1993",
    "track": "Nothingness {Remix}"
    },
    {
    "alltime": False,
    "artist": "Barefoot",
    "country": "Australia",
    "id": "612",
    "pollyear": 1993,
    "position": 72,
    "releaseyear": "1993",
    "track": "Baby"
    },
    {
    "alltime": False,
    "artist": "Arrested Development",
    "country": "USA",
    "id": "613",
    "pollyear": 1993,
    "position": 73,
    "releaseyear": "1993",
    "track": "Mr. Wendal"
    },
    {
    "alltime": False,
    "artist": "Suede",
    "country": "UK",
    "id": "614",
    "pollyear": 1993,
    "position": 75,
    "releaseyear": "1993",
    "track": "The Drowners"
    },
    {
    "alltime": False,
    "artist": "Caligula",
    "country": "Australia",
    "id": "615",
    "pollyear": 1993,
    "position": 76,
    "releaseyear": "1993",
    "track": "Before"
    },
    {
    "alltime": False,
    "artist": "The Badloves",
    "country": "Australia",
    "id": "616",
    "pollyear": 1993,
    "position": 77,
    "releaseyear": "1993",
    "track": "Lost"
    },
    {
    "alltime": False,
    "artist": "East 17",
    "country": "UK",
    "id": "617",
    "pollyear": 1993,
    "position": 78,
    "releaseyear": "1993",
    "track": "Deep"
    },
    {
    "alltime": False,
    "artist": "The Lemonheads",
    "country": "USA",
    "id": "618",
    "pollyear": 1993,
    "position": 79,
    "releaseyear": "1993",
    "track": "Mrs. Robinson"
    },
    {
    "alltime": False,
    "artist": "Alice in Chains",
    "country": "USA",
    "id": "619",
    "pollyear": 1993,
    "position": 80,
    "releaseyear": "1993",
    "track": "Rooster"
    },
    {
    "alltime": False,
    "artist": "Cypress Hill",
    "country": "USA",
    "id": "620",
    "pollyear": 1993,
    "position": 81,
    "releaseyear": "1993",
    "track": "Insane in the Brain"
    },
    {
    "alltime": False,
    "artist": "The Badloves",
    "country": "Australia",
    "id": "621",
    "pollyear": 1993,
    "position": 82,
    "releaseyear": "1993",
    "track": "Green Limousine"
    },
    {
    "alltime": False,
    "artist": "Underground Lovers",
    "country": "Australia",
    "id": "622",
    "pollyear": 1993,
    "position": 83,
    "releaseyear": "1993",
    "track": "Your Eyes {Remix}"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "623",
    "pollyear": 1993,
    "position": 84,
    "releaseyear": "1993",
    "track": "Bullet in the Head"
    },
    {
    "alltime": False,
    "artist": "Green Jelly",
    "country": "USA",
    "id": "624",
    "pollyear": 1993,
    "position": 85,
    "releaseyear": "1993",
    "track": "Three Little Pigs"
    },
    {
    "alltime": False,
    "artist": "New Order",
    "country": "UK",
    "id": "625",
    "pollyear": 1993,
    "position": 86,
    "releaseyear": "1993",
    "track": "World (The Price of Love)"
    },
    {
    "alltime": False,
    "artist": "Swoop",
    "country": "Australia",
    "id": "626",
    "pollyear": 1993,
    "position": 87,
    "releaseyear": "1993",
    "track": "Do It"
    },
    {
    "alltime": False,
    "artist": "Grant Lee Buffalo",
    "country": "USA",
    "id": "627",
    "pollyear": 1993,
    "position": 88,
    "releaseyear": "1993",
    "track": "Dixie Drug Store"
    },
    {
    "alltime": False,
    "artist": "Mixed Relations",
    "country": "Australia",
    "id": "628",
    "pollyear": 1993,
    "position": 89,
    "releaseyear": "1993",
    "track": "Aboriginal Woman"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "629",
    "pollyear": 1993,
    "position": 90,
    "releaseyear": "1993",
    "track": "For Tomorrow"
    },
    {
    "alltime": False,
    "artist": "Things of Stone and Wood",
    "country": "Australia",
    "id": "630",
    "pollyear": 1993,
    "position": 91,
    "releaseyear": "1993",
    "track": "Happy Birthday Helen"
    },
    {
    "alltime": False,
    "artist": "Depeche Mode",
    "country": "UK",
    "id": "631",
    "pollyear": 1993,
    "position": 92,
    "releaseyear": "1993",
    "track": "I Feel You"
    },
    {
    "alltime": False,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "632",
    "pollyear": 1993,
    "position": 93,
    "releaseyear": "1993",
    "track": "Man on the Moon"
    },
    {
    "alltime": False,
    "artist": "Inner Circle",
    "country": "Jamaica",
    "id": "633",
    "pollyear": 1993,
    "position": 94,
    "releaseyear": "1993",
    "track": "Sweat (A La La La La Long)"
    },
    {
    "alltime": False,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "634",
    "pollyear": 1993,
    "position": 95,
    "releaseyear": "1993",
    "track": "Delivery Man"
    },
    {
    "alltime": False,
    "artist": "10,000 Maniacs",
    "country": "USA",
    "id": "635",
    "pollyear": 1993,
    "position": 96,
    "releaseyear": "1993",
    "track": "Candy Everybody Wants"
    },
    {
    "alltime": False,
    "artist": "Kate Bush",
    "country": "UK",
    "id": "636",
    "pollyear": 1993,
    "position": 97,
    "releaseyear": "1993",
    "track": "Rubberband Girl"
    },
    {
    "alltime": False,
    "artist": "Kev Carmody",
    "country": "Australia",
    "id": "637",
    "pollyear": 1993,
    "position": 98,
    "releaseyear": "1993",
    "track": "Freedom"
    },
    {
    "alltime": False,
    "artist": "The Shamen",
    "country": "UK",
    "id": "638",
    "pollyear": 1993,
    "position": 99,
    "releaseyear": "1993",
    "track": "Ebeneezer Goode"
    },
    {
    "alltime": False,
    "artist": "Van Morrison & John Lee Hooker",
    "country": "UK",
    "id": "639",
    "pollyear": 1993,
    "position": 100,
    "releaseyear": "1993",
    "track": "Gloria"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "640",
    "pollyear": 1998,
    "position": 1,
    "releaseyear": "1998",
    "track": "Pretty Fly (For a White Guy)"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "641",
    "pollyear": 1998,
    "position": 2,
    "releaseyear": "1998",
    "track": "Cigarettes Will Kill You"
    },
    {
    "alltime": False,
    "artist": "Hole",
    "country": "USA",
    "id": "642",
    "pollyear": 1998,
    "position": 4,
    "releaseyear": "1998",
    "track": "Celebrity Skin"
    },
    {
    "alltime": False,
    "artist": "Korn",
    "country": "USA",
    "id": "643",
    "pollyear": 1998,
    "position": 5,
    "releaseyear": "1998",
    "track": "Got the Life"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "644",
    "pollyear": 1998,
    "position": 6,
    "releaseyear": "1998",
    "track": "! (Song Formerly Known As)"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "645",
    "pollyear": 1998,
    "position": 7,
    "releaseyear": "1998",
    "track": "Harpoon"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "646",
    "pollyear": 1998,
    "position": 8,
    "releaseyear": "1998",
    "track": "The Day You Come"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "647",
    "pollyear": 1998,
    "position": 9,
    "releaseyear": "1998",
    "track": "Heavy Heart"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "648",
    "pollyear": 1998,
    "position": 10,
    "releaseyear": "1998",
    "track": "Save The Day"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "649",
    "pollyear": 1998,
    "position": 11,
    "releaseyear": "1998",
    "track": "The Sweetest Thing"
    },
    {
    "alltime": False,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "650",
    "pollyear": 1998,
    "position": 12,
    "releaseyear": "1998",
    "track": "Brick"
    },
    {
    "alltime": False,
    "artist": "They Might Be Giants",
    "country": "USA",
    "id": "651",
    "pollyear": 1998,
    "position": 13,
    "releaseyear": "1998",
    "track": "Dr. Worm"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "652",
    "pollyear": 1998,
    "position": 15,
    "releaseyear": "1998",
    "track": "Second Solution"
    },
    {
    "alltime": False,
    "artist": "Josh Abrahams & Amiel Daemion",
    "country": "Australia",
    "id": "653",
    "pollyear": 1998,
    "position": 16,
    "releaseyear": "1998",
    "track": "Addicted to Bass"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "654",
    "pollyear": 1998,
    "position": 17,
    "releaseyear": "1998",
    "track": "Tainted Love {Live}"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "655",
    "pollyear": 1998,
    "position": 18,
    "releaseyear": "1998",
    "track": "Just Ace"
    },
    {
    "alltime": False,
    "artist": "Wyclef Jean",
    "country": "USA",
    "id": "656",
    "pollyear": 1998,
    "position": 19,
    "releaseyear": "1998",
    "track": "Bubblegoose"
    },
    {
    "alltime": False,
    "artist": "Chef",
    "country": "USA",
    "id": "657",
    "pollyear": 1998,
    "position": 20,
    "releaseyear": "1998",
    "track": "Simultaneous"
    },
    {
    "alltime": False,
    "artist": "Marcy Playground",
    "country": "USA",
    "id": "658",
    "pollyear": 1998,
    "position": 21,
    "releaseyear": "1998",
    "track": "Sex and Candy"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "659",
    "pollyear": 1998,
    "position": 22,
    "releaseyear": "1998",
    "track": "Black Friday"
    },
    {
    "alltime": False,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "660",
    "pollyear": 1998,
    "position": 23,
    "releaseyear": "1998",
    "track": "Teardrop"
    },
    {
    "alltime": False,
    "artist": "Custard",
    "country": "Australia",
    "id": "661",
    "pollyear": 1998,
    "position": 24,
    "releaseyear": "1998",
    "track": "Music Is Crap"
    },
    {
    "alltime": False,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "662",
    "pollyear": 1998,
    "position": 25,
    "releaseyear": "1998",
    "track": "Intergalactic"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "663",
    "pollyear": 1998,
    "position": 26,
    "releaseyear": "1998",
    "track": "Polyester Girl"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "664",
    "pollyear": 1998,
    "position": 27,
    "releaseyear": "1998",
    "track": "I Like Your Old Remix Better Than Your New Remix"
    },
    {
    "alltime": False,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "665",
    "pollyear": 1998,
    "position": 29,
    "releaseyear": "1998",
    "track": "Everybody Here Wants You"
    },
    {
    "alltime": False,
    "artist": "Cake",
    "country": "USA",
    "id": "666",
    "pollyear": 1998,
    "position": 30,
    "releaseyear": "1998",
    "track": "Never There"
    },
    {
    "alltime": False,
    "artist": "Paul McDermott",
    "country": "Australia",
    "id": "667",
    "pollyear": 1998,
    "position": 31,
    "releaseyear": "1998",
    "track": "Throw Your Arms Around Me"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "668",
    "pollyear": 1998,
    "position": 32,
    "releaseyear": "1998",
    "track": "Black Bugs"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "669",
    "pollyear": 1998,
    "position": 33,
    "releaseyear": "1998",
    "track": "Sweater"
    },
    {
    "alltime": False,
    "artist": "Barenaked Ladies",
    "country": "Canada",
    "id": "670",
    "pollyear": 1998,
    "position": 34,
    "releaseyear": "1998",
    "track": "One Week"
    },
    {
    "alltime": False,
    "artist": "Harvey Danger",
    "country": "USA",
    "id": "671",
    "pollyear": 1998,
    "position": 35,
    "releaseyear": "1998",
    "track": "Flagpole Sitta"
    },
    {
    "alltime": False,
    "artist": "TISM",
    "country": "Australia",
    "id": "672",
    "pollyear": 1998,
    "position": 36,
    "releaseyear": "1998",
    "track": "Whatareya?"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "673",
    "pollyear": 1998,
    "position": 37,
    "releaseyear": "1998",
    "track": "Buy Now Pay Later (Charlie No 2)"
    },
    {
    "alltime": False,
    "artist": "The Mighty Mighty Bosstones",
    "country": "USA",
    "id": "674",
    "pollyear": 1998,
    "position": 38,
    "releaseyear": "1998",
    "track": "The Impression That I Get"
    },
    {
    "alltime": False,
    "artist": "Adam Sandler",
    "country": "USA",
    "id": "675",
    "pollyear": 1998,
    "position": 39,
    "releaseyear": "1998",
    "track": "Somebody Kill Me"
    },
    {
    "alltime": False,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "676",
    "pollyear": 1998,
    "position": 40,
    "releaseyear": "1998",
    "track": "Song For The Dumped"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "677",
    "pollyear": 1998,
    "position": 41,
    "releaseyear": "1998",
    "track": "Pure Morning"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "678",
    "pollyear": 1998,
    "position": 42,
    "releaseyear": "1998",
    "track": "Teflon"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "679",
    "pollyear": 1998,
    "position": 43,
    "releaseyear": "1998",
    "track": "Melbourne"
    },
    {
    "alltime": False,
    "artist": "Marilyn Manson",
    "country": "USA",
    "id": "680",
    "pollyear": 1998,
    "position": 44,
    "releaseyear": "1998",
    "track": "The Dope Show"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "681",
    "pollyear": 1998,
    "position": 45,
    "releaseyear": "1998",
    "track": "Ava Adore"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "682",
    "pollyear": 1998,
    "position": 47,
    "releaseyear": "1998",
    "track": "Do the Evolution"
    },
    {
    "alltime": False,
    "artist": "Catatonia",
    "country": "UK",
    "id": "683",
    "pollyear": 1998,
    "position": 48,
    "releaseyear": "1998",
    "track": "Road Rage"
    },
    {
    "alltime": False,
    "artist": "Hole",
    "country": "USA",
    "id": "684",
    "pollyear": 1998,
    "position": 49,
    "releaseyear": "1998",
    "track": "Malibu"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "685",
    "pollyear": 1998,
    "position": 51,
    "releaseyear": "1998",
    "track": "Given to Fly"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "686",
    "pollyear": 1998,
    "position": 52,
    "releaseyear": "1998",
    "track": "The Grouch"
    },
    {
    "alltime": False,
    "artist": "Everclear",
    "country": "USA",
    "id": "687",
    "pollyear": 1998,
    "position": 53,
    "releaseyear": "1998",
    "track": "Father of Mine"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "688",
    "pollyear": 1998,
    "position": 54,
    "releaseyear": "1998",
    "track": "Mum Changed The Locks"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "689",
    "pollyear": 1998,
    "position": 55,
    "releaseyear": "1998",
    "track": "No Surprises"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "690",
    "pollyear": 1998,
    "position": 56,
    "releaseyear": "1998",
    "track": "Charlie No 3"
    },
    {
    "alltime": False,
    "artist": "Propellerheads & Shirley Bassey",
    "country": "UK",
    "id": "691",
    "pollyear": 1998,
    "position": 59,
    "releaseyear": "1998",
    "track": "History Repeating"
    },
    {
    "alltime": False,
    "artist": "Ani DiFranco",
    "country": "USA",
    "id": "692",
    "pollyear": 1998,
    "position": 60,
    "releaseyear": "1998",
    "track": "Untouchable Face"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "693",
    "pollyear": 1998,
    "position": 62,
    "releaseyear": "1998",
    "track": "Gone Away"
    },
    {
    "alltime": False,
    "artist": "Fatboy Slim",
    "country": "UK",
    "id": "694",
    "pollyear": 1998,
    "position": 63,
    "releaseyear": "1998",
    "track": "The Rockafeller Skank"
    },
    {
    "alltime": False,
    "artist": "Antenna",
    "country": "Australia",
    "id": "695",
    "pollyear": 1998,
    "position": 64,
    "releaseyear": "1998",
    "track": "Come On Spring"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "696",
    "pollyear": 1998,
    "position": 65,
    "releaseyear": "1998",
    "track": "Rumble"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "697",
    "pollyear": 1998,
    "position": 66,
    "releaseyear": "1998",
    "track": "No Shelter"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "698",
    "pollyear": 1998,
    "position": 67,
    "releaseyear": "1998",
    "track": "The Unforgiven II"
    },
    {
    "alltime": False,
    "artist": "Dandy Warhols",
    "country": "USA",
    "id": "699",
    "pollyear": 1998,
    "position": 68,
    "releaseyear": "1998",
    "track": "Every Day Should Be A Holiday"
    },
    {
    "alltime": False,
    "artist": "Pollyanna",
    "country": "Australia",
    "id": "700",
    "pollyear": 1998,
    "position": 69,
    "releaseyear": "1998",
    "track": "Cinnamon Lip"
    },
    {
    "alltime": False,
    "artist": "Manic Street Preachers",
    "country": "UK",
    "id": "701",
    "pollyear": 1998,
    "position": 70,
    "releaseyear": "1998",
    "track": "If You Tolerate This Your Children Will Be Next"
    },
    {
    "alltime": False,
    "artist": "Happyland",
    "country": "Australia",
    "id": "702",
    "pollyear": 1998,
    "position": 71,
    "releaseyear": "1998",
    "track": "Hello"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "703",
    "pollyear": 1998,
    "position": 72,
    "releaseyear": "1998",
    "track": "Mr Charisma"
    },
    {
    "alltime": False,
    "artist": "Stardust",
    "country": "France",
    "id": "704",
    "pollyear": 1998,
    "position": 73,
    "releaseyear": "1998",
    "track": "Music Sounds Better with You"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "705",
    "pollyear": 1998,
    "position": 74,
    "releaseyear": "1998",
    "track": "My Hero"
    },
    {
    "alltime": False,
    "artist": "Rob Zombie",
    "country": "USA",
    "id": "706",
    "pollyear": 1998,
    "position": 75,
    "releaseyear": "1998",
    "track": "Dragula"
    },
    {
    "alltime": False,
    "artist": "Marcy Playground",
    "country": "USA",
    "id": "707",
    "pollyear": 1998,
    "position": 76,
    "releaseyear": "1998",
    "track": "Saint Joe on the School Bus"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "708",
    "pollyear": 1998,
    "position": 77,
    "releaseyear": "1998",
    "track": "Fuel"
    },
    {
    "alltime": False,
    "artist": "Fuel",
    "country": "USA",
    "id": "709",
    "pollyear": 1998,
    "position": 78,
    "releaseyear": "1998",
    "track": "Shimmer"
    },
    {
    "alltime": False,
    "artist": "Babybird",
    "country": "UK",
    "id": "710",
    "pollyear": 1998,
    "position": 80,
    "releaseyear": "1998",
    "track": "Bad Old Man"
    },
    {
    "alltime": False,
    "artist": "Bran Van 3000",
    "country": "Canada",
    "id": "711",
    "pollyear": 1998,
    "position": 81,
    "releaseyear": "1998",
    "track": "Drinking in L.A."
    },
    {
    "alltime": False,
    "artist": "Drugstore",
    "country": "UK",
    "id": "712",
    "pollyear": 1998,
    "position": 82,
    "releaseyear": "1998",
    "track": "El President"
    },
    {
    "alltime": False,
    "artist": "The Superjesus",
    "country": "Australia",
    "id": "713",
    "pollyear": 1998,
    "position": 83,
    "releaseyear": "1998",
    "track": "Now And Then"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "714",
    "pollyear": 1998,
    "position": 84,
    "releaseyear": "1998",
    "track": "Good Riddance (Time of Your Life)"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "715",
    "pollyear": 1998,
    "position": 85,
    "releaseyear": "1998",
    "track": "Harpoon"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "716",
    "pollyear": 1998,
    "position": 87,
    "releaseyear": "1998",
    "track": "Push It"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "717",
    "pollyear": 1998,
    "position": 88,
    "releaseyear": "1998",
    "track": "Wishlist"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "718",
    "pollyear": 1998,
    "position": 89,
    "releaseyear": "1998",
    "track": "Special"
    },
    {
    "alltime": False,
    "artist": "Chef",
    "country": "USA",
    "id": "719",
    "pollyear": 1998,
    "position": 90,
    "releaseyear": "1998",
    "track": "No Substitute"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "720",
    "pollyear": 1998,
    "position": 91,
    "releaseyear": "1998",
    "track": "Benedict"
    },
    {
    "alltime": False,
    "artist": "Space with Cerys Matthews",
    "country": "UK",
    "id": "721",
    "pollyear": 1998,
    "position": 92,
    "releaseyear": "1998",
    "track": "The Ballad of Tom Jones"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "722",
    "pollyear": 1998,
    "position": 93,
    "releaseyear": "1998",
    "track": "Untitled"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "723",
    "pollyear": 1998,
    "position": 94,
    "releaseyear": "1998",
    "track": "Perfect"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "724",
    "pollyear": 1998,
    "position": 95,
    "releaseyear": "1998",
    "track": "Tropicalia"
    },
    {
    "alltime": False,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "725",
    "pollyear": 1998,
    "position": 96,
    "releaseyear": "1998",
    "track": "Redneck Wonderland"
    },
    {
    "alltime": False,
    "artist": "Even",
    "country": "Australia",
    "id": "726",
    "pollyear": 1998,
    "position": 97,
    "releaseyear": "1998",
    "track": "Black Umbrella"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "727",
    "pollyear": 1998,
    "position": 98,
    "releaseyear": "1998",
    "track": "Baker Street"
    },
    {
    "alltime": False,
    "artist": "Superjesus",
    "country": "Australia",
    "id": "728",
    "pollyear": 1998,
    "position": 99,
    "releaseyear": "1998",
    "track": "Saturation"
    },
    {
    "alltime": False,
    "artist": "Not From There",
    "country": "Australia",
    "id": "729",
    "pollyear": 1998,
    "position": 100,
    "releaseyear": "1998",
    "track": "Sich Offnen"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "730",
    "pollyear": 2004,
    "position": 1,
    "releaseyear": "2004",
    "track": "Take Me Out"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "731",
    "pollyear": 2004,
    "position": 2,
    "releaseyear": "2004",
    "track": "Scar"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "732",
    "pollyear": 2004,
    "position": 3,
    "releaseyear": "2004",
    "track": "From the Sea"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "733",
    "pollyear": 2004,
    "position": 4,
    "releaseyear": "2004",
    "track": "Somebody Told Me"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "734",
    "pollyear": 2004,
    "position": 5,
    "releaseyear": "2004",
    "track": "Black Betty"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "735",
    "pollyear": 2004,
    "position": 6,
    "releaseyear": "2004",
    "track": "Ten Days"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "736",
    "pollyear": 2004,
    "position": 7,
    "releaseyear": "2004",
    "track": "Somethings Gotta Give"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "737",
    "pollyear": 2004,
    "position": 8,
    "releaseyear": "2004",
    "track": "Beautiful to Me"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "738",
    "pollyear": 2004,
    "position": 9,
    "releaseyear": "2004",
    "track": "Bless My Soul"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "739",
    "pollyear": 2004,
    "position": 10,
    "releaseyear": "2004",
    "track": "Jolene {Live}"
    },
    {
    "alltime": False,
    "artist": "Modest Mouse",
    "country": "USA",
    "id": "740",
    "pollyear": 2004,
    "position": 11,
    "releaseyear": "2004",
    "track": "Float On"
    },
    {
    "alltime": False,
    "artist": "The Dresden Dolls",
    "country": "USA",
    "id": "741",
    "pollyear": 2004,
    "position": 12,
    "releaseyear": "2004",
    "track": "Coin-Operated Boy"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "742",
    "pollyear": 2004,
    "position": 13,
    "releaseyear": "2004",
    "track": "Mr. Brightside"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "743",
    "pollyear": 2004,
    "position": 15,
    "releaseyear": "2004",
    "track": "Gamble Everything for Love"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "744",
    "pollyear": 2004,
    "position": 16,
    "releaseyear": "2004",
    "track": "Hard Act to Follow"
    },
    {
    "alltime": False,
    "artist": "Butterfingers",
    "country": "Australia",
    "id": "745",
    "pollyear": 2004,
    "position": 17,
    "releaseyear": "2004",
    "track": "Yo Mama"
    },
    {
    "alltime": False,
    "artist": "The Streets",
    "country": "UK",
    "id": "746",
    "pollyear": 2004,
    "position": 18,
    "releaseyear": "2004",
    "track": "Fit But You Know It"
    },
    {
    "alltime": False,
    "artist": "The Streets",
    "country": "UK",
    "id": "747",
    "pollyear": 2004,
    "position": 19,
    "releaseyear": "2004",
    "track": "Dry Your Eyes"
    },
    {
    "alltime": False,
    "artist": "William Shatner",
    "country": "Canada",
    "id": "748",
    "pollyear": 2004,
    "position": 21,
    "releaseyear": "2004",
    "track": "Common People"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "749",
    "pollyear": 2004,
    "position": 22,
    "releaseyear": "2004",
    "track": "American Idiot"
    },
    {
    "alltime": False,
    "artist": "Scissor Sisters",
    "country": "USA",
    "id": "750",
    "pollyear": 2004,
    "position": 23,
    "releaseyear": "2004",
    "track": "Take Your Mama"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "751",
    "pollyear": 2004,
    "position": 26,
    "releaseyear": "2004",
    "track": "Better Off Alone"
    },
    {
    "alltime": False,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "752",
    "pollyear": 2004,
    "position": 28,
    "releaseyear": "2004",
    "track": "Ch-Check It Out"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "753",
    "pollyear": 2004,
    "position": 29,
    "releaseyear": "2004",
    "track": "This Fire"
    },
    {
    "alltime": False,
    "artist": "The Dresden Dolls",
    "country": "USA",
    "id": "754",
    "pollyear": 2004,
    "position": 30,
    "releaseyear": "2004",
    "track": "Girl Anachronism"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "755",
    "pollyear": 2004,
    "position": 31,
    "releaseyear": "2004",
    "track": "The Bucket"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "756",
    "pollyear": 2004,
    "position": 32,
    "releaseyear": "2004",
    "track": "Older Than You"
    },
    {
    "alltime": False,
    "artist": "The Bees",
    "country": "UK",
    "id": "757",
    "pollyear": 2004,
    "position": 33,
    "releaseyear": "2004",
    "track": "Chicken Payback"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "758",
    "pollyear": 2004,
    "position": 34,
    "releaseyear": "2004",
    "track": "What the Fuck?"
    },
    {
    "alltime": False,
    "artist": "Scribe",
    "country": "New Zealand",
    "id": "759",
    "pollyear": 2004,
    "position": 35,
    "releaseyear": "2004",
    "track": "Not Many - The Remix!"
    },
    {
    "alltime": False,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "760",
    "pollyear": 2004,
    "position": 36,
    "releaseyear": "2004",
    "track": "Forget Her"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "761",
    "pollyear": 2004,
    "position": 37,
    "releaseyear": "2004",
    "track": "Adelaide"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "762",
    "pollyear": 2004,
    "position": 38,
    "releaseyear": "2004",
    "track": "Vertigo"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "763",
    "pollyear": 2004,
    "position": 39,
    "releaseyear": "2004",
    "track": "Smile Like You Mean It"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "764",
    "pollyear": 2004,
    "position": 40,
    "releaseyear": "2004",
    "track": "This is a Love Song"
    },
    {
    "alltime": False,
    "artist": "Faithless",
    "country": "UK",
    "id": "765",
    "pollyear": 2004,
    "position": 41,
    "releaseyear": "2004",
    "track": "Mass Destruction"
    },
    {
    "alltime": False,
    "artist": "Lior",
    "country": "Australia",
    "id": "766",
    "pollyear": 2004,
    "position": 42,
    "releaseyear": "2004",
    "track": "This Old Love"
    },
    {
    "alltime": False,
    "artist": "Dogs Die in Hot Cars",
    "country": "UK",
    "id": "767",
    "pollyear": 2004,
    "position": 43,
    "releaseyear": "2004",
    "track": "Godhopping"
    },
    {
    "alltime": False,
    "artist": "Scissor Sisters",
    "country": "USA",
    "id": "768",
    "pollyear": 2004,
    "position": 44,
    "releaseyear": "2004",
    "track": "Take Me Out {Franz Ferdinand cover}"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "769",
    "pollyear": 2004,
    "position": 45,
    "releaseyear": "2004",
    "track": "Woman"
    },
    {
    "alltime": False,
    "artist": "Rammstein",
    "country": "Germany",
    "id": "770",
    "pollyear": 2004,
    "position": 46,
    "releaseyear": "2004",
    "track": "Amerika"
    },
    {
    "alltime": False,
    "artist": "Elliott Smith",
    "country": "USA",
    "id": "771",
    "pollyear": 2004,
    "position": 48,
    "releaseyear": "2004",
    "track": "Memory Lane"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "772",
    "pollyear": 2004,
    "position": 49,
    "releaseyear": "2004",
    "track": "Casualty"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "773",
    "pollyear": 2004,
    "position": 50,
    "releaseyear": "2004",
    "track": "The Dark of the Matinee"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "774",
    "pollyear": 2004,
    "position": 51,
    "releaseyear": "2004",
    "track": "What You Want"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "775",
    "pollyear": 2004,
    "position": 52,
    "releaseyear": "2004",
    "track": "My Friend Robot"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "776",
    "pollyear": 2004,
    "position": 53,
    "releaseyear": "2004",
    "track": "English Summer Rain"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "777",
    "pollyear": 2004,
    "position": 54,
    "releaseyear": "2004",
    "track": "Bridal Train"
    },
    {
    "alltime": False,
    "artist": "The Hives",
    "country": "Sweden",
    "id": "778",
    "pollyear": 2004,
    "position": 55,
    "releaseyear": "2004",
    "track": "Walk Idiot Walk"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "779",
    "pollyear": 2004,
    "position": 56,
    "releaseyear": "2004",
    "track": "Shelter"
    },
    {
    "alltime": False,
    "artist": "Evermore",
    "country": "New Zealand",
    "id": "780",
    "pollyear": 2004,
    "position": 57,
    "releaseyear": "2004",
    "track": "For One Day"
    },
    {
    "alltime": False,
    "artist": "Scissor Sisters",
    "country": "USA",
    "id": "781",
    "pollyear": 2004,
    "position": 58,
    "releaseyear": "2004",
    "track": "Laura"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "782",
    "pollyear": 2004,
    "position": 59,
    "releaseyear": "2004",
    "track": "Solace"
    },
    {
    "alltime": False,
    "artist": "Your Wedding Night",
    "country": "Australia",
    "id": "783",
    "pollyear": 2004,
    "position": 60,
    "releaseyear": "2004",
    "track": "Lachlan"
    },
    {
    "alltime": False,
    "artist": "Deep Dish",
    "country": "USA",
    "id": "784",
    "pollyear": 2004,
    "position": 61,
    "releaseyear": "2004",
    "track": "Flash Dance"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "785",
    "pollyear": 2004,
    "position": 62,
    "releaseyear": "2004",
    "track": "Smoke"
    },
    {
    "alltime": False,
    "artist": "N.E.R.D.",
    "country": "USA",
    "id": "786",
    "pollyear": 2004,
    "position": 63,
    "releaseyear": "2004",
    "track": "She Wants to Move"
    },
    {
    "alltime": False,
    "artist": "Epicure",
    "country": "Australia",
    "id": "787",
    "pollyear": 2004,
    "position": 64,
    "releaseyear": "2004",
    "track": "Self Destruct in 5"
    },
    {
    "alltime": False,
    "artist": "Chemical Brothers",
    "country": "UK",
    "id": "788",
    "pollyear": 2004,
    "position": 65,
    "releaseyear": "2004",
    "track": "Galvanize"
    },
    {
    "alltime": False,
    "artist": "Devendra Banhart",
    "country": "USA",
    "id": "789",
    "pollyear": 2004,
    "position": 66,
    "releaseyear": "2004",
    "track": "Little Yellow Spider"
    },
    {
    "alltime": False,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "790",
    "pollyear": 2004,
    "position": 67,
    "releaseyear": "2004",
    "track": "10am Automatic"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "791",
    "pollyear": 2004,
    "position": 68,
    "releaseyear": "2004",
    "track": "Process This"
    },
    {
    "alltime": False,
    "artist": "The Freestylers",
    "country": "UK",
    "id": "792",
    "pollyear": 2004,
    "position": 69,
    "releaseyear": "2004",
    "track": "Push Up"
    },
    {
    "alltime": False,
    "artist": "Starsailor",
    "country": "UK",
    "id": "793",
    "pollyear": 2004,
    "position": 70,
    "releaseyear": "2004",
    "track": "Four to the Floor {Thin White Duke Remix}"
    },
    {
    "alltime": False,
    "artist": "The Polyphonic Spree",
    "country": "USA",
    "id": "794",
    "pollyear": 2004,
    "position": 72,
    "releaseyear": "2004",
    "track": "Hold Me Now"
    },
    {
    "alltime": False,
    "artist": "The Panda Band",
    "country": "Australia",
    "id": "795",
    "pollyear": 2004,
    "position": 73,
    "releaseyear": "2004",
    "track": "Sleepy Little Deathtoll Town"
    },
    {
    "alltime": False,
    "artist": "Interpol",
    "country": "USA",
    "id": "796",
    "pollyear": 2004,
    "position": 74,
    "releaseyear": "2004",
    "track": "Slow Hands"
    },
    {
    "alltime": False,
    "artist": "Interpol",
    "country": "USA",
    "id": "797",
    "pollyear": 2004,
    "position": 76,
    "releaseyear": "2004",
    "track": "Evil"
    },
    {
    "alltime": False,
    "artist": "Snow Patrol",
    "country": "UK",
    "id": "798",
    "pollyear": 2004,
    "position": 77,
    "releaseyear": "2004",
    "track": "Run"
    },
    {
    "alltime": False,
    "artist": "Dallas Crane",
    "country": "Australia",
    "id": "799",
    "pollyear": 2004,
    "position": 79,
    "releaseyear": "2004",
    "track": "Dirty Hearts"
    },
    {
    "alltime": False,
    "artist": "The Dissociatives",
    "country": "Australia",
    "id": "800",
    "pollyear": 2004,
    "position": 80,
    "releaseyear": "2004",
    "track": "Young Man Old Man"
    },
    {
    "alltime": False,
    "artist": "End of Fashion",
    "country": "Australia",
    "id": "801",
    "pollyear": 2004,
    "position": 81,
    "releaseyear": "2004",
    "track": "Rough Diamonds"
    },
    {
    "alltime": False,
    "artist": "Mylo",
    "country": "UK",
    "id": "802",
    "pollyear": 2004,
    "position": 82,
    "releaseyear": "2004",
    "track": "Drop the Pressure"
    },
    {
    "alltime": False,
    "artist": "Dallas Crane",
    "country": "Australia",
    "id": "803",
    "pollyear": 2004,
    "position": 83,
    "releaseyear": "2004",
    "track": "Numb All Over"
    },
    {
    "alltime": False,
    "artist": "Dogs Die in Hot Cars",
    "country": "UK",
    "id": "804",
    "pollyear": 2004,
    "position": 84,
    "releaseyear": "2004",
    "track": "I Love You Because I Have To"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "805",
    "pollyear": 2004,
    "position": 85,
    "releaseyear": "2004",
    "track": "The Drop"
    },
    {
    "alltime": False,
    "artist": "The Unicorns",
    "country": "Canada",
    "id": "806",
    "pollyear": 2004,
    "position": 86,
    "releaseyear": "2004",
    "track": "I Was Born (A Unicorn)"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "807",
    "pollyear": 2004,
    "position": 87,
    "releaseyear": "2004",
    "track": "Breathe Me"
    },
    {
    "alltime": False,
    "artist": "A Perfect Circle",
    "country": "USA",
    "id": "808",
    "pollyear": 2004,
    "position": 88,
    "releaseyear": "2004",
    "track": "Imagine"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "809",
    "pollyear": 2004,
    "position": 89,
    "releaseyear": "2004",
    "track": "Get What You Need"
    },
    {
    "alltime": False,
    "artist": "The Greenskeepers",
    "country": "USA",
    "id": "810",
    "pollyear": 2004,
    "position": 90,
    "releaseyear": "2004",
    "track": "Lotion"
    },
    {
    "alltime": False,
    "artist": "Decoder Ring",
    "country": "Australia",
    "id": "811",
    "pollyear": 2004,
    "position": 91,
    "releaseyear": "2004",
    "track": "Somersault"
    },
    {
    "alltime": False,
    "artist": "Scissor Sisters",
    "country": "USA",
    "id": "812",
    "pollyear": 2004,
    "position": 92,
    "releaseyear": "2004",
    "track": "Comfortably Numb"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "813",
    "pollyear": 2004,
    "position": 93,
    "releaseyear": "2004",
    "track": "Hello"
    },
    {
    "alltime": False,
    "artist": "The Vines",
    "country": "Australia",
    "id": "814",
    "pollyear": 2004,
    "position": 94,
    "releaseyear": "2004",
    "track": "Ride"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "815",
    "pollyear": 2004,
    "position": 95,
    "releaseyear": "2004",
    "track": "Twenty Years"
    },
    {
    "alltime": False,
    "artist": "After the Fall",
    "country": "Australia",
    "id": "816",
    "pollyear": 2004,
    "position": 96,
    "releaseyear": "2004",
    "track": "Mirror Mirror"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "817",
    "pollyear": 2004,
    "position": 97,
    "releaseyear": "2004",
    "track": "Safe Forever"
    },
    {
    "alltime": False,
    "artist": "Gomez",
    "country": "UK",
    "id": "818",
    "pollyear": 2004,
    "position": 98,
    "releaseyear": "2004",
    "track": "Catch Me Up"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "819",
    "pollyear": 2004,
    "position": 99,
    "releaseyear": "2004",
    "track": "Always"
    },
    {
    "alltime": True,
    "artist": "Joy Division",
    "country": "UK",
    "id": "820",
    "pollyear": 1990,
    "position": 1,
    "releaseyear": "1980",
    "track": "Love Will Tear Us Apart"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "821",
    "pollyear": 1990,
    "position": 2,
    "releaseyear": "1985",
    "track": "Throw Your Arms Around Me"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "822",
    "pollyear": 1990,
    "position": 3,
    "releaseyear": "1984",
    "track": "How Soon Is Now?"
    },
    {
    "alltime": True,
    "artist": "The The",
    "country": "UK",
    "id": "823",
    "pollyear": 1990,
    "position": 4,
    "releaseyear": "1983",
    "track": "Uncertain Smile"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "824",
    "pollyear": 1990,
    "position": 5,
    "releaseyear": "1983",
    "track": "Blue Monday"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "825",
    "pollyear": 1990,
    "position": 7,
    "releaseyear": "1983",
    "track": "This Charming Man"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "826",
    "pollyear": 1990,
    "position": 11,
    "releaseyear": "1980",
    "track": "A Forest"
    },
    {
    "alltime": True,
    "artist": "Dead Kennedys",
    "country": "USA",
    "id": "827",
    "pollyear": 1990,
    "position": 12,
    "releaseyear": "1980",
    "track": "Holiday in Cambodia"
    },
    {
    "alltime": True,
    "artist": "The Church",
    "country": "Australia",
    "id": "828",
    "pollyear": 1990,
    "position": 14,
    "releaseyear": "1988",
    "track": "Under the Milky Way"
    },
    {
    "alltime": True,
    "artist": "Boys Next Door",
    "country": "Australia",
    "id": "829",
    "pollyear": 1990,
    "position": 15,
    "releaseyear": "1978",
    "track": "Shivers"
    },
    {
    "alltime": True,
    "artist": "The Sugarcubes",
    "country": "Iceland",
    "id": "830",
    "pollyear": 1990,
    "position": 16,
    "releaseyear": "1987",
    "track": "Birthday"
    },
    {
    "alltime": True,
    "artist": "Kate Bush",
    "country": "UK",
    "id": "831",
    "pollyear": 1990,
    "position": 17,
    "releaseyear": "1978",
    "track": "Wuthering Heights"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "832",
    "pollyear": 1990,
    "position": 18,
    "releaseyear": "1988",
    "track": "Debaser"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "833",
    "pollyear": 1990,
    "position": 19,
    "releaseyear": "1981",
    "track": "Primary"
    },
    {
    "alltime": True,
    "artist": "Sex Pistols",
    "country": "UK",
    "id": "834",
    "pollyear": 1990,
    "position": 20,
    "releaseyear": "1976",
    "track": "Anarchy in the U.K."
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "835",
    "pollyear": 1990,
    "position": 21,
    "releaseyear": "1986",
    "track": "Bizarre Love Triangle"
    },
    {
    "alltime": True,
    "artist": "The Cult",
    "country": "UK",
    "id": "836",
    "pollyear": 1990,
    "position": 22,
    "releaseyear": "1985",
    "track": "She Sells Sanctuary"
    },
    {
    "alltime": True,
    "artist": "Black Box",
    "country": "Italy",
    "id": "837",
    "pollyear": 1990,
    "position": 24,
    "releaseyear": "1989",
    "track": "Ride On Time"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "838",
    "pollyear": 1990,
    "position": 25,
    "releaseyear": "1987",
    "track": "Just Like Heaven"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "839",
    "pollyear": 1990,
    "position": 26,
    "releaseyear": "1984",
    "track": "The Slab"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "840",
    "pollyear": 1990,
    "position": 27,
    "releaseyear": "1983",
    "track": "Cattle And Cane"
    },
    {
    "alltime": True,
    "artist": "The Clash",
    "country": "UK",
    "id": "841",
    "pollyear": 1990,
    "position": 28,
    "releaseyear": "1979",
    "track": "London Calling"
    },
    {
    "alltime": True,
    "artist": "Public Enemy",
    "country": "USA",
    "id": "842",
    "pollyear": 1990,
    "position": 29,
    "releaseyear": "1989",
    "track": "Fight the Power"
    },
    {
    "alltime": True,
    "artist": "The Only Ones",
    "country": "UK",
    "id": "843",
    "pollyear": 1990,
    "position": 30,
    "releaseyear": "1978",
    "track": "Another Girl, Another Planet"
    },
    {
    "alltime": True,
    "artist": "This Mortal Coil",
    "country": "UK",
    "id": "844",
    "pollyear": 1990,
    "position": 31,
    "releaseyear": "1983",
    "track": "Song to the Siren"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "845",
    "pollyear": 1990,
    "position": 32,
    "releaseyear": "1982",
    "track": "Talking to a Stranger"
    },
    {
    "alltime": True,
    "artist": "N.W.A.",
    "country": "USA",
    "id": "846",
    "pollyear": 1990,
    "position": 33,
    "releaseyear": "1988",
    "track": "Fuck tha Police"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "847",
    "pollyear": 1990,
    "position": 34,
    "releaseyear": "1989",
    "track": "Monkey Gone to Heaven"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "848",
    "pollyear": 1990,
    "position": 35,
    "releaseyear": "1975",
    "track": "Wish You Were Here"
    },
    {
    "alltime": True,
    "artist": "Neneh Cherry",
    "country": "Sweden",
    "id": "849",
    "pollyear": 1990,
    "position": 36,
    "releaseyear": "1988",
    "track": "Buffalo Stance"
    },
    {
    "alltime": True,
    "artist": "Prince",
    "country": "USA",
    "id": "850",
    "pollyear": 1990,
    "position": 37,
    "releaseyear": "1987",
    "track": "Sign 'O' the Times"
    },
    {
    "alltime": True,
    "artist": "Soft Cell",
    "country": "UK",
    "id": "851",
    "pollyear": 1990,
    "position": 38,
    "releaseyear": "1981",
    "track": "Tainted Love"
    },
    {
    "alltime": True,
    "artist": "Prince",
    "country": "USA",
    "id": "852",
    "pollyear": 1990,
    "position": 39,
    "releaseyear": "1986",
    "track": "Kiss"
    },
    {
    "alltime": True,
    "artist": "Soul II Soul",
    "country": "UK",
    "id": "853",
    "pollyear": 1990,
    "position": 40,
    "releaseyear": "1989",
    "track": "Back to Life (However Do You Want Me)"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "854",
    "pollyear": 1990,
    "position": 41,
    "releaseyear": "1983",
    "track": "Blister In The Sun"
    },
    {
    "alltime": True,
    "artist": "Aretha Franklin",
    "country": "USA",
    "id": "855",
    "pollyear": 1990,
    "position": 42,
    "releaseyear": "1965",
    "track": "Respect"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "856",
    "pollyear": 1990,
    "position": 43,
    "releaseyear": "1989",
    "track": "Lullaby"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "857",
    "pollyear": 1990,
    "position": 44,
    "releaseyear": "1985",
    "track": "There Is a Light That Never Goes Out"
    },
    {
    "alltime": True,
    "artist": "Jesus Jones",
    "country": "UK",
    "id": "858",
    "pollyear": 1990,
    "position": 45,
    "releaseyear": "1989",
    "track": "Info Freako"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "859",
    "pollyear": 1990,
    "position": 46,
    "releaseyear": "1987",
    "track": "The One I Love"
    },
    {
    "alltime": True,
    "artist": "Died Pretty",
    "country": "Australia",
    "id": "860",
    "pollyear": 1990,
    "position": 47,
    "releaseyear": "1989",
    "track": "Everybody Moves"
    },
    {
    "alltime": True,
    "artist": "ABBA",
    "country": "Sweden",
    "id": "861",
    "pollyear": 1990,
    "position": 48,
    "releaseyear": "1975",
    "track": "Dancing Queen"
    },
    {
    "alltime": True,
    "artist": "The Triffids",
    "country": "Australia",
    "id": "862",
    "pollyear": 1990,
    "position": 49,
    "releaseyear": "1986",
    "track": "Wide Open Road"
    },
    {
    "alltime": True,
    "artist": "David Bowie",
    "country": "UK",
    "id": "863",
    "pollyear": 1990,
    "position": 50,
    "releaseyear": "1977",
    "track": "Heroes"
    },
    {
    "alltime": True,
    "artist": "The Stone Roses",
    "country": "UK",
    "id": "864",
    "pollyear": 1990,
    "position": 51,
    "releaseyear": "1989",
    "track": "She Bangs The Drums"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "865",
    "pollyear": 1990,
    "position": 52,
    "releaseyear": "1967",
    "track": "The End"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "866",
    "pollyear": 1990,
    "position": 53,
    "releaseyear": "1986",
    "track": "Bigmouth Strikes Again"
    },
    {
    "alltime": True,
    "artist": "Radio Birdman",
    "country": "Australia",
    "id": "867",
    "pollyear": 1990,
    "position": 54,
    "releaseyear": "1978",
    "track": "Aloha Steve and Danno"
    },
    {
    "alltime": True,
    "artist": "Pixies",
    "country": "USA",
    "id": "868",
    "pollyear": 1990,
    "position": 55,
    "releaseyear": "1989",
    "track": "Here Comes Your Man"
    },
    {
    "alltime": True,
    "artist": "The Church",
    "country": "Australia",
    "id": "869",
    "pollyear": 1990,
    "position": 57,
    "releaseyear": "1981",
    "track": "The Unguarded Moment"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "870",
    "pollyear": 1990,
    "position": 58,
    "releaseyear": "1988",
    "track": "Waiting for the Great Leap Forwards"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "871",
    "pollyear": 1990,
    "position": 59,
    "releaseyear": "1986",
    "track": "Greetings to the New Brunette"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "872",
    "pollyear": 1990,
    "position": 60,
    "releaseyear": "1988",
    "track": "Deanna"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "873",
    "pollyear": 1990,
    "position": 61,
    "releaseyear": "1971",
    "track": "Stairway to Heaven"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "874",
    "pollyear": 1990,
    "position": 62,
    "releaseyear": "1971",
    "track": "L.A. Woman"
    },
    {
    "alltime": True,
    "artist": "Elvis Costello",
    "country": "UK",
    "id": "875",
    "pollyear": 1990,
    "position": 63,
    "releaseyear": "1977",
    "track": "Alison"
    },
    {
    "alltime": True,
    "artist": "Simple Minds",
    "country": "UK",
    "id": "876",
    "pollyear": 1990,
    "position": 64,
    "releaseyear": "1981",
    "track": "Love Song"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "877",
    "pollyear": 1990,
    "position": 65,
    "releaseyear": "1982",
    "track": "Temptation"
    },
    {
    "alltime": True,
    "artist": "John Lennon",
    "country": "UK",
    "id": "878",
    "pollyear": 1990,
    "position": 66,
    "releaseyear": "1971",
    "track": "Imagine"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "879",
    "pollyear": 1990,
    "position": 67,
    "releaseyear": "1983",
    "track": "The Lovecats"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "880",
    "pollyear": 1990,
    "position": 68,
    "releaseyear": "1987",
    "track": "True Faith"
    },
    {
    "alltime": True,
    "artist": "Pop Will Eat Itself",
    "country": "UK",
    "id": "881",
    "pollyear": 1990,
    "position": 70,
    "releaseyear": "1989",
    "track": "Wise Up! Sucker"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "882",
    "pollyear": 1990,
    "position": 71,
    "releaseyear": "1986",
    "track": "Say Goodbye"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "883",
    "pollyear": 1990,
    "position": 72,
    "releaseyear": "1985",
    "track": "In Between Days"
    },
    {
    "alltime": True,
    "artist": "Elvis Costello",
    "country": "UK",
    "id": "884",
    "pollyear": 1990,
    "position": 73,
    "releaseyear": "1986",
    "track": "I Want You"
    },
    {
    "alltime": True,
    "artist": "Dinosaur Jr",
    "country": "USA",
    "id": "885",
    "pollyear": 1990,
    "position": 74,
    "releaseyear": "1988",
    "track": "Freak Scene"
    },
    {
    "alltime": True,
    "artist": "Sakamoto And Sylvian",
    "country": "Japan",
    "id": "886",
    "pollyear": 1990,
    "position": 75,
    "releaseyear": "1983",
    "track": "Forbidden Colours"
    },
    {
    "alltime": True,
    "artist": "Concrete Blonde",
    "country": "USA",
    "id": "887",
    "pollyear": 1990,
    "position": 76,
    "releaseyear": "1989",
    "track": "God Is a Bullet"
    },
    {
    "alltime": True,
    "artist": "The Rolling Stones",
    "country": "UK",
    "id": "888",
    "pollyear": 1990,
    "position": 77,
    "releaseyear": "1968",
    "track": "Sympathy for the Devil"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "889",
    "pollyear": 1990,
    "position": 78,
    "releaseyear": "1986",
    "track": "Fall On Me"
    },
    {
    "alltime": True,
    "artist": "Talking Heads",
    "country": "USA",
    "id": "890",
    "pollyear": 1990,
    "position": 79,
    "releaseyear": "1981",
    "track": "Once In A Lifetime"
    },
    {
    "alltime": True,
    "artist": "Madonna",
    "country": "USA",
    "id": "891",
    "pollyear": 1990,
    "position": 80,
    "releaseyear": "1985",
    "track": "Into the Groove"
    },
    {
    "alltime": True,
    "artist": "Double Trouble And Rebel MC",
    "country": "UK",
    "id": "892",
    "pollyear": 1990,
    "position": 81,
    "releaseyear": "1989",
    "track": "Street Tuff"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "893",
    "pollyear": 1990,
    "position": 82,
    "releaseyear": "1986",
    "track": "Levi Stubbs Tears"
    },
    {
    "alltime": True,
    "artist": "The Jimi Hendrix Experience",
    "country": "USA",
    "id": "894",
    "pollyear": 1990,
    "position": 83,
    "releaseyear": "1968",
    "track": "All Along the Watchtower"
    },
    {
    "alltime": True,
    "artist": "Joy Division",
    "country": "UK",
    "id": "895",
    "pollyear": 1990,
    "position": 84,
    "releaseyear": "1980",
    "track": "Atmosphere"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "896",
    "pollyear": 1990,
    "position": 85,
    "releaseyear": "1987",
    "track": "Bye Bye Pride"
    },
    {
    "alltime": True,
    "artist": "Laughing Clowns",
    "country": "Australia",
    "id": "897",
    "pollyear": 1990,
    "position": 86,
    "releaseyear": "1984",
    "track": "Eternally Yours"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "898",
    "pollyear": 1990,
    "position": 87,
    "releaseyear": "1983",
    "track": "Add It Up"
    },
    {
    "alltime": True,
    "artist": "Sonic Youth",
    "country": "USA",
    "id": "899",
    "pollyear": 1990,
    "position": 89,
    "releaseyear": "1988",
    "track": "Teen Age Riot"
    },
    {
    "alltime": True,
    "artist": "Marvin Gaye",
    "country": "USA",
    "id": "900",
    "pollyear": 1990,
    "position": 90,
    "releaseyear": "1982",
    "track": "Sexual Healing"
    },
    {
    "alltime": True,
    "artist": "De La Soul",
    "country": "USA",
    "id": "901",
    "pollyear": 1990,
    "position": 91,
    "releaseyear": "1988",
    "track": "Say No Go"
    },
    {
    "alltime": True,
    "artist": "The Church",
    "country": "Australia",
    "id": "902",
    "pollyear": 1990,
    "position": 92,
    "releaseyear": "1988",
    "track": "Reptile"
    },
    {
    "alltime": True,
    "artist": "Tall Tales And True",
    "country": "Australia",
    "id": "903",
    "pollyear": 1990,
    "position": 93,
    "releaseyear": "1989",
    "track": "Trust"
    },
    {
    "alltime": True,
    "artist": "The The",
    "country": "UK",
    "id": "904",
    "pollyear": 1990,
    "position": 94,
    "releaseyear": "1983",
    "track": "This Is the Day"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "905",
    "pollyear": 1990,
    "position": 95,
    "releaseyear": "1979",
    "track": "Comfortably Numb"
    },
    {
    "alltime": True,
    "artist": "Concrete Blonde",
    "country": "USA",
    "id": "906",
    "pollyear": 1990,
    "position": 96,
    "releaseyear": "1989",
    "track": "Happy Birthday"
    },
    {
    "alltime": True,
    "artist": "Lou Reed",
    "country": "USA",
    "id": "907",
    "pollyear": 1990,
    "position": 98,
    "releaseyear": "1972",
    "track": "Walk On The Wild Side"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "908",
    "pollyear": 1990,
    "position": 99,
    "releaseyear": "1988",
    "track": "Orange Crush"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "909",
    "pollyear": 1997,
    "position": 1,
    "releaseyear": "1997",
    "track": "No Aphrodisiac"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "910",
    "pollyear": 1997,
    "position": 2,
    "releaseyear": "1997",
    "track": "Song 2"
    },
    {
    "alltime": False,
    "artist": "Chumbawamba",
    "country": "UK",
    "id": "911",
    "pollyear": 1997,
    "position": 3,
    "releaseyear": "1997",
    "track": "Tubthumping"
    },
    {
    "alltime": False,
    "artist": "The Verve",
    "country": "UK",
    "id": "912",
    "pollyear": 1997,
    "position": 4,
    "releaseyear": "1997",
    "track": "Bitter Sweet Symphony"
    },
    {
    "alltime": False,
    "artist": "Pauline Pantsdown",
    "country": "Australia",
    "id": "913",
    "pollyear": 1997,
    "position": 5,
    "releaseyear": "1997",
    "track": "Backdoor Man"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "914",
    "pollyear": 1997,
    "position": 6,
    "releaseyear": "1997",
    "track": "Dammit (Growing Up)"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "915",
    "pollyear": 1997,
    "position": 7,
    "releaseyear": "1997",
    "track": "Paranoid Android"
    },
    {
    "alltime": False,
    "artist": "Marilyn Manson",
    "country": "USA",
    "id": "916",
    "pollyear": 1997,
    "position": 8,
    "releaseyear": "1997",
    "track": "The Beautiful People"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "917",
    "pollyear": 1997,
    "position": 9,
    "releaseyear": "1997",
    "track": "Karma Police"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "918",
    "pollyear": 1997,
    "position": 10,
    "releaseyear": "1997",
    "track": "Leaving Home"
    },
    {
    "alltime": False,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "919",
    "pollyear": 1997,
    "position": 12,
    "releaseyear": "1997",
    "track": "One Angry Dwarf And 200 Solemn Faces"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "920",
    "pollyear": 1997,
    "position": 13,
    "releaseyear": "1997",
    "track": "Freak"
    },
    {
    "alltime": False,
    "artist": "The Superjesus",
    "country": "Australia",
    "id": "921",
    "pollyear": 1997,
    "position": 14,
    "releaseyear": "1997",
    "track": "Down Again"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "922",
    "pollyear": 1997,
    "position": 15,
    "releaseyear": "1997",
    "track": "Prisoner Of Society"
    },
    {
    "alltime": False,
    "artist": "Cordrazine",
    "country": "Australia",
    "id": "923",
    "pollyear": 1997,
    "position": 17,
    "releaseyear": "1997",
    "track": "Crazy"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "924",
    "pollyear": 1997,
    "position": 18,
    "releaseyear": "1997",
    "track": "Into My Arms"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "925",
    "pollyear": 1997,
    "position": 19,
    "releaseyear": "1997",
    "track": "Every Day Formula"
    },
    {
    "alltime": False,
    "artist": "Cake",
    "country": "USA",
    "id": "926",
    "pollyear": 1997,
    "position": 20,
    "releaseyear": "1997",
    "track": "I Will Survive"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "927",
    "pollyear": 1997,
    "position": 21,
    "releaseyear": "1997",
    "track": "Monkey Wrench"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "928",
    "pollyear": 1997,
    "position": 23,
    "releaseyear": "1997",
    "track": "Calypso"
    },
    {
    "alltime": False,
    "artist": "Korn",
    "country": "USA",
    "id": "929",
    "pollyear": 1997,
    "position": 24,
    "releaseyear": "1997",
    "track": "A.D.I.D.A.S."
    },
    {
    "alltime": False,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "930",
    "pollyear": 1997,
    "position": 26,
    "releaseyear": "1997",
    "track": "The Perfect Drug"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "931",
    "pollyear": 1997,
    "position": 27,
    "releaseyear": "1997",
    "track": "The Door"
    },
    {
    "alltime": False,
    "artist": "Dana Lyons",
    "country": "USA",
    "id": "932",
    "pollyear": 1997,
    "position": 28,
    "releaseyear": "1997",
    "track": "Cows With Guns"
    },
    {
    "alltime": False,
    "artist": "Third Eye Blind",
    "country": "USA",
    "id": "933",
    "pollyear": 1997,
    "position": 29,
    "releaseyear": "1997",
    "track": "Semi-Charmed Life"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "934",
    "pollyear": 1997,
    "position": 30,
    "releaseyear": "1997",
    "track": "Forty-Six & 2"
    },
    {
    "alltime": False,
    "artist": "Faith No More",
    "country": "USA",
    "id": "935",
    "pollyear": 1997,
    "position": 31,
    "releaseyear": "1997",
    "track": "Ashes To Ashes"
    },
    {
    "alltime": False,
    "artist": "Pendulum {Melbourne}",
    "country": "Australia",
    "id": "936",
    "pollyear": 1997,
    "position": 32,
    "releaseyear": "1997",
    "track": "Coma"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "937",
    "pollyear": 1997,
    "position": 33,
    "releaseyear": "1997",
    "track": "Military Strongmen"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "938",
    "pollyear": 1997,
    "position": 34,
    "releaseyear": "1997",
    "track": "Dcx3"
    },
    {
    "alltime": False,
    "artist": "The Sundays",
    "country": "UK",
    "id": "939",
    "pollyear": 1997,
    "position": 35,
    "releaseyear": "1997",
    "track": "Summertime"
    },
    {
    "alltime": False,
    "artist": "Ween",
    "country": "USA",
    "id": "940",
    "pollyear": 1997,
    "position": 36,
    "releaseyear": "1997",
    "track": "Mutilated Lips"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "941",
    "pollyear": 1997,
    "position": 38,
    "releaseyear": "1997",
    "track": "The Memory Remains"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "942",
    "pollyear": 1997,
    "position": 39,
    "releaseyear": "1997",
    "track": "Captain (Million Miles)"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "943",
    "pollyear": 1997,
    "position": 41,
    "releaseyear": "1997",
    "track": "Deadweight"
    },
    {
    "alltime": False,
    "artist": "Cornershop",
    "country": "UK",
    "id": "944",
    "pollyear": 1997,
    "position": 42,
    "releaseyear": "1997",
    "track": "Brimful of Asha"
    },
    {
    "alltime": False,
    "artist": "The Tea Party",
    "country": "Canada",
    "id": "945",
    "pollyear": 1997,
    "position": 44,
    "releaseyear": "1997",
    "track": "Temptation"
    },
    {
    "alltime": False,
    "artist": "The Cure",
    "country": "UK",
    "id": "946",
    "pollyear": 1997,
    "position": 45,
    "releaseyear": "1997",
    "track": "Wrong Number"
    },
    {
    "alltime": False,
    "artist": "The Bloodhound Gang",
    "country": "USA",
    "id": "947",
    "pollyear": 1997,
    "position": 46,
    "releaseyear": "1997",
    "track": "Fire Water Burn"
    },
    {
    "alltime": False,
    "artist": "Custard",
    "country": "Australia",
    "id": "948",
    "pollyear": 1997,
    "position": 48,
    "releaseyear": "1997",
    "track": "Anatomically Correct"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "949",
    "pollyear": 1997,
    "position": 49,
    "releaseyear": "1997",
    "track": "From Here On In"
    },
    {
    "alltime": False,
    "artist": "Arkarna",
    "country": "UK",
    "id": "950",
    "pollyear": 1997,
    "position": 50,
    "releaseyear": "1997",
    "track": "Eat Me"
    },
    {
    "alltime": False,
    "artist": "Everclear",
    "country": "USA",
    "id": "951",
    "pollyear": 1997,
    "position": 51,
    "releaseyear": "1997",
    "track": "So Much For The Afterglow"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "952",
    "pollyear": 1997,
    "position": 52,
    "releaseyear": "1997",
    "track": "#1 Crush"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "953",
    "pollyear": 1997,
    "position": 53,
    "releaseyear": "1997",
    "track": "You Sound Like Louis Burdett"
    },
    {
    "alltime": False,
    "artist": "Everclear",
    "country": "USA",
    "id": "954",
    "pollyear": 1997,
    "position": 54,
    "releaseyear": "1997",
    "track": "Everything To Everyone"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "955",
    "pollyear": 1997,
    "position": 55,
    "releaseyear": "1997",
    "track": "Love Rollercoaster"
    },
    {
    "alltime": False,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "956",
    "pollyear": 1997,
    "position": 56,
    "releaseyear": "1997",
    "track": "Funky Shit"
    },
    {
    "alltime": False,
    "artist": "My Drug Hell",
    "country": "UK",
    "id": "957",
    "pollyear": 1997,
    "position": 57,
    "releaseyear": "1997",
    "track": "Girl At The Bus Stop"
    },
    {
    "alltime": False,
    "artist": "Diana Ah Naid",
    "country": "Australia",
    "id": "958",
    "pollyear": 1997,
    "position": 58,
    "releaseyear": "1997",
    "track": "I Go Off"
    },
    {
    "alltime": False,
    "artist": "White Town",
    "country": "UK",
    "id": "959",
    "pollyear": 1997,
    "position": 59,
    "releaseyear": "1997",
    "track": "Your Woman"
    },
    {
    "alltime": False,
    "artist": "They Might Be Giants",
    "country": "USA",
    "id": "960",
    "pollyear": 1997,
    "position": 60,
    "releaseyear": "1997",
    "track": "New York City"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "961",
    "pollyear": 1997,
    "position": 62,
    "releaseyear": "1997",
    "track": "The End Is the Beginning Is the End"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "962",
    "pollyear": 1997,
    "position": 63,
    "releaseyear": "1997",
    "track": "Repeat"
    },
    {
    "alltime": False,
    "artist": "Faith No More",
    "country": "USA",
    "id": "963",
    "pollyear": 1997,
    "position": 64,
    "releaseyear": "1997",
    "track": "Stripsearch"
    },
    {
    "alltime": False,
    "artist": "The Lemonheads",
    "country": "USA",
    "id": "964",
    "pollyear": 1997,
    "position": 65,
    "releaseyear": "1997",
    "track": "Outdoor Type"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "965",
    "pollyear": 1997,
    "position": 66,
    "releaseyear": "1997",
    "track": "JC"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "966",
    "pollyear": 1997,
    "position": 67,
    "releaseyear": "1997",
    "track": "I Choose"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "967",
    "pollyear": 1997,
    "position": 68,
    "releaseyear": "1997",
    "track": "Cosmic Girl"
    },
    {
    "alltime": False,
    "artist": "Ween",
    "country": "USA",
    "id": "968",
    "pollyear": 1997,
    "position": 69,
    "releaseyear": "1997",
    "track": "Waving My Dick In The Wind"
    },
    {
    "alltime": False,
    "artist": "Reef",
    "country": "UK",
    "id": "969",
    "pollyear": 1997,
    "position": 70,
    "releaseyear": "1997",
    "track": "Place Your Hands"
    },
    {
    "alltime": False,
    "artist": "Robyn Loau",
    "country": "Australia",
    "id": "970",
    "pollyear": 1997,
    "position": 71,
    "releaseyear": "1997",
    "track": "Sick With Love"
    },
    {
    "alltime": False,
    "artist": "Front End Loader",
    "country": "Australia",
    "id": "971",
    "pollyear": 1997,
    "position": 72,
    "releaseyear": "1997",
    "track": "Pulse"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "972",
    "pollyear": 1997,
    "position": 74,
    "releaseyear": "1997",
    "track": "The Ghost of Tom Joad"
    },
    {
    "alltime": False,
    "artist": "Space",
    "country": "UK",
    "id": "973",
    "pollyear": 1997,
    "position": 75,
    "releaseyear": "1997",
    "track": "Female of the Species"
    },
    {
    "alltime": False,
    "artist": "Imani Coppola",
    "country": "USA",
    "id": "974",
    "pollyear": 1997,
    "position": 76,
    "releaseyear": "1997",
    "track": "Legend Of A Cowgirl"
    },
    {
    "alltime": False,
    "artist": "The Cardigans",
    "country": "Sweden",
    "id": "975",
    "pollyear": 1997,
    "position": 77,
    "releaseyear": "1997",
    "track": "Lovefool"
    },
    {
    "alltime": False,
    "artist": "The Mark of Cain",
    "country": "Australia",
    "id": "976",
    "pollyear": 1997,
    "position": 78,
    "releaseyear": "1997",
    "track": "Degenerate Boy"
    },
    {
    "alltime": False,
    "artist": "Portishead",
    "country": "UK",
    "id": "977",
    "pollyear": 1997,
    "position": 79,
    "releaseyear": "1997",
    "track": "All Mine"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "978",
    "pollyear": 1997,
    "position": 80,
    "releaseyear": "1997",
    "track": "Faded"
    },
    {
    "alltime": False,
    "artist": "Kylie Minogue",
    "country": "Australia",
    "id": "979",
    "pollyear": 1997,
    "position": 81,
    "releaseyear": "1997",
    "track": "Did It Again"
    },
    {
    "alltime": False,
    "artist": "Primus",
    "country": "USA",
    "id": "980",
    "pollyear": 1997,
    "position": 82,
    "releaseyear": "1997",
    "track": "Shake Hands with Beef"
    },
    {
    "alltime": False,
    "artist": "Lard",
    "country": "Australia",
    "id": "981",
    "pollyear": 1997,
    "position": 83,
    "releaseyear": "1997",
    "track": "I Wanna Be A Drug-Sniffing Dog"
    },
    {
    "alltime": False,
    "artist": "Brainbug",
    "country": "UK",
    "id": "982",
    "pollyear": 1997,
    "position": 85,
    "releaseyear": "1997",
    "track": "Nightmare"
    },
    {
    "alltime": False,
    "artist": "Sneaker Pimps",
    "country": "UK",
    "id": "983",
    "pollyear": 1997,
    "position": 87,
    "releaseyear": "1997",
    "track": "6 Underground"
    },
    {
    "alltime": False,
    "artist": "Beaverloop",
    "country": "Australia",
    "id": "984",
    "pollyear": 1997,
    "position": 88,
    "releaseyear": "1997",
    "track": "Nothing"
    },
    {
    "alltime": False,
    "artist": "Dandy Warhols",
    "country": "USA",
    "id": "985",
    "pollyear": 1997,
    "position": 89,
    "releaseyear": "1997",
    "track": "Last Junkie on Earth"
    },
    {
    "alltime": False,
    "artist": "Pennywise",
    "country": "USA",
    "id": "986",
    "pollyear": 1997,
    "position": 90,
    "releaseyear": "1997",
    "track": "Society"
    },
    {
    "alltime": False,
    "artist": "Blue Boy",
    "country": "UK",
    "id": "987",
    "pollyear": 1997,
    "position": 91,
    "releaseyear": "1997",
    "track": "Remember Me"
    },
    {
    "alltime": False,
    "artist": "Sidewinder",
    "country": "Australia",
    "id": "988",
    "pollyear": 1997,
    "position": 92,
    "releaseyear": "1997",
    "track": "Titanic Days"
    },
    {
    "alltime": False,
    "artist": "Skunkhour",
    "country": "Australia",
    "id": "989",
    "pollyear": 1997,
    "position": 93,
    "releaseyear": "1997",
    "track": "Weightlessness"
    },
    {
    "alltime": False,
    "artist": "Local H",
    "country": "USA",
    "id": "990",
    "pollyear": 1997,
    "position": 96,
    "releaseyear": "1997",
    "track": "Bound for the Floor"
    },
    {
    "alltime": False,
    "artist": "Arkarna",
    "country": "USA",
    "id": "991",
    "pollyear": 1997,
    "position": 97,
    "releaseyear": "1997",
    "track": "Futures Overrated"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "992",
    "pollyear": 1997,
    "position": 98,
    "releaseyear": "1997",
    "track": "Da Funk"
    },
    {
    "alltime": False,
    "artist": "Luscious Jackson",
    "country": "USA",
    "id": "993",
    "pollyear": 1997,
    "position": 99,
    "releaseyear": "1997",
    "track": "Naked Eye"
    },
    {
    "alltime": False,
    "artist": "Effigy",
    "country": "Australia",
    "id": "994",
    "pollyear": 1997,
    "position": 100,
    "releaseyear": "1997",
    "track": "I Give In"
    },
    {
    "alltime": False,
    "artist": "Alex Lloyd",
    "country": "Australia",
    "id": "995",
    "pollyear": 2001,
    "position": 1,
    "releaseyear": "2001",
    "track": "Amazing"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "996",
    "pollyear": 2001,
    "position": 2,
    "releaseyear": "2001",
    "track": "Monsters"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "997",
    "pollyear": 2001,
    "position": 3,
    "releaseyear": "2001",
    "track": "Chop Suey!"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "998",
    "pollyear": 2001,
    "position": 5,
    "releaseyear": "2001",
    "track": "Betterman"
    },
    {
    "alltime": False,
    "artist": "Alien Ant Farm",
    "country": "USA",
    "id": "999",
    "pollyear": 2001,
    "position": 6,
    "releaseyear": "2001",
    "track": "Smooth Criminal"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "1000",
    "pollyear": 2001,
    "position": 7,
    "releaseyear": "2001",
    "track": "Island In The Sun"
    },
    {
    "alltime": False,
    "artist": "The Avalanches",
    "country": "Australia",
    "id": "1001",
    "pollyear": 2001,
    "position": 8,
    "releaseyear": "2001",
    "track": "Since I Left You"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "1002",
    "pollyear": 2001,
    "position": 9,
    "releaseyear": "2001",
    "track": "Clint Eastwood"
    },
    {
    "alltime": False,
    "artist": "Cake",
    "country": "USA",
    "id": "1003",
    "pollyear": 2001,
    "position": 10,
    "releaseyear": "2001",
    "track": "Short Skirt/Long Jacket"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "1004",
    "pollyear": 2001,
    "position": 11,
    "releaseyear": "2001",
    "track": "Cherry Lips (Go Baby Go!)"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1005",
    "pollyear": 2001,
    "position": 12,
    "releaseyear": "2001",
    "track": "Last Nite"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "1006",
    "pollyear": 2001,
    "position": 13,
    "releaseyear": "2001",
    "track": "Three Dimensions"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "1007",
    "pollyear": 2001,
    "position": 14,
    "releaseyear": "2001",
    "track": "Schism"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "1008",
    "pollyear": 2001,
    "position": 15,
    "releaseyear": "2001",
    "track": "19-2000"
    },
    {
    "alltime": False,
    "artist": "28 Days/Apollo 440",
    "country": "Australia",
    "id": "1009",
    "pollyear": 2001,
    "position": 16,
    "releaseyear": "2001",
    "track": "Say What?"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "1010",
    "pollyear": 2001,
    "position": 18,
    "releaseyear": "2001",
    "track": "Renegades of Funk"
    },
    {
    "alltime": False,
    "artist": "George",
    "country": "Australia",
    "id": "1011",
    "pollyear": 2001,
    "position": 19,
    "releaseyear": "2001",
    "track": "Special Ones"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "1012",
    "pollyear": 2001,
    "position": 20,
    "releaseyear": "2001",
    "track": "Hash Pipe"
    },
    {
    "alltime": False,
    "artist": "Fatboy Slim",
    "country": "UK",
    "id": "1013",
    "pollyear": 2001,
    "position": 21,
    "releaseyear": "2001",
    "track": "Weapon of Choice"
    },
    {
    "alltime": False,
    "artist": "Gerling",
    "country": "Australia",
    "id": "1014",
    "pollyear": 2001,
    "position": 24,
    "releaseyear": "2001",
    "track": "Dust Me Selecta"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1015",
    "pollyear": 2001,
    "position": 25,
    "releaseyear": "2001",
    "track": "Wake Up"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "1016",
    "pollyear": 2001,
    "position": 26,
    "releaseyear": "2001",
    "track": "Little L"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "1017",
    "pollyear": 2001,
    "position": 27,
    "releaseyear": "2001",
    "track": "Fat Cop"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "1018",
    "pollyear": 2001,
    "position": 28,
    "releaseyear": "2001",
    "track": "Fall Down"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "1019",
    "pollyear": 2001,
    "position": 29,
    "releaseyear": "2001",
    "track": "Take"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "1020",
    "pollyear": 2001,
    "position": 30,
    "releaseyear": "2001",
    "track": "The Girl Of My Dreams (Is Giving Me Nightmares)"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1021",
    "pollyear": 2001,
    "position": 31,
    "releaseyear": "2001",
    "track": "Planet Earth"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1022",
    "pollyear": 2001,
    "position": 32,
    "releaseyear": "2001",
    "track": "Special K"
    },
    {
    "alltime": False,
    "artist": "James",
    "country": "UK",
    "id": "1023",
    "pollyear": 2001,
    "position": 33,
    "releaseyear": "2001",
    "track": "Getting Away With It (All Messed Up)"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1024",
    "pollyear": 2001,
    "position": 34,
    "releaseyear": "2001",
    "track": "Who Sold Her Out"
    },
    {
    "alltime": False,
    "artist": "Dido",
    "country": "UK",
    "id": "1025",
    "pollyear": 2001,
    "position": 35,
    "releaseyear": "2001",
    "track": "Thank You"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "1026",
    "pollyear": 2001,
    "position": 36,
    "releaseyear": "2001",
    "track": "Pyramid Song"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "1027",
    "pollyear": 2001,
    "position": 37,
    "releaseyear": "2001",
    "track": "Twenty Years"
    },
    {
    "alltime": False,
    "artist": "New Order",
    "country": "UK",
    "id": "1028",
    "pollyear": 2001,
    "position": 38,
    "releaseyear": "2001",
    "track": "Crystal"
    },
    {
    "alltime": False,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "1029",
    "pollyear": 2001,
    "position": 39,
    "releaseyear": "2001",
    "track": "Cocaine"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "1030",
    "pollyear": 2001,
    "position": 40,
    "releaseyear": "2001",
    "track": "Elevation {Tomb Raider Remix}"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "1031",
    "pollyear": 2001,
    "position": 41,
    "releaseyear": "2001",
    "track": "Superstraight"
    },
    {
    "alltime": False,
    "artist": "The Eels",
    "country": "USA",
    "id": "1032",
    "pollyear": 2001,
    "position": 43,
    "releaseyear": "2001",
    "track": "Souljacker"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "1033",
    "pollyear": 2001,
    "position": 44,
    "releaseyear": "2001",
    "track": "Androgyny"
    },
    {
    "alltime": False,
    "artist": "Tori Amos",
    "country": "USA",
    "id": "1034",
    "pollyear": 2001,
    "position": 45,
    "releaseyear": "2001",
    "track": "Strange Little Girl"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "1035",
    "pollyear": 2001,
    "position": 46,
    "releaseyear": "2001",
    "track": "Untitled"
    },
    {
    "alltime": False,
    "artist": "Augie March",
    "country": "Australia",
    "id": "1036",
    "pollyear": 2001,
    "position": 47,
    "releaseyear": "2001",
    "track": "There Is No Such Place"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "1037",
    "pollyear": 2001,
    "position": 49,
    "releaseyear": "2001",
    "track": "Parabola"
    },
    {
    "alltime": False,
    "artist": "Paul Mac",
    "country": "Australia",
    "id": "1038",
    "pollyear": 2001,
    "position": 50,
    "releaseyear": "2001",
    "track": "Just The Thing"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "1039",
    "pollyear": 2001,
    "position": 51,
    "releaseyear": "2001",
    "track": "Fifteen Feet Of Pure White Snow"
    },
    {
    "alltime": False,
    "artist": "Motor Ace",
    "country": "Australia",
    "id": "1040",
    "pollyear": 2001,
    "position": 53,
    "releaseyear": "2001",
    "track": "Hey Driver"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "1041",
    "pollyear": 2001,
    "position": 54,
    "releaseyear": "2001",
    "track": "The Rock Show"
    },
    {
    "alltime": False,
    "artist": "Linkin Park",
    "country": "USA",
    "id": "1042",
    "pollyear": 2001,
    "position": 55,
    "releaseyear": "2001",
    "track": "One Step Closer"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "1043",
    "pollyear": 2001,
    "position": 56,
    "releaseyear": "2001",
    "track": "Kick A Hole In The Sky"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "1044",
    "pollyear": 2001,
    "position": 57,
    "releaseyear": "2001",
    "track": "Get Up"
    },
    {
    "alltime": False,
    "artist": "Jimmy Eat World",
    "country": "USA",
    "id": "1045",
    "pollyear": 2001,
    "position": 58,
    "releaseyear": "2001",
    "track": "Bleed American"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1046",
    "pollyear": 2001,
    "position": 59,
    "releaseyear": "2001",
    "track": "Hard To Explain"
    },
    {
    "alltime": False,
    "artist": "At the Drive-In",
    "country": "USA",
    "id": "1047",
    "pollyear": 2001,
    "position": 60,
    "releaseyear": "2001",
    "track": "Pattern Against User"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "1048",
    "pollyear": 2001,
    "position": 61,
    "releaseyear": "2001",
    "track": "One More Time"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "1049",
    "pollyear": 2001,
    "position": 62,
    "releaseyear": "2001",
    "track": "You Give Me Something"
    },
    {
    "alltime": False,
    "artist": "Alex Lloyd",
    "country": "Australia",
    "id": "1050",
    "pollyear": 2001,
    "position": 63,
    "releaseyear": "2001",
    "track": "Downtown"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1051",
    "pollyear": 2001,
    "position": 64,
    "releaseyear": "2001",
    "track": "Hotel Yorba"
    },
    {
    "alltime": False,
    "artist": "Ash",
    "country": "Ireland",
    "id": "1052",
    "pollyear": 2001,
    "position": 65,
    "releaseyear": "2001",
    "track": "Burn Baby Burn"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1053",
    "pollyear": 2001,
    "position": 66,
    "releaseyear": "2001",
    "track": "New York City Cops"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "1054",
    "pollyear": 2001,
    "position": 67,
    "releaseyear": "2001",
    "track": "Not The Same"
    },
    {
    "alltime": False,
    "artist": "Blueline Medic",
    "country": "Australia",
    "id": "1055",
    "pollyear": 2001,
    "position": 68,
    "releaseyear": "2001",
    "track": "Making The Nouveau Riche"
    },
    {
    "alltime": False,
    "artist": "Unwritten Law",
    "country": "USA",
    "id": "1056",
    "pollyear": 2001,
    "position": 69,
    "releaseyear": "2001",
    "track": "Up All Night"
    },
    {
    "alltime": False,
    "artist": "Rammstein",
    "country": "Germany",
    "id": "1057",
    "pollyear": 2001,
    "position": 70,
    "releaseyear": "2001",
    "track": "Links 2-3-4"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1058",
    "pollyear": 2001,
    "position": 71,
    "releaseyear": "2001",
    "track": "Outta My Head"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1059",
    "pollyear": 2001,
    "position": 72,
    "releaseyear": "2001",
    "track": "Roll On"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1060",
    "pollyear": 2001,
    "position": 73,
    "releaseyear": "2001",
    "track": "Plug In Baby"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "1061",
    "pollyear": 2001,
    "position": 74,
    "releaseyear": "2001",
    "track": "Knives Out"
    },
    {
    "alltime": False,
    "artist": "Groove Armada",
    "country": "UK",
    "id": "1062",
    "pollyear": 2001,
    "position": 75,
    "releaseyear": "2001",
    "track": "My Friend"
    },
    {
    "alltime": False,
    "artist": "The Avalanches",
    "country": "Australia",
    "id": "1063",
    "pollyear": 2001,
    "position": 76,
    "releaseyear": "2001",
    "track": "Radio"
    },
    {
    "alltime": False,
    "artist": "Big Heavy Stuff",
    "country": "Australia",
    "id": "1064",
    "pollyear": 2001,
    "position": 77,
    "releaseyear": "2001",
    "track": "Hibernate"
    },
    {
    "alltime": False,
    "artist": "Cruel Sea",
    "country": "Australia",
    "id": "1065",
    "pollyear": 2001,
    "position": 78,
    "releaseyear": "2001",
    "track": "A Simple Goodbye"
    },
    {
    "alltime": False,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "1066",
    "pollyear": 2001,
    "position": 79,
    "releaseyear": "2001",
    "track": "Imitation of Life"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1067",
    "pollyear": 2001,
    "position": 80,
    "releaseyear": "2001",
    "track": "Bliss"
    },
    {
    "alltime": False,
    "artist": "Crazy Town",
    "country": "USA",
    "id": "1068",
    "pollyear": 2001,
    "position": 81,
    "releaseyear": "2001",
    "track": "Butterfly"
    },
    {
    "alltime": False,
    "artist": "Ash",
    "country": "UK",
    "id": "1069",
    "pollyear": 2001,
    "position": 83,
    "releaseyear": "2001",
    "track": "Shining Light"
    },
    {
    "alltime": False,
    "artist": "Supermen Lovers",
    "country": "France",
    "id": "1070",
    "pollyear": 2001,
    "position": 84,
    "releaseyear": "2001",
    "track": "Starlight"
    },
    {
    "alltime": False,
    "artist": "At the Drive-In",
    "country": "USA",
    "id": "1071",
    "pollyear": 2001,
    "position": 85,
    "releaseyear": "2001",
    "track": "Invalid Litter Dept."
    },
    {
    "alltime": False,
    "artist": "Rhubarb",
    "country": "Australia",
    "id": "1072",
    "pollyear": 2001,
    "position": 86,
    "releaseyear": "2001",
    "track": "Light On Your Shoulder"
    },
    {
    "alltime": False,
    "artist": "Michael Franti and Spearhead",
    "country": "USA",
    "id": "1073",
    "pollyear": 2001,
    "position": 87,
    "releaseyear": "2001",
    "track": "Rock The Nation"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1074",
    "pollyear": 2001,
    "position": 88,
    "releaseyear": "2001",
    "track": "Four On The Floor"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1075",
    "pollyear": 2001,
    "position": 89,
    "releaseyear": "2001",
    "track": "New Born"
    },
    {
    "alltime": False,
    "artist": "New Order",
    "country": "UK",
    "id": "1076",
    "pollyear": 2001,
    "position": 90,
    "releaseyear": "2001",
    "track": "60 Miles an Hour"
    },
    {
    "alltime": False,
    "artist": "Sum 41",
    "country": "Canada",
    "id": "1077",
    "pollyear": 2001,
    "position": 91,
    "releaseyear": "2001",
    "track": "Fat Lip"
    },
    {
    "alltime": False,
    "artist": "George",
    "country": "Australia",
    "id": "1078",
    "pollyear": 2001,
    "position": 92,
    "releaseyear": "2001",
    "track": "Run"
    },
    {
    "alltime": False,
    "artist": "Butthole Surfers",
    "country": "USA",
    "id": "1079",
    "pollyear": 2001,
    "position": 93,
    "releaseyear": "2001",
    "track": "The Shame of Life"
    },
    {
    "alltime": False,
    "artist": "Depeche Mode",
    "country": "UK",
    "id": "1080",
    "pollyear": 2001,
    "position": 94,
    "releaseyear": "2001",
    "track": "I Feel Loved"
    },
    {
    "alltime": False,
    "artist": "Good Charlotte",
    "country": "USA",
    "id": "1081",
    "pollyear": 2001,
    "position": 95,
    "releaseyear": "2001",
    "track": "Little Things"
    },
    {
    "alltime": False,
    "artist": "Pennywise",
    "country": "USA",
    "id": "1082",
    "pollyear": 2001,
    "position": 96,
    "releaseyear": "2001",
    "track": "Fuck Authority"
    },
    {
    "alltime": False,
    "artist": "Superheist",
    "country": "Australia",
    "id": "1083",
    "pollyear": 2001,
    "position": 97,
    "releaseyear": "2001",
    "track": "Step Back"
    },
    {
    "alltime": False,
    "artist": "Faithless",
    "country": "UK",
    "id": "1084",
    "pollyear": 2001,
    "position": 98,
    "releaseyear": "2001",
    "track": "We Come 1"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "1085",
    "pollyear": 2001,
    "position": 99,
    "releaseyear": "2001",
    "track": "It Began in Afrika"
    },
    {
    "alltime": False,
    "artist": "Endorphin",
    "country": "Australia",
    "id": "1086",
    "pollyear": 2001,
    "position": 100,
    "releaseyear": "2001",
    "track": "Sex And Violence"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1087",
    "pollyear": 2007,
    "position": 1,
    "releaseyear": "2007",
    "track": "Knights of Cydonia"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1088",
    "pollyear": 2007,
    "position": 2,
    "releaseyear": "2007",
    "track": "Straight Lines"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1089",
    "pollyear": 2007,
    "position": 3,
    "releaseyear": "2007",
    "track": "On Call"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "1090",
    "pollyear": 2007,
    "position": 4,
    "releaseyear": "2007",
    "track": "Better Than"
    },
    {
    "alltime": False,
    "artist": "Faker",
    "country": "Australia",
    "id": "1091",
    "pollyear": 2007,
    "position": 5,
    "releaseyear": "2007",
    "track": "This Heart Attack"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1092",
    "pollyear": 2007,
    "position": 6,
    "releaseyear": "2007",
    "track": "The Pretender"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "1093",
    "pollyear": 2007,
    "position": 7,
    "releaseyear": "2007",
    "track": "Harder, Better, Faster, Stronger {Alive 2007}"
    },
    {
    "alltime": False,
    "artist": "Cold War Kids",
    "country": "USA",
    "id": "1094",
    "pollyear": 2007,
    "position": 8,
    "releaseyear": "2007",
    "track": "Hang Me Up to Dry"
    },
    {
    "alltime": False,
    "artist": "Bluejuice",
    "country": "Australia",
    "id": "1095",
    "pollyear": 2007,
    "position": 11,
    "releaseyear": "2007",
    "track": "Vitriol"
    },
    {
    "alltime": False,
    "artist": "Kaiser Chiefs",
    "country": "UK",
    "id": "1096",
    "pollyear": 2007,
    "position": 13,
    "releaseyear": "2007",
    "track": "Ruby"
    },
    {
    "alltime": False,
    "artist": "Muscles",
    "country": "Australia",
    "id": "1097",
    "pollyear": 2007,
    "position": 14,
    "releaseyear": "2007",
    "track": "Ice Cream"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1098",
    "pollyear": 2007,
    "position": 15,
    "releaseyear": "2007",
    "track": "Lost and Running"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "1099",
    "pollyear": 2007,
    "position": 16,
    "releaseyear": "2007",
    "track": "Snakeskin"
    },
    {
    "alltime": False,
    "artist": "M.I.A",
    "country": "UK",
    "id": "1100",
    "pollyear": 2007,
    "position": 17,
    "releaseyear": "2007",
    "track": "Paper Planes"
    },
    {
    "alltime": False,
    "artist": "The Presets",
    "country": "Australia",
    "id": "1101",
    "pollyear": 2007,
    "position": 18,
    "releaseyear": "2007",
    "track": "My People"
    },
    {
    "alltime": False,
    "artist": "Architecture in Helsinki",
    "country": "Australia",
    "id": "1102",
    "pollyear": 2007,
    "position": 19,
    "releaseyear": "2007",
    "track": "Heart It Races"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "1103",
    "pollyear": 2007,
    "position": 20,
    "releaseyear": "2007",
    "track": "Stronger"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "1104",
    "pollyear": 2007,
    "position": 21,
    "releaseyear": "2007",
    "track": "The Salmon Dance"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "1105",
    "pollyear": 2007,
    "position": 22,
    "releaseyear": "2007",
    "track": "Used To Get High"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1106",
    "pollyear": 2007,
    "position": 23,
    "releaseyear": "2007",
    "track": "Icky Thump"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1107",
    "pollyear": 2007,
    "position": 24,
    "releaseyear": "2007",
    "track": "Hunting For Witches"
    },
    {
    "alltime": False,
    "artist": "Urthboy",
    "country": "Australia",
    "id": "1108",
    "pollyear": 2007,
    "position": 25,
    "releaseyear": "2007",
    "track": "We Get Around"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1109",
    "pollyear": 2007,
    "position": 26,
    "releaseyear": "2007",
    "track": "Recapturing The Vibe (Restrung)"
    },
    {
    "alltime": False,
    "artist": "Operator Please",
    "country": "Australia",
    "id": "1110",
    "pollyear": 2007,
    "position": 27,
    "releaseyear": "2007",
    "track": "Just a Song About Ping Pong"
    },
    {
    "alltime": False,
    "artist": "Silversun Pickups",
    "country": "USA",
    "id": "1111",
    "pollyear": 2007,
    "position": 28,
    "releaseyear": "2007",
    "track": "Lazy Eye"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "1112",
    "pollyear": 2007,
    "position": 29,
    "releaseyear": "2007",
    "track": "Real Love {Like A Version}"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1113",
    "pollyear": 2007,
    "position": 30,
    "releaseyear": "2007",
    "track": "If You Keep Losing Sleep"
    },
    {
    "alltime": False,
    "artist": "Angus and Julia Stone",
    "country": "Australia",
    "id": "1114",
    "pollyear": 2007,
    "position": 31,
    "releaseyear": "2007",
    "track": "Wasted"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1115",
    "pollyear": 2007,
    "position": 33,
    "releaseyear": "2007",
    "track": "Fans"
    },
    {
    "alltime": False,
    "artist": "Feist",
    "country": "Canada",
    "id": "1116",
    "pollyear": 2007,
    "position": 34,
    "releaseyear": "2007",
    "track": "1234"
    },
    {
    "alltime": False,
    "artist": "Justice",
    "country": "France",
    "id": "1117",
    "pollyear": 2007,
    "position": 35,
    "releaseyear": "2007",
    "track": "D.A.N.C.E."
    },
    {
    "alltime": False,
    "artist": "Architecture in Helsinki",
    "country": "Australia",
    "id": "1118",
    "pollyear": 2007,
    "position": 36,
    "releaseyear": "2007",
    "track": "Hold Music"
    },
    {
    "alltime": False,
    "artist": "Cold War Kids",
    "country": "USA",
    "id": "1119",
    "pollyear": 2007,
    "position": 37,
    "releaseyear": "2007",
    "track": "Hospital Beds"
    },
    {
    "alltime": False,
    "artist": "The Beautiful Girls",
    "country": "Australia",
    "id": "1120",
    "pollyear": 2007,
    "position": 38,
    "releaseyear": "2007",
    "track": "I Thought About You"
    },
    {
    "alltime": False,
    "artist": "Cut Copy",
    "country": "Australia",
    "id": "1121",
    "pollyear": 2007,
    "position": 39,
    "releaseyear": "2007",
    "track": "Hearts on Fire"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1122",
    "pollyear": 2007,
    "position": 40,
    "releaseyear": "2007",
    "track": "I Still Remember"
    },
    {
    "alltime": False,
    "artist": "Modest Mouse",
    "country": "USA",
    "id": "1123",
    "pollyear": 2007,
    "position": 41,
    "releaseyear": "2007",
    "track": "Dashboard"
    },
    {
    "alltime": False,
    "artist": "Tegan and Sara",
    "country": "Canada",
    "id": "1124",
    "pollyear": 2007,
    "position": 42,
    "releaseyear": "2007",
    "track": "Back In Your Head"
    },
    {
    "alltime": False,
    "artist": "Lupe Fiasco",
    "country": "USA",
    "id": "1125",
    "pollyear": 2007,
    "position": 43,
    "releaseyear": "2007",
    "track": "Superstar"
    },
    {
    "alltime": False,
    "artist": "My Chemical Romance",
    "country": "USA",
    "id": "1126",
    "pollyear": 2007,
    "position": 44,
    "releaseyear": "2007",
    "track": "Teenagers"
    },
    {
    "alltime": False,
    "artist": "Angus and Julia Stone",
    "country": "Australia",
    "id": "1127",
    "pollyear": 2007,
    "position": 45,
    "releaseyear": "2007",
    "track": "The Beast"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "1128",
    "pollyear": 2007,
    "position": 46,
    "releaseyear": "2007",
    "track": "Tie Up My Hands"
    },
    {
    "alltime": False,
    "artist": "Cog",
    "country": "Australia",
    "id": "1129",
    "pollyear": 2007,
    "position": 47,
    "releaseyear": "2007",
    "track": "What If"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1130",
    "pollyear": 2007,
    "position": 48,
    "releaseyear": "2007",
    "track": "Flux"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "1131",
    "pollyear": 2007,
    "position": 49,
    "releaseyear": "2007",
    "track": "Fluorescent Adolescent"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1132",
    "pollyear": 2007,
    "position": 50,
    "releaseyear": "2007",
    "track": "So Many Nights"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "1133",
    "pollyear": 2007,
    "position": 51,
    "releaseyear": "2007",
    "track": "Peachy"
    },
    {
    "alltime": False,
    "artist": "Kisschasy",
    "country": "Australia",
    "id": "1134",
    "pollyear": 2007,
    "position": 52,
    "releaseyear": "2007",
    "track": "Spray on Pants"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "1135",
    "pollyear": 2007,
    "position": 53,
    "releaseyear": "2007",
    "track": "Steer"
    },
    {
    "alltime": False,
    "artist": "Klaxons",
    "country": "UK",
    "id": "1136",
    "pollyear": 2007,
    "position": 54,
    "releaseyear": "2007",
    "track": "Golden Skans"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "1137",
    "pollyear": 2007,
    "position": 55,
    "releaseyear": "2007",
    "track": "Good Excuse"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "1138",
    "pollyear": 2007,
    "position": 56,
    "releaseyear": "2007",
    "track": "Better People"
    },
    {
    "alltime": False,
    "artist": "Midnight Juggernauts",
    "country": "Australia",
    "id": "1139",
    "pollyear": 2007,
    "position": 57,
    "releaseyear": "2007",
    "track": "Into the Galaxy"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1140",
    "pollyear": 2007,
    "position": 58,
    "releaseyear": "2007",
    "track": "Invincible"
    },
    {
    "alltime": False,
    "artist": "The Fratellis",
    "country": "UK",
    "id": "1141",
    "pollyear": 2007,
    "position": 59,
    "releaseyear": "2007",
    "track": "Chelsea Dagger"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1142",
    "pollyear": 2007,
    "position": 60,
    "releaseyear": "2007",
    "track": "Charmer"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "1143",
    "pollyear": 2007,
    "position": 61,
    "releaseyear": "2007",
    "track": "Wayside"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1144",
    "pollyear": 2007,
    "position": 62,
    "releaseyear": "2007",
    "track": "No Longer There"
    },
    {
    "alltime": False,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "1145",
    "pollyear": 2007,
    "position": 63,
    "releaseyear": "2007",
    "track": "The Only Way {Gotye cover}"
    },
    {
    "alltime": False,
    "artist": "The Shins",
    "country": "USA",
    "id": "1146",
    "pollyear": 2007,
    "position": 64,
    "releaseyear": "2007",
    "track": "Australia"
    },
    {
    "alltime": False,
    "artist": "Editors",
    "country": "UK",
    "id": "1147",
    "pollyear": 2007,
    "position": 65,
    "releaseyear": "2007",
    "track": "Smokers Outside the Hospital Doors"
    },
    {
    "alltime": False,
    "artist": "Amy Winehouse",
    "country": "UK",
    "id": "1148",
    "pollyear": 2007,
    "position": 67,
    "releaseyear": "2007",
    "track": "Rehab {Jay-Z Remix}"
    },
    {
    "alltime": False,
    "artist": "Ben Kweller",
    "country": "USA",
    "id": "1149",
    "pollyear": 2007,
    "position": 68,
    "releaseyear": "2007",
    "track": "Penny on the Train Track"
    },
    {
    "alltime": False,
    "artist": "Digitalism",
    "country": "Germany",
    "id": "1150",
    "pollyear": 2007,
    "position": 69,
    "releaseyear": "2007",
    "track": "Pogo"
    },
    {
    "alltime": False,
    "artist": "Tegan and Sara",
    "country": "Canada",
    "id": "1151",
    "pollyear": 2007,
    "position": 70,
    "releaseyear": "2007",
    "track": "The Con"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "1152",
    "pollyear": 2007,
    "position": 71,
    "releaseyear": "2007",
    "track": "Reach"
    },
    {
    "alltime": False,
    "artist": "Jose Gonzalez",
    "country": "Sweden",
    "id": "1153",
    "pollyear": 2007,
    "position": 72,
    "releaseyear": "2007",
    "track": "Down the Line"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "1154",
    "pollyear": 2007,
    "position": 73,
    "releaseyear": "2007",
    "track": "Black Tattoo"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "1155",
    "pollyear": 2007,
    "position": 74,
    "releaseyear": "2007",
    "track": "Run the Red Light"
    },
    {
    "alltime": False,
    "artist": "Kasabian",
    "country": "UK",
    "id": "1156",
    "pollyear": 2007,
    "position": 75,
    "releaseyear": "2007",
    "track": "Shoot the Runner"
    },
    {
    "alltime": False,
    "artist": "Muscles",
    "country": "Australia",
    "id": "1157",
    "pollyear": 2007,
    "position": 76,
    "releaseyear": "2007",
    "track": "Sweaty"
    },
    {
    "alltime": False,
    "artist": "Operator Please",
    "country": "Australia",
    "id": "1158",
    "pollyear": 2007,
    "position": 77,
    "releaseyear": "2007",
    "track": "Get What You Want"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "1159",
    "pollyear": 2007,
    "position": 78,
    "releaseyear": "2007",
    "track": "Brianstorm"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1160",
    "pollyear": 2007,
    "position": 79,
    "releaseyear": "2007",
    "track": "Lines On Palms"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1161",
    "pollyear": 2007,
    "position": 80,
    "releaseyear": "2007",
    "track": "Reflections of a Sound"
    },
    {
    "alltime": False,
    "artist": "Arcade Fire",
    "country": "Canada",
    "id": "1162",
    "pollyear": 2007,
    "position": 81,
    "releaseyear": "2007",
    "track": "No Cars Go"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1163",
    "pollyear": 2007,
    "position": 82,
    "releaseyear": "2007",
    "track": "Long Road to Ruin"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1164",
    "pollyear": 2007,
    "position": 83,
    "releaseyear": "2007",
    "track": "Pleased to Meet You"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "1165",
    "pollyear": 2007,
    "position": 84,
    "releaseyear": "2007",
    "track": "Do It Again"
    },
    {
    "alltime": False,
    "artist": "Yeah Yeah Yeahs",
    "country": "USA",
    "id": "1166",
    "pollyear": 2007,
    "position": 85,
    "releaseyear": "2007",
    "track": "Down Boy"
    },
    {
    "alltime": False,
    "artist": "Midnight Juggernauts",
    "country": "Australia",
    "id": "1167",
    "pollyear": 2007,
    "position": 86,
    "releaseyear": "2007",
    "track": "Tombstone"
    },
    {
    "alltime": False,
    "artist": "Jackson Jackson",
    "country": "Australia",
    "id": "1168",
    "pollyear": 2007,
    "position": 87,
    "releaseyear": "2007",
    "track": "Eliza"
    },
    {
    "alltime": False,
    "artist": "The Cops",
    "country": "Australia",
    "id": "1169",
    "pollyear": 2007,
    "position": 88,
    "releaseyear": "2007",
    "track": "The Message"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "1170",
    "pollyear": 2007,
    "position": 89,
    "releaseyear": "2007",
    "track": "Sick, Sick, Sick"
    },
    {
    "alltime": False,
    "artist": "Clare Bowditch and the Feeding Set",
    "country": "Australia",
    "id": "1171",
    "pollyear": 2007,
    "position": 90,
    "releaseyear": "2007",
    "track": "When the Lights Went Down"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1172",
    "pollyear": 2007,
    "position": 91,
    "releaseyear": "2007",
    "track": "Sew My Name"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "1173",
    "pollyear": 2007,
    "position": 92,
    "releaseyear": "2007",
    "track": "Sun Dirt Water"
    },
    {
    "alltime": False,
    "artist": "The Bumblebeez",
    "country": "Australia",
    "id": "1174",
    "pollyear": 2007,
    "position": 93,
    "releaseyear": "2007",
    "track": "Dr. Love"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "1175",
    "pollyear": 2007,
    "position": 94,
    "releaseyear": "2007",
    "track": "Jigsaw Falling Into Place"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "1176",
    "pollyear": 2007,
    "position": 95,
    "releaseyear": "2007",
    "track": "Samson"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "1177",
    "pollyear": 2007,
    "position": 96,
    "releaseyear": "2007",
    "track": "Love Me Like the World Is Ending"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1178",
    "pollyear": 2007,
    "position": 97,
    "releaseyear": "2007",
    "track": "Forever Song"
    },
    {
    "alltime": False,
    "artist": "Interpol",
    "country": "USA",
    "id": "1179",
    "pollyear": 2007,
    "position": 98,
    "releaseyear": "2007",
    "track": "The Heinrich Maneuver"
    },
    {
    "alltime": False,
    "artist": "The Hives",
    "country": "Sweden",
    "id": "1180",
    "pollyear": 2007,
    "position": 99,
    "releaseyear": "2007",
    "track": "Tick Tick Boom"
    },
    {
    "alltime": False,
    "artist": "Pnau",
    "country": "Australia",
    "id": "1181",
    "pollyear": 2007,
    "position": 100,
    "releaseyear": "2007",
    "track": "Wild Strawberries"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1182",
    "pollyear": 2008,
    "position": 1,
    "releaseyear": "2008",
    "track": "Sex on Fire"
    },
    {
    "alltime": False,
    "artist": "MGMT",
    "country": "USA",
    "id": "1183",
    "pollyear": 2008,
    "position": 2,
    "releaseyear": "2008",
    "track": "Electric Feel"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1184",
    "pollyear": 2008,
    "position": 3,
    "releaseyear": "2008",
    "track": "Use Somebody"
    },
    {
    "alltime": False,
    "artist": "Empire of the Sun",
    "country": "Australia",
    "id": "1185",
    "pollyear": 2008,
    "position": 4,
    "releaseyear": "2008",
    "track": "Walking on a Dream"
    },
    {
    "alltime": False,
    "artist": "MGMT",
    "country": "USA",
    "id": "1186",
    "pollyear": 2008,
    "position": 5,
    "releaseyear": "2008",
    "track": "Kids"
    },
    {
    "alltime": False,
    "artist": "The Presets",
    "country": "Australia",
    "id": "1187",
    "pollyear": 2008,
    "position": 6,
    "releaseyear": "2008",
    "track": "Talk Like That"
    },
    {
    "alltime": False,
    "artist": "Pez",
    "country": "Australia",
    "id": "1188",
    "pollyear": 2008,
    "position": 7,
    "releaseyear": "2008",
    "track": "The Festival Song {ft. 360 & Hailey Cramer}"
    },
    {
    "alltime": False,
    "artist": "Drapht",
    "country": "Australia",
    "id": "1189",
    "pollyear": 2008,
    "position": 10,
    "releaseyear": "2008",
    "track": "Jimmy Recard"
    },
    {
    "alltime": False,
    "artist": "Ladyhawke",
    "country": "New Zealand",
    "id": "1190",
    "pollyear": 2008,
    "position": 11,
    "releaseyear": "2008",
    "track": "My Delirium"
    },
    {
    "alltime": False,
    "artist": "Pnau",
    "country": "Australia",
    "id": "1191",
    "pollyear": 2008,
    "position": 12,
    "releaseyear": "2008",
    "track": "Embrace {ft. Ladyhawke}"
    },
    {
    "alltime": False,
    "artist": "The Herd",
    "country": "Australia",
    "id": "1192",
    "pollyear": 2008,
    "position": 13,
    "releaseyear": "2008",
    "track": "The King Is Dead"
    },
    {
    "alltime": False,
    "artist": "The Rapture",
    "country": "USA",
    "id": "1193",
    "pollyear": 2008,
    "position": 14,
    "releaseyear": "2008",
    "track": "No Sex for Ben"
    },
    {
    "alltime": False,
    "artist": "Cut Copy",
    "country": "Australia",
    "id": "1194",
    "pollyear": 2008,
    "position": 15,
    "releaseyear": "2008",
    "track": "Lights & Music"
    },
    {
    "alltime": False,
    "artist": "Dizzee Rascal",
    "country": "UK",
    "id": "1195",
    "pollyear": 2008,
    "position": 17,
    "releaseyear": "2008",
    "track": "Dance Wiv Me {ft. Calvin Harris & Chrome}"
    },
    {
    "alltime": False,
    "artist": "MGMT",
    "country": "USA",
    "id": "1196",
    "pollyear": 2008,
    "position": 18,
    "releaseyear": "2008",
    "track": "Time to Pretend"
    },
    {
    "alltime": False,
    "artist": "Flight of the Conchords",
    "country": "New Zealand",
    "id": "1197",
    "pollyear": 2008,
    "position": 19,
    "releaseyear": "2008",
    "track": "Business Time"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "1198",
    "pollyear": 2008,
    "position": 20,
    "releaseyear": "2008",
    "track": "Broken Bones"
    },
    {
    "alltime": False,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "1199",
    "pollyear": 2008,
    "position": 21,
    "releaseyear": "2008",
    "track": "Skinny Love"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "1200",
    "pollyear": 2008,
    "position": 22,
    "releaseyear": "2008",
    "track": "Silhouettic"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1201",
    "pollyear": 2008,
    "position": 23,
    "releaseyear": "2008",
    "track": "White Noise"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1202",
    "pollyear": 2008,
    "position": 24,
    "releaseyear": "2008",
    "track": "Closer"
    },
    {
    "alltime": False,
    "artist": "Kaiser Chiefs",
    "country": "UK",
    "id": "1203",
    "pollyear": 2008,
    "position": 25,
    "releaseyear": "2008",
    "track": "Never Miss a Beat"
    },
    {
    "alltime": False,
    "artist": "Ladyhawke",
    "country": "New Zealand",
    "id": "1204",
    "pollyear": 2008,
    "position": 26,
    "releaseyear": "2008",
    "track": "Paris Is Burning"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1205",
    "pollyear": 2008,
    "position": 27,
    "releaseyear": "2008",
    "track": "The Lighthouse Song"
    },
    {
    "alltime": False,
    "artist": "Architecture in Helsinki",
    "country": "Australia",
    "id": "1206",
    "pollyear": 2008,
    "position": 28,
    "releaseyear": "2008",
    "track": "That Beep"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1207",
    "pollyear": 2008,
    "position": 29,
    "releaseyear": "2008",
    "track": "Make You Happy"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "1208",
    "pollyear": 2008,
    "position": 30,
    "releaseyear": "2008",
    "track": "Oxford Comma"
    },
    {
    "alltime": False,
    "artist": "Cog",
    "country": "Australia",
    "id": "1209",
    "pollyear": 2008,
    "position": 31,
    "releaseyear": "2008",
    "track": "Bird of Feather"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "1210",
    "pollyear": 2008,
    "position": 32,
    "releaseyear": "2008",
    "track": "A-Punk"
    },
    {
    "alltime": False,
    "artist": "The Kooks",
    "country": "UK",
    "id": "1211",
    "pollyear": 2008,
    "position": 33,
    "releaseyear": "2008",
    "track": "Always Where I Need to Be"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1212",
    "pollyear": 2008,
    "position": 34,
    "releaseyear": "2008",
    "track": "Burn Bridges"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "1213",
    "pollyear": 2008,
    "position": 35,
    "releaseyear": "2008",
    "track": "Dig, Lazarus, Dig!!!"
    },
    {
    "alltime": False,
    "artist": "Death Cab For Cutie",
    "country": "USA",
    "id": "1214",
    "pollyear": 2008,
    "position": 36,
    "releaseyear": "2008",
    "track": "I Will Possess Your Heart"
    },
    {
    "alltime": False,
    "artist": "Cold War Kids",
    "country": "USA",
    "id": "1215",
    "pollyear": 2008,
    "position": 38,
    "releaseyear": "2008",
    "track": "Something Is Not Right With Me"
    },
    {
    "alltime": False,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "1216",
    "pollyear": 2008,
    "position": 40,
    "releaseyear": "2008",
    "track": "Eye of the Storm"
    },
    {
    "alltime": False,
    "artist": "Soko",
    "country": "France",
    "id": "1217",
    "pollyear": 2008,
    "position": 41,
    "releaseyear": "2008",
    "track": "I Will Never Love You More"
    },
    {
    "alltime": False,
    "artist": "Emiliana Torrini",
    "country": "Iceland",
    "id": "1218",
    "pollyear": 2008,
    "position": 42,
    "releaseyear": "2008",
    "track": "Jungle Drum"
    },
    {
    "alltime": False,
    "artist": "Laura Marling",
    "country": "UK",
    "id": "1219",
    "pollyear": 2008,
    "position": 43,
    "releaseyear": "2008",
    "track": "Ghosts"
    },
    {
    "alltime": False,
    "artist": "Art vs Science",
    "country": "Australia",
    "id": "1220",
    "pollyear": 2008,
    "position": 44,
    "releaseyear": "2008",
    "track": "Flippers"
    },
    {
    "alltime": False,
    "artist": "Muscles",
    "country": "Australia",
    "id": "1221",
    "pollyear": 2008,
    "position": 45,
    "releaseyear": "2008",
    "track": "Ice Cream {Triple J live acoustic version}"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "1222",
    "pollyear": 2008,
    "position": 46,
    "releaseyear": "2008",
    "track": "The Fear"
    },
    {
    "alltime": False,
    "artist": "Little Red",
    "country": "Australia",
    "id": "1223",
    "pollyear": 2008,
    "position": 47,
    "releaseyear": "2008",
    "track": "Coca Cola"
    },
    {
    "alltime": False,
    "artist": "Something With Numbers",
    "country": "Australia",
    "id": "1224",
    "pollyear": 2008,
    "position": 48,
    "releaseyear": "2008",
    "track": "Stay With Me Bright Eyes"
    },
    {
    "alltime": False,
    "artist": "Mystery Jets",
    "country": "UK",
    "id": "1225",
    "pollyear": 2008,
    "position": 49,
    "releaseyear": "2008",
    "track": "Young Love"
    },
    {
    "alltime": False,
    "artist": "Ash Grunwald",
    "country": "Australia",
    "id": "1226",
    "pollyear": 2008,
    "position": 50,
    "releaseyear": "2008",
    "track": "Breakout"
    },
    {
    "alltime": False,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "1227",
    "pollyear": 2008,
    "position": 51,
    "releaseyear": "2008",
    "track": "Wild Eyed Boy"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "1228",
    "pollyear": 2008,
    "position": 52,
    "releaseyear": "2008",
    "track": "Human"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "1229",
    "pollyear": 2008,
    "position": 53,
    "releaseyear": "2008",
    "track": "Window and the Watcher"
    },
    {
    "alltime": False,
    "artist": "Pnau",
    "country": "Australia",
    "id": "1230",
    "pollyear": 2008,
    "position": 54,
    "releaseyear": "2008",
    "track": "Baby"
    },
    {
    "alltime": False,
    "artist": "Ween",
    "country": "USA",
    "id": "1231",
    "pollyear": 2008,
    "position": 55,
    "releaseyear": "2008",
    "track": "Your Party"
    },
    {
    "alltime": False,
    "artist": "The Presets",
    "country": "Australia",
    "id": "1232",
    "pollyear": 2008,
    "position": 56,
    "releaseyear": "2008",
    "track": "Yippiyo-Ay"
    },
    {
    "alltime": False,
    "artist": "Santogold",
    "country": "USA",
    "id": "1233",
    "pollyear": 2008,
    "position": 57,
    "releaseyear": "2008",
    "track": "L.E.S. Artistes"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "1234",
    "pollyear": 2008,
    "position": 58,
    "releaseyear": "2008",
    "track": "Cape Cod Kwassa Kwassa"
    },
    {
    "alltime": False,
    "artist": "The Getaway Plan",
    "country": "Australia",
    "id": "1235",
    "pollyear": 2008,
    "position": 59,
    "releaseyear": "2008",
    "track": "Where the City Meets the Sea"
    },
    {
    "alltime": False,
    "artist": "Flight of the Conchords",
    "country": "New Zealand",
    "id": "1236",
    "pollyear": 2008,
    "position": 60,
    "releaseyear": "2008",
    "track": "Most Beautiful Girl in the Room"
    },
    {
    "alltime": False,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "1237",
    "pollyear": 2008,
    "position": 61,
    "releaseyear": "2008",
    "track": "The Sea is Rising"
    },
    {
    "alltime": False,
    "artist": "Faker",
    "country": "Australia",
    "id": "1238",
    "pollyear": 2008,
    "position": 62,
    "releaseyear": "2008",
    "track": "Sleepwalking"
    },
    {
    "alltime": False,
    "artist": "The Herd",
    "country": "Australia",
    "id": "1239",
    "pollyear": 2008,
    "position": 63,
    "releaseyear": "2008",
    "track": "2020"
    },
    {
    "alltime": False,
    "artist": "Does It Offend You, Yeah?",
    "country": "UK",
    "id": "1240",
    "pollyear": 2008,
    "position": 64,
    "releaseyear": "2008",
    "track": "Dawn of the Dead"
    },
    {
    "alltime": False,
    "artist": "Fleet Foxes",
    "country": "USA",
    "id": "1241",
    "pollyear": 2008,
    "position": 65,
    "releaseyear": "2008",
    "track": "White Winter Hymnal"
    },
    {
    "alltime": False,
    "artist": "Children Collide",
    "country": "Australia",
    "id": "1242",
    "pollyear": 2008,
    "position": 66,
    "releaseyear": "2008",
    "track": "Farewell Rocketship"
    },
    {
    "alltime": False,
    "artist": "Flight of the Conchords",
    "country": "New Zealand",
    "id": "1243",
    "pollyear": 2008,
    "position": 67,
    "releaseyear": "2008",
    "track": "Hiphopopotamus vs. Rhymenoceros"
    },
    {
    "alltime": False,
    "artist": "Empire of the Sun",
    "country": "Australia",
    "id": "1244",
    "pollyear": 2008,
    "position": 68,
    "releaseyear": "2008",
    "track": "We Are the People"
    },
    {
    "alltime": False,
    "artist": "Hot Chip",
    "country": "UK",
    "id": "1245",
    "pollyear": 2008,
    "position": 69,
    "releaseyear": "2008",
    "track": "Ready for the Floor"
    },
    {
    "alltime": False,
    "artist": "Kings of Leon",
    "country": "USA",
    "id": "1246",
    "pollyear": 2008,
    "position": 70,
    "releaseyear": "2008",
    "track": "Crawl"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "1247",
    "pollyear": 2008,
    "position": 73,
    "releaseyear": "2008",
    "track": "Spaceman"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "1248",
    "pollyear": 2008,
    "position": 75,
    "releaseyear": "2008",
    "track": "Half Full Glass of Wine"
    },
    {
    "alltime": False,
    "artist": "Yves Klein Blue",
    "country": "Australia",
    "id": "1249",
    "pollyear": 2008,
    "position": 76,
    "releaseyear": "2008",
    "track": "Polka"
    },
    {
    "alltime": False,
    "artist": "Drapht",
    "country": "Australia",
    "id": "1250",
    "pollyear": 2008,
    "position": 77,
    "releaseyear": "2008",
    "track": "Falling"
    },
    {
    "alltime": False,
    "artist": "The Ting Tings",
    "country": "UK",
    "id": "1251",
    "pollyear": 2008,
    "position": 78,
    "releaseyear": "2008",
    "track": "Shut Up and Let Me Go"
    },
    {
    "alltime": False,
    "artist": "Sparkadia",
    "country": "Australia",
    "id": "1252",
    "pollyear": 2008,
    "position": 79,
    "releaseyear": "2008",
    "track": "Jealousy"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1253",
    "pollyear": 2008,
    "position": 80,
    "releaseyear": "2008",
    "track": "Aw Yeah"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "1254",
    "pollyear": 2008,
    "position": 81,
    "releaseyear": "2008",
    "track": "Pork and Beans"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "1255",
    "pollyear": 2008,
    "position": 82,
    "releaseyear": "2008",
    "track": "Ulysses"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1256",
    "pollyear": 2008,
    "position": 83,
    "releaseyear": "2008",
    "track": "Carve Your Name"
    },
    {
    "alltime": False,
    "artist": "Rise Against",
    "country": "USA",
    "id": "1257",
    "pollyear": 2008,
    "position": 84,
    "releaseyear": "2008",
    "track": "Re-Education (Through Labor)"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "1258",
    "pollyear": 2008,
    "position": 85,
    "releaseyear": "2008",
    "track": "1981"
    },
    {
    "alltime": False,
    "artist": "Muph & Plutonic",
    "country": "Australia",
    "id": "1259",
    "pollyear": 2008,
    "position": 86,
    "releaseyear": "2008",
    "track": "Beautiful Ugly"
    },
    {
    "alltime": False,
    "artist": "Jack White and Alicia Keys",
    "country": "USA",
    "id": "1260",
    "pollyear": 2008,
    "position": 87,
    "releaseyear": "2008",
    "track": "Another Way to Die"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "1261",
    "pollyear": 2008,
    "position": 88,
    "releaseyear": "2008",
    "track": "The Day That Never Comes"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "1262",
    "pollyear": 2008,
    "position": 89,
    "releaseyear": "2008",
    "track": "Love Lockdown"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "1263",
    "pollyear": 2008,
    "position": 90,
    "releaseyear": "2008",
    "track": "Fuck You"
    },
    {
    "alltime": False,
    "artist": "Lisa Mitchell",
    "country": "Australia",
    "id": "1264",
    "pollyear": 2008,
    "position": 91,
    "releaseyear": "2008",
    "track": "Neopolitan Dreams"
    },
    {
    "alltime": False,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "1265",
    "pollyear": 2008,
    "position": 92,
    "releaseyear": "2008",
    "track": "Propane Nightmares"
    },
    {
    "alltime": False,
    "artist": "Sigur Ros",
    "country": "Iceland",
    "id": "1266",
    "pollyear": 2008,
    "position": 93,
    "releaseyear": "2008",
    "track": "Gobbledigook"
    },
    {
    "alltime": False,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "1267",
    "pollyear": 2008,
    "position": 94,
    "releaseyear": "2008",
    "track": "Woodstock 2008"
    },
    {
    "alltime": False,
    "artist": "Wiley",
    "country": "UK",
    "id": "1268",
    "pollyear": 2008,
    "position": 95,
    "releaseyear": "2008",
    "track": "Wearing My Rolex"
    },
    {
    "alltime": False,
    "artist": "Dizzee Rascal",
    "country": "UK",
    "id": "1269",
    "pollyear": 2008,
    "position": 96,
    "releaseyear": "2008",
    "track": "Flex {Dave Spoon Reflex}"
    },
    {
    "alltime": False,
    "artist": "Cog",
    "country": "Australia",
    "id": "1270",
    "pollyear": 2008,
    "position": 97,
    "releaseyear": "2008",
    "track": "Are You Interested?"
    },
    {
    "alltime": False,
    "artist": "Lyrics Born",
    "country": "USA",
    "id": "1271",
    "pollyear": 2008,
    "position": 98,
    "releaseyear": "2008",
    "track": "I Like It, I Love It"
    },
    {
    "alltime": False,
    "artist": "Augie March",
    "country": "Australia",
    "id": "1272",
    "pollyear": 2006,
    "position": 1,
    "releaseyear": "2006",
    "track": "One Crowded Hour"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1273",
    "pollyear": 2006,
    "position": 2,
    "releaseyear": "2006",
    "track": "Black Fingernails, Red Wine"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1274",
    "pollyear": 2006,
    "position": 3,
    "releaseyear": "2006",
    "track": "The Hard Road"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "1275",
    "pollyear": 2006,
    "position": 4,
    "releaseyear": "2006",
    "track": "When You Were Young"
    },
    {
    "alltime": False,
    "artist": "Gnarls Barkley",
    "country": "USA",
    "id": "1276",
    "pollyear": 2006,
    "position": 6,
    "releaseyear": "2006",
    "track": "Crazy"
    },
    {
    "alltime": False,
    "artist": "Snow Patrol",
    "country": "UK",
    "id": "1277",
    "pollyear": 2006,
    "position": 7,
    "releaseyear": "2006",
    "track": "Chasing Cars"
    },
    {
    "alltime": False,
    "artist": "Gotye",
    "country": "Australia",
    "id": "1278",
    "pollyear": 2006,
    "position": 8,
    "releaseyear": "2006",
    "track": "Hearts a Mess"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1279",
    "pollyear": 2006,
    "position": 9,
    "releaseyear": "2006",
    "track": "Starlight"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1280",
    "pollyear": 2006,
    "position": 10,
    "releaseyear": "2006",
    "track": "19-20-20"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "1281",
    "pollyear": 2006,
    "position": 11,
    "releaseyear": "2006",
    "track": "Come On, Come On"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "1282",
    "pollyear": 2006,
    "position": 12,
    "releaseyear": "2006",
    "track": "Funky Tonight"
    },
    {
    "alltime": False,
    "artist": "My Chemical Romance",
    "country": "USA",
    "id": "1283",
    "pollyear": 2006,
    "position": 13,
    "releaseyear": "2006",
    "track": "Welcome to the Black Parade"
    },
    {
    "alltime": False,
    "artist": "OK Go",
    "country": "USA",
    "id": "1284",
    "pollyear": 2006,
    "position": 14,
    "releaseyear": "2006",
    "track": "Here It Goes Again"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "1285",
    "pollyear": 2006,
    "position": 15,
    "releaseyear": "2006",
    "track": "Smile"
    },
    {
    "alltime": False,
    "artist": "Peter Bjorn and John",
    "country": "Sweden",
    "id": "1286",
    "pollyear": 2006,
    "position": 16,
    "releaseyear": "2006",
    "track": "Young Folks"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1287",
    "pollyear": 2006,
    "position": 17,
    "releaseyear": "2006",
    "track": "Science is Golden"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1288",
    "pollyear": 2006,
    "position": 18,
    "releaseyear": "2006",
    "track": "Supermassive Black Hole"
    },
    {
    "alltime": False,
    "artist": "Lupe Fiasco",
    "country": "USA",
    "id": "1289",
    "pollyear": 2006,
    "position": 19,
    "releaseyear": "2006",
    "track": "Kick, Push"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "1290",
    "pollyear": 2006,
    "position": 20,
    "releaseyear": "2006",
    "track": "Fidelity"
    },
    {
    "alltime": False,
    "artist": "Youth Group",
    "country": "Australia",
    "id": "1291",
    "pollyear": 2006,
    "position": 21,
    "releaseyear": "2006",
    "track": "Forever Young"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "1292",
    "pollyear": 2006,
    "position": 22,
    "releaseyear": "2006",
    "track": "Vicarious"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1293",
    "pollyear": 2006,
    "position": 23,
    "releaseyear": "2006",
    "track": "Clown Prince"
    },
    {
    "alltime": False,
    "artist": "Yeah Yeah Yeahs",
    "country": "USA",
    "id": "1294",
    "pollyear": 2006,
    "position": 24,
    "releaseyear": "2006",
    "track": "Gold Lion"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1295",
    "pollyear": 2006,
    "position": 25,
    "releaseyear": "2006",
    "track": "Meds"
    },
    {
    "alltime": False,
    "artist": "Camille",
    "country": "France",
    "id": "1296",
    "pollyear": 2006,
    "position": 26,
    "releaseyear": "2006",
    "track": "Ta Douleur"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1297",
    "pollyear": 2006,
    "position": 27,
    "releaseyear": "2006",
    "track": "You Only Live Once"
    },
    {
    "alltime": False,
    "artist": "The Saboteurs",
    "country": "USA",
    "id": "1298",
    "pollyear": 2006,
    "position": 28,
    "releaseyear": "2006",
    "track": "Steady, As She Goes"
    },
    {
    "alltime": False,
    "artist": "Tool",
    "country": "USA",
    "id": "1299",
    "pollyear": 2006,
    "position": 29,
    "releaseyear": "2006",
    "track": "The Pot"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "1300",
    "pollyear": 2006,
    "position": 30,
    "releaseyear": "2006",
    "track": "When the Sun Goes Down"
    },
    {
    "alltime": False,
    "artist": "The Killers",
    "country": "USA",
    "id": "1301",
    "pollyear": 2006,
    "position": 31,
    "releaseyear": "2006",
    "track": "Bones"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "1302",
    "pollyear": 2006,
    "position": 32,
    "releaseyear": "2006",
    "track": "Gone"
    },
    {
    "alltime": False,
    "artist": "The Cops",
    "country": "Australia",
    "id": "1303",
    "pollyear": 2006,
    "position": 33,
    "releaseyear": "2006",
    "track": "Call Me Anytime"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1304",
    "pollyear": 2006,
    "position": 34,
    "releaseyear": "2006",
    "track": "Dani California"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "1305",
    "pollyear": 2006,
    "position": 35,
    "releaseyear": "2006",
    "track": "LDN"
    },
    {
    "alltime": False,
    "artist": "Bob Evans",
    "country": "Australia",
    "id": "1306",
    "pollyear": 2006,
    "position": 36,
    "releaseyear": "2006",
    "track": "Nowhere Without You"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1307",
    "pollyear": 2006,
    "position": 38,
    "releaseyear": "2006",
    "track": "Memories and Dust"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "1308",
    "pollyear": 2006,
    "position": 39,
    "releaseyear": "2006",
    "track": "A Slow Descent"
    },
    {
    "alltime": False,
    "artist": "Basement Jaxx",
    "country": "UK",
    "id": "1309",
    "pollyear": 2006,
    "position": 40,
    "releaseyear": "2006",
    "track": "Take Me Back to Your House"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1310",
    "pollyear": 2006,
    "position": 41,
    "releaseyear": "2006",
    "track": "What a Great Night"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1311",
    "pollyear": 2006,
    "position": 42,
    "releaseyear": "2006",
    "track": "Inside Outside"
    },
    {
    "alltime": False,
    "artist": "Angus and Julia Stone",
    "country": "Australia",
    "id": "1312",
    "pollyear": 2006,
    "position": 43,
    "releaseyear": "2006",
    "track": "Paper Aeroplane"
    },
    {
    "alltime": False,
    "artist": "Lady Sovereign",
    "country": "UK",
    "id": "1313",
    "pollyear": 2006,
    "position": 44,
    "releaseyear": "2006",
    "track": "Love Me or Hate Me"
    },
    {
    "alltime": False,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "1314",
    "pollyear": 2006,
    "position": 45,
    "releaseyear": "2006",
    "track": "Roquefort {ft. The Cat Empire}"
    },
    {
    "alltime": False,
    "artist": "AFI",
    "country": "USA",
    "id": "1315",
    "pollyear": 2006,
    "position": 46,
    "releaseyear": "2006",
    "track": "Miss Murder"
    },
    {
    "alltime": False,
    "artist": "Pony Up!",
    "country": "Canada",
    "id": "1316",
    "pollyear": 2006,
    "position": 47,
    "releaseyear": "2006",
    "track": "The Truth About Cats & Dogs (Is That They Die)"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "1317",
    "pollyear": 2006,
    "position": 48,
    "releaseyear": "2006",
    "track": "On the Radio"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "1318",
    "pollyear": 2006,
    "position": 49,
    "releaseyear": "2006",
    "track": "Fake Tales of San Francisco"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1319",
    "pollyear": 2006,
    "position": 50,
    "releaseyear": "2006",
    "track": "Heart in a Cage"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "1320",
    "pollyear": 2006,
    "position": 51,
    "releaseyear": "2006",
    "track": "Cigarettes and Suitcases"
    },
    {
    "alltime": False,
    "artist": "The Herd",
    "country": "Australia",
    "id": "1321",
    "pollyear": 2006,
    "position": 52,
    "releaseyear": "2006",
    "track": "Unpredictable"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1322",
    "pollyear": 2006,
    "position": 53,
    "releaseyear": "2006",
    "track": "Wake Up"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1323",
    "pollyear": 2006,
    "position": 55,
    "releaseyear": "2006",
    "track": "Woman {MSTRKRFT Remix}"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1324",
    "pollyear": 2006,
    "position": 56,
    "releaseyear": "2006",
    "track": "Stopping All Stations"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1325",
    "pollyear": 2006,
    "position": 57,
    "releaseyear": "2006",
    "track": "Private Education"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "1326",
    "pollyear": 2006,
    "position": 58,
    "releaseyear": "2006",
    "track": "Always On This Line"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1327",
    "pollyear": 2006,
    "position": 59,
    "releaseyear": "2006",
    "track": "Song to Say Goodbye"
    },
    {
    "alltime": False,
    "artist": "Hot Chip",
    "country": "UK",
    "id": "1328",
    "pollyear": 2006,
    "position": 60,
    "releaseyear": "2006",
    "track": "Over and Over"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1329",
    "pollyear": 2006,
    "position": 61,
    "releaseyear": "2006",
    "track": "Everlong {Acoustic Live}"
    },
    {
    "alltime": False,
    "artist": "Justice Vs Simian",
    "country": "France",
    "id": "1330",
    "pollyear": 2006,
    "position": 62,
    "releaseyear": "2006",
    "track": "We Are Your Friends"
    },
    {
    "alltime": False,
    "artist": "TV on the Radio",
    "country": "USA",
    "id": "1331",
    "pollyear": 2006,
    "position": 63,
    "releaseyear": "2006",
    "track": "Wolf Like Me"
    },
    {
    "alltime": False,
    "artist": "Something With Numbers",
    "country": "Australia",
    "id": "1332",
    "pollyear": 2006,
    "position": 64,
    "releaseyear": "2006",
    "track": "Apple of the Eye (Lay Me Down)"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1333",
    "pollyear": 2006,
    "position": 65,
    "releaseyear": "2006",
    "track": "The Prayer"
    },
    {
    "alltime": False,
    "artist": "Yeah Yeah Yeahs",
    "country": "USA",
    "id": "1334",
    "pollyear": 2006,
    "position": 66,
    "releaseyear": "2006",
    "track": "Phenomena"
    },
    {
    "alltime": False,
    "artist": "AFI",
    "country": "USA",
    "id": "1335",
    "pollyear": 2006,
    "position": 67,
    "releaseyear": "2006",
    "track": "Love Like Winter"
    },
    {
    "alltime": False,
    "artist": "Darren Hanlon",
    "country": "Australia",
    "id": "1336",
    "pollyear": 2006,
    "position": 68,
    "releaseyear": "2006",
    "track": "Happiness Is A Chemical"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "1337",
    "pollyear": 2006,
    "position": 69,
    "releaseyear": "2006",
    "track": "Nausea"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "1338",
    "pollyear": 2006,
    "position": 70,
    "releaseyear": "2006",
    "track": "Such Great Heights"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "1339",
    "pollyear": 2006,
    "position": 71,
    "releaseyear": "2006",
    "track": "Lies Are Much More Fun"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "1340",
    "pollyear": 2006,
    "position": 72,
    "releaseyear": "2006",
    "track": "Put Your Money Where Your Mouth Is"
    },
    {
    "alltime": False,
    "artist": "Matisyahu",
    "country": "USA",
    "id": "1341",
    "pollyear": 2006,
    "position": 73,
    "releaseyear": "2006",
    "track": "King Without a Crown"
    },
    {
    "alltime": False,
    "artist": "Snow Patrol",
    "country": "UK",
    "id": "1342",
    "pollyear": 2006,
    "position": 74,
    "releaseyear": "2006",
    "track": "Hands Open"
    },
    {
    "alltime": False,
    "artist": "Ben Kweller",
    "country": "USA",
    "id": "1343",
    "pollyear": 2006,
    "position": 75,
    "releaseyear": "2006",
    "track": "Sundress"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "1344",
    "pollyear": 2006,
    "position": 76,
    "releaseyear": "2006",
    "track": "Rip It Up"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1345",
    "pollyear": 2006,
    "position": 77,
    "releaseyear": "2006",
    "track": "Recapturing The Vibe"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1346",
    "pollyear": 2006,
    "position": 78,
    "releaseyear": "2006",
    "track": "Infra-red"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "1347",
    "pollyear": 2006,
    "position": 79,
    "releaseyear": "2006",
    "track": "Explain"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1348",
    "pollyear": 2006,
    "position": 80,
    "releaseyear": "2006",
    "track": "Love Train"
    },
    {
    "alltime": False,
    "artist": "Gnarls Barkley",
    "country": "USA",
    "id": "1349",
    "pollyear": 2006,
    "position": 81,
    "releaseyear": "2006",
    "track": "Gone Daddy Gone"
    },
    {
    "alltime": False,
    "artist": "Freestylers/Pendulum",
    "country": "Australia",
    "id": "1350",
    "pollyear": 2006,
    "position": 82,
    "releaseyear": "2006",
    "track": "Painkiller"
    },
    {
    "alltime": False,
    "artist": "Butterfingers",
    "country": "Australia",
    "id": "1351",
    "pollyear": 2006,
    "position": 83,
    "releaseyear": "2006",
    "track": "Get Up Outta The Dirt"
    },
    {
    "alltime": False,
    "artist": "Thom Yorke",
    "country": "UK",
    "id": "1352",
    "pollyear": 2006,
    "position": 84,
    "releaseyear": "2006",
    "track": "Black Swan"
    },
    {
    "alltime": False,
    "artist": "Infadels",
    "country": "UK",
    "id": "1353",
    "pollyear": 2006,
    "position": 85,
    "releaseyear": "2006",
    "track": "Love Like Semtex"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "1354",
    "pollyear": 2006,
    "position": 86,
    "releaseyear": "2006",
    "track": "Touch the Sky {ft. Lupe Fiasco}"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "1355",
    "pollyear": 2006,
    "position": 87,
    "releaseyear": "2006",
    "track": "Better Way"
    },
    {
    "alltime": False,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "1356",
    "pollyear": 2006,
    "position": 88,
    "releaseyear": "2006",
    "track": "Tarantula"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "1357",
    "pollyear": 2006,
    "position": 89,
    "releaseyear": "2006",
    "track": "Mardy Bum"
    },
    {
    "alltime": False,
    "artist": "Jurassic 5",
    "country": "USA",
    "id": "1358",
    "pollyear": 2006,
    "position": 90,
    "releaseyear": "2006",
    "track": "Work It Out {ft. Dave Matthews Band}"
    },
    {
    "alltime": False,
    "artist": "Panic! at the Disco",
    "country": "USA",
    "id": "1359",
    "pollyear": 2006,
    "position": 91,
    "releaseyear": "2006",
    "track": "The Only Difference Between Martyrdom and Suicide Is Press Coverage"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "1360",
    "pollyear": 2006,
    "position": 92,
    "releaseyear": "2006",
    "track": "Alfie"
    },
    {
    "alltime": False,
    "artist": "Gotye",
    "country": "Australia",
    "id": "1361",
    "pollyear": 2006,
    "position": 94,
    "releaseyear": "2006",
    "track": "Learnalilgivinanlovin"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1362",
    "pollyear": 2006,
    "position": 95,
    "releaseyear": "2006",
    "track": "New York"
    },
    {
    "alltime": False,
    "artist": "Red Riders",
    "country": "Australia",
    "id": "1363",
    "pollyear": 2006,
    "position": 96,
    "releaseyear": "2006",
    "track": "Slide In Next To Me"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "1364",
    "pollyear": 2006,
    "position": 97,
    "releaseyear": "2006",
    "track": "World Wide Suicide"
    },
    {
    "alltime": False,
    "artist": "The Gossip",
    "country": "USA",
    "id": "1365",
    "pollyear": 2006,
    "position": 98,
    "releaseyear": "2006",
    "track": "Standing In The Way Of Control"
    },
    {
    "alltime": False,
    "artist": "Audioslave",
    "country": "USA",
    "id": "1366",
    "pollyear": 2006,
    "position": 99,
    "releaseyear": "2006",
    "track": "Original Fire"
    },
    {
    "alltime": False,
    "artist": "Blue King Brown",
    "country": "Australia",
    "id": "1367",
    "pollyear": 2006,
    "position": 100,
    "releaseyear": "2006",
    "track": "Come And Check Your Head"
    },
    {
    "alltime": False,
    "artist": "Oasis",
    "country": "UK",
    "id": "1368",
    "pollyear": 1995,
    "position": 1,
    "releaseyear": "1995",
    "track": "Wonderwall"
    },
    {
    "alltime": False,
    "artist": "Smashing Pumpkins",
    "country": "USA",
    "id": "1369",
    "pollyear": 1995,
    "position": 2,
    "releaseyear": "1995",
    "track": "Bullet with Butterfly Wings"
    },
    {
    "alltime": False,
    "artist": "Presidents of the U.S.A.",
    "country": "USA",
    "id": "1370",
    "pollyear": 1995,
    "position": 4,
    "releaseyear": "1995",
    "track": "Kitty"
    },
    {
    "alltime": False,
    "artist": "Everclear",
    "country": "USA",
    "id": "1371",
    "pollyear": 1995,
    "position": 6,
    "releaseyear": "1995",
    "track": "Heroin Girl"
    },
    {
    "alltime": False,
    "artist": "Custard",
    "country": "Australia",
    "id": "1372",
    "pollyear": 1995,
    "position": 7,
    "releaseyear": "1995",
    "track": "Apartment"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds and Kylie Minogue",
    "country": "Australia",
    "id": "1373",
    "pollyear": 1995,
    "position": 8,
    "releaseyear": "1995",
    "track": "Where the Wild Roses Grow"
    },
    {
    "alltime": False,
    "artist": "TISM",
    "country": "Australia",
    "id": "1374",
    "pollyear": 1995,
    "position": 10,
    "releaseyear": "1995",
    "track": "Greg! The Stop Sign!!"
    },
    {
    "alltime": False,
    "artist": "Presidents of the U.S.A.",
    "country": "USA",
    "id": "1375",
    "pollyear": 1995,
    "position": 11,
    "releaseyear": "1995",
    "track": "Lump"
    },
    {
    "alltime": False,
    "artist": "Mindless Drug Hoover",
    "country": "UK",
    "id": "1376",
    "pollyear": 1995,
    "position": 12,
    "releaseyear": "1995",
    "track": "The Reefer Song"
    },
    {
    "alltime": False,
    "artist": "Oasis",
    "country": "UK",
    "id": "1377",
    "pollyear": 1995,
    "position": 13,
    "releaseyear": "1995",
    "track": "Morning Glory"
    },
    {
    "alltime": False,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "1378",
    "pollyear": 1995,
    "position": 14,
    "releaseyear": "1995",
    "track": "Last Goodbye"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "UK",
    "id": "1379",
    "pollyear": 1995,
    "position": 15,
    "releaseyear": "1995",
    "track": "Vow"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "1380",
    "pollyear": 1995,
    "position": 17,
    "releaseyear": "1995",
    "track": "Blubber Boy"
    },
    {
    "alltime": False,
    "artist": "Jill Sobule",
    "country": "USA",
    "id": "1381",
    "pollyear": 1995,
    "position": 18,
    "releaseyear": "1995",
    "track": "I Kissed a Girl"
    },
    {
    "alltime": False,
    "artist": "Tripping Daisy",
    "country": "USA",
    "id": "1382",
    "pollyear": 1995,
    "position": 19,
    "releaseyear": "1995",
    "track": "I Got a Girl"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1383",
    "pollyear": 1995,
    "position": 20,
    "releaseyear": "1995",
    "track": "My Friends"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "UK",
    "id": "1384",
    "pollyear": 1995,
    "position": 21,
    "releaseyear": "1995",
    "track": "Queer"
    },
    {
    "alltime": False,
    "artist": "Live",
    "country": "USA",
    "id": "1385",
    "pollyear": 1995,
    "position": 22,
    "releaseyear": "1995",
    "track": "Lightning Crashes"
    },
    {
    "alltime": False,
    "artist": "Passengers",
    "country": "Ireland",
    "id": "1386",
    "pollyear": 1995,
    "position": 23,
    "releaseyear": "1995",
    "track": "Miss Sarajevo"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "1387",
    "pollyear": 1995,
    "position": 24,
    "releaseyear": "1995",
    "track": "Purple Sneakers"
    },
    {
    "alltime": False,
    "artist": "Insurge",
    "country": "Australia",
    "id": "1388",
    "pollyear": 1995,
    "position": 25,
    "releaseyear": "1995",
    "track": "Political Prisoners"
    },
    {
    "alltime": False,
    "artist": "Neil Young",
    "country": "Canada",
    "id": "1389",
    "pollyear": 1995,
    "position": 26,
    "releaseyear": "1995",
    "track": "Downtown"
    },
    {
    "alltime": False,
    "artist": "Ammonia",
    "country": "Australia",
    "id": "1390",
    "pollyear": 1995,
    "position": 27,
    "releaseyear": "1995",
    "track": "Drugs"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1391",
    "pollyear": 1995,
    "position": 28,
    "releaseyear": "1995",
    "track": "Aeroplane"
    },
    {
    "alltime": False,
    "artist": "Faith No More",
    "country": "USA",
    "id": "1392",
    "pollyear": 1995,
    "position": 29,
    "releaseyear": "1995",
    "track": "Evidence"
    },
    {
    "alltime": False,
    "artist": "Natalie Merchant",
    "country": "USA",
    "id": "1393",
    "pollyear": 1995,
    "position": 30,
    "releaseyear": "1995",
    "track": "Carnival"
    },
    {
    "alltime": False,
    "artist": "Rancid",
    "country": "USA",
    "id": "1394",
    "pollyear": 1995,
    "position": 31,
    "releaseyear": "1995",
    "track": "Time Bomb"
    },
    {
    "alltime": False,
    "artist": "Swoop",
    "country": "Australia",
    "id": "1395",
    "pollyear": 1995,
    "position": 32,
    "releaseyear": "1995",
    "track": "Apple Eyes"
    },
    {
    "alltime": False,
    "artist": "Bush",
    "country": "UK",
    "id": "1396",
    "pollyear": 1995,
    "position": 33,
    "releaseyear": "1995",
    "track": "Everything Zen"
    },
    {
    "alltime": False,
    "artist": "Live",
    "country": "USA",
    "id": "1397",
    "pollyear": 1995,
    "position": 34,
    "releaseyear": "1995",
    "track": "I Alone"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "1398",
    "pollyear": 1995,
    "position": 35,
    "releaseyear": "1995",
    "track": "I Got Id"
    },
    {
    "alltime": False,
    "artist": "Tricky",
    "country": "UK",
    "id": "1399",
    "pollyear": 1995,
    "position": 36,
    "releaseyear": "1995",
    "track": "Black Steel"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1400",
    "pollyear": 1995,
    "position": 37,
    "releaseyear": "1995",
    "track": "This Is a Call"
    },
    {
    "alltime": False,
    "artist": "Pulp",
    "country": "UK",
    "id": "1401",
    "pollyear": 1995,
    "position": 38,
    "releaseyear": "1995",
    "track": "Common People"
    },
    {
    "alltime": False,
    "artist": "Alanis Morissette",
    "country": "Canada",
    "id": "1402",
    "pollyear": 1995,
    "position": 39,
    "releaseyear": "1995",
    "track": "You Oughta Know"
    },
    {
    "alltime": False,
    "artist": "Skunk Anansie",
    "country": "UK",
    "id": "1403",
    "pollyear": 1995,
    "position": 41,
    "releaseyear": "1995",
    "track": "I Can Dream"
    },
    {
    "alltime": False,
    "artist": "Sonic Youth",
    "country": "USA",
    "id": "1404",
    "pollyear": 1995,
    "position": 42,
    "releaseyear": "1995",
    "track": "The Diamond Sea"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1405",
    "pollyear": 1995,
    "position": 43,
    "releaseyear": "1995",
    "track": "Monty"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "1406",
    "pollyear": 1995,
    "position": 44,
    "releaseyear": "1995",
    "track": "Better Man"
    },
    {
    "alltime": False,
    "artist": "Portishead",
    "country": "UK",
    "id": "1407",
    "pollyear": 1995,
    "position": 45,
    "releaseyear": "1995",
    "track": "Glory Box"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1408",
    "pollyear": 1995,
    "position": 46,
    "releaseyear": "1995",
    "track": "Geek Stink Breath"
    },
    {
    "alltime": False,
    "artist": "Christine Anu",
    "country": "Australia",
    "id": "1409",
    "pollyear": 1995,
    "position": 47,
    "releaseyear": "1995",
    "track": "My Island Home"
    },
    {
    "alltime": False,
    "artist": "Technohead",
    "country": "UK",
    "id": "1410",
    "pollyear": 1995,
    "position": 48,
    "releaseyear": "1995",
    "track": "I Wanna be a Hippy"
    },
    {
    "alltime": False,
    "artist": "White Zombie",
    "country": "USA",
    "id": "1411",
    "pollyear": 1995,
    "position": 49,
    "releaseyear": "1995",
    "track": "More Human than Human"
    },
    {
    "alltime": False,
    "artist": "Buffalo Tom",
    "country": "USA",
    "id": "1412",
    "pollyear": 1995,
    "position": 50,
    "releaseyear": "1995",
    "track": "Summer"
    },
    {
    "alltime": False,
    "artist": "Def FX",
    "country": "Australia",
    "id": "1413",
    "pollyear": 1995,
    "position": 51,
    "releaseyear": "1995",
    "track": "Psychoactive Summer"
    },
    {
    "alltime": False,
    "artist": "The Murmurs",
    "country": "USA",
    "id": "1414",
    "pollyear": 1995,
    "position": 52,
    "releaseyear": "1995",
    "track": "You Suck"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "1415",
    "pollyear": 1995,
    "position": 53,
    "releaseyear": "1995",
    "track": "Country House"
    },
    {
    "alltime": False,
    "artist": "The Vaughans",
    "country": "Australia",
    "id": "1416",
    "pollyear": 1995,
    "position": 54,
    "releaseyear": "1995",
    "track": "Who Farted?"
    },
    {
    "alltime": False,
    "artist": "Skunkhour",
    "country": "Australia",
    "id": "1417",
    "pollyear": 1995,
    "position": 55,
    "releaseyear": "1995",
    "track": "Up to Our Necks In It"
    },
    {
    "alltime": False,
    "artist": "Phunk Junkeez",
    "country": "USA",
    "id": "1418",
    "pollyear": 1995,
    "position": 56,
    "releaseyear": "1995",
    "track": "Chuck"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "1419",
    "pollyear": 1995,
    "position": 57,
    "releaseyear": "1995",
    "track": "Hold Me, Thrill Me, Kiss Me, Kill Me"
    },
    {
    "alltime": False,
    "artist": "Pollyanna",
    "country": "Australia",
    "id": "1420",
    "pollyear": 1995,
    "position": 58,
    "releaseyear": "1995",
    "track": "Lemonsuck"
    },
    {
    "alltime": False,
    "artist": "Jill Sobule",
    "country": "USA",
    "id": "1421",
    "pollyear": 1995,
    "position": 59,
    "releaseyear": "1995",
    "track": "Supermodel"
    },
    {
    "alltime": False,
    "artist": "Screaming Jets",
    "country": "Australia",
    "id": "1422",
    "pollyear": 1995,
    "position": 61,
    "releaseyear": "1995",
    "track": "Sad Song"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "1423",
    "pollyear": 1995,
    "position": 63,
    "releaseyear": "1995",
    "track": "Smash It Up"
    },
    {
    "alltime": False,
    "artist": "Shaggy",
    "country": "Jamaica",
    "id": "1424",
    "pollyear": 1995,
    "position": 65,
    "releaseyear": "1995",
    "track": "Boombastic"
    },
    {
    "alltime": False,
    "artist": "The Tea Party",
    "country": "Canada",
    "id": "1425",
    "pollyear": 1995,
    "position": 66,
    "releaseyear": "1995",
    "track": "Fire in the Head"
    },
    {
    "alltime": False,
    "artist": "Chris Isaak",
    "country": "USA",
    "id": "1426",
    "pollyear": 1995,
    "position": 67,
    "releaseyear": "1995",
    "track": "Baby Did a Bad, Bad Thing"
    },
    {
    "alltime": False,
    "artist": "Pollyanna",
    "country": "Australia",
    "id": "1427",
    "pollyear": 1995,
    "position": 68,
    "releaseyear": "1995",
    "track": "Pale Grey Eyes"
    },
    {
    "alltime": False,
    "artist": "Live",
    "country": "USA",
    "id": "1428",
    "pollyear": 1995,
    "position": 71,
    "releaseyear": "1995",
    "track": "All Over You"
    },
    {
    "alltime": False,
    "artist": "Rail",
    "country": "Australia",
    "id": "1429",
    "pollyear": 1995,
    "position": 72,
    "releaseyear": "1995",
    "track": "Immune Deficiency"
    },
    {
    "alltime": False,
    "artist": "The Cure",
    "country": "UK",
    "id": "1430",
    "pollyear": 1995,
    "position": 73,
    "releaseyear": "1995",
    "track": "Dredd Song"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "1431",
    "pollyear": 1995,
    "position": 74,
    "releaseyear": "1995",
    "track": "Sickfest"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1432",
    "pollyear": 1995,
    "position": 75,
    "releaseyear": "1995",
    "track": "Warped"
    },
    {
    "alltime": False,
    "artist": "Bad Religion",
    "country": "USA",
    "id": "1433",
    "pollyear": 1995,
    "position": 76,
    "releaseyear": "1995",
    "track": "21st Century (Digital Boy)"
    },
    {
    "alltime": False,
    "artist": "Severed Heads",
    "country": "Australia",
    "id": "1434",
    "pollyear": 1995,
    "position": 77,
    "releaseyear": "1995",
    "track": "Heart of the Party"
    },
    {
    "alltime": False,
    "artist": "Strawpeople",
    "country": "New Zealand",
    "id": "1435",
    "pollyear": 1995,
    "position": 78,
    "releaseyear": "1995",
    "track": "Trick with a Knife"
    },
    {
    "alltime": False,
    "artist": "Supergrass",
    "country": "UK",
    "id": "1436",
    "pollyear": 1995,
    "position": 79,
    "releaseyear": "1995",
    "track": "Alright"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1437",
    "pollyear": 1995,
    "position": 80,
    "releaseyear": "1995",
    "track": "Brain Stew"
    },
    {
    "alltime": False,
    "artist": "Mr Blonde",
    "country": "Australia",
    "id": "1438",
    "pollyear": 1995,
    "position": 82,
    "releaseyear": "1995",
    "track": "Sunday"
    },
    {
    "alltime": False,
    "artist": "Bjork",
    "country": "Iceland",
    "id": "1439",
    "pollyear": 1995,
    "position": 83,
    "releaseyear": "1995",
    "track": "Army of Me"
    },
    {
    "alltime": False,
    "artist": "Alanis Morissette",
    "country": "Canada",
    "id": "1440",
    "pollyear": 1995,
    "position": 85,
    "releaseyear": "1995",
    "track": "Hand in My Pocket"
    },
    {
    "alltime": False,
    "artist": "TLC",
    "country": "USA",
    "id": "1441",
    "pollyear": 1995,
    "position": 86,
    "releaseyear": "1995",
    "track": "Waterfalls"
    },
    {
    "alltime": False,
    "artist": "Yothu Yindi",
    "country": "Australia",
    "id": "1442",
    "pollyear": 1995,
    "position": 87,
    "releaseyear": "1995",
    "track": "Jailbreak"
    },
    {
    "alltime": False,
    "artist": "Alice in Chains",
    "country": "USA",
    "id": "1443",
    "pollyear": 1995,
    "position": 88,
    "releaseyear": "1995",
    "track": "Grind"
    },
    {
    "alltime": False,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "1444",
    "pollyear": 1995,
    "position": 89,
    "releaseyear": "1995",
    "track": "Grace"
    },
    {
    "alltime": False,
    "artist": "Alanis Morissette",
    "country": "Canada",
    "id": "1445",
    "pollyear": 1995,
    "position": 90,
    "releaseyear": "1995",
    "track": "All I Really Want"
    },
    {
    "alltime": False,
    "artist": "Faith No More",
    "country": "USA",
    "id": "1446",
    "pollyear": 1995,
    "position": 91,
    "releaseyear": "1995",
    "track": "Digging the Grave"
    },
    {
    "alltime": False,
    "artist": "Matthew Sweet",
    "country": "USA",
    "id": "1447",
    "pollyear": 1995,
    "position": 92,
    "releaseyear": "1995",
    "track": "Sick of Myself"
    },
    {
    "alltime": False,
    "artist": "TISM",
    "country": "Australia",
    "id": "1448",
    "pollyear": 1995,
    "position": 93,
    "releaseyear": "1995",
    "track": "All Homeboys Are Dickheads"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "1449",
    "pollyear": 1995,
    "position": 94,
    "releaseyear": "1995",
    "track": "Jewels and Bullets"
    },
    {
    "alltime": False,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "1450",
    "pollyear": 1995,
    "position": 95,
    "releaseyear": "1995",
    "track": "Protection"
    },
    {
    "alltime": False,
    "artist": "Tumbleweed",
    "country": "Australia",
    "id": "1451",
    "pollyear": 1995,
    "position": 96,
    "releaseyear": "1995",
    "track": "Hang Around"
    },
    {
    "alltime": False,
    "artist": "Pop!",
    "country": "Australia",
    "id": "1452",
    "pollyear": 1995,
    "position": 97,
    "releaseyear": "1995",
    "track": "Tingly {ft. Angie Hart}"
    },
    {
    "alltime": False,
    "artist": "Hecate",
    "country": "Australia",
    "id": "1453",
    "pollyear": 1995,
    "position": 98,
    "releaseyear": "1995",
    "track": "By Myself"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1454",
    "pollyear": 1995,
    "position": 99,
    "releaseyear": "1995",
    "track": "When I Come Around"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1455",
    "pollyear": 2000,
    "position": 1,
    "releaseyear": "2000",
    "track": "My Happiness"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "1456",
    "pollyear": 2000,
    "position": 2,
    "releaseyear": "2000",
    "track": "Beautiful Day"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1457",
    "pollyear": 2000,
    "position": 3,
    "releaseyear": "2000",
    "track": "My Kind of Scene"
    },
    {
    "alltime": False,
    "artist": "Wheatus",
    "country": "USA",
    "id": "1458",
    "pollyear": 2000,
    "position": 4,
    "releaseyear": "2000",
    "track": "Teenage Dirtbag"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "1459",
    "pollyear": 2000,
    "position": 5,
    "releaseyear": "2000",
    "track": "Yellow"
    },
    {
    "alltime": False,
    "artist": "The Avalanches",
    "country": "Australia",
    "id": "1460",
    "pollyear": 2000,
    "position": 6,
    "releaseyear": "2000",
    "track": "Frontier Psychiatrist"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1461",
    "pollyear": 2000,
    "position": 7,
    "releaseyear": "2000",
    "track": "Californication"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1462",
    "pollyear": 2000,
    "position": 8,
    "releaseyear": "2000",
    "track": "Generator"
    },
    {
    "alltime": False,
    "artist": "Paul Kelly",
    "country": "Australia",
    "id": "1463",
    "pollyear": 2000,
    "position": 9,
    "releaseyear": "2000",
    "track": "Every Fucking City"
    },
    {
    "alltime": False,
    "artist": "Dandy Warhols",
    "country": "USA",
    "id": "1464",
    "pollyear": 2000,
    "position": 10,
    "releaseyear": "2000",
    "track": "Bohemian Like You"
    },
    {
    "alltime": False,
    "artist": "28 Days",
    "country": "Australia",
    "id": "1465",
    "pollyear": 2000,
    "position": 11,
    "releaseyear": "2000",
    "track": "Rip It Up"
    },
    {
    "alltime": False,
    "artist": "Magic Dirt",
    "country": "Australia",
    "id": "1466",
    "pollyear": 2000,
    "position": 12,
    "releaseyear": "2000",
    "track": "Dirty Jeans"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "1467",
    "pollyear": 2000,
    "position": 13,
    "releaseyear": "2000",
    "track": "Sleep Now in the Fire"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1468",
    "pollyear": 2000,
    "position": 14,
    "releaseyear": "2000",
    "track": "Minority"
    },
    {
    "alltime": False,
    "artist": "Lo-Tel",
    "country": "Australia",
    "id": "1469",
    "pollyear": 2000,
    "position": 15,
    "releaseyear": "2000",
    "track": "Teenager Of The Year"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "1470",
    "pollyear": 2000,
    "position": 16,
    "releaseyear": "2000",
    "track": "Unsent Letter"
    },
    {
    "alltime": False,
    "artist": "The Superjesus",
    "country": "Australia",
    "id": "1471",
    "pollyear": 2000,
    "position": 17,
    "releaseyear": "2000",
    "track": "Gravity"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1472",
    "pollyear": 2000,
    "position": 18,
    "releaseyear": "2000",
    "track": "Stacked Actors"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1473",
    "pollyear": 2000,
    "position": 19,
    "releaseyear": "2000",
    "track": "Pictures in the Mirror"
    },
    {
    "alltime": False,
    "artist": "Bodyjar",
    "country": "Australia",
    "id": "1474",
    "pollyear": 2000,
    "position": 20,
    "releaseyear": "2000",
    "track": "Not The Same"
    },
    {
    "alltime": False,
    "artist": "Limp Bizkit",
    "country": "USA",
    "id": "1475",
    "pollyear": 2000,
    "position": 21,
    "releaseyear": "2000",
    "track": "My Generation"
    },
    {
    "alltime": False,
    "artist": "Moby",
    "country": "USA",
    "id": "1476",
    "pollyear": 2000,
    "position": 22,
    "releaseyear": "2000",
    "track": "Porcelain"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "1477",
    "pollyear": 2000,
    "position": 23,
    "releaseyear": "2000",
    "track": "Damage"
    },
    {
    "alltime": False,
    "artist": "Bomfunk MCs",
    "country": "Finland",
    "id": "1478",
    "pollyear": 2000,
    "position": 24,
    "releaseyear": "2000",
    "track": "Freestyler"
    },
    {
    "alltime": False,
    "artist": "Shihad",
    "country": "New Zealand",
    "id": "1479",
    "pollyear": 2000,
    "position": 25,
    "releaseyear": "2000",
    "track": "Pacifier"
    },
    {
    "alltime": False,
    "artist": "Limp Bizkit",
    "country": "USA",
    "id": "1480",
    "pollyear": 2000,
    "position": 27,
    "releaseyear": "2000",
    "track": "Take a Look Around"
    },
    {
    "alltime": False,
    "artist": "George",
    "country": "Australia",
    "id": "1481",
    "pollyear": 2000,
    "position": 28,
    "releaseyear": "2000",
    "track": "Bastard Son"
    },
    {
    "alltime": False,
    "artist": "Stone Temple Pilots",
    "country": "USA",
    "id": "1482",
    "pollyear": 2000,
    "position": 29,
    "releaseyear": "2000",
    "track": "Sour Girl"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "1483",
    "pollyear": 2000,
    "position": 30,
    "releaseyear": "2000",
    "track": "Please Leave"
    },
    {
    "alltime": False,
    "artist": "Travis",
    "country": "UK",
    "id": "1484",
    "pollyear": 2000,
    "position": 31,
    "releaseyear": "2000",
    "track": "Why Does It Always Rain On Me?"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "1485",
    "pollyear": 2000,
    "position": 33,
    "releaseyear": "2000",
    "track": "Rock Show"
    },
    {
    "alltime": False,
    "artist": "A Perfect Circle",
    "country": "USA",
    "id": "1486",
    "pollyear": 2000,
    "position": 34,
    "releaseyear": "2000",
    "track": "Judith"
    },
    {
    "alltime": False,
    "artist": "Cypress Hill",
    "country": "USA",
    "id": "1487",
    "pollyear": 2000,
    "position": 36,
    "releaseyear": "2000",
    "track": "Rock Superstar"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "1488",
    "pollyear": 2000,
    "position": 37,
    "releaseyear": "2000",
    "track": "Thank You (For Loving Me at My Worst)"
    },
    {
    "alltime": False,
    "artist": "Gomez",
    "country": "UK",
    "id": "1489",
    "pollyear": 2000,
    "position": 38,
    "releaseyear": "2000",
    "track": "Machismo"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1490",
    "pollyear": 2000,
    "position": 39,
    "releaseyear": "2000",
    "track": "Taste in Men"
    },
    {
    "alltime": False,
    "artist": "Papa Roach",
    "country": "USA",
    "id": "1491",
    "pollyear": 2000,
    "position": 40,
    "releaseyear": "2000",
    "track": "Last Resort"
    },
    {
    "alltime": False,
    "artist": "Millencolin",
    "country": "Sweden",
    "id": "1492",
    "pollyear": 2000,
    "position": 41,
    "releaseyear": "2000",
    "track": "Penguins & Polarbears"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "1493",
    "pollyear": 2000,
    "position": 42,
    "releaseyear": "2000",
    "track": "Everything in Its Right Place"
    },
    {
    "alltime": False,
    "artist": "Fatboy Slim",
    "country": "UK",
    "id": "1494",
    "pollyear": 2000,
    "position": 43,
    "releaseyear": "2000",
    "track": "Sunset (Bird of Prey)"
    },
    {
    "alltime": False,
    "artist": "Moloko",
    "country": "UK",
    "id": "1495",
    "pollyear": 2000,
    "position": 45,
    "releaseyear": "2000",
    "track": "The Time Is Now"
    },
    {
    "alltime": False,
    "artist": "Filter",
    "country": "USA",
    "id": "1496",
    "pollyear": 2000,
    "position": 46,
    "releaseyear": "2000",
    "track": "Take a Picture"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1497",
    "pollyear": 2000,
    "position": 47,
    "releaseyear": "2000",
    "track": "Slave to the Wage"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "1498",
    "pollyear": 2000,
    "position": 48,
    "releaseyear": "2000",
    "track": "Crush The Losers"
    },
    {
    "alltime": False,
    "artist": "Dandy Warhols",
    "country": "USA",
    "id": "1499",
    "pollyear": 2000,
    "position": 49,
    "releaseyear": "2000",
    "track": "Get Off"
    },
    {
    "alltime": False,
    "artist": "Skulker",
    "country": "Australia",
    "id": "1500",
    "pollyear": 2000,
    "position": 50,
    "releaseyear": "2000",
    "track": "Naughty"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "1501",
    "pollyear": 2000,
    "position": 51,
    "releaseyear": "2000",
    "track": "Original Prankster"
    },
    {
    "alltime": False,
    "artist": "28 Days",
    "country": "Australia",
    "id": "1502",
    "pollyear": 2000,
    "position": 52,
    "releaseyear": "2000",
    "track": "Sucker"
    },
    {
    "alltime": False,
    "artist": "The Hippos",
    "country": "USA",
    "id": "1503",
    "pollyear": 2000,
    "position": 53,
    "releaseyear": "2000",
    "track": "Wasting My Life"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "1504",
    "pollyear": 2000,
    "position": 54,
    "releaseyear": "2000",
    "track": "Man Overboard"
    },
    {
    "alltime": False,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "1505",
    "pollyear": 2000,
    "position": 55,
    "releaseyear": "2000",
    "track": "The Great Beyond"
    },
    {
    "alltime": False,
    "artist": "Friendly",
    "country": "Australia",
    "id": "1506",
    "pollyear": 2000,
    "position": 56,
    "releaseyear": "2000",
    "track": "I Love You But"
    },
    {
    "alltime": False,
    "artist": "Groove Armada",
    "country": "UK",
    "id": "1507",
    "pollyear": 2000,
    "position": 57,
    "releaseyear": "2000",
    "track": "I See You Baby"
    },
    {
    "alltime": False,
    "artist": "The Fauves",
    "country": "Australia",
    "id": "1508",
    "pollyear": 2000,
    "position": 58,
    "releaseyear": "2000",
    "track": "Give Up Your Day Job"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "1509",
    "pollyear": 2000,
    "position": 59,
    "releaseyear": "2000",
    "track": "Beautiful Sharks"
    },
    {
    "alltime": False,
    "artist": "George",
    "country": "Australia",
    "id": "1510",
    "pollyear": 2000,
    "position": 61,
    "releaseyear": "2000",
    "track": "Spawn"
    },
    {
    "alltime": False,
    "artist": "Fiona Apple",
    "country": "USA",
    "id": "1511",
    "pollyear": 2000,
    "position": 62,
    "releaseyear": "2000",
    "track": "Fast as You Can"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "1512",
    "pollyear": 2000,
    "position": 63,
    "releaseyear": "2000",
    "track": "Shiver"
    },
    {
    "alltime": False,
    "artist": "Everlast",
    "country": "USA",
    "id": "1513",
    "pollyear": 2000,
    "position": 64,
    "releaseyear": "2000",
    "track": "Black Jesus"
    },
    {
    "alltime": False,
    "artist": "Motor Ace",
    "country": "Australia",
    "id": "1514",
    "pollyear": 2000,
    "position": 65,
    "releaseyear": "2000",
    "track": "American Shoes"
    },
    {
    "alltime": False,
    "artist": "Bodyjar",
    "country": "Australia",
    "id": "1515",
    "pollyear": 2000,
    "position": 66,
    "releaseyear": "2000",
    "track": "Fall to the Ground"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "1516",
    "pollyear": 2000,
    "position": 67,
    "releaseyear": "2000",
    "track": "Mofo On A Motor Cycle"
    },
    {
    "alltime": False,
    "artist": "OPM",
    "country": "USA",
    "id": "1517",
    "pollyear": 2000,
    "position": 68,
    "releaseyear": "2000",
    "track": "Heaven Is A Halfpipe"
    },
    {
    "alltime": False,
    "artist": "MxPx",
    "country": "USA",
    "id": "1518",
    "pollyear": 2000,
    "position": 69,
    "releaseyear": "2000",
    "track": "Responsibility"
    },
    {
    "alltime": False,
    "artist": "Killing Heidi",
    "country": "Australia",
    "id": "1519",
    "pollyear": 2000,
    "position": 70,
    "releaseyear": "2000",
    "track": "Superman/Supergirl"
    },
    {
    "alltime": False,
    "artist": "Tex Perkins",
    "country": "Australia",
    "id": "1520",
    "pollyear": 2000,
    "position": 72,
    "releaseyear": "2000",
    "track": "I Know You Know I Know"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "1521",
    "pollyear": 2000,
    "position": 73,
    "releaseyear": "2000",
    "track": "Secrets"
    },
    {
    "alltime": False,
    "artist": "Groove Terminator",
    "country": "Australia",
    "id": "1522",
    "pollyear": 2000,
    "position": 74,
    "releaseyear": "2000",
    "track": "One More Time (Sunshine Song)"
    },
    {
    "alltime": False,
    "artist": "Slipknot",
    "country": "USA",
    "id": "1523",
    "pollyear": 2000,
    "position": 75,
    "releaseyear": "2000",
    "track": "Wait and Bleed"
    },
    {
    "alltime": False,
    "artist": "NOFX",
    "country": "USA",
    "id": "1524",
    "pollyear": 2000,
    "position": 76,
    "releaseyear": "2000",
    "track": "Bottles To The Ground"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "1525",
    "pollyear": 2000,
    "position": 77,
    "releaseyear": "2000",
    "track": "Maria"
    },
    {
    "alltime": False,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "1526",
    "pollyear": 2000,
    "position": 78,
    "releaseyear": "2000",
    "track": "Stand Inside Your Love"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "1527",
    "pollyear": 2000,
    "position": 79,
    "releaseyear": "2000",
    "track": "No Leaf Clover"
    },
    {
    "alltime": False,
    "artist": "Skulker",
    "country": "Australia",
    "id": "1528",
    "pollyear": 2000,
    "position": 80,
    "releaseyear": "2000",
    "track": "Hej"
    },
    {
    "alltime": False,
    "artist": "Korn",
    "country": "USA",
    "id": "1529",
    "pollyear": 2000,
    "position": 81,
    "releaseyear": "2000",
    "track": "Make Me Bad"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1530",
    "pollyear": 2000,
    "position": 82,
    "releaseyear": "2000",
    "track": "Sunburn"
    },
    {
    "alltime": False,
    "artist": "Skunkhour",
    "country": "Australia",
    "id": "1531",
    "pollyear": 2000,
    "position": 83,
    "releaseyear": "2000",
    "track": "Kick In The Door"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "1532",
    "pollyear": 2000,
    "position": 84,
    "releaseyear": "2000",
    "track": "I Disappear"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "1533",
    "pollyear": 2000,
    "position": 85,
    "releaseyear": "2000",
    "track": "Nothing as It Seems"
    },
    {
    "alltime": False,
    "artist": "Klinger",
    "country": "Australia",
    "id": "1534",
    "pollyear": 2000,
    "position": 86,
    "releaseyear": "2000",
    "track": "Hello Cruel World"
    },
    {
    "alltime": False,
    "artist": "Madonna",
    "country": "USA",
    "id": "1535",
    "pollyear": 2000,
    "position": 87,
    "releaseyear": "2000",
    "track": "Music"
    },
    {
    "alltime": False,
    "artist": "Brassy",
    "country": "UK",
    "id": "1536",
    "pollyear": 2000,
    "position": 89,
    "releaseyear": "2000",
    "track": "Work It Out"
    },
    {
    "alltime": False,
    "artist": "PJ Harvey",
    "country": "UK",
    "id": "1537",
    "pollyear": 2000,
    "position": 90,
    "releaseyear": "2000",
    "track": "Good Fortune"
    },
    {
    "alltime": False,
    "artist": "Area-7",
    "country": "Australia",
    "id": "1538",
    "pollyear": 2000,
    "position": 91,
    "releaseyear": "2000",
    "track": "Start Making Sense"
    },
    {
    "alltime": False,
    "artist": "Killing Heidi",
    "country": "Australia",
    "id": "1539",
    "pollyear": 2000,
    "position": 92,
    "releaseyear": "2000",
    "track": "Live Without It"
    },
    {
    "alltime": False,
    "artist": "Reef",
    "country": "UK",
    "id": "1540",
    "pollyear": 2000,
    "position": 93,
    "releaseyear": "2000",
    "track": "Set The Record Straight"
    },
    {
    "alltime": False,
    "artist": "U2",
    "country": "Ireland",
    "id": "1541",
    "pollyear": 2000,
    "position": 94,
    "releaseyear": "2000",
    "track": "The Ground Beneath Her Feet"
    },
    {
    "alltime": False,
    "artist": "Rage Against the Machine",
    "country": "USA",
    "id": "1542",
    "pollyear": 2000,
    "position": 95,
    "releaseyear": "2000",
    "track": "Renegades of Funk"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1543",
    "pollyear": 2000,
    "position": 96,
    "releaseyear": "2000",
    "track": "Paint Pastel Princess"
    },
    {
    "alltime": False,
    "artist": "Klinger",
    "country": "Australia",
    "id": "1544",
    "pollyear": 2000,
    "position": 97,
    "releaseyear": "2000",
    "track": "Ben Lee"
    },
    {
    "alltime": False,
    "artist": "Motor Ace",
    "country": "Australia",
    "id": "1545",
    "pollyear": 2000,
    "position": 98,
    "releaseyear": "2000",
    "track": "Death Defy"
    },
    {
    "alltime": False,
    "artist": "Madison Avenue",
    "country": "Australia",
    "id": "1546",
    "pollyear": 2000,
    "position": 99,
    "releaseyear": "2000",
    "track": "Who the Hell Are You"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1547",
    "pollyear": 2000,
    "position": 100,
    "releaseyear": "2000",
    "track": "Warning"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "1548",
    "pollyear": 2003,
    "position": 1,
    "releaseyear": "2003",
    "track": "Are You Gonna Be My Girl?"
    },
    {
    "alltime": False,
    "artist": "OutKast",
    "country": "USA",
    "id": "1549",
    "pollyear": 2003,
    "position": 2,
    "releaseyear": "2003",
    "track": "Hey Ya!"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1550",
    "pollyear": 2003,
    "position": 3,
    "releaseyear": "2003",
    "track": "Seven Nation Army"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1551",
    "pollyear": 2003,
    "position": 4,
    "releaseyear": "2003",
    "track": "(Baby I've Got You) On My Mind"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "1552",
    "pollyear": 2003,
    "position": 5,
    "releaseyear": "2003",
    "track": "Clocks {Royksopp Remix}"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1553",
    "pollyear": 2003,
    "position": 6,
    "releaseyear": "2003",
    "track": "Hello"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1554",
    "pollyear": 2003,
    "position": 7,
    "releaseyear": "2003",
    "track": "Sunsets"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "1555",
    "pollyear": 2003,
    "position": 8,
    "releaseyear": "2003",
    "track": "Zebra"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1556",
    "pollyear": 2003,
    "position": 9,
    "releaseyear": "2003",
    "track": "The Nosebleed Section"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1557",
    "pollyear": 2003,
    "position": 10,
    "releaseyear": "2003",
    "track": "Love Your Way"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "1558",
    "pollyear": 2003,
    "position": 11,
    "releaseyear": "2003",
    "track": "Deja Vu"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "1559",
    "pollyear": 2003,
    "position": 12,
    "releaseyear": "2003",
    "track": "Lighthouse"
    },
    {
    "alltime": False,
    "artist": "The Dandy Warhols",
    "country": "USA",
    "id": "1560",
    "pollyear": 2003,
    "position": 13,
    "releaseyear": "2003",
    "track": "We Used to Be Friends"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1561",
    "pollyear": 2003,
    "position": 14,
    "releaseyear": "2003",
    "track": "The Hardest Button to Button"
    },
    {
    "alltime": False,
    "artist": "Butterfingers",
    "country": "Australia",
    "id": "1562",
    "pollyear": 2003,
    "position": 15,
    "releaseyear": "2003",
    "track": "I Love Work"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "1563",
    "pollyear": 2003,
    "position": 16,
    "releaseyear": "2003",
    "track": "Relapse"
    },
    {
    "alltime": False,
    "artist": "Jack Johnson",
    "country": "USA",
    "id": "1564",
    "pollyear": 2003,
    "position": 17,
    "releaseyear": "2003",
    "track": "Taylor"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "1565",
    "pollyear": 2003,
    "position": 18,
    "releaseyear": "2003",
    "track": "Diamonds on the Inside"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "1566",
    "pollyear": 2003,
    "position": 19,
    "releaseyear": "2003",
    "track": "Rollover DJ"
    },
    {
    "alltime": False,
    "artist": "Pete Murray",
    "country": "Australia",
    "id": "1567",
    "pollyear": 2003,
    "position": 20,
    "releaseyear": "2003",
    "track": "Feeler"
    },
    {
    "alltime": False,
    "artist": "Epicure",
    "country": "Australia",
    "id": "1568",
    "pollyear": 2003,
    "position": 21,
    "releaseyear": "2003",
    "track": "Armies Against Me"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1569",
    "pollyear": 2003,
    "position": 22,
    "releaseyear": "2003",
    "track": "Fortune Faded"
    },
    {
    "alltime": False,
    "artist": "Jack Johnson",
    "country": "USA",
    "id": "1570",
    "pollyear": 2003,
    "position": 24,
    "releaseyear": "2003",
    "track": "The Horizon Has Been Defeated"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "1571",
    "pollyear": 2003,
    "position": 25,
    "releaseyear": "2003",
    "track": "Baby Blue"
    },
    {
    "alltime": False,
    "artist": "Electric Six",
    "country": "USA",
    "id": "1572",
    "pollyear": 2003,
    "position": 28,
    "releaseyear": "2003",
    "track": "Danger! High Voltage"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "1573",
    "pollyear": 2003,
    "position": 29,
    "releaseyear": "2003",
    "track": "With My Own Two Hands"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1574",
    "pollyear": 2003,
    "position": 30,
    "releaseyear": "2003",
    "track": "The Bitter End"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1575",
    "pollyear": 2003,
    "position": 31,
    "releaseyear": "2003",
    "track": "Time Is Running Out"
    },
    {
    "alltime": False,
    "artist": "The Dandy Warhols",
    "country": "USA",
    "id": "1576",
    "pollyear": 2003,
    "position": 32,
    "releaseyear": "2003",
    "track": "You Were The Last High"
    },
    {
    "alltime": False,
    "artist": "Electric Six",
    "country": "USA",
    "id": "1577",
    "pollyear": 2003,
    "position": 33,
    "releaseyear": "2003",
    "track": "Gay Bar"
    },
    {
    "alltime": False,
    "artist": "Michael Franti and Spearhead",
    "country": "USA",
    "id": "1578",
    "pollyear": 2003,
    "position": 34,
    "releaseyear": "2003",
    "track": "Everyone Deserves Music"
    },
    {
    "alltime": False,
    "artist": "Magic Dirt",
    "country": "Australia",
    "id": "1579",
    "pollyear": 2003,
    "position": 35,
    "releaseyear": "2003",
    "track": "Plastic Loveless Letter"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1580",
    "pollyear": 2003,
    "position": 37,
    "releaseyear": "2003",
    "track": "Days Like These"
    },
    {
    "alltime": False,
    "artist": "Butterfingers",
    "country": "Australia",
    "id": "1581",
    "pollyear": 2003,
    "position": 38,
    "releaseyear": "2003",
    "track": "Everytime"
    },
    {
    "alltime": False,
    "artist": "Alex Lloyd",
    "country": "Australia",
    "id": "1582",
    "pollyear": 2003,
    "position": 39,
    "releaseyear": "2003",
    "track": "Coming Home"
    },
    {
    "alltime": False,
    "artist": "Jack Johnson",
    "country": "USA",
    "id": "1583",
    "pollyear": 2003,
    "position": 40,
    "releaseyear": "2003",
    "track": "Times Like These"
    },
    {
    "alltime": False,
    "artist": "The Beautiful Girls",
    "country": "Australia",
    "id": "1584",
    "pollyear": 2003,
    "position": 41,
    "releaseyear": "2003",
    "track": "Black Bird"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1585",
    "pollyear": 2003,
    "position": 42,
    "releaseyear": "2003",
    "track": "Stockholm Syndrome"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1586",
    "pollyear": 2003,
    "position": 43,
    "releaseyear": "2003",
    "track": "12:51"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "1587",
    "pollyear": 2003,
    "position": 44,
    "releaseyear": "2003",
    "track": "Dumb Enough"
    },
    {
    "alltime": False,
    "artist": "A Perfect Circle",
    "country": "USA",
    "id": "1588",
    "pollyear": 2003,
    "position": 45,
    "releaseyear": "2003",
    "track": "Weak and Powerless"
    },
    {
    "alltime": False,
    "artist": "The Herd",
    "country": "Australia",
    "id": "1589",
    "pollyear": 2003,
    "position": 46,
    "releaseyear": "2003",
    "track": "77%"
    },
    {
    "alltime": False,
    "artist": "Michael Franti and Spearhead",
    "country": "USA",
    "id": "1590",
    "pollyear": 2003,
    "position": 47,
    "releaseyear": "2003",
    "track": "Bomb The World"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "1591",
    "pollyear": 2003,
    "position": 48,
    "releaseyear": "2003",
    "track": "There There"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "1592",
    "pollyear": 2003,
    "position": 49,
    "releaseyear": "2003",
    "track": "2 + 2 = 5"
    },
    {
    "alltime": False,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "1593",
    "pollyear": 2003,
    "position": 51,
    "releaseyear": "2003",
    "track": "Sista (Live)"
    },
    {
    "alltime": False,
    "artist": "The Bens",
    "country": "Australia",
    "id": "1594",
    "pollyear": 2003,
    "position": 52,
    "releaseyear": "2003",
    "track": "Just Pretend"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "1595",
    "pollyear": 2003,
    "position": 53,
    "releaseyear": "2003",
    "track": "Feeling This"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "1596",
    "pollyear": 2003,
    "position": 54,
    "releaseyear": "2003",
    "track": "Let Me Be"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "1597",
    "pollyear": 2003,
    "position": 55,
    "releaseyear": "2003",
    "track": "Greed For Your Love"
    },
    {
    "alltime": False,
    "artist": "NOFX",
    "country": "USA",
    "id": "1598",
    "pollyear": 2003,
    "position": 56,
    "releaseyear": "2003",
    "track": "Franco Un-American"
    },
    {
    "alltime": False,
    "artist": "Missy Elliott",
    "country": "USA",
    "id": "1599",
    "pollyear": 2003,
    "position": 57,
    "releaseyear": "2003",
    "track": "Work It"
    },
    {
    "alltime": False,
    "artist": "AFI",
    "country": "USA",
    "id": "1600",
    "pollyear": 2003,
    "position": 58,
    "releaseyear": "2003",
    "track": "The Leaving Song, Pt. II"
    },
    {
    "alltime": False,
    "artist": "Gus and Frank",
    "country": "Australia",
    "id": "1601",
    "pollyear": 2003,
    "position": 59,
    "releaseyear": "2003",
    "track": "So Entertaining"
    },
    {
    "alltime": False,
    "artist": "Magic Dirt",
    "country": "Australia",
    "id": "1602",
    "pollyear": 2003,
    "position": 60,
    "releaseyear": "2003",
    "track": "Watch Out Boys"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "1603",
    "pollyear": 2003,
    "position": 61,
    "releaseyear": "2003",
    "track": "St. Anger"
    },
    {
    "alltime": False,
    "artist": "The Beautiful Girls",
    "country": "Australia",
    "id": "1604",
    "pollyear": 2003,
    "position": 62,
    "releaseyear": "2003",
    "track": "Music"
    },
    {
    "alltime": False,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "1605",
    "pollyear": 2003,
    "position": 63,
    "releaseyear": "2003",
    "track": "Song For A Sleepwalker"
    },
    {
    "alltime": False,
    "artist": "Belle and Sebastian",
    "country": "UK",
    "id": "1606",
    "pollyear": 2003,
    "position": 64,
    "releaseyear": "2003",
    "track": "Step into My Office, Baby"
    },
    {
    "alltime": False,
    "artist": "Andromeda",
    "country": "Australia",
    "id": "1607",
    "pollyear": 2003,
    "position": 65,
    "releaseyear": "2003",
    "track": "Something White And Sigmund"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1608",
    "pollyear": 2003,
    "position": 66,
    "releaseyear": "2003",
    "track": "Tabloid Magazine"
    },
    {
    "alltime": False,
    "artist": "Amiel",
    "country": "Australia",
    "id": "1609",
    "pollyear": 2003,
    "position": 67,
    "releaseyear": "2003",
    "track": "Lovesong"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "1610",
    "pollyear": 2003,
    "position": 68,
    "releaseyear": "2003",
    "track": "1 Second Of Insanity"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "1611",
    "pollyear": 2003,
    "position": 69,
    "releaseyear": "2003",
    "track": "Hysteria"
    },
    {
    "alltime": False,
    "artist": "A Perfect Circle",
    "country": "USA",
    "id": "1612",
    "pollyear": 2003,
    "position": 70,
    "releaseyear": "2003",
    "track": "The Outsider"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1613",
    "pollyear": 2003,
    "position": 72,
    "releaseyear": "2003",
    "track": "Running Up That Hill"
    },
    {
    "alltime": False,
    "artist": "Epicure",
    "country": "Australia",
    "id": "1614",
    "pollyear": 2003,
    "position": 73,
    "releaseyear": "2003",
    "track": "Life Sentence"
    },
    {
    "alltime": False,
    "artist": "Cody ChesnuTT",
    "country": "USA",
    "id": "1615",
    "pollyear": 2003,
    "position": 74,
    "releaseyear": "2003",
    "track": "Look Good In Leather"
    },
    {
    "alltime": False,
    "artist": "The Roots",
    "country": "USA",
    "id": "1616",
    "pollyear": 2003,
    "position": 75,
    "releaseyear": "2003",
    "track": "The Seed (2.0) {ft. Cody ChesnuTT}"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1617",
    "pollyear": 2003,
    "position": 76,
    "releaseyear": "2003",
    "track": "Rockin' Rocks"
    },
    {
    "alltime": False,
    "artist": "Kelis",
    "country": "USA",
    "id": "1618",
    "pollyear": 2003,
    "position": 79,
    "releaseyear": "2003",
    "track": "Milkshake"
    },
    {
    "alltime": False,
    "artist": "Benny Benassi Presents The Biz",
    "country": "Italy",
    "id": "1619",
    "pollyear": 2003,
    "position": 80,
    "releaseyear": "2003",
    "track": "Satisfaction"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "1620",
    "pollyear": 2003,
    "position": 81,
    "releaseyear": "2003",
    "track": "The Golden Path {ft. The Flaming Lips}"
    },
    {
    "alltime": False,
    "artist": "Basement Jaxx",
    "country": "UK",
    "id": "1621",
    "pollyear": 2003,
    "position": 82,
    "releaseyear": "2003",
    "track": "Good Luck {ft. Lisa Kekaula}"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1622",
    "pollyear": 2003,
    "position": 83,
    "releaseyear": "2003",
    "track": "Reptilia"
    },
    {
    "alltime": False,
    "artist": "Missy Elliott",
    "country": "USA",
    "id": "1623",
    "pollyear": 2003,
    "position": 85,
    "releaseyear": "2003",
    "track": "Pass That Dutch"
    },
    {
    "alltime": False,
    "artist": "Pete Murray",
    "country": "Australia",
    "id": "1624",
    "pollyear": 2003,
    "position": 86,
    "releaseyear": "2003",
    "track": "Lines"
    },
    {
    "alltime": False,
    "artist": "Junior Senior",
    "country": "Denmark",
    "id": "1625",
    "pollyear": 2003,
    "position": 87,
    "releaseyear": "2003",
    "track": "Move Your Feet"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "1626",
    "pollyear": 2003,
    "position": 88,
    "releaseyear": "2003",
    "track": "Voices In My Head"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1627",
    "pollyear": 2003,
    "position": 89,
    "releaseyear": "2003",
    "track": "Girl, You Have No Faith In Medicine"
    },
    {
    "alltime": False,
    "artist": "Offcutts",
    "country": "Australia",
    "id": "1628",
    "pollyear": 2003,
    "position": 90,
    "releaseyear": "2003",
    "track": "Break It (Down James Brown)"
    },
    {
    "alltime": False,
    "artist": "The Sleepy Jackson",
    "country": "Australia",
    "id": "1629",
    "pollyear": 2003,
    "position": 91,
    "releaseyear": "2003",
    "track": "Vampire Racecourse"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "1630",
    "pollyear": 2003,
    "position": 92,
    "releaseyear": "2003",
    "track": "Doctor, Doctor"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1631",
    "pollyear": 2003,
    "position": 94,
    "releaseyear": "2003",
    "track": "In The Cold, Cold Night"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1632",
    "pollyear": 2003,
    "position": 95,
    "releaseyear": "2003",
    "track": "Special Needs"
    },
    {
    "alltime": False,
    "artist": "Soggy Bottom Boys",
    "country": "USA",
    "id": "1633",
    "pollyear": 2003,
    "position": 96,
    "releaseyear": "2003",
    "track": "Man of Constant Sorrow {Skeewiff Remix}"
    },
    {
    "alltime": False,
    "artist": "The Darkness",
    "country": "UK",
    "id": "1634",
    "pollyear": 2003,
    "position": 97,
    "releaseyear": "2003",
    "track": "Growing On Me"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "1635",
    "pollyear": 2003,
    "position": 98,
    "releaseyear": "2003",
    "track": "Out of Time"
    },
    {
    "alltime": False,
    "artist": "The Mars Volta",
    "country": "USA",
    "id": "1636",
    "pollyear": 2003,
    "position": 99,
    "releaseyear": "2003",
    "track": "Inertiatic ESP"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1637",
    "pollyear": 2003,
    "position": 100,
    "releaseyear": "2003",
    "track": "The Chariot"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1638",
    "pollyear": 1999,
    "position": 1,
    "releaseyear": "1999",
    "track": "These Days"
    },
    {
    "alltime": False,
    "artist": "Killing Heidi",
    "country": "Australia",
    "id": "1639",
    "pollyear": 1999,
    "position": 2,
    "releaseyear": "1999",
    "track": "Weir"
    },
    {
    "alltime": False,
    "artist": "The Tenants",
    "country": "Australia",
    "id": "1640",
    "pollyear": 1999,
    "position": 3,
    "releaseyear": "1999",
    "track": "You Shit Me To Tears"
    },
    {
    "alltime": False,
    "artist": "Fatboy Slim",
    "country": "UK",
    "id": "1641",
    "pollyear": 1999,
    "position": 4,
    "releaseyear": "1999",
    "track": "Praise You"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "1642",
    "pollyear": 1999,
    "position": 5,
    "releaseyear": "1999",
    "track": "Every You Every Me"
    },
    {
    "alltime": False,
    "artist": "Bloodhound Gang",
    "country": "USA",
    "id": "1643",
    "pollyear": 1999,
    "position": 6,
    "releaseyear": "1999",
    "track": "The Bad Touch"
    },
    {
    "alltime": False,
    "artist": "Rage Against The Machine",
    "country": "USA",
    "id": "1644",
    "pollyear": 1999,
    "position": 7,
    "releaseyear": "1999",
    "track": "Guerrilla Radio"
    },
    {
    "alltime": False,
    "artist": "Limp Bizkit",
    "country": "USA",
    "id": "1645",
    "pollyear": 1999,
    "position": 8,
    "releaseyear": "1999",
    "track": "Nookie"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "1646",
    "pollyear": 1999,
    "position": 9,
    "releaseyear": "1999",
    "track": "Last Kiss"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1647",
    "pollyear": 1999,
    "position": 10,
    "releaseyear": "1999",
    "track": "Scar Tissue"
    },
    {
    "alltime": False,
    "artist": "The Foo Fighters",
    "country": "USA",
    "id": "1648",
    "pollyear": 1999,
    "position": 11,
    "releaseyear": "1999",
    "track": "Learn To Fly"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "1649",
    "pollyear": 1999,
    "position": 12,
    "releaseyear": "1999",
    "track": "When I Grow Up"
    },
    {
    "alltime": False,
    "artist": "Killing Heidi",
    "country": "Australia",
    "id": "1650",
    "pollyear": 1999,
    "position": 14,
    "releaseyear": "1999",
    "track": "Mascara"
    },
    {
    "alltime": False,
    "artist": "Korn",
    "country": "USA",
    "id": "1651",
    "pollyear": 1999,
    "position": 16,
    "releaseyear": "1999",
    "track": "Freak On A Leash"
    },
    {
    "alltime": False,
    "artist": "Korn",
    "country": "USA",
    "id": "1652",
    "pollyear": 1999,
    "position": 17,
    "releaseyear": "1999",
    "track": "Falling Away From Me"
    },
    {
    "alltime": False,
    "artist": "Sonic Animation",
    "country": "Australia",
    "id": "1653",
    "pollyear": 1999,
    "position": 18,
    "releaseyear": "1999",
    "track": "Theophilus Thistler (An Exercise In Vowels)"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "1654",
    "pollyear": 1999,
    "position": 19,
    "releaseyear": "1999",
    "track": "Animal"
    },
    {
    "alltime": False,
    "artist": "Rhubarb",
    "country": "Australia",
    "id": "1655",
    "pollyear": 1999,
    "position": 20,
    "releaseyear": "1999",
    "track": "Exerciser"
    },
    {
    "alltime": False,
    "artist": "Alex Lloyd",
    "country": "Australia",
    "id": "1656",
    "pollyear": 1999,
    "position": 21,
    "releaseyear": "1999",
    "track": "Lucky Star"
    },
    {
    "alltime": False,
    "artist": "Fatboy Slim",
    "country": "UK",
    "id": "1657",
    "pollyear": 1999,
    "position": 23,
    "releaseyear": "1999",
    "track": "Right Here, Right Now"
    },
    {
    "alltime": False,
    "artist": "Macy Gray",
    "country": "USA",
    "id": "1658",
    "pollyear": 1999,
    "position": 24,
    "releaseyear": "1999",
    "track": "I Try"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1659",
    "pollyear": 1999,
    "position": 25,
    "releaseyear": "1999",
    "track": "Already Gone"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "1660",
    "pollyear": 1999,
    "position": 26,
    "releaseyear": "1999",
    "track": "Never Had So Much Fun"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "1661",
    "pollyear": 1999,
    "position": 27,
    "releaseyear": "1999",
    "track": "Hey Boy Hey Girl"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "1662",
    "pollyear": 1999,
    "position": 28,
    "releaseyear": "1999",
    "track": "Feet Touch the Ground"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1663",
    "pollyear": 1999,
    "position": 29,
    "releaseyear": "1999",
    "track": "Anthem for the Year 2000"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1664",
    "pollyear": 1999,
    "position": 30,
    "releaseyear": "1999",
    "track": "Miss You Love"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "1665",
    "pollyear": 1999,
    "position": 31,
    "releaseyear": "1999",
    "track": "All the Small Things"
    },
    {
    "alltime": False,
    "artist": "The Tea Party",
    "country": "Canada",
    "id": "1666",
    "pollyear": 1999,
    "position": 32,
    "releaseyear": "1999",
    "track": "Heaven Coming Down"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "1667",
    "pollyear": 1999,
    "position": 33,
    "releaseyear": "1999",
    "track": "Ready 1"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "1668",
    "pollyear": 1999,
    "position": 34,
    "releaseyear": "1999",
    "track": "You Are Not My Friend"
    },
    {
    "alltime": False,
    "artist": "Peter Helliar",
    "country": "Australia",
    "id": "1669",
    "pollyear": 1999,
    "position": 35,
    "releaseyear": "1999",
    "track": "Bevan The Musical"
    },
    {
    "alltime": False,
    "artist": "Bodyjar",
    "country": "Australia",
    "id": "1670",
    "pollyear": 1999,
    "position": 36,
    "releaseyear": "1999",
    "track": "Hazy Shade Of Winter"
    },
    {
    "alltime": False,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "1671",
    "pollyear": 1999,
    "position": 37,
    "releaseyear": "1999",
    "track": "Around The World"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "1672",
    "pollyear": 1999,
    "position": 38,
    "releaseyear": "1999",
    "track": "Chunky Chunky Air Guitar"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1673",
    "pollyear": 1999,
    "position": 39,
    "releaseyear": "1999",
    "track": "Turn Up Your Stereo"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1674",
    "pollyear": 1999,
    "position": 40,
    "releaseyear": "1999",
    "track": "Shazam!"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1675",
    "pollyear": 1999,
    "position": 41,
    "releaseyear": "1999",
    "track": "All Torn Down"
    },
    {
    "alltime": False,
    "artist": "Custard",
    "country": "Australia",
    "id": "1676",
    "pollyear": 1999,
    "position": 42,
    "releaseyear": "1999",
    "track": "Ringo (I Feel Like)"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1677",
    "pollyear": 1999,
    "position": 43,
    "releaseyear": "1999",
    "track": "Emotion Sickness"
    },
    {
    "alltime": False,
    "artist": "Something For Kate",
    "country": "Australia",
    "id": "1678",
    "pollyear": 1999,
    "position": 44,
    "releaseyear": "1999",
    "track": "Electricity"
    },
    {
    "alltime": False,
    "artist": "Gerling",
    "country": "Australia",
    "id": "1679",
    "pollyear": 1999,
    "position": 45,
    "releaseyear": "1999",
    "track": "Enter, Space Capsule"
    },
    {
    "alltime": False,
    "artist": "Bush",
    "country": "UK",
    "id": "1680",
    "pollyear": 1999,
    "position": 46,
    "releaseyear": "1999",
    "track": "The Chemicals Between Us"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "1681",
    "pollyear": 1999,
    "position": 47,
    "releaseyear": "1999",
    "track": "Coffee & TV"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "1682",
    "pollyear": 1999,
    "position": 48,
    "releaseyear": "1999",
    "track": "West End Riot"
    },
    {
    "alltime": False,
    "artist": "Area-7",
    "country": "Australia",
    "id": "1683",
    "pollyear": 1999,
    "position": 49,
    "releaseyear": "1999",
    "track": "Second Class Citizen"
    },
    {
    "alltime": False,
    "artist": "The Fauves",
    "country": "Australia",
    "id": "1684",
    "pollyear": 1999,
    "position": 50,
    "releaseyear": "1999",
    "track": "Bigger Than Tina"
    },
    {
    "alltime": False,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "1685",
    "pollyear": 1999,
    "position": 51,
    "releaseyear": "1999",
    "track": "Army"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "1686",
    "pollyear": 1999,
    "position": 53,
    "releaseyear": "1999",
    "track": "Sexx Laws"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "1687",
    "pollyear": 1999,
    "position": 54,
    "releaseyear": "1999",
    "track": "Thank You (For Loving Me at My Worst)"
    },
    {
    "alltime": False,
    "artist": "Diana Ah Naid",
    "country": "Australia",
    "id": "1688",
    "pollyear": 1999,
    "position": 55,
    "releaseyear": "1999",
    "track": "Perfect Family"
    },
    {
    "alltime": False,
    "artist": "Metallica",
    "country": "USA",
    "id": "1689",
    "pollyear": 1999,
    "position": 56,
    "releaseyear": "1999",
    "track": "No Leaf Clover"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "1690",
    "pollyear": 1999,
    "position": 57,
    "releaseyear": "1999",
    "track": "Tender"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "1691",
    "pollyear": 1999,
    "position": 58,
    "releaseyear": "1999",
    "track": "I Want To Be A Nudist"
    },
    {
    "alltime": False,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "1692",
    "pollyear": 1999,
    "position": 59,
    "releaseyear": "1999",
    "track": "Mutha Fukka On A Motorcycle"
    },
    {
    "alltime": False,
    "artist": "VAST",
    "country": "USA",
    "id": "1693",
    "pollyear": 1999,
    "position": 60,
    "releaseyear": "1999",
    "track": "Touched"
    },
    {
    "alltime": False,
    "artist": "Augie March",
    "country": "Australia",
    "id": "1694",
    "pollyear": 1999,
    "position": 61,
    "releaseyear": "1999",
    "track": "Asleep In Perfection"
    },
    {
    "alltime": False,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "1695",
    "pollyear": 1999,
    "position": 62,
    "releaseyear": "1999",
    "track": "Happiness (Rotting My Brain)"
    },
    {
    "alltime": False,
    "artist": "Jamiroquai",
    "country": "UK",
    "id": "1696",
    "pollyear": 1999,
    "position": 63,
    "releaseyear": "1999",
    "track": "Canned Heat"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "1697",
    "pollyear": 1999,
    "position": 65,
    "releaseyear": "1999",
    "track": "Burn to Shine"
    },
    {
    "alltime": False,
    "artist": "Testeagles",
    "country": "Australia",
    "id": "1698",
    "pollyear": 1999,
    "position": 66,
    "releaseyear": "1999",
    "track": "Turn That Shit Up"
    },
    {
    "alltime": False,
    "artist": "Madonna",
    "country": "USA",
    "id": "1699",
    "pollyear": 1999,
    "position": 67,
    "releaseyear": "1999",
    "track": "Beautiful Stranger"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1700",
    "pollyear": 1999,
    "position": 68,
    "releaseyear": "1999",
    "track": "Good-Day Ray"
    },
    {
    "alltime": False,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "1701",
    "pollyear": 1999,
    "position": 69,
    "releaseyear": "1999",
    "track": "Starfuckers, Inc."
    },
    {
    "alltime": False,
    "artist": "Something For Kate",
    "country": "Australia",
    "id": "1702",
    "pollyear": 1999,
    "position": 70,
    "releaseyear": "1999",
    "track": "Whatever You Want"
    },
    {
    "alltime": False,
    "artist": "The Mutton Birds",
    "country": "New Zealand",
    "id": "1703",
    "pollyear": 1999,
    "position": 71,
    "releaseyear": "1999",
    "track": "Pulled Along By Love"
    },
    {
    "alltime": False,
    "artist": "Something For Kate",
    "country": "Australia",
    "id": "1704",
    "pollyear": 1999,
    "position": 72,
    "releaseyear": "1999",
    "track": "Hallways"
    },
    {
    "alltime": False,
    "artist": "Supergrass",
    "country": "UK",
    "id": "1705",
    "pollyear": 1999,
    "position": 73,
    "releaseyear": "1999",
    "track": "Pumping on Your Stereo"
    },
    {
    "alltime": False,
    "artist": "Deadstar",
    "country": "Australia",
    "id": "1706",
    "pollyear": 1999,
    "position": 74,
    "releaseyear": "1999",
    "track": "Deeper Water"
    },
    {
    "alltime": False,
    "artist": "Friendly",
    "country": "Australia",
    "id": "1707",
    "pollyear": 1999,
    "position": 75,
    "releaseyear": "1999",
    "track": "Some Kind Of Love Song"
    },
    {
    "alltime": False,
    "artist": "Bob Marley/Funkstar De Luxe",
    "country": "Jamaica",
    "id": "1708",
    "pollyear": 1999,
    "position": 77,
    "releaseyear": "1999",
    "track": "Sun Is Shining"
    },
    {
    "alltime": False,
    "artist": "The Cardigans",
    "country": "Sweden",
    "id": "1709",
    "pollyear": 1999,
    "position": 78,
    "releaseyear": "1999",
    "track": "My Favourite Game"
    },
    {
    "alltime": False,
    "artist": "Moby",
    "country": "UK",
    "id": "1710",
    "pollyear": 1999,
    "position": 79,
    "releaseyear": "1999",
    "track": "Bodyrock"
    },
    {
    "alltime": False,
    "artist": "Moloko",
    "country": "UK",
    "id": "1711",
    "pollyear": 1999,
    "position": 80,
    "releaseyear": "1999",
    "track": "Sing It Back"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "1712",
    "pollyear": 1999,
    "position": 81,
    "releaseyear": "1999",
    "track": "Nothing Much Happens"
    },
    {
    "alltime": False,
    "artist": "Skunkhour",
    "country": "Australia",
    "id": "1713",
    "pollyear": 1999,
    "position": 82,
    "releaseyear": "1999",
    "track": "Home"
    },
    {
    "alltime": False,
    "artist": "Custard",
    "country": "Australia",
    "id": "1714",
    "pollyear": 1999,
    "position": 83,
    "releaseyear": "1999",
    "track": "Hit Song"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1715",
    "pollyear": 1999,
    "position": 84,
    "releaseyear": "1999",
    "track": "Stevie"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "1716",
    "pollyear": 1999,
    "position": 85,
    "releaseyear": "1999",
    "track": "Steal My Kisses"
    },
    {
    "alltime": False,
    "artist": "Orgy",
    "country": "USA",
    "id": "1717",
    "pollyear": 1999,
    "position": 86,
    "releaseyear": "1999",
    "track": "Blue Monday"
    },
    {
    "alltime": False,
    "artist": "Moby",
    "country": "UK",
    "id": "1718",
    "pollyear": 1999,
    "position": 88,
    "releaseyear": "1999",
    "track": "Run On"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1719",
    "pollyear": 1999,
    "position": 89,
    "releaseyear": "1999",
    "track": "Nice Guys Finish Last"
    },
    {
    "alltime": False,
    "artist": "Rammstein",
    "country": "Germany",
    "id": "1720",
    "pollyear": 1999,
    "position": 90,
    "releaseyear": "1999",
    "track": "Stripped"
    },
    {
    "alltime": False,
    "artist": "Pennywise",
    "country": "USA",
    "id": "1721",
    "pollyear": 1999,
    "position": 91,
    "releaseyear": "1999",
    "track": "Down Under"
    },
    {
    "alltime": False,
    "artist": "Macy Gray",
    "country": "USA",
    "id": "1722",
    "pollyear": 1999,
    "position": 92,
    "releaseyear": "1999",
    "track": "Sex-O-Matic Venus Freak"
    },
    {
    "alltime": False,
    "artist": "Elliott Smith",
    "country": "USA",
    "id": "1723",
    "pollyear": 1999,
    "position": 93,
    "releaseyear": "1999",
    "track": "Waltz #2"
    },
    {
    "alltime": False,
    "artist": "Turnstyle",
    "country": "Australia",
    "id": "1724",
    "pollyear": 1999,
    "position": 94,
    "releaseyear": "1999",
    "track": "Spray Water On The Stereo"
    },
    {
    "alltime": False,
    "artist": "Public Image Ltd.",
    "country": "UK",
    "id": "1725",
    "pollyear": 1999,
    "position": 95,
    "releaseyear": "1999",
    "track": "The Order Of Death"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "1726",
    "pollyear": 1999,
    "position": 96,
    "releaseyear": "1999",
    "track": "Plastic"
    },
    {
    "alltime": False,
    "artist": "Sugar Ray",
    "country": "USA",
    "id": "1727",
    "pollyear": 1999,
    "position": 98,
    "releaseyear": "1999",
    "track": "Every Morning"
    },
    {
    "alltime": False,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "1728",
    "pollyear": 1999,
    "position": 99,
    "releaseyear": "1999",
    "track": "Ruby Wednesday"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "1729",
    "pollyear": 1999,
    "position": 100,
    "releaseyear": "1999",
    "track": "Passenger"
    },
    {
    "alltime": False,
    "artist": "Bernard Fanning",
    "country": "Australia",
    "id": "1730",
    "pollyear": 2005,
    "position": 1,
    "releaseyear": "2005",
    "track": "Wish You Well"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "1731",
    "pollyear": 2005,
    "position": 2,
    "releaseyear": "2005",
    "track": "Catch My Disease"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "1732",
    "pollyear": 2005,
    "position": 3,
    "releaseyear": "2005",
    "track": "Feel Good Inc."
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1733",
    "pollyear": 2005,
    "position": 4,
    "releaseyear": "2005",
    "track": "Best of You"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "1734",
    "pollyear": 2005,
    "position": 5,
    "releaseyear": "2005",
    "track": "DARE"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1735",
    "pollyear": 2005,
    "position": 7,
    "releaseyear": "2005",
    "track": "My Doorbell"
    },
    {
    "alltime": False,
    "artist": "End of Fashion",
    "country": "Australia",
    "id": "1736",
    "pollyear": 2005,
    "position": 8,
    "releaseyear": "2005",
    "track": "O Yeah"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1737",
    "pollyear": 2005,
    "position": 9,
    "releaseyear": "2005",
    "track": "Joker and the Thief"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "1738",
    "pollyear": 2005,
    "position": 10,
    "releaseyear": "2005",
    "track": "Do You Want To"
    },
    {
    "alltime": False,
    "artist": "Datarock",
    "country": "Norway",
    "id": "1739",
    "pollyear": 2005,
    "position": 12,
    "releaseyear": "2005",
    "track": "Computer Camp Love"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "1740",
    "pollyear": 2005,
    "position": 13,
    "releaseyear": "2005",
    "track": "Gold Digger"
    },
    {
    "alltime": False,
    "artist": "Bernard Fanning",
    "country": "Australia",
    "id": "1741",
    "pollyear": 2005,
    "position": 14,
    "releaseyear": "2005",
    "track": "Songbird"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "1742",
    "pollyear": 2005,
    "position": 15,
    "releaseyear": "2005",
    "track": "Flame Trees"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1743",
    "pollyear": 2005,
    "position": 16,
    "releaseyear": "2005",
    "track": "Apple Tree"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1744",
    "pollyear": 2005,
    "position": 17,
    "releaseyear": "2005",
    "track": "Blue Orchid"
    },
    {
    "alltime": False,
    "artist": "The Herd",
    "country": "Australia",
    "id": "1745",
    "pollyear": 2005,
    "position": 18,
    "releaseyear": "2005",
    "track": "I Was Only 19"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "1746",
    "pollyear": 2005,
    "position": 19,
    "releaseyear": "2005",
    "track": "Middle Of The Hill"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "1747",
    "pollyear": 2005,
    "position": 20,
    "releaseyear": "2005",
    "track": "DOA"
    },
    {
    "alltime": False,
    "artist": "Faker",
    "country": "Australia",
    "id": "1748",
    "pollyear": 2005,
    "position": 21,
    "releaseyear": "2005",
    "track": "Hurricane"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1749",
    "pollyear": 2005,
    "position": 23,
    "releaseyear": "2005",
    "track": "Two More Years"
    },
    {
    "alltime": False,
    "artist": "The Bloodhound Gang",
    "country": "USA",
    "id": "1750",
    "pollyear": 2005,
    "position": 24,
    "releaseyear": "2005",
    "track": "Foxtrot Uniform Charlie Kilo"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1751",
    "pollyear": 2005,
    "position": 25,
    "releaseyear": "2005",
    "track": "The Car Song"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "1752",
    "pollyear": 2005,
    "position": 26,
    "releaseyear": "2005",
    "track": "Fix You"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "1753",
    "pollyear": 2005,
    "position": 27,
    "releaseyear": "2005",
    "track": "B.Y.O.B."
    },
    {
    "alltime": False,
    "artist": "Kaiser Chiefs",
    "country": "UK",
    "id": "1754",
    "pollyear": 2005,
    "position": 28,
    "releaseyear": "2005",
    "track": "Everyday I Love You Less And Less"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "1755",
    "pollyear": 2005,
    "position": 29,
    "releaseyear": "2005",
    "track": "Fast Girl"
    },
    {
    "alltime": False,
    "artist": "After The Fall",
    "country": "Australia",
    "id": "1756",
    "pollyear": 2005,
    "position": 30,
    "releaseyear": "2005",
    "track": "Concrete Boots"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "1757",
    "pollyear": 2005,
    "position": 31,
    "releaseyear": "2005",
    "track": "The Special Two"
    },
    {
    "alltime": False,
    "artist": "Cog",
    "country": "Australia",
    "id": "1758",
    "pollyear": 2005,
    "position": 32,
    "releaseyear": "2005",
    "track": "My Enemy"
    },
    {
    "alltime": False,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "1759",
    "pollyear": 2005,
    "position": 33,
    "releaseyear": "2005",
    "track": "Phoenix"
    },
    {
    "alltime": False,
    "artist": "Kaiser Chiefs",
    "country": "UK",
    "id": "1760",
    "pollyear": 2005,
    "position": 34,
    "releaseyear": "2005",
    "track": "I Predict a Riot"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "1761",
    "pollyear": 2005,
    "position": 35,
    "releaseyear": "2005",
    "track": "Girl"
    },
    {
    "alltime": False,
    "artist": "Coldplay",
    "country": "UK",
    "id": "1762",
    "pollyear": 2005,
    "position": 36,
    "releaseyear": "2005",
    "track": "Speed of Sound"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1763",
    "pollyear": 2005,
    "position": 37,
    "releaseyear": "2005",
    "track": "Dimension"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1764",
    "pollyear": 2005,
    "position": 38,
    "releaseyear": "2005",
    "track": "Sly"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1765",
    "pollyear": 2005,
    "position": 39,
    "releaseyear": "2005",
    "track": "Colossal"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1766",
    "pollyear": 2005,
    "position": 40,
    "releaseyear": "2005",
    "track": "Helicopter"
    },
    {
    "alltime": False,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "1767",
    "pollyear": 2005,
    "position": 41,
    "releaseyear": "2005",
    "track": "Dirty Harry"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "1768",
    "pollyear": 2005,
    "position": 42,
    "releaseyear": "2005",
    "track": "Sweet as Sugar"
    },
    {
    "alltime": False,
    "artist": "Lior",
    "country": "Australia",
    "id": "1769",
    "pollyear": 2005,
    "position": 43,
    "releaseyear": "2005",
    "track": "Autumn Flow"
    },
    {
    "alltime": False,
    "artist": "Emiliana Torrini",
    "country": "Iceland",
    "id": "1770",
    "pollyear": 2005,
    "position": 44,
    "releaseyear": "2005",
    "track": "Sunny Road"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1771",
    "pollyear": 2005,
    "position": 45,
    "releaseyear": "2005",
    "track": "Positive Tension"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "1772",
    "pollyear": 2005,
    "position": 46,
    "releaseyear": "2005",
    "track": "Juicebox"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "1773",
    "pollyear": 2005,
    "position": 47,
    "releaseyear": "2005",
    "track": "Stuff and Nonsense"
    },
    {
    "alltime": False,
    "artist": "The Bravery",
    "country": "USA",
    "id": "1774",
    "pollyear": 2005,
    "position": 48,
    "releaseyear": "2005",
    "track": "An Honest Mistake"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "1775",
    "pollyear": 2005,
    "position": 50,
    "releaseyear": "2005",
    "track": "I Bet You Look Good on the Dancefloor"
    },
    {
    "alltime": False,
    "artist": "Audioslave",
    "country": "USA",
    "id": "1776",
    "pollyear": 2005,
    "position": 51,
    "releaseyear": "2005",
    "track": "Be Yourself"
    },
    {
    "alltime": False,
    "artist": "DVDA (from Team America: World Police)",
    "country": "USA",
    "id": "1777",
    "pollyear": 2005,
    "position": 52,
    "releaseyear": "2005",
    "track": "America, Fuck Yeah"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1778",
    "pollyear": 2005,
    "position": 54,
    "releaseyear": "2005",
    "track": "Two Shoes"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "1779",
    "pollyear": 2005,
    "position": 55,
    "releaseyear": "2005",
    "track": "Landed"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "1780",
    "pollyear": 2005,
    "position": 57,
    "releaseyear": "2005",
    "track": "Radio/Video"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "1781",
    "pollyear": 2005,
    "position": 58,
    "releaseyear": "2005",
    "track": "Little Sister"
    },
    {
    "alltime": False,
    "artist": "Martha Wainwright",
    "country": "USA",
    "id": "1782",
    "pollyear": 2005,
    "position": 59,
    "releaseyear": "2005",
    "track": "Bloody Mother Fucking Asshole"
    },
    {
    "alltime": False,
    "artist": "The Dandy Warhols",
    "country": "USA",
    "id": "1783",
    "pollyear": 2005,
    "position": 60,
    "releaseyear": "2005",
    "track": "All the Money or the Simple Life Honey"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1784",
    "pollyear": 2005,
    "position": 61,
    "releaseyear": "2005",
    "track": "Jesus of Suburbia"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "1785",
    "pollyear": 2005,
    "position": 62,
    "releaseyear": "2005",
    "track": "Beware Wolf"
    },
    {
    "alltime": False,
    "artist": "Clare Bowditch",
    "country": "Australia",
    "id": "1786",
    "pollyear": 2005,
    "position": 63,
    "releaseyear": "2005",
    "track": "Divorcee By 23"
    },
    {
    "alltime": False,
    "artist": "Jack Johnson",
    "country": "USA",
    "id": "1787",
    "pollyear": 2005,
    "position": 64,
    "releaseyear": "2005",
    "track": "Sitting, Waiting, Wishing"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "1788",
    "pollyear": 2005,
    "position": 65,
    "releaseyear": "2005",
    "track": "Always Worth It"
    },
    {
    "alltime": False,
    "artist": "Ween",
    "country": "USA",
    "id": "1789",
    "pollyear": 2005,
    "position": 66,
    "releaseyear": "2005",
    "track": "Gabrielle"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "1790",
    "pollyear": 2005,
    "position": 67,
    "releaseyear": "2005",
    "track": "The Denial Twist"
    },
    {
    "alltime": False,
    "artist": "The Beautiful Girls",
    "country": "Australia",
    "id": "1791",
    "pollyear": 2005,
    "position": 68,
    "releaseyear": "2005",
    "track": "Ashes"
    },
    {
    "alltime": False,
    "artist": "Butterfingers",
    "country": "Australia",
    "id": "1792",
    "pollyear": 2005,
    "position": 69,
    "releaseyear": "2005",
    "track": "Jesus I Was Evil"
    },
    {
    "alltime": False,
    "artist": "The Mountain Goats",
    "country": "USA",
    "id": "1793",
    "pollyear": 2005,
    "position": 70,
    "releaseyear": "2005",
    "track": "This Year"
    },
    {
    "alltime": False,
    "artist": "Cog",
    "country": "Australia",
    "id": "1794",
    "pollyear": 2005,
    "position": 71,
    "releaseyear": "2005",
    "track": "Run"
    },
    {
    "alltime": False,
    "artist": "Jack Johnson",
    "country": "USA",
    "id": "1795",
    "pollyear": 2005,
    "position": 73,
    "releaseyear": "2005",
    "track": "Better Together"
    },
    {
    "alltime": False,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "1796",
    "pollyear": 2005,
    "position": 74,
    "releaseyear": "2005",
    "track": "The Sound Of White"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "1797",
    "pollyear": 2005,
    "position": 75,
    "releaseyear": "2005",
    "track": "Que Onda Guero"
    },
    {
    "alltime": False,
    "artist": "System of a Down",
    "country": "USA",
    "id": "1798",
    "pollyear": 2005,
    "position": 76,
    "releaseyear": "2005",
    "track": "Hypnotize"
    },
    {
    "alltime": False,
    "artist": "Bright Eyes",
    "country": "USA",
    "id": "1799",
    "pollyear": 2005,
    "position": 77,
    "releaseyear": "2005",
    "track": "First Day of My Life"
    },
    {
    "alltime": False,
    "artist": "After The Fall",
    "country": "Australia",
    "id": "1800",
    "pollyear": 2005,
    "position": 78,
    "releaseyear": "2005",
    "track": "The Fighter"
    },
    {
    "alltime": False,
    "artist": "Babyshambles",
    "country": "UK",
    "id": "1801",
    "pollyear": 2005,
    "position": 79,
    "releaseyear": "2005",
    "track": "Fuck Forever"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "1802",
    "pollyear": 2005,
    "position": 80,
    "releaseyear": "2005",
    "track": "Believe"
    },
    {
    "alltime": False,
    "artist": "The Dandy Warhols",
    "country": "USA",
    "id": "1803",
    "pollyear": 2005,
    "position": 82,
    "releaseyear": "2005",
    "track": "Smoke It"
    },
    {
    "alltime": False,
    "artist": "Scissor Sisters",
    "country": "USA",
    "id": "1804",
    "pollyear": 2005,
    "position": 83,
    "releaseyear": "2005",
    "track": "Filthy/Gorgeous"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "1805",
    "pollyear": 2005,
    "position": 84,
    "releaseyear": "2005",
    "track": "White Unicorn"
    },
    {
    "alltime": False,
    "artist": "Epicure",
    "country": "Australia",
    "id": "1806",
    "pollyear": 2005,
    "position": 85,
    "releaseyear": "2005",
    "track": "Tightrope Walker"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "1807",
    "pollyear": 2005,
    "position": 86,
    "releaseyear": "2005",
    "track": "Into the Dark"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "1808",
    "pollyear": 2005,
    "position": 88,
    "releaseyear": "2005",
    "track": "Like Eating Glass"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "1809",
    "pollyear": 2005,
    "position": 89,
    "releaseyear": "2005",
    "track": "Bastard"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "1810",
    "pollyear": 2005,
    "position": 90,
    "releaseyear": "2005",
    "track": "Walk Away"
    },
    {
    "alltime": False,
    "artist": "Emiliana Torrini",
    "country": "Iceland",
    "id": "1811",
    "pollyear": 2005,
    "position": 91,
    "releaseyear": "2005",
    "track": "Heartstopper"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "1812",
    "pollyear": 2005,
    "position": 92,
    "releaseyear": "2005",
    "track": "Messages"
    },
    {
    "alltime": False,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "1813",
    "pollyear": 2005,
    "position": 93,
    "releaseyear": "2005",
    "track": "The Fallen"
    },
    {
    "alltime": False,
    "artist": "Clare Bowditch",
    "country": "Australia",
    "id": "1814",
    "pollyear": 2005,
    "position": 94,
    "releaseyear": "2005",
    "track": "On This Side"
    },
    {
    "alltime": False,
    "artist": "Kisschasy",
    "country": "Australia",
    "id": "1815",
    "pollyear": 2005,
    "position": 95,
    "releaseyear": "2005",
    "track": "Face Without a Name"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "1816",
    "pollyear": 2005,
    "position": 96,
    "releaseyear": "2005",
    "track": "Six Months in a Leaky Boat"
    },
    {
    "alltime": False,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "1817",
    "pollyear": 2005,
    "position": 97,
    "releaseyear": "2005",
    "track": "Themata"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "1818",
    "pollyear": 2005,
    "position": 98,
    "releaseyear": "2005",
    "track": "Why Do You Love Me"
    },
    {
    "alltime": False,
    "artist": "The Wrights",
    "country": "Australia",
    "id": "1819",
    "pollyear": 2005,
    "position": 99,
    "releaseyear": "2005",
    "track": "Evie Pt. 1"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "1820",
    "pollyear": 2005,
    "position": 100,
    "releaseyear": "2005",
    "track": "Party Started"
    },
    {
    "alltime": False,
    "artist": "The Cranberries",
    "country": "Ireland",
    "id": "1821",
    "pollyear": 1994,
    "position": 1,
    "releaseyear": "1994",
    "track": "Zombie"
    },
    {
    "alltime": False,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "1822",
    "pollyear": 1994,
    "position": 2,
    "releaseyear": "1994",
    "track": "Closer"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "1823",
    "pollyear": 1994,
    "position": 3,
    "releaseyear": "1994",
    "track": "Self Esteem"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "1824",
    "pollyear": 1994,
    "position": 4,
    "releaseyear": "1994",
    "track": "Come Out & Play"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "1825",
    "pollyear": 1994,
    "position": 5,
    "releaseyear": "1994",
    "track": "Tomorrow"
    },
    {
    "alltime": False,
    "artist": "Veruca Salt",
    "country": "USA",
    "id": "1826",
    "pollyear": 1994,
    "position": 6,
    "releaseyear": "1994",
    "track": "Seether"
    },
    {
    "alltime": False,
    "artist": "Nirvana",
    "country": "USA",
    "id": "1827",
    "pollyear": 1994,
    "position": 7,
    "releaseyear": "1994",
    "track": "About a Girl"
    },
    {
    "alltime": False,
    "artist": "Max Sharam",
    "country": "Australia",
    "id": "1828",
    "pollyear": 1994,
    "position": 8,
    "releaseyear": "1994",
    "track": "Coma"
    },
    {
    "alltime": False,
    "artist": "Tom Jones",
    "country": "UK",
    "id": "1829",
    "pollyear": 1994,
    "position": 9,
    "releaseyear": "1994",
    "track": "If I Only Knew"
    },
    {
    "alltime": False,
    "artist": "Severed Heads",
    "country": "Australia",
    "id": "1830",
    "pollyear": 1994,
    "position": 10,
    "releaseyear": "1994",
    "track": "Dead Eyes Opened {1994 Remix}"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "1831",
    "pollyear": 1994,
    "position": 11,
    "releaseyear": "1994",
    "track": "Do You Love Me?"
    },
    {
    "alltime": False,
    "artist": "James",
    "country": "UK",
    "id": "1832",
    "pollyear": 1994,
    "position": 12,
    "releaseyear": "1994",
    "track": "Laid"
    },
    {
    "alltime": False,
    "artist": "Bomb The Bass",
    "country": "UK",
    "id": "1833",
    "pollyear": 1994,
    "position": 13,
    "releaseyear": "1994",
    "track": "Bug Powder Dust"
    },
    {
    "alltime": False,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "1834",
    "pollyear": 1994,
    "position": 14,
    "releaseyear": "1994",
    "track": "Better Get A Lawyer"
    },
    {
    "alltime": False,
    "artist": "Sheryl Crow",
    "country": "USA",
    "id": "1835",
    "pollyear": 1994,
    "position": 15,
    "releaseyear": "1994",
    "track": "All I Wanna Do"
    },
    {
    "alltime": False,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "1836",
    "pollyear": 1994,
    "position": 16,
    "releaseyear": "1994",
    "track": "Sabotage"
    },
    {
    "alltime": False,
    "artist": "Stone Temple Pilots",
    "country": "USA",
    "id": "1837",
    "pollyear": 1994,
    "position": 17,
    "releaseyear": "1994",
    "track": "Interstate Love Song"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1838",
    "pollyear": 1994,
    "position": 18,
    "releaseyear": "1994",
    "track": "Longview"
    },
    {
    "alltime": False,
    "artist": "Nick Barker",
    "country": "Australia",
    "id": "1839",
    "pollyear": 1994,
    "position": 20,
    "releaseyear": "1994",
    "track": "Time Bomb"
    },
    {
    "alltime": False,
    "artist": "Itch-E and Scratch-E",
    "country": "Australia",
    "id": "1840",
    "pollyear": 1994,
    "position": 21,
    "releaseyear": "1994",
    "track": "Sweetness & Light"
    },
    {
    "alltime": False,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "1841",
    "pollyear": 1994,
    "position": 22,
    "releaseyear": "1994",
    "track": "Black Hole Sun"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "1842",
    "pollyear": 1994,
    "position": 23,
    "releaseyear": "1994",
    "track": "Berlin Chair"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "1843",
    "pollyear": 1994,
    "position": 24,
    "releaseyear": "1994",
    "track": "Basket Case"
    },
    {
    "alltime": False,
    "artist": "Smashing Pumpkins",
    "country": "USA",
    "id": "1844",
    "pollyear": 1994,
    "position": 25,
    "releaseyear": "1994",
    "track": "Today"
    },
    {
    "alltime": False,
    "artist": "Live",
    "country": "USA",
    "id": "1845",
    "pollyear": 1994,
    "position": 27,
    "releaseyear": "1994",
    "track": "I Alone"
    },
    {
    "alltime": False,
    "artist": "Hole",
    "country": "USA",
    "id": "1846",
    "pollyear": 1994,
    "position": 28,
    "releaseyear": "1994",
    "track": "Doll Parts"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "1847",
    "pollyear": 1994,
    "position": 29,
    "releaseyear": "1994",
    "track": "Beercan"
    },
    {
    "alltime": False,
    "artist": "Kylie Minogue",
    "country": "Australia",
    "id": "1848",
    "pollyear": 1994,
    "position": 30,
    "releaseyear": "1994",
    "track": "Confide in Me"
    },
    {
    "alltime": False,
    "artist": "Single Gun Theory",
    "country": "Australia",
    "id": "1849",
    "pollyear": 1994,
    "position": 31,
    "releaseyear": "1994",
    "track": "Fall"
    },
    {
    "alltime": False,
    "artist": "Mazzy Star",
    "country": "USA",
    "id": "1850",
    "pollyear": 1994,
    "position": 32,
    "releaseyear": "1994",
    "track": "Fade into You"
    },
    {
    "alltime": False,
    "artist": "Liz Phair",
    "country": "USA",
    "id": "1851",
    "pollyear": 1994,
    "position": 33,
    "releaseyear": "1994",
    "track": "Supernova"
    },
    {
    "alltime": False,
    "artist": "Hole",
    "country": "USA",
    "id": "1852",
    "pollyear": 1994,
    "position": 34,
    "releaseyear": "1994",
    "track": "Miss World"
    },
    {
    "alltime": False,
    "artist": "Tori Amos",
    "country": "USA",
    "id": "1853",
    "pollyear": 1994,
    "position": 35,
    "releaseyear": "1994",
    "track": "Cornflake Girl"
    },
    {
    "alltime": False,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "1854",
    "pollyear": 1994,
    "position": 36,
    "releaseyear": "1994",
    "track": "Spin the Black Circle"
    },
    {
    "alltime": False,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "1855",
    "pollyear": 1994,
    "position": 37,
    "releaseyear": "1994",
    "track": "Voodoo People"
    },
    {
    "alltime": False,
    "artist": "Dave Pike Set",
    "country": "USA",
    "id": "1856",
    "pollyear": 1994,
    "position": 39,
    "releaseyear": "1994",
    "track": "Mathar"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "1857",
    "pollyear": 1994,
    "position": 40,
    "releaseyear": "1994",
    "track": "Undone - The Sweater Song"
    },
    {
    "alltime": False,
    "artist": "Kristin Hersh",
    "country": "USA",
    "id": "1858",
    "pollyear": 1994,
    "position": 41,
    "releaseyear": "1994",
    "track": "Your Ghost"
    },
    {
    "alltime": False,
    "artist": "Pet Shop Boys",
    "country": "UK",
    "id": "1859",
    "pollyear": 1994,
    "position": 42,
    "releaseyear": "1994",
    "track": "Absolutely Fabulous"
    },
    {
    "alltime": False,
    "artist": "Christine Anu",
    "country": "Australia",
    "id": "1860",
    "pollyear": 1994,
    "position": 43,
    "releaseyear": "1994",
    "track": "Monkey & The Turtle"
    },
    {
    "alltime": False,
    "artist": "The Grid",
    "country": "UK",
    "id": "1861",
    "pollyear": 1994,
    "position": 44,
    "releaseyear": "1994",
    "track": "Swamp Thing"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "1862",
    "pollyear": 1994,
    "position": 45,
    "releaseyear": "1994",
    "track": "Loser"
    },
    {
    "alltime": False,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "1863",
    "pollyear": 1994,
    "position": 46,
    "releaseyear": "1994",
    "track": "My Wave"
    },
    {
    "alltime": False,
    "artist": "Counting Crows",
    "country": "USA",
    "id": "1864",
    "pollyear": 1994,
    "position": 47,
    "releaseyear": "1994",
    "track": "Einstein on the Beach (For An Eggman)"
    },
    {
    "alltime": False,
    "artist": "Counting Crows",
    "country": "USA",
    "id": "1865",
    "pollyear": 1994,
    "position": 48,
    "releaseyear": "1994",
    "track": "Mr. Jones"
    },
    {
    "alltime": False,
    "artist": "Falling Joys",
    "country": "Australia",
    "id": "1866",
    "pollyear": 1994,
    "position": 49,
    "releaseyear": "1994",
    "track": "Amen {Remix}"
    },
    {
    "alltime": False,
    "artist": "Tumbleweed",
    "country": "Australia",
    "id": "1867",
    "pollyear": 1994,
    "position": 50,
    "releaseyear": "1994",
    "track": "Daddy Long Legs"
    },
    {
    "alltime": False,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "1868",
    "pollyear": 1994,
    "position": 51,
    "releaseyear": "1994",
    "track": "Spoonman"
    },
    {
    "alltime": False,
    "artist": "Penny Flanagan",
    "country": "Australia",
    "id": "1869",
    "pollyear": 1994,
    "position": 52,
    "releaseyear": "1994",
    "track": "Lap It Up"
    },
    {
    "alltime": False,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "1870",
    "pollyear": 1994,
    "position": 53,
    "releaseyear": "1994",
    "track": "Fell on Black Days"
    },
    {
    "alltime": False,
    "artist": "Stone Temple Pilots",
    "country": "USA",
    "id": "1871",
    "pollyear": 1994,
    "position": 54,
    "releaseyear": "1994",
    "track": "Vasoline"
    },
    {
    "alltime": False,
    "artist": "Ed Kuepper",
    "country": "Australia",
    "id": "1872",
    "pollyear": 1994,
    "position": 55,
    "releaseyear": "1994",
    "track": "La Di Doh"
    },
    {
    "alltime": False,
    "artist": "Frente!",
    "country": "Australia",
    "id": "1873",
    "pollyear": 1994,
    "position": 56,
    "releaseyear": "1994",
    "track": "Bizarre Love Triangle"
    },
    {
    "alltime": False,
    "artist": "The Cure",
    "country": "UK",
    "id": "1874",
    "pollyear": 1994,
    "position": 57,
    "releaseyear": "1994",
    "track": "Burn"
    },
    {
    "alltime": False,
    "artist": "The Jesus and Mary Chain",
    "country": "UK",
    "id": "1875",
    "pollyear": 1994,
    "position": 59,
    "releaseyear": "1994",
    "track": "Sometimes Always"
    },
    {
    "alltime": False,
    "artist": "Pavement",
    "country": "USA",
    "id": "1876",
    "pollyear": 1994,
    "position": 60,
    "releaseyear": "1994",
    "track": "Cut Your Hair"
    },
    {
    "alltime": False,
    "artist": "Gin Blossoms",
    "country": "USA",
    "id": "1877",
    "pollyear": 1994,
    "position": 61,
    "releaseyear": "1994",
    "track": "Hey Jealousy"
    },
    {
    "alltime": False,
    "artist": "Pale",
    "country": "Australia",
    "id": "1878",
    "pollyear": 1994,
    "position": 62,
    "releaseyear": "1994",
    "track": "Lemon Sparked"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "1879",
    "pollyear": 1994,
    "position": 63,
    "releaseyear": "1994",
    "track": "Parklife"
    },
    {
    "alltime": False,
    "artist": "The Black Crowes",
    "country": "USA",
    "id": "1880",
    "pollyear": 1994,
    "position": 64,
    "releaseyear": "1994",
    "track": "A Conspiracy"
    },
    {
    "alltime": False,
    "artist": "Sonic Youth",
    "country": "USA",
    "id": "1881",
    "pollyear": 1994,
    "position": 65,
    "releaseyear": "1994",
    "track": "Bull in the Heather"
    },
    {
    "alltime": False,
    "artist": "Whale",
    "country": "Sweden",
    "id": "1882",
    "pollyear": 1994,
    "position": 66,
    "releaseyear": "1994",
    "track": "Hobo Humpin Slobo Babe"
    },
    {
    "alltime": False,
    "artist": "L7",
    "country": "USA",
    "id": "1883",
    "pollyear": 1994,
    "position": 67,
    "releaseyear": "1994",
    "track": "Andres"
    },
    {
    "alltime": False,
    "artist": "Dinosaur Jr.",
    "country": "USA",
    "id": "1884",
    "pollyear": 1994,
    "position": 68,
    "releaseyear": "1994",
    "track": "Feel the Pain"
    },
    {
    "alltime": False,
    "artist": "Crash Test Dummies",
    "country": "Canada",
    "id": "1885",
    "pollyear": 1994,
    "position": 69,
    "releaseyear": "1994",
    "track": "Mmm Mmm Mmm Mmm"
    },
    {
    "alltime": False,
    "artist": "Urge Overkill",
    "country": "USA",
    "id": "1886",
    "pollyear": 1994,
    "position": 71,
    "releaseyear": "1994",
    "track": "Dropout"
    },
    {
    "alltime": False,
    "artist": "Lucas",
    "country": "Denmark",
    "id": "1887",
    "pollyear": 1994,
    "position": 72,
    "releaseyear": "1994",
    "track": "Lucas With The Lid Off"
    },
    {
    "alltime": False,
    "artist": "The Sharp",
    "country": "Australia",
    "id": "1888",
    "pollyear": 1994,
    "position": 73,
    "releaseyear": "1994",
    "track": "Alone Like Me"
    },
    {
    "alltime": False,
    "artist": "Swoop",
    "country": "Australia",
    "id": "1889",
    "pollyear": 1994,
    "position": 74,
    "releaseyear": "1994",
    "track": "Neighbourhood Freak"
    },
    {
    "alltime": False,
    "artist": "Francis Dunnery",
    "country": "UK",
    "id": "1890",
    "pollyear": 1994,
    "position": 76,
    "releaseyear": "1994",
    "track": "American Life in the Summertime"
    },
    {
    "alltime": False,
    "artist": "Cracker",
    "country": "USA",
    "id": "1891",
    "pollyear": 1994,
    "position": 78,
    "releaseyear": "1994",
    "track": "Low"
    },
    {
    "alltime": False,
    "artist": "Alice in Chains",
    "country": "USA",
    "id": "1892",
    "pollyear": 1994,
    "position": 80,
    "releaseyear": "1994",
    "track": "No Excuses"
    },
    {
    "alltime": False,
    "artist": "Sisters Underground",
    "country": "New Zealand",
    "id": "1893",
    "pollyear": 1994,
    "position": 81,
    "releaseyear": "1994",
    "track": "In The Neighbourhood"
    },
    {
    "alltime": False,
    "artist": "Neil Young",
    "country": "Canada",
    "id": "1894",
    "pollyear": 1994,
    "position": 82,
    "releaseyear": "1994",
    "track": "Piece Of Crap"
    },
    {
    "alltime": False,
    "artist": "Love Spit Love",
    "country": "USA",
    "id": "1895",
    "pollyear": 1994,
    "position": 83,
    "releaseyear": "1994",
    "track": "Am I Wrong?"
    },
    {
    "alltime": False,
    "artist": "The Breeders",
    "country": "USA",
    "id": "1896",
    "pollyear": 1994,
    "position": 84,
    "releaseyear": "1994",
    "track": "Saints"
    },
    {
    "alltime": False,
    "artist": "G Love & Special Sauce",
    "country": "USA",
    "id": "1897",
    "pollyear": 1994,
    "position": 85,
    "releaseyear": "1994",
    "track": "Blues Music"
    },
    {
    "alltime": False,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "1898",
    "pollyear": 1994,
    "position": 86,
    "releaseyear": "1994",
    "track": "Thirsty Dog"
    },
    {
    "alltime": False,
    "artist": "Morrissey",
    "country": "UK",
    "id": "1899",
    "pollyear": 1994,
    "position": 87,
    "releaseyear": "1994",
    "track": "The More You Ignore Me, the Closer I Get"
    },
    {
    "alltime": False,
    "artist": "The Cure",
    "country": "UK",
    "id": "1900",
    "pollyear": 1994,
    "position": 88,
    "releaseyear": "1994",
    "track": "Purple Haze"
    },
    {
    "alltime": False,
    "artist": "Warren G & Nate Dogg",
    "country": "USA",
    "id": "1901",
    "pollyear": 1994,
    "position": 89,
    "releaseyear": "1994",
    "track": "Regulate"
    },
    {
    "alltime": False,
    "artist": "Smashing Pumpkins",
    "country": "USA",
    "id": "1902",
    "pollyear": 1994,
    "position": 90,
    "releaseyear": "1994",
    "track": "Dancing in the Moonlight"
    },
    {
    "alltime": False,
    "artist": "Counting Crows",
    "country": "USA",
    "id": "1903",
    "pollyear": 1994,
    "position": 91,
    "releaseyear": "1994",
    "track": "Round Here"
    },
    {
    "alltime": False,
    "artist": "Collective Soul",
    "country": "USA",
    "id": "1904",
    "pollyear": 1994,
    "position": 92,
    "releaseyear": "1994",
    "track": "Shine"
    },
    {
    "alltime": False,
    "artist": "Things of Stone and Wood",
    "country": "Australia",
    "id": "1905",
    "pollyear": 1994,
    "position": 93,
    "releaseyear": "1994",
    "track": "Wildflowers"
    },
    {
    "alltime": False,
    "artist": "Page and Plant",
    "country": "UK",
    "id": "1906",
    "pollyear": 1994,
    "position": 94,
    "releaseyear": "1994",
    "track": "Gallows Pole"
    },
    {
    "alltime": False,
    "artist": "Def FX",
    "country": "Australia",
    "id": "1907",
    "pollyear": 1994,
    "position": 95,
    "releaseyear": "1994",
    "track": "Masses Like Asses"
    },
    {
    "alltime": False,
    "artist": "Blur",
    "country": "UK",
    "id": "1908",
    "pollyear": 1994,
    "position": 96,
    "releaseyear": "1994",
    "track": "Girls & Boys {Remix}"
    },
    {
    "alltime": False,
    "artist": "Ini Kamoze",
    "country": "Jamaica",
    "id": "1909",
    "pollyear": 1994,
    "position": 97,
    "releaseyear": "1994",
    "track": "Here Comes the Hotstepper"
    },
    {
    "alltime": False,
    "artist": "The Tea Party",
    "country": "Canada",
    "id": "1910",
    "pollyear": 1994,
    "position": 98,
    "releaseyear": "1994",
    "track": "A Certain Slant of Light"
    },
    {
    "alltime": False,
    "artist": "Angelique Kidjo",
    "country": "Benin",
    "id": "1911",
    "pollyear": 1994,
    "position": 99,
    "releaseyear": "1994",
    "track": "Agolo"
    },
    {
    "alltime": False,
    "artist": "Lisa Loeb & Nine Stories",
    "country": "USA",
    "id": "1912",
    "pollyear": 1994,
    "position": 100,
    "releaseyear": "1994",
    "track": "Stay (I Missed You)"
    },
    {
    "alltime": True,
    "artist": "Joy Division",
    "country": "UK",
    "id": "1913",
    "pollyear": 1989,
    "position": 1,
    "releaseyear": "1980",
    "track": "Love Will Tear Us Apart"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "1914",
    "pollyear": 1989,
    "position": 2,
    "releaseyear": "1985",
    "track": "Throw Your Arms Around Me"
    },
    {
    "alltime": True,
    "artist": "The The",
    "country": "UK",
    "id": "1915",
    "pollyear": 1989,
    "position": 3,
    "releaseyear": "1983",
    "track": "Uncertain Smile"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "1916",
    "pollyear": 1989,
    "position": 5,
    "releaseyear": "1983",
    "track": "Blue Monday"
    },
    {
    "alltime": True,
    "artist": "Dead Kennedys",
    "country": "USA",
    "id": "1917",
    "pollyear": 1989,
    "position": 6,
    "releaseyear": "1980",
    "track": "Holiday in Cambodia"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "1918",
    "pollyear": 1989,
    "position": 7,
    "releaseyear": "1984",
    "track": "How Soon Is Now?"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "1919",
    "pollyear": 1989,
    "position": 8,
    "releaseyear": "1982",
    "track": "Talking To A Stranger"
    },
    {
    "alltime": True,
    "artist": "The Sugarcubes",
    "country": "Iceland",
    "id": "1920",
    "pollyear": 1989,
    "position": 9,
    "releaseyear": "1987",
    "track": "Birthday"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "1921",
    "pollyear": 1989,
    "position": 10,
    "releaseyear": "1980",
    "track": "A Forest"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "1922",
    "pollyear": 1989,
    "position": 11,
    "releaseyear": "1983",
    "track": "Cattle And Cane"
    },
    {
    "alltime": True,
    "artist": "Boys Next Door",
    "country": "Australia",
    "id": "1923",
    "pollyear": 1989,
    "position": 12,
    "releaseyear": "1979",
    "track": "Shivers"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "1924",
    "pollyear": 1989,
    "position": 13,
    "releaseyear": "1983",
    "track": "This Charming Man"
    },
    {
    "alltime": True,
    "artist": "This Mortal Coil",
    "country": "UK",
    "id": "1925",
    "pollyear": 1989,
    "position": 15,
    "releaseyear": "1983",
    "track": "Song To The Siren"
    },
    {
    "alltime": True,
    "artist": "Elvis Costello",
    "country": "UK",
    "id": "1926",
    "pollyear": 1989,
    "position": 16,
    "releaseyear": "1977",
    "track": "Alison"
    },
    {
    "alltime": True,
    "artist": "Sex Pistols",
    "country": "UK",
    "id": "1927",
    "pollyear": 1989,
    "position": 17,
    "releaseyear": "1976",
    "track": "Anarchy in the U.K."
    },
    {
    "alltime": True,
    "artist": "The Clash",
    "country": "UK",
    "id": "1928",
    "pollyear": 1989,
    "position": 18,
    "releaseyear": "1979",
    "track": "London Calling"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "1929",
    "pollyear": 1989,
    "position": 19,
    "releaseyear": "1981",
    "track": "Primary"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "1930",
    "pollyear": 1989,
    "position": 20,
    "releaseyear": "1988",
    "track": "Waiting For The Great Leap Forwards"
    },
    {
    "alltime": True,
    "artist": "Aretha Franklin",
    "country": "USA",
    "id": "1931",
    "pollyear": 1989,
    "position": 21,
    "releaseyear": "1967",
    "track": "Respect"
    },
    {
    "alltime": True,
    "artist": "Radio Birdman",
    "country": "Australia",
    "id": "1932",
    "pollyear": 1989,
    "position": 23,
    "releaseyear": "1978",
    "track": "Aloha Steve And Danno"
    },
    {
    "alltime": True,
    "artist": "Art Of Noise and Tom Jones",
    "country": "UK",
    "id": "1933",
    "pollyear": 1989,
    "position": 24,
    "releaseyear": "1988",
    "track": "Kiss"
    },
    {
    "alltime": True,
    "artist": "Machinations",
    "country": "Australia",
    "id": "1934",
    "pollyear": 1989,
    "position": 25,
    "releaseyear": "1981",
    "track": "Average Inadequacy"
    },
    {
    "alltime": True,
    "artist": "The Only Ones",
    "country": "UK",
    "id": "1935",
    "pollyear": 1989,
    "position": 26,
    "releaseyear": "1978",
    "track": "Another Girl, Another Planet"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "1936",
    "pollyear": 1989,
    "position": 27,
    "releaseyear": "1986",
    "track": "Bigmouth Strikes Again"
    },
    {
    "alltime": True,
    "artist": "The Saints",
    "country": "Australia",
    "id": "1937",
    "pollyear": 1989,
    "position": 28,
    "releaseyear": "1978",
    "track": "Know Your Product"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "1938",
    "pollyear": 1989,
    "position": 30,
    "releaseyear": "1971",
    "track": "Stairway to Heaven"
    },
    {
    "alltime": True,
    "artist": "John Lennon",
    "country": "UK",
    "id": "1939",
    "pollyear": 1989,
    "position": 31,
    "releaseyear": "1971",
    "track": "Imagine"
    },
    {
    "alltime": True,
    "artist": "Talking Heads",
    "country": "USA",
    "id": "1940",
    "pollyear": 1989,
    "position": 32,
    "releaseyear": "1977",
    "track": "Psycho Killer"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "1941",
    "pollyear": 1989,
    "position": 33,
    "releaseyear": "1975",
    "track": "Wish You Were Here"
    },
    {
    "alltime": True,
    "artist": "Prince",
    "country": "USA",
    "id": "1942",
    "pollyear": 1989,
    "position": 34,
    "releaseyear": "1986",
    "track": "Kiss"
    },
    {
    "alltime": True,
    "artist": "The Cult",
    "country": "UK",
    "id": "1943",
    "pollyear": 1989,
    "position": 35,
    "releaseyear": "1985",
    "track": "She Sells Sanctuary"
    },
    {
    "alltime": True,
    "artist": "Simple Minds",
    "country": "UK",
    "id": "1944",
    "pollyear": 1989,
    "position": 36,
    "releaseyear": "1981",
    "track": "Love Song"
    },
    {
    "alltime": True,
    "artist": "Prince",
    "country": "USA",
    "id": "1945",
    "pollyear": 1989,
    "position": 37,
    "releaseyear": "1987",
    "track": "Sign 'O' the Times"
    },
    {
    "alltime": True,
    "artist": "Billy Bragg",
    "country": "UK",
    "id": "1946",
    "pollyear": 1989,
    "position": 38,
    "releaseyear": "1986",
    "track": "Greetings To The New Brunette"
    },
    {
    "alltime": True,
    "artist": "David Bowie",
    "country": "UK",
    "id": "1947",
    "pollyear": 1989,
    "position": 39,
    "releaseyear": "1977",
    "track": "Heroes"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "1948",
    "pollyear": 1989,
    "position": 40,
    "releaseyear": "1971",
    "track": "L.A. Woman"
    },
    {
    "alltime": True,
    "artist": "The Church",
    "country": "Australia",
    "id": "1949",
    "pollyear": 1989,
    "position": 42,
    "releaseyear": "1981",
    "track": "The Unguarded Moment"
    },
    {
    "alltime": True,
    "artist": "Kate Bush",
    "country": "UK",
    "id": "1950",
    "pollyear": 1989,
    "position": 43,
    "releaseyear": "1978",
    "track": "Wuthering Heights"
    },
    {
    "alltime": True,
    "artist": "The Damned",
    "country": "UK",
    "id": "1951",
    "pollyear": 1989,
    "position": 44,
    "releaseyear": "1979",
    "track": "Smash It Up"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "1952",
    "pollyear": 1989,
    "position": 45,
    "releaseyear": "1987",
    "track": "The One I Love"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "1953",
    "pollyear": 1989,
    "position": 46,
    "releaseyear": "1982",
    "track": "Blister In The Sun"
    },
    {
    "alltime": True,
    "artist": "Iggy Pop",
    "country": "USA",
    "id": "1954",
    "pollyear": 1989,
    "position": 47,
    "releaseyear": "1977",
    "track": "Lust For Life"
    },
    {
    "alltime": True,
    "artist": "Enya",
    "country": "Ireland",
    "id": "1955",
    "pollyear": 1989,
    "position": 48,
    "releaseyear": "1988",
    "track": "Orinoco Flow"
    },
    {
    "alltime": True,
    "artist": "The Jimi Hendrix Experience",
    "country": "USA",
    "id": "1956",
    "pollyear": 1989,
    "position": 49,
    "releaseyear": "1968",
    "track": "All Along the Watchtower"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "1957",
    "pollyear": 1989,
    "position": 50,
    "releaseyear": "1967",
    "track": "The End"
    },
    {
    "alltime": True,
    "artist": "Womack & Womack",
    "country": "USA",
    "id": "1958",
    "pollyear": 1989,
    "position": 52,
    "releaseyear": "1988",
    "track": "Teardrops"
    },
    {
    "alltime": True,
    "artist": "Sex Pistols",
    "country": "UK",
    "id": "1959",
    "pollyear": 1989,
    "position": 53,
    "releaseyear": "1977",
    "track": "God Save the Queen"
    },
    {
    "alltime": True,
    "artist": "Echo & The Bunnymen",
    "country": "UK",
    "id": "1960",
    "pollyear": 1989,
    "position": 54,
    "releaseyear": "1983",
    "track": "The Cutter"
    },
    {
    "alltime": True,
    "artist": "Television",
    "country": "USA",
    "id": "1961",
    "pollyear": 1989,
    "position": 55,
    "releaseyear": "1977",
    "track": "Marquee Moon"
    },
    {
    "alltime": True,
    "artist": "The Sunnyboys",
    "country": "Australia",
    "id": "1962",
    "pollyear": 1989,
    "position": 56,
    "releaseyear": "1981",
    "track": "Alone With You"
    },
    {
    "alltime": True,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "1963",
    "pollyear": 1989,
    "position": 57,
    "releaseyear": "1980",
    "track": "Wedding Cake Island"
    },
    {
    "alltime": True,
    "artist": "Elvis Costello",
    "country": "UK",
    "id": "1964",
    "pollyear": 1989,
    "position": 58,
    "releaseyear": "1986",
    "track": "I Want You"
    },
    {
    "alltime": True,
    "artist": "Art Of Noise",
    "country": "UK",
    "id": "1965",
    "pollyear": 1989,
    "position": 59,
    "releaseyear": "1983",
    "track": "Moments In Love"
    },
    {
    "alltime": True,
    "artist": "Sakamoto And Sylvian",
    "country": "Japan",
    "id": "1966",
    "pollyear": 1989,
    "position": 60,
    "releaseyear": "1983",
    "track": "Forbidden Colours"
    },
    {
    "alltime": True,
    "artist": "Neneh Cherry",
    "country": "Sweden",
    "id": "1967",
    "pollyear": 1989,
    "position": 61,
    "releaseyear": "1988",
    "track": "Buffalo Stance"
    },
    {
    "alltime": True,
    "artist": "Marvin Gaye",
    "country": "USA",
    "id": "1968",
    "pollyear": 1989,
    "position": 62,
    "releaseyear": "1982",
    "track": "Sexual Healing"
    },
    {
    "alltime": True,
    "artist": "The Rolling Stones",
    "country": "UK",
    "id": "1969",
    "pollyear": 1989,
    "position": 63,
    "releaseyear": "1968",
    "track": "Sympathy for the Devil"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "1970",
    "pollyear": 1989,
    "position": 64,
    "releaseyear": "1986",
    "track": "There Is a Light That Never Goes Out"
    },
    {
    "alltime": True,
    "artist": "Sex Pistols",
    "country": "UK",
    "id": "1971",
    "pollyear": 1989,
    "position": 65,
    "releaseyear": "1977",
    "track": "Pretty Vacant"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "1972",
    "pollyear": 1989,
    "position": 66,
    "releaseyear": "1985",
    "track": "Close To Me"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "1973",
    "pollyear": 1989,
    "position": 67,
    "releaseyear": "1986",
    "track": "Bizarre Love Triangle"
    },
    {
    "alltime": True,
    "artist": "The Triffids",
    "country": "Australia",
    "id": "1974",
    "pollyear": 1989,
    "position": 68,
    "releaseyear": "1986",
    "track": "Wide Open Road"
    },
    {
    "alltime": True,
    "artist": "The Beatles",
    "country": "UK",
    "id": "1975",
    "pollyear": 1989,
    "position": 69,
    "releaseyear": "1967",
    "track": "A Day in the Life"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "1976",
    "pollyear": 1989,
    "position": 70,
    "releaseyear": "1988",
    "track": "Deanna"
    },
    {
    "alltime": True,
    "artist": "Elvis Costello",
    "country": "UK",
    "id": "1977",
    "pollyear": 1989,
    "position": 71,
    "releaseyear": "1978",
    "track": "Pump It Up"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "1978",
    "pollyear": 1989,
    "position": 72,
    "releaseyear": "1984",
    "track": "Bachelor Kisses"
    },
    {
    "alltime": True,
    "artist": "Elvis Costello",
    "country": "UK",
    "id": "1979",
    "pollyear": 1989,
    "position": 73,
    "releaseyear": "1977",
    "track": "Watching The Detectives"
    },
    {
    "alltime": True,
    "artist": "Propaganda",
    "country": "Germany",
    "id": "1980",
    "pollyear": 1989,
    "position": 74,
    "releaseyear": "1985",
    "track": "Duel"
    },
    {
    "alltime": True,
    "artist": "The Jam",
    "country": "UK",
    "id": "1981",
    "pollyear": 1989,
    "position": 75,
    "releaseyear": "1980",
    "track": "Going Underground"
    },
    {
    "alltime": True,
    "artist": "Derek And The Dominos",
    "country": "USA",
    "id": "1982",
    "pollyear": 1989,
    "position": 76,
    "releaseyear": "1970",
    "track": "Layla"
    },
    {
    "alltime": True,
    "artist": "Lou Reed",
    "country": "USA",
    "id": "1983",
    "pollyear": 1989,
    "position": 77,
    "releaseyear": "1972",
    "track": "Walk On The Wild Side"
    },
    {
    "alltime": True,
    "artist": "The Saints",
    "country": "Australia",
    "id": "1984",
    "pollyear": 1989,
    "position": 78,
    "releaseyear": "1984",
    "track": "Ghost Ships"
    },
    {
    "alltime": True,
    "artist": "Warumpi Band",
    "country": "Australia",
    "id": "1985",
    "pollyear": 1989,
    "position": 79,
    "releaseyear": "1987",
    "track": "My Island Home"
    },
    {
    "alltime": True,
    "artist": "Cocteau Twins",
    "country": "UK",
    "id": "1986",
    "pollyear": 1989,
    "position": 80,
    "releaseyear": "1988",
    "track": "Blue Bell Knoll"
    },
    {
    "alltime": True,
    "artist": "XTC",
    "country": "UK",
    "id": "1987",
    "pollyear": 1989,
    "position": 81,
    "releaseyear": "1979",
    "track": "Making Plans For Nigel"
    },
    {
    "alltime": True,
    "artist": "The Stranglers",
    "country": "UK",
    "id": "1988",
    "pollyear": 1989,
    "position": 82,
    "releaseyear": "1981",
    "track": "Golden Brown"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "1989",
    "pollyear": 1989,
    "position": 83,
    "releaseyear": "1984",
    "track": "The Slab"
    },
    {
    "alltime": True,
    "artist": "Talking Heads",
    "country": "USA",
    "id": "1990",
    "pollyear": 1989,
    "position": 84,
    "releaseyear": "1983",
    "track": "Burning Down The House"
    },
    {
    "alltime": True,
    "artist": "Grandmaster Flash",
    "country": "USA",
    "id": "1991",
    "pollyear": 1989,
    "position": 85,
    "releaseyear": "1982",
    "track": "The Message"
    },
    {
    "alltime": True,
    "artist": "The Doors",
    "country": "USA",
    "id": "1992",
    "pollyear": 1989,
    "position": 86,
    "releaseyear": "1971",
    "track": "Riders On The Storm"
    },
    {
    "alltime": True,
    "artist": "The Jam",
    "country": "UK",
    "id": "1993",
    "pollyear": 1989,
    "position": 87,
    "releaseyear": "1978",
    "track": "Down in the Tube Station at Midnight"
    },
    {
    "alltime": True,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "1994",
    "pollyear": 1989,
    "position": 88,
    "releaseyear": "1982",
    "track": "Power And The Passion"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "1995",
    "pollyear": 1989,
    "position": 89,
    "releaseyear": "1987",
    "track": "Bye Bye Pride"
    },
    {
    "alltime": True,
    "artist": "Daddy Cool",
    "country": "Australia",
    "id": "1996",
    "pollyear": 1989,
    "position": 90,
    "releaseyear": "1971",
    "track": "Eagle Rock"
    },
    {
    "alltime": True,
    "artist": "Elvis Presley",
    "country": "USA",
    "id": "1997",
    "pollyear": 1989,
    "position": 91,
    "releaseyear": "1969",
    "track": "Suspicious Minds"
    },
    {
    "alltime": True,
    "artist": "Aretha Franklin",
    "country": "USA",
    "id": "1998",
    "pollyear": 1989,
    "position": 92,
    "releaseyear": "1968",
    "track": "I Say A Little Prayer"
    },
    {
    "alltime": True,
    "artist": "Lime Spiders",
    "country": "Australia",
    "id": "1999",
    "pollyear": 1989,
    "position": 93,
    "releaseyear": "1984",
    "track": "Slave Girl"
    },
    {
    "alltime": True,
    "artist": "Blondie",
    "country": "USA",
    "id": "2000",
    "pollyear": 1989,
    "position": 94,
    "releaseyear": "1978",
    "track": "Heart of Glass"
    },
    {
    "alltime": True,
    "artist": "Cold Chisel",
    "country": "Australia",
    "id": "2001",
    "pollyear": 1989,
    "position": 95,
    "releaseyear": "1978",
    "track": "Khe Sanh"
    },
    {
    "alltime": True,
    "artist": "Laurie Anderson",
    "country": "USA",
    "id": "2002",
    "pollyear": 1989,
    "position": 96,
    "releaseyear": "1981",
    "track": "O Superman"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "2003",
    "pollyear": 1989,
    "position": 97,
    "releaseyear": "1986",
    "track": "Say Goodbye"
    },
    {
    "alltime": True,
    "artist": "Do-Re-Mi",
    "country": "Australia",
    "id": "2004",
    "pollyear": 1989,
    "position": 98,
    "releaseyear": "1985",
    "track": "Man Overboard"
    },
    {
    "alltime": True,
    "artist": "Outline",
    "country": "Australia",
    "id": "2005",
    "pollyear": 1989,
    "position": 99,
    "releaseyear": "1980",
    "track": "Cicada That Ate Five Dock"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2006",
    "pollyear": 1989,
    "position": 100,
    "releaseyear": "1988",
    "track": "The Mercy Seat"
    },
    {
    "alltime": False,
    "artist": "Baby Bird",
    "country": "UK",
    "id": "2007",
    "pollyear": 1996,
    "position": 10,
    "releaseyear": "1996",
    "track": "You're Gorgeous"
    },
    {
    "alltime": False,
    "artist": "Fun Lovin' Criminals",
    "country": "USA",
    "id": "2008",
    "pollyear": 1996,
    "position": 14,
    "releaseyear": "1996",
    "track": "Scooby Snacks"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "2009",
    "pollyear": 1996,
    "position": 29,
    "releaseyear": "1996",
    "track": "Devil's Haircut"
    },
    {
    "alltime": False,
    "artist": "Beck",
    "country": "USA",
    "id": "2010",
    "pollyear": 1996,
    "position": 43,
    "releaseyear": "1996",
    "track": "Where It's At"
    },
    {
    "alltime": False,
    "artist": "The Lemonheads",
    "country": "USA",
    "id": "2011",
    "pollyear": 1996,
    "position": 54,
    "releaseyear": "1996",
    "track": "If I Could Talk I'd Tell You"
    },
    {
    "alltime": False,
    "artist": "The Eels",
    "country": "USA",
    "id": "2012",
    "pollyear": 1996,
    "position": 56,
    "releaseyear": "1996",
    "track": "Susan's House"
    },
    {
    "alltime": False,
    "artist": "Rebecca's Empire",
    "country": "Australia",
    "id": "2013",
    "pollyear": 1996,
    "position": 57,
    "releaseyear": "1996",
    "track": "So Rude"
    },
    {
    "alltime": False,
    "artist": "Def FX",
    "country": "Australia",
    "id": "2014",
    "pollyear": 1996,
    "position": 61,
    "releaseyear": "1996",
    "track": "I'll Be Your Majick"
    },
    {
    "alltime": False,
    "artist": "Frente!",
    "country": "Australia",
    "id": "2015",
    "pollyear": 1996,
    "position": 66,
    "releaseyear": "1996",
    "track": "What's Come Over Me"
    },
    {
    "alltime": False,
    "artist": "Deadstar",
    "country": "Australia",
    "id": "2016",
    "pollyear": 1996,
    "position": 70,
    "releaseyear": "1996",
    "track": "Don't It Get You Down"
    },
    {
    "alltime": False,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "2017",
    "pollyear": 1996,
    "position": 75,
    "releaseyear": "1996",
    "track": "Surf's Up Tonight"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2018",
    "pollyear": 1996,
    "position": 84,
    "releaseyear": "1996",
    "track": "Good Mornin'"
    },
    {
    "alltime": False,
    "artist": "The Mavis's",
    "country": "Australia",
    "id": "2019",
    "pollyear": 1996,
    "position": 92,
    "releaseyear": "1996",
    "track": "Thunder"
    },
    {
    "alltime": False,
    "artist": "Matthew Trapnell",
    "country": "Australia",
    "id": "2020",
    "pollyear": 1996,
    "position": 96,
    "releaseyear": "1996",
    "track": "Ella's Uncle"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "2021",
    "pollyear": 1991,
    "position": 12,
    "releaseyear": "1987",
    "track": "It's The End Of The World"
    },
    {
    "alltime": True,
    "artist": "Jane's Addiction",
    "country": "USA",
    "id": "2022",
    "pollyear": 1991,
    "position": 15,
    "releaseyear": "1990",
    "track": "Been Caught Stealing"
    },
    {
    "alltime": True,
    "artist": "Jane's Addiction",
    "country": "USA",
    "id": "2023",
    "pollyear": 1991,
    "position": 17,
    "releaseyear": "1990",
    "track": "Jane Says"
    },
    {
    "alltime": True,
    "artist": "The Jam",
    "country": "UK",
    "id": "2024",
    "pollyear": 1991,
    "position": 23,
    "releaseyear": "1980",
    "track": "That's Entertainment"
    },
    {
    "alltime": True,
    "artist": "Guns N' Roses",
    "country": "USA",
    "id": "2025",
    "pollyear": 1991,
    "position": 27,
    "releaseyear": "1987",
    "track": "Sweet Child o' Mine"
    },
    {
    "alltime": True,
    "artist": "Ratcat",
    "country": "Australia",
    "id": "2026",
    "pollyear": 1991,
    "position": 41,
    "releaseyear": "1990",
    "track": "That Ain't Bad"
    },
    {
    "alltime": True,
    "artist": "Sinead O'Connor",
    "country": "Ireland",
    "id": "2027",
    "pollyear": 1991,
    "position": 42,
    "releaseyear": "1987",
    "track": "Troy"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2028",
    "pollyear": 1991,
    "position": 43,
    "releaseyear": "1980",
    "track": "Boys Don't Cry"
    },
    {
    "alltime": True,
    "artist": "Ned's Atomic Dustbin",
    "country": "UK",
    "id": "2029",
    "pollyear": 1991,
    "position": 71,
    "releaseyear": "1991",
    "track": "Grey Cell Green"
    },
    {
    "alltime": True,
    "artist": "The B-52's",
    "country": "USA",
    "id": "2030",
    "pollyear": 1991,
    "position": 77,
    "releaseyear": "1978",
    "track": "Rock Lobster"
    },
    {
    "alltime": True,
    "artist": "Dramarama",
    "country": "USA",
    "id": "2031",
    "pollyear": 1991,
    "position": 85,
    "releaseyear": "1985",
    "track": "Anything, Anything (I'll Give You)"
    },
    {
    "alltime": False,
    "artist": "Nirvana",
    "country": "USA",
    "id": "2032",
    "pollyear": 2002,
    "position": 12,
    "releaseyear": "2002",
    "track": "You Know You're Right"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "2033",
    "pollyear": 2002,
    "position": 24,
    "releaseyear": "2002",
    "track": "Keep Fishin'"
    },
    {
    "alltime": False,
    "artist": "28 Days",
    "country": "Australia",
    "id": "2034",
    "pollyear": 2002,
    "position": 41,
    "releaseyear": "2002",
    "track": "What's the Deal"
    },
    {
    "alltime": False,
    "artist": "The Streets",
    "country": "UK",
    "id": "2035",
    "pollyear": 2002,
    "position": 42,
    "releaseyear": "2002",
    "track": "Don't Mug Yourself"
    },
    {
    "alltime": False,
    "artist": "Darren Hanlon",
    "country": "Australia",
    "id": "2036",
    "pollyear": 2002,
    "position": 45,
    "releaseyear": "2002",
    "track": "Punk's Not Dead"
    },
    {
    "alltime": False,
    "artist": "Jurassic 5",
    "country": "USA",
    "id": "2037",
    "pollyear": 2002,
    "position": 49,
    "releaseyear": "2002",
    "track": "What's Golden"
    },
    {
    "alltime": False,
    "artist": "Black Rebel Motorcycle Club",
    "country": "USA",
    "id": "2038",
    "pollyear": 2002,
    "position": 68,
    "releaseyear": "2002",
    "track": "Whatever Happened to My Rock'n Roll"
    },
    {
    "alltime": False,
    "artist": "Sonic Animation",
    "country": "Australia",
    "id": "2039",
    "pollyear": 2002,
    "position": 74,
    "releaseyear": "2002",
    "track": "I'm a DJ"
    },
    {
    "alltime": False,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "2040",
    "pollyear": 2002,
    "position": 81,
    "releaseyear": "2002",
    "track": "You Think I Ain't Worth a Dollar"
    },
    {
    "alltime": False,
    "artist": "The Fergusons",
    "country": "Australia",
    "id": "2041",
    "pollyear": 2002,
    "position": 88,
    "releaseyear": "2002",
    "track": "Everything's Gone Bad"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "2042",
    "pollyear": 2002,
    "position": 94,
    "releaseyear": "2002",
    "track": "Arse Huggin' Pants"
    },
    {
    "alltime": False,
    "artist": "Jamie T",
    "country": "UK",
    "id": "2043",
    "pollyear": 2009,
    "position": 14,
    "releaseyear": "2009",
    "track": "Sticks 'n' Stones"
    },
    {
    "alltime": False,
    "artist": "Metric",
    "country": "Canada",
    "id": "2044",
    "pollyear": 2009,
    "position": 26,
    "releaseyear": "2009",
    "track": "Help I'm Alive"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "2045",
    "pollyear": 2009,
    "position": 28,
    "releaseyear": "2009",
    "track": "We Won't Run"
    },
    {
    "alltime": False,
    "artist": "Weezer",
    "country": "USA",
    "id": "2046",
    "pollyear": 2009,
    "position": 36,
    "releaseyear": "2009",
    "track": "(If You're Wondering If I Want You To) I Want You To"
    },
    {
    "alltime": False,
    "artist": "Calvin Harris",
    "country": "UK",
    "id": "2047",
    "pollyear": 2009,
    "position": 59,
    "releaseyear": "2009",
    "track": "I'm Not Alone"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "2048",
    "pollyear": 2009,
    "position": 72,
    "releaseyear": "2009",
    "track": "You've Changed"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "2049",
    "pollyear": 2009,
    "position": 77,
    "releaseyear": "2009",
    "track": "She's a Genius"
    },
    {
    "alltime": False,
    "artist": "Manchester Orchestra",
    "country": "USA",
    "id": "2050",
    "pollyear": 2009,
    "position": 91,
    "releaseyear": "2009",
    "track": "I've Got Friends"
    },
    {
    "alltime": True,
    "artist": "Guns N' Roses",
    "country": "USA",
    "id": "2051",
    "pollyear": 2009,
    "position": 49,
    "releaseyear": "1988",
    "track": "Sweet Child o' Mine"
    },
    {
    "alltime": True,
    "artist": "Crowded House",
    "country": "Australia",
    "id": "2052",
    "pollyear": 2009,
    "position": 50,
    "releaseyear": "1986",
    "track": "Don't Dream It's Over"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "2053",
    "pollyear": 2009,
    "position": 56,
    "releaseyear": "1994",
    "track": "Lover, You Should've Come Over"
    },
    {
    "alltime": False,
    "artist": "Cloud Control",
    "country": "Australia",
    "id": "2054",
    "pollyear": 2010,
    "position": 18,
    "releaseyear": "2010",
    "track": "There's Nothing in the Water We Can't Fight"
    },
    {
    "alltime": False,
    "artist": "Sparkadia",
    "country": "Australia",
    "id": "2055",
    "pollyear": 2010,
    "position": 24,
    "releaseyear": "2010",
    "track": "Talking Like I'm Falling Down Stairs"
    },
    {
    "alltime": False,
    "artist": "Gyroscope",
    "country": "Australia",
    "id": "2056",
    "pollyear": 2010,
    "position": 40,
    "releaseyear": "2010",
    "track": "Baby, I'm Gettin' Better"
    },
    {
    "alltime": False,
    "artist": "Ou Est Le Swimming Pool",
    "country": "UK",
    "id": "2057",
    "pollyear": 2010,
    "position": 61,
    "releaseyear": "2010",
    "track": "Jackson's Last Stand"
    },
    {
    "alltime": False,
    "artist": "Gypsy & the Cat",
    "country": "Australia",
    "id": "2058",
    "pollyear": 2010,
    "position": 71,
    "releaseyear": "2010",
    "track": "The Piper's Song"
    },
    {
    "alltime": False,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "2059",
    "pollyear": 2010,
    "position": 80,
    "releaseyear": "2010",
    "track": "Howlin' for You"
    },
    {
    "alltime": False,
    "artist": "The National",
    "country": "USA",
    "id": "2060",
    "pollyear": 2010,
    "position": 93,
    "releaseyear": "2010",
    "track": "Anyone's Ghost"
    },
    {
    "alltime": False,
    "artist": "4 Non Blondes",
    "country": "USA",
    "id": "2061",
    "pollyear": 1993,
    "position": 24,
    "releaseyear": "1993",
    "track": "What's Up?"
    },
    {
    "alltime": False,
    "artist": "The Cure",
    "country": "UK",
    "id": "2062",
    "pollyear": 1993,
    "position": 39,
    "releaseyear": "1993",
    "track": "Friday I'm in Love"
    },
    {
    "alltime": False,
    "artist": "Ween",
    "country": "USA",
    "id": "2063",
    "pollyear": 1993,
    "position": 40,
    "releaseyear": "1993",
    "track": "Push th' Little Daisies"
    },
    {
    "alltime": False,
    "artist": "Dave Graney 'n' the Coral Snakes",
    "country": "Australia",
    "id": "2064",
    "pollyear": 1993,
    "position": 48,
    "releaseyear": "1993",
    "track": "Night of the Wolverine"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2065",
    "pollyear": 1993,
    "position": 50,
    "releaseyear": "1993",
    "track": "Adam's Ribs"
    },
    {
    "alltime": False,
    "artist": "Dave Graney 'n' the Coral Snakes",
    "country": "Australia",
    "id": "2066",
    "pollyear": 1993,
    "position": 59,
    "releaseyear": "1993",
    "track": "You're Just too Hip Baby"
    },
    {
    "alltime": False,
    "artist": "Sub Sub",
    "country": "UK",
    "id": "2067",
    "pollyear": 1993,
    "position": 74,
    "releaseyear": "1993",
    "track": "Ain't No Love (Ain't No Use)"
    },
    {
    "alltime": False,
    "artist": "Custard",
    "country": "Australia",
    "id": "2068",
    "pollyear": 1998,
    "position": 3,
    "releaseyear": "1998",
    "track": "Girls Like That (Don't Go For Guys Like Us)"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "2069",
    "pollyear": 1998,
    "position": 14,
    "releaseyear": "1998",
    "track": "Josie (Everything's Gonna Be Fine)"
    },
    {
    "alltime": False,
    "artist": "Happyland",
    "country": "Australia",
    "id": "2070",
    "pollyear": 1998,
    "position": 28,
    "releaseyear": "1998",
    "track": "Don't You Know Who I Am"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2071",
    "pollyear": 1998,
    "position": 46,
    "releaseyear": "1998",
    "track": "Don't Wanna Be Left Out"
    },
    {
    "alltime": False,
    "artist": "Run-D.M.C. vs Jason Nevins",
    "country": "USA",
    "id": "2072",
    "pollyear": 1998,
    "position": 50,
    "releaseyear": "1998",
    "track": "It's Like That"
    },
    {
    "alltime": False,
    "artist": "Garbage",
    "country": "USA",
    "id": "2073",
    "pollyear": 1998,
    "position": 57,
    "releaseyear": "1998",
    "track": "I Think I'm Paranoid"
    },
    {
    "alltime": False,
    "artist": "Pauline Pantsdown",
    "country": "Australia",
    "id": "2074",
    "pollyear": 1998,
    "position": 58,
    "releaseyear": "1998",
    "track": "I Don't Like It"
    },
    {
    "alltime": False,
    "artist": "The Mavis's",
    "country": "Australia",
    "id": "2075",
    "pollyear": 1998,
    "position": 61,
    "releaseyear": "1998",
    "track": "Cry"
    },
    {
    "alltime": False,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "2076",
    "pollyear": 1998,
    "position": 79,
    "releaseyear": "1998",
    "track": "Don't Go Away"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "2077",
    "pollyear": 1998,
    "position": 86,
    "releaseyear": "1998",
    "track": "Mama's Trippin'"
    },
    {
    "alltime": False,
    "artist": "Evermore",
    "country": "New Zealand",
    "id": "2078",
    "pollyear": 2004,
    "position": 14,
    "releaseyear": "2004",
    "track": "It's Too Late"
    },
    {
    "alltime": False,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "2079",
    "pollyear": 2004,
    "position": 20,
    "releaseyear": "2004",
    "track": "Fucken Awesome"
    },
    {
    "alltime": False,
    "artist": "Jet",
    "country": "Australia",
    "id": "2080",
    "pollyear": 2004,
    "position": 24,
    "releaseyear": "2004",
    "track": "Look What You've Done"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "2081",
    "pollyear": 2004,
    "position": 25,
    "releaseyear": "2004",
    "track": "Treat Yo' Mama"
    },
    {
    "alltime": False,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "2082",
    "pollyear": 2004,
    "position": 27,
    "releaseyear": "2004",
    "track": "Don't U Eva"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "2083",
    "pollyear": 2004,
    "position": 47,
    "releaseyear": "2004",
    "track": "I Can't Give You What I Haven't Got"
    },
    {
    "alltime": False,
    "artist": "The Von Bondies",
    "country": "USA",
    "id": "2084",
    "pollyear": 2004,
    "position": 71,
    "releaseyear": "2004",
    "track": "C'mon C'mon"
    },
    {
    "alltime": False,
    "artist": "The Spazzys",
    "country": "Australia",
    "id": "2085",
    "pollyear": 2004,
    "position": 75,
    "releaseyear": "2004",
    "track": "Paco Doesn't Love Me"
    },
    {
    "alltime": False,
    "artist": "Little Birdy",
    "country": "Australia",
    "id": "2086",
    "pollyear": 2004,
    "position": 78,
    "releaseyear": "2004",
    "track": "Tonight's the Night"
    },
    {
    "alltime": False,
    "artist": "Fabienne Delsol",
    "country": "France",
    "id": "2087",
    "pollyear": 2004,
    "position": 100,
    "releaseyear": "2004",
    "track": "I'm Gonna Haunt You"
    },
    {
    "alltime": True,
    "artist": "The Stone Roses",
    "country": "UK",
    "id": "2088",
    "pollyear": 1990,
    "position": 6,
    "releaseyear": "1989",
    "track": "Fool's Gold"
    },
    {
    "alltime": True,
    "artist": "The B-52's",
    "country": "USA",
    "id": "2089",
    "pollyear": 1990,
    "position": 8,
    "releaseyear": "1978",
    "track": "Rock Lobster"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "2090",
    "pollyear": 1990,
    "position": 9,
    "releaseyear": "1987",
    "track": "It's The End Of The World"
    },
    {
    "alltime": True,
    "artist": "The Jam",
    "country": "UK",
    "id": "2091",
    "pollyear": 1990,
    "position": 10,
    "releaseyear": "1980",
    "track": "That's Entertainment"
    },
    {
    "alltime": True,
    "artist": "Sinead O'Connor",
    "country": "Ireland",
    "id": "2092",
    "pollyear": 1990,
    "position": 13,
    "releaseyear": "1987",
    "track": "Troy"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2093",
    "pollyear": 1990,
    "position": 23,
    "releaseyear": "1980",
    "track": "Boys Don't Cry"
    },
    {
    "alltime": True,
    "artist": "The Sundays",
    "country": "UK",
    "id": "2094",
    "pollyear": 1990,
    "position": 56,
    "releaseyear": "1989",
    "track": "Can't Be Sure"
    },
    {
    "alltime": True,
    "artist": "Sinead O'Connor",
    "country": "Ireland",
    "id": "2095",
    "pollyear": 1990,
    "position": 69,
    "releaseyear": "1990",
    "track": "Nothing Compares 2 U"
    },
    {
    "alltime": True,
    "artist": "The B-52's",
    "country": "USA",
    "id": "2096",
    "pollyear": 1990,
    "position": 88,
    "releaseyear": "1989",
    "track": "Love Shack"
    },
    {
    "alltime": True,
    "artist": "The B-52's",
    "country": "USA",
    "id": "2097",
    "pollyear": 1990,
    "position": 97,
    "releaseyear": "1989",
    "track": "Roam"
    },
    {
    "alltime": True,
    "artist": "Depeche Mode",
    "country": "UK",
    "id": "2098",
    "pollyear": 1990,
    "position": 100,
    "releaseyear": "1981",
    "track": "Just Can't Get Enough"
    },
    {
    "alltime": False,
    "artist": "Smash Mouth",
    "country": "USA",
    "id": "2099",
    "pollyear": 1997,
    "position": 11,
    "releaseyear": "1997",
    "track": "Walkin' on the Sun"
    },
    {
    "alltime": False,
    "artist": "Quindon Tarver/Lee Perry",
    "country": "USA",
    "id": "2100",
    "pollyear": 1997,
    "position": 16,
    "releaseyear": "1997",
    "track": "Everybody's Free (To Wear Sunscreen)"
    },
    {
    "alltime": False,
    "artist": "The Verve",
    "country": "UK",
    "id": "2101",
    "pollyear": 1997,
    "position": 22,
    "releaseyear": "1997",
    "track": "The Drugs Don't Work"
    },
    {
    "alltime": False,
    "artist": "Green Day",
    "country": "USA",
    "id": "2102",
    "pollyear": 1997,
    "position": 25,
    "releaseyear": "1997",
    "track": "Hitchin' a Ride"
    },
    {
    "alltime": False,
    "artist": "The Mavis's",
    "country": "Australia",
    "id": "2103",
    "pollyear": 1997,
    "position": 37,
    "releaseyear": "1997",
    "track": "Naughty Boy"
    },
    {
    "alltime": False,
    "artist": "The Bloodhound Gang",
    "country": "USA",
    "id": "2104",
    "pollyear": 1997,
    "position": 40,
    "releaseyear": "1997",
    "track": "Why's Everybody Always Pickin' On Me?"
    },
    {
    "alltime": False,
    "artist": "Ammonia",
    "country": "Australia",
    "id": "2105",
    "pollyear": 1997,
    "position": 43,
    "releaseyear": "1997",
    "track": "You're Not The Only One"
    },
    {
    "alltime": False,
    "artist": "Filter And The Crystal Method",
    "country": "USA",
    "id": "2106",
    "pollyear": 1997,
    "position": 47,
    "releaseyear": "1997",
    "track": "(Can't You) Trip Like I Do"
    },
    {
    "alltime": False,
    "artist": "Chemical Brothers",
    "country": "UK",
    "id": "2107",
    "pollyear": 1997,
    "position": 61,
    "releaseyear": "1997",
    "track": "Block Rockin' Beats"
    },
    {
    "alltime": False,
    "artist": "Live",
    "country": "USA",
    "id": "2108",
    "pollyear": 1997,
    "position": 73,
    "releaseyear": "1997",
    "track": "Lakini's Juice"
    },
    {
    "alltime": False,
    "artist": "Dave Graney",
    "country": "Australia",
    "id": "2109",
    "pollyear": 1997,
    "position": 84,
    "releaseyear": "1997",
    "track": "Feelin' Kinda Sporty"
    },
    {
    "alltime": False,
    "artist": "Blackeyed Susans",
    "country": "Australia",
    "id": "2110",
    "pollyear": 1997,
    "position": 86,
    "releaseyear": "1997",
    "track": "Smokin' Johnny Cash"
    },
    {
    "alltime": False,
    "artist": "Rebecca's Empire",
    "country": "Australia",
    "id": "2111",
    "pollyear": 1997,
    "position": 94,
    "releaseyear": "1997",
    "track": "Way Of All Things"
    },
    {
    "alltime": False,
    "artist": "Faithless",
    "country": "UK",
    "id": "2112",
    "pollyear": 1997,
    "position": 95,
    "releaseyear": "1997",
    "track": "Don't Leave"
    },
    {
    "alltime": False,
    "artist": "Basement Jaxx",
    "country": "UK",
    "id": "2113",
    "pollyear": 2001,
    "position": 4,
    "releaseyear": "2001",
    "track": "Where's Your Head At?"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "2114",
    "pollyear": 2001,
    "position": 17,
    "releaseyear": "2001",
    "track": "Rockin' The Suburbs"
    },
    {
    "alltime": False,
    "artist": "Ben Harper",
    "country": "USA",
    "id": "2115",
    "pollyear": 2001,
    "position": 22,
    "releaseyear": "2001",
    "track": "Drugs Don't Work"
    },
    {
    "alltime": False,
    "artist": "PJ Harvey/Thom Yorke",
    "country": "UK",
    "id": "2116",
    "pollyear": 2001,
    "position": 23,
    "releaseyear": "2001",
    "track": "This Mess We're In"
    },
    {
    "alltime": False,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "2117",
    "pollyear": 2001,
    "position": 42,
    "releaseyear": "2001",
    "track": "Duffy's Song (I Will Not Go Quietly)"
    },
    {
    "alltime": False,
    "artist": "Groove Armada",
    "country": "UK",
    "id": "2118",
    "pollyear": 2001,
    "position": 48,
    "releaseyear": "2001",
    "track": "Superstylin'"
    },
    {
    "alltime": False,
    "artist": "They Might Be Giants",
    "country": "USA",
    "id": "2119",
    "pollyear": 2001,
    "position": 52,
    "releaseyear": "2001",
    "track": "Man It's So Loud In Here"
    },
    {
    "alltime": False,
    "artist": "Lazaro's Dog",
    "country": "Australia",
    "id": "2120",
    "pollyear": 2001,
    "position": 82,
    "releaseyear": "2001",
    "track": "Home Entertainment System"
    },
    {
    "alltime": False,
    "artist": "Soko",
    "country": "France",
    "id": "2121",
    "pollyear": 2007,
    "position": 9,
    "releaseyear": "2007",
    "track": "I'll Kill Her"
    },
    {
    "alltime": False,
    "artist": "The Panics",
    "country": "Australia",
    "id": "2122",
    "pollyear": 2007,
    "position": 10,
    "releaseyear": "2007",
    "track": "Don't Fight It"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2123",
    "pollyear": 2007,
    "position": 12,
    "releaseyear": "2007",
    "track": "Let's Dance to Joy Division"
    },
    {
    "alltime": False,
    "artist": "Kisschasy",
    "country": "Australia",
    "id": "2124",
    "pollyear": 2007,
    "position": 32,
    "releaseyear": "2007",
    "track": "Opinions Won't Keep You Warm at Night"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2125",
    "pollyear": 2007,
    "position": 66,
    "releaseyear": "2007",
    "track": "I Don't Remember"
    },
    {
    "alltime": False,
    "artist": "The Presets",
    "country": "Australia",
    "id": "2126",
    "pollyear": 2008,
    "position": 8,
    "releaseyear": "2008",
    "track": "This Boy's in Love"
    },
    {
    "alltime": False,
    "artist": "The Ting Tings",
    "country": "UK",
    "id": "2127",
    "pollyear": 2008,
    "position": 9,
    "releaseyear": "2008",
    "track": "That's Not My Name"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "2128",
    "pollyear": 2008,
    "position": 16,
    "releaseyear": "2008",
    "track": "You Don't Know Me {ft. Regina Spektor}"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "2129",
    "pollyear": 2008,
    "position": 37,
    "releaseyear": "2008",
    "track": "I Said I'm Sorry"
    },
    {
    "alltime": False,
    "artist": "Ida Maria",
    "country": "Norway",
    "id": "2130",
    "pollyear": 2008,
    "position": 39,
    "releaseyear": "2008",
    "track": "I Like You So Much Better When You're Naked"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "2131",
    "pollyear": 2008,
    "position": 71,
    "releaseyear": "2008",
    "track": "One (Blake's Got a New Face)"
    },
    {
    "alltime": False,
    "artist": "Band of Horses",
    "country": "USA",
    "id": "2132",
    "pollyear": 2008,
    "position": 72,
    "releaseyear": "2008",
    "track": "No One's Gonna Love You"
    },
    {
    "alltime": False,
    "artist": "Black Kids",
    "country": "USA",
    "id": "2133",
    "pollyear": 2008,
    "position": 74,
    "releaseyear": "2008",
    "track": "I'm Not Gonna Teach Your Boyfriend How To Dance With You"
    },
    {
    "alltime": False,
    "artist": "Muph & Plutonic",
    "country": "Australia",
    "id": "2134",
    "pollyear": 2008,
    "position": 99,
    "releaseyear": "2008",
    "track": "Don't Worry About Nothin'"
    },
    {
    "alltime": False,
    "artist": "Dukes of Windsor",
    "country": "Australia",
    "id": "2135",
    "pollyear": 2008,
    "position": 100,
    "releaseyear": "2008",
    "track": "It's A War"
    },
    {
    "alltime": False,
    "artist": "Scissor Sisters",
    "country": "USA",
    "id": "2136",
    "pollyear": 2006,
    "position": 5,
    "releaseyear": "2006",
    "track": "I Don't Feel Like Dancin'"
    },
    {
    "alltime": False,
    "artist": "Bob Evans",
    "country": "Australia",
    "id": "2137",
    "pollyear": 2006,
    "position": 37,
    "releaseyear": "2006",
    "track": "Don't You Think It's Time"
    },
    {
    "alltime": False,
    "artist": "Eagles of Death Metal",
    "country": "USA",
    "id": "2138",
    "pollyear": 2006,
    "position": 54,
    "releaseyear": "2006",
    "track": "I Want You So Hard (Boy's Bad News)"
    },
    {
    "alltime": False,
    "artist": "Lily Allen",
    "country": "UK",
    "id": "2139",
    "pollyear": 2006,
    "position": 93,
    "releaseyear": "2006",
    "track": "Everything's Just Wonderful"
    },
    {
    "alltime": False,
    "artist": "Coolio",
    "country": "USA",
    "id": "2140",
    "pollyear": 1995,
    "position": 3,
    "releaseyear": "1995",
    "track": "Gangsta's Paradise"
    },
    {
    "alltime": False,
    "artist": "Bjork",
    "country": "Iceland",
    "id": "2141",
    "pollyear": 1995,
    "position": 5,
    "releaseyear": "1995",
    "track": "It's Oh So Quiet"
    },
    {
    "alltime": False,
    "artist": "TISM",
    "country": "Australia",
    "id": "2142",
    "pollyear": 1995,
    "position": 9,
    "releaseyear": "1995",
    "track": "(He'll Never Be An) Ol' Man River"
    },
    {
    "alltime": False,
    "artist": "Dave Graney 'n' The Coral Snakes",
    "country": "Australia",
    "id": "2143",
    "pollyear": 1995,
    "position": 16,
    "releaseyear": "1995",
    "track": "Rock 'n' Roll is where I hide"
    },
    {
    "alltime": False,
    "artist": "Primus",
    "country": "USA",
    "id": "2144",
    "pollyear": 1995,
    "position": 40,
    "releaseyear": "1995",
    "track": "Wynona's Big Brown Beaver"
    },
    {
    "alltime": False,
    "artist": "Teenage Fanclub",
    "country": "UK",
    "id": "2145",
    "pollyear": 1995,
    "position": 60,
    "releaseyear": "1995",
    "track": "Sparky's Dream"
    },
    {
    "alltime": False,
    "artist": "Rebecca's Empire",
    "country": "Australia",
    "id": "2146",
    "pollyear": 1995,
    "position": 62,
    "releaseyear": "1995",
    "track": "Empty"
    },
    {
    "alltime": False,
    "artist": "N-Trance",
    "country": "UK",
    "id": "2147",
    "pollyear": 1995,
    "position": 64,
    "releaseyear": "1995",
    "track": "Stayin' Alive"
    },
    {
    "alltime": False,
    "artist": "Dash Rip Rock",
    "country": "USA",
    "id": "2148",
    "pollyear": 1995,
    "position": 69,
    "releaseyear": "1995",
    "track": "(Let's Go) Smoke Some Pot"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "2149",
    "pollyear": 1995,
    "position": 70,
    "releaseyear": "1995",
    "track": "I'll Stick Around"
    },
    {
    "alltime": False,
    "artist": "The Caulfields",
    "country": "USA",
    "id": "2150",
    "pollyear": 1995,
    "position": 81,
    "releaseyear": "1995",
    "track": "Devil's Diary"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2151",
    "pollyear": 1995,
    "position": 84,
    "releaseyear": "1995",
    "track": "Cathy's Clown"
    },
    {
    "alltime": False,
    "artist": "Todd Snider",
    "country": "USA",
    "id": "2152",
    "pollyear": 1995,
    "position": 100,
    "releaseyear": "1995",
    "track": "Talkin' Seattle Grunge Rock Blues"
    },
    {
    "alltime": False,
    "artist": "The Eels",
    "country": "USA",
    "id": "2153",
    "pollyear": 2000,
    "position": 26,
    "releaseyear": "2000",
    "track": "Mr. E's Beautiful Blues"
    },
    {
    "alltime": False,
    "artist": "Spiller",
    "country": "Italy",
    "id": "2154",
    "pollyear": 2000,
    "position": 32,
    "releaseyear": "2000",
    "track": "Groovejet (If This Ain't Love)"
    },
    {
    "alltime": False,
    "artist": "Gomez",
    "country": "UK",
    "id": "2155",
    "pollyear": 2000,
    "position": 35,
    "releaseyear": "2000",
    "track": "We Haven't Turned Around"
    },
    {
    "alltime": False,
    "artist": "Sinead O'Connor",
    "country": "Ireland",
    "id": "2156",
    "pollyear": 2000,
    "position": 44,
    "releaseyear": "2000",
    "track": "Daddy I'm Fine"
    },
    {
    "alltime": False,
    "artist": "Sinead O'Connor",
    "country": "Ireland",
    "id": "2157",
    "pollyear": 2000,
    "position": 60,
    "releaseyear": "2000",
    "track": "No Man's Woman"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "2158",
    "pollyear": 2000,
    "position": 71,
    "releaseyear": "2000",
    "track": "Nothing's Wrong"
    },
    {
    "alltime": False,
    "artist": "Morcheeba",
    "country": "UK",
    "id": "2159",
    "pollyear": 2000,
    "position": 88,
    "releaseyear": "2000",
    "track": "Rome Wasn't Built In A Day"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "2160",
    "pollyear": 2003,
    "position": 23,
    "releaseyear": "2003",
    "track": "Who's Gonna Save Us?"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "2161",
    "pollyear": 2003,
    "position": 26,
    "releaseyear": "2003",
    "track": "Russell Crowe's Band"
    },
    {
    "alltime": False,
    "artist": "Ben Folds",
    "country": "USA",
    "id": "2162",
    "pollyear": 2003,
    "position": 27,
    "releaseyear": "2003",
    "track": "There's Always Someone Cooler Than You"
    },
    {
    "alltime": False,
    "artist": "Jane's Addiction",
    "country": "USA",
    "id": "2163",
    "pollyear": 2003,
    "position": 36,
    "releaseyear": "2003",
    "track": "Just Because"
    },
    {
    "alltime": False,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "2164",
    "pollyear": 2003,
    "position": 50,
    "releaseyear": "2003",
    "track": "Fisherman's Daughter"
    },
    {
    "alltime": False,
    "artist": "AFI",
    "country": "USA",
    "id": "2165",
    "pollyear": 2003,
    "position": 71,
    "releaseyear": "2003",
    "track": "Girl's Not Grey"
    },
    {
    "alltime": False,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2166",
    "pollyear": 2003,
    "position": 77,
    "releaseyear": "2003",
    "track": "Stumblin'"
    },
    {
    "alltime": False,
    "artist": "Gerling",
    "country": "Australia",
    "id": "2167",
    "pollyear": 2003,
    "position": 78,
    "releaseyear": "2003",
    "track": "Who's Ya Daddy?"
    },
    {
    "alltime": False,
    "artist": "Chicks On Speed",
    "country": "Germany",
    "id": "2168",
    "pollyear": 2003,
    "position": 84,
    "releaseyear": "2003",
    "track": "We Don't Play Guitars {ft. Peaches}"
    },
    {
    "alltime": False,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "2169",
    "pollyear": 2003,
    "position": 93,
    "releaseyear": "2003",
    "track": "I Just Don't Know What to Do with Myself"
    },
    {
    "alltime": False,
    "artist": "Blink-182",
    "country": "USA",
    "id": "2170",
    "pollyear": 1999,
    "position": 13,
    "releaseyear": "1999",
    "track": "What's My Age Again?"
    },
    {
    "alltime": False,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2171",
    "pollyear": 1999,
    "position": 15,
    "releaseyear": "1999",
    "track": "Ana's Song (Open Fire)"
    },
    {
    "alltime": False,
    "artist": "Madison Avenue",
    "country": "Australia",
    "id": "2172",
    "pollyear": 1999,
    "position": 22,
    "releaseyear": "1999",
    "track": "Don't Call Me Baby"
    },
    {
    "alltime": False,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "2173",
    "pollyear": 1999,
    "position": 52,
    "releaseyear": "1999",
    "track": "It Won't Last"
    },
    {
    "alltime": False,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "2174",
    "pollyear": 1999,
    "position": 64,
    "releaseyear": "1999",
    "track": "We're Going Out Tonight"
    },
    {
    "alltime": False,
    "artist": "Everlast",
    "country": "USA",
    "id": "2175",
    "pollyear": 1999,
    "position": 76,
    "releaseyear": "1999",
    "track": "What It's Like"
    },
    {
    "alltime": False,
    "artist": "Placebo",
    "country": "UK",
    "id": "2176",
    "pollyear": 1999,
    "position": 87,
    "releaseyear": "1999",
    "track": "You Don't Care About Us"
    },
    {
    "alltime": False,
    "artist": "The Offspring",
    "country": "USA",
    "id": "2177",
    "pollyear": 1999,
    "position": 97,
    "releaseyear": "1999",
    "track": "The Kids Aren't Alright"
    },
    {
    "alltime": False,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "2178",
    "pollyear": 2005,
    "position": 6,
    "releaseyear": "2005",
    "track": "Mind's Eye"
    },
    {
    "alltime": False,
    "artist": "Butterfingers",
    "country": "Australia",
    "id": "2179",
    "pollyear": 2005,
    "position": 11,
    "releaseyear": "2005",
    "track": "Figjam (Fuck I'm Good, Just Ask Me)"
    },
    {
    "alltime": False,
    "artist": "Kisschasy",
    "country": "Australia",
    "id": "2180",
    "pollyear": 2005,
    "position": 22,
    "releaseyear": "2005",
    "track": "Do-Do's & Whoa-Oh's"
    },
    {
    "alltime": False,
    "artist": "The Living End",
    "country": "Australia",
    "id": "2181",
    "pollyear": 2005,
    "position": 49,
    "releaseyear": "2005",
    "track": "What's on Your Radio"
    },
    {
    "alltime": False,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "2182",
    "pollyear": 2005,
    "position": 53,
    "releaseyear": "2005",
    "track": "We're All In This Together"
    },
    {
    "alltime": False,
    "artist": "Architecture in Helsinki",
    "country": "Australia",
    "id": "2183",
    "pollyear": 2005,
    "position": 56,
    "releaseyear": "2005",
    "track": "It'5!"
    },
    {
    "alltime": False,
    "artist": "The Bedroom Philosopher",
    "country": "Australia",
    "id": "2184",
    "pollyear": 2005,
    "position": 72,
    "releaseyear": "2005",
    "track": "I'm So Postmodern"
    },
    {
    "alltime": False,
    "artist": "The Beautiful Girls",
    "country": "Australia",
    "id": "2185",
    "pollyear": 2005,
    "position": 81,
    "releaseyear": "2005",
    "track": "Let's Take the Long Way Home"
    },
    {
    "alltime": False,
    "artist": "The Herd",
    "country": "Australia",
    "id": "2186",
    "pollyear": 2005,
    "position": 87,
    "releaseyear": "2005",
    "track": "We Can't Hear You"
    },
    {
    "alltime": False,
    "artist": "Underground Lovers",
    "country": "Australia",
    "id": "2187",
    "pollyear": 1994,
    "position": 19,
    "releaseyear": "1994",
    "track": "Losin' It"
    },
    {
    "alltime": False,
    "artist": "Youssou N'dour & Neneh Cherry",
    "country": "Senegal",
    "id": "2188",
    "pollyear": 1994,
    "position": 26,
    "releaseyear": "1994",
    "track": "7 Seconds"
    },
    {
    "alltime": False,
    "artist": "Rebecca's Empire",
    "country": "Australia",
    "id": "2189",
    "pollyear": 1994,
    "position": 38,
    "releaseyear": "1994",
    "track": "Atomic Electric"
    },
    {
    "alltime": False,
    "artist": "Pop Will Eat Itself",
    "country": "UK",
    "id": "2190",
    "pollyear": 1994,
    "position": 58,
    "releaseyear": "1994",
    "track": "Everything's Cool"
    },
    {
    "alltime": False,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "2191",
    "pollyear": 1994,
    "position": 70,
    "releaseyear": "1994",
    "track": "What's The Frequency Kenneth?"
    },
    {
    "alltime": False,
    "artist": "PM Dawn",
    "country": "USA",
    "id": "2192",
    "pollyear": 1994,
    "position": 75,
    "releaseyear": "1994",
    "track": "You Got Me Floatin'"
    },
    {
    "alltime": False,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2193",
    "pollyear": 1994,
    "position": 77,
    "releaseyear": "1994",
    "track": "Jaimme's Got A Gal"
    },
    {
    "alltime": False,
    "artist": "Dave Graney 'n' the Coral Snakes",
    "country": "Australia",
    "id": "2194",
    "pollyear": 1994,
    "position": 79,
    "releaseyear": "1994",
    "track": "I'm Gonna Release Your Soul"
    },
    {
    "alltime": True,
    "artist": "The Jam",
    "country": "UK",
    "id": "2195",
    "pollyear": 1989,
    "position": 4,
    "releaseyear": "1980",
    "track": "That's Entertainment"
    },
    {
    "alltime": True,
    "artist": "The B-52's",
    "country": "USA",
    "id": "2196",
    "pollyear": 1989,
    "position": 14,
    "releaseyear": "1978",
    "track": "Rock Lobster"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "2197",
    "pollyear": 1989,
    "position": 22,
    "releaseyear": "1987",
    "track": "It's The End Of The World As We Know It"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2198",
    "pollyear": 1989,
    "position": 29,
    "releaseyear": "1979",
    "track": "Boys Don't Cry"
    },
    {
    "alltime": True,
    "artist": "Sinead O'Connor",
    "country": "Ireland",
    "id": "2199",
    "pollyear": 1989,
    "position": 41,
    "releaseyear": "1987",
    "track": "Troy"
    },
    {
    "alltime": True,
    "artist": "The Saints",
    "country": "Australia",
    "id": "2200",
    "pollyear": 1989,
    "position": 51,
    "releaseyear": "1976",
    "track": "(I'm) Stranded"
    },
    {
    "alltime": False,
    "artist": "Gotye",
    "country": "Australia",
    "id": "2201",
    "pollyear": 2011,
    "position": 1,
    "releaseyear": "2011",
    "track": "Somebody That I Used to Know {ft. Kimbra}"
    },
    {
    "alltime": False,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "2202",
    "pollyear": 2011,
    "position": 2,
    "releaseyear": "2011",
    "track": "Lonely Boy"
    },
    {
    "alltime": False,
    "artist": "Matt Corby",
    "country": "Australia",
    "id": "2203",
    "pollyear": 2011,
    "position": 3,
    "releaseyear": "2011",
    "track": "Brother"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "2204",
    "pollyear": 2011,
    "position": 4,
    "releaseyear": "2011",
    "track": "Feeding Line"
    },
    {
    "alltime": False,
    "artist": "M83",
    "country": "France",
    "id": "2205",
    "pollyear": 2011,
    "position": 5,
    "releaseyear": "2011",
    "track": "Midnight City"
    },
    {
    "alltime": False,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2206",
    "pollyear": 2011,
    "position": 6,
    "releaseyear": "2011",
    "track": "Video Games"
    },
    {
    "alltime": False,
    "artist": "San Cisco",
    "country": "Australia",
    "id": "2207",
    "pollyear": 2011,
    "position": 7,
    "releaseyear": "2011",
    "track": "Awkward"
    },
    {
    "alltime": False,
    "artist": "360",
    "country": "Australia",
    "id": "2208",
    "pollyear": 2011,
    "position": 8,
    "releaseyear": "2011",
    "track": "Boys Like You {ft. Gossling}"
    },
    {
    "alltime": False,
    "artist": "The Jezabels",
    "country": "Australia",
    "id": "2209",
    "pollyear": 2011,
    "position": 9,
    "releaseyear": "2011",
    "track": "Endless Summer"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2210",
    "pollyear": 2011,
    "position": 10,
    "releaseyear": "2011",
    "track": "I Love It {ft. Sia}"
    },
    {
    "alltime": False,
    "artist": "Calvin Harris",
    "country": "UK",
    "id": "2211",
    "pollyear": 2011,
    "position": 11,
    "releaseyear": "2011",
    "track": "Feel So Close"
    },
    {
    "alltime": False,
    "artist": "Architecture in Helsinki",
    "country": "Australia",
    "id": "2212",
    "pollyear": 2011,
    "position": 12,
    "releaseyear": "2011",
    "track": "Contact High"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "2213",
    "pollyear": 2011,
    "position": 13,
    "releaseyear": "2011",
    "track": "Shake It Out"
    },
    {
    "alltime": False,
    "artist": "Foster the People",
    "country": "USA",
    "id": "2214",
    "pollyear": 2011,
    "position": 14,
    "releaseyear": "2011",
    "track": "Call It What You Want"
    },
    {
    "alltime": False,
    "artist": "Foster the People",
    "country": "USA",
    "id": "2215",
    "pollyear": 2011,
    "position": 15,
    "releaseyear": "2011",
    "track": "Helena Beat"
    },
    {
    "alltime": False,
    "artist": "Grouplove",
    "country": "USA",
    "id": "2216",
    "pollyear": 2011,
    "position": 16,
    "releaseyear": "2011",
    "track": "Tongue Tied"
    },
    {
    "alltime": False,
    "artist": "Seeker Lover Keeper",
    "country": "Australia",
    "id": "2217",
    "pollyear": 2011,
    "position": 17,
    "releaseyear": "2011",
    "track": "Even Though I'm a Woman"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2218",
    "pollyear": 2011,
    "position": 18,
    "releaseyear": "2011",
    "track": "Jump into the Fog"
    },
    {
    "alltime": False,
    "artist": "Nero",
    "country": "UK",
    "id": "2219",
    "pollyear": 2011,
    "position": 19,
    "releaseyear": "2011",
    "track": "Promises"
    },
    {
    "alltime": False,
    "artist": "Bluejuice",
    "country": "Australia",
    "id": "2220",
    "pollyear": 2011,
    "position": 20,
    "releaseyear": "2011",
    "track": "Act Yr Age"
    },
    {
    "alltime": False,
    "artist": "Skrillex",
    "country": "USA",
    "id": "2221",
    "pollyear": 2011,
    "position": 21,
    "releaseyear": "2011",
    "track": "Scary Monsters and Nice Sprites"
    },
    {
    "alltime": False,
    "artist": "Snakadaktal",
    "country": "Australia",
    "id": "2222",
    "pollyear": 2011,
    "position": 22,
    "releaseyear": "2011",
    "track": "Air"
    },
    {
    "alltime": False,
    "artist": "Emma Louise",
    "country": "Australia",
    "id": "2223",
    "pollyear": 2011,
    "position": 23,
    "releaseyear": "2011",
    "track": "Jungle"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2224",
    "pollyear": 2011,
    "position": 24,
    "releaseyear": "2011",
    "track": "1996"
    },
    {
    "alltime": False,
    "artist": "Kimbra",
    "country": "New Zealand",
    "id": "2225",
    "pollyear": 2011,
    "position": 25,
    "releaseyear": "2011",
    "track": "Cameo Lover"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2226",
    "pollyear": 2011,
    "position": 26,
    "releaseyear": "2011",
    "track": "Techno Fan"
    },
    {
    "alltime": False,
    "artist": "Example",
    "country": "UK",
    "id": "2227",
    "pollyear": 2011,
    "position": 27,
    "releaseyear": "2011",
    "track": "Changed the Way You Kiss Me"
    },
    {
    "alltime": False,
    "artist": "Owl Eyes",
    "country": "Australia",
    "id": "2228",
    "pollyear": 2011,
    "position": 28,
    "releaseyear": "2011",
    "track": "Pumped Up Kicks {Like a Version}"
    },
    {
    "alltime": False,
    "artist": "Drapht",
    "country": "Australia",
    "id": "2229",
    "pollyear": 2011,
    "position": 29,
    "releaseyear": "2011",
    "track": "Sing It (The Life of Riley)"
    },
    {
    "alltime": False,
    "artist": "Calvin Harris",
    "country": "UK",
    "id": "2230",
    "pollyear": 2011,
    "position": 30,
    "releaseyear": "2011",
    "track": "Bounce {ft. Kelis}"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2231",
    "pollyear": 2011,
    "position": 31,
    "releaseyear": "2011",
    "track": "It's Nice to Be Alive"
    },
    {
    "alltime": False,
    "artist": "Noah & the Whale",
    "country": "UK",
    "id": "2232",
    "pollyear": 2011,
    "position": 32,
    "releaseyear": "2011",
    "track": "L.I.F.E.G.O.E.S.O.N."
    },
    {
    "alltime": False,
    "artist": "Jay-Z & Kanye West",
    "country": "USA",
    "id": "2233",
    "pollyear": 2011,
    "position": 33,
    "releaseyear": "2011",
    "track": "Otis {ft. Otis Redding}"
    },
    {
    "alltime": False,
    "artist": "Gotye",
    "country": "Australia",
    "id": "2234",
    "pollyear": 2011,
    "position": 34,
    "releaseyear": "2011",
    "track": "I Feel Better"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "2235",
    "pollyear": 2011,
    "position": 35,
    "releaseyear": "2011",
    "track": "Cigarettes"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "2236",
    "pollyear": 2011,
    "position": 36,
    "releaseyear": "2011",
    "track": "No Light, No Light"
    },
    {
    "alltime": False,
    "artist": "360",
    "country": "Australia",
    "id": "2237",
    "pollyear": 2011,
    "position": 37,
    "releaseyear": "2011",
    "track": "Killer"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2238",
    "pollyear": 2011,
    "position": 38,
    "releaseyear": "2011",
    "track": "All I Want Is You"
    },
    {
    "alltime": False,
    "artist": "Benny Benassi",
    "country": "Italy",
    "id": "2239",
    "pollyear": 2011,
    "position": 39,
    "releaseyear": "2011",
    "track": "Cinema {ft. Gary Go} {Skrillex Remix}"
    },
    {
    "alltime": False,
    "artist": "Foster The People",
    "country": "USA",
    "id": "2240",
    "pollyear": 2011,
    "position": 40,
    "releaseyear": "2011",
    "track": "Houdini"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "2241",
    "pollyear": 2011,
    "position": 41,
    "releaseyear": "2011",
    "track": "Under Cover of Darkness"
    },
    {
    "alltime": False,
    "artist": "Florence and the Machine",
    "country": "UK",
    "id": "2242",
    "pollyear": 2011,
    "position": 42,
    "releaseyear": "2011",
    "track": "What the Water Gave Me"
    },
    {
    "alltime": False,
    "artist": "Grouplove",
    "country": "USA",
    "id": "2243",
    "pollyear": 2011,
    "position": 43,
    "releaseyear": "2011",
    "track": "Itchin' on a Photograph"
    },
    {
    "alltime": False,
    "artist": "Hermitude",
    "country": "Australia",
    "id": "2244",
    "pollyear": 2011,
    "position": 44,
    "releaseyear": "2011",
    "track": "Speak of the Devil"
    },
    {
    "alltime": False,
    "artist": "The Kooks",
    "country": "UK",
    "id": "2245",
    "pollyear": 2011,
    "position": 45,
    "releaseyear": "2011",
    "track": "Junk of the Heart (Happy)"
    },
    {
    "alltime": False,
    "artist": "Active Child",
    "country": "USA",
    "id": "2246",
    "pollyear": 2011,
    "position": 46,
    "releaseyear": "2011",
    "track": "Hanging On"
    },
    {
    "alltime": False,
    "artist": "Sparkadia",
    "country": "Australia",
    "id": "2247",
    "pollyear": 2011,
    "position": 47,
    "releaseyear": "2011",
    "track": "Mary"
    },
    {
    "alltime": False,
    "artist": "Art vs. Science",
    "country": "Australia",
    "id": "2248",
    "pollyear": 2011,
    "position": 48,
    "releaseyear": "2011",
    "track": "A.I.M. Fire!"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "2249",
    "pollyear": 2011,
    "position": 49,
    "releaseyear": "2011",
    "track": "Milk & Sticks"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "2250",
    "pollyear": 2011,
    "position": 50,
    "releaseyear": "2011",
    "track": "Part Time Believer"
    },
    {
    "alltime": False,
    "artist": "The Drums",
    "country": "USA",
    "id": "2251",
    "pollyear": 2011,
    "position": 51,
    "releaseyear": "2011",
    "track": "Money"
    },
    {
    "alltime": False,
    "artist": "Kimbra",
    "country": "New Zealand",
    "id": "2252",
    "pollyear": 2011,
    "position": 52,
    "releaseyear": "2011",
    "track": "Good Intent"
    },
    {
    "alltime": False,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "2253",
    "pollyear": 2011,
    "position": 53,
    "releaseyear": "2011",
    "track": "Holocene"
    },
    {
    "alltime": False,
    "artist": "The Grates",
    "country": "Australia",
    "id": "2254",
    "pollyear": 2011,
    "position": 54,
    "releaseyear": "2011",
    "track": "Turn Me On"
    },
    {
    "alltime": False,
    "artist": "Architecture In Helsinki",
    "country": "Australia",
    "id": "2255",
    "pollyear": 2011,
    "position": 55,
    "releaseyear": "2011",
    "track": "Escapee"
    },
    {
    "alltime": False,
    "artist": "Sparkadia",
    "country": "Australia",
    "id": "2256",
    "pollyear": 2011,
    "position": 56,
    "releaseyear": "2011",
    "track": "China"
    },
    {
    "alltime": False,
    "artist": "The Rubens",
    "country": "Australia",
    "id": "2257",
    "pollyear": 2011,
    "position": 57,
    "releaseyear": "2011",
    "track": "Lay It Down"
    },
    {
    "alltime": False,
    "artist": "Lykke Li",
    "country": "Sweden",
    "id": "2258",
    "pollyear": 2011,
    "position": 58,
    "releaseyear": "2011",
    "track": "I Follow Rivers"
    },
    {
    "alltime": False,
    "artist": "Washington",
    "country": "Australia",
    "id": "2259",
    "pollyear": 2011,
    "position": 59,
    "releaseyear": "2011",
    "track": "Holy Moses"
    },
    {
    "alltime": False,
    "artist": "Joe Goddard",
    "country": "UK",
    "id": "2260",
    "pollyear": 2011,
    "position": 60,
    "releaseyear": "2011",
    "track": "Gabriel {ft. Valentina}"
    },
    {
    "alltime": False,
    "artist": "Radiohead",
    "country": "UK",
    "id": "2261",
    "pollyear": 2011,
    "position": 61,
    "releaseyear": "2011",
    "track": "Lotus Flower"
    },
    {
    "alltime": False,
    "artist": "Stonefield",
    "country": "Australia",
    "id": "2262",
    "pollyear": 2011,
    "position": 62,
    "releaseyear": "2011",
    "track": "Black Water Rising"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "2263",
    "pollyear": 2011,
    "position": 63,
    "releaseyear": "2011",
    "track": "Rope"
    },
    {
    "alltime": False,
    "artist": "Owl Eyes",
    "country": "Australia",
    "id": "2264",
    "pollyear": 2011,
    "position": 64,
    "releaseyear": "2011",
    "track": "Raiders"
    },
    {
    "alltime": False,
    "artist": "Kasabian",
    "country": "UK",
    "id": "2265",
    "pollyear": 2011,
    "position": 65,
    "releaseyear": "2011",
    "track": "Re-Wired"
    },
    {
    "alltime": False,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "2266",
    "pollyear": 2011,
    "position": 66,
    "releaseyear": "2011",
    "track": "Perth"
    },
    {
    "alltime": False,
    "artist": "New Navy",
    "country": "Australia",
    "id": "2267",
    "pollyear": 2011,
    "position": 67,
    "releaseyear": "2011",
    "track": "Zimbabwe"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "2268",
    "pollyear": 2011,
    "position": 68,
    "releaseyear": "2011",
    "track": "Don't Sit Down 'Cause I've Moved Your Chair"
    },
    {
    "alltime": False,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "2269",
    "pollyear": 2011,
    "position": 69,
    "releaseyear": "2011",
    "track": "Calgary"
    },
    {
    "alltime": False,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "2270",
    "pollyear": 2011,
    "position": 70,
    "releaseyear": "2011",
    "track": "She's Like a Comet"
    },
    {
    "alltime": False,
    "artist": "Luke Million",
    "country": "Australia",
    "id": "2271",
    "pollyear": 2011,
    "position": 71,
    "releaseyear": "2011",
    "track": "Arnold"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2272",
    "pollyear": 2011,
    "position": 72,
    "releaseyear": "2011",
    "track": "Foreign Language {ft. Jess Higgs}"
    },
    {
    "alltime": False,
    "artist": "Skrillex",
    "country": "USA",
    "id": "2273",
    "pollyear": 2011,
    "position": 73,
    "releaseyear": "2011",
    "track": "First of the Year (Equinox)"
    },
    {
    "alltime": False,
    "artist": "Drapht",
    "country": "Australia",
    "id": "2274",
    "pollyear": 2011,
    "position": 74,
    "releaseyear": "2011",
    "track": "Bali Party {ft. N'fa}"
    },
    {
    "alltime": False,
    "artist": "Example & Skream",
    "country": "UK",
    "id": "2275",
    "pollyear": 2011,
    "position": 75,
    "releaseyear": "2011",
    "track": "Shot Yourself In the Foot Again"
    },
    {
    "alltime": False,
    "artist": "Redcoats",
    "country": "Australia",
    "id": "2276",
    "pollyear": 2011,
    "position": 76,
    "releaseyear": "2011",
    "track": "Dreamshaker"
    },
    {
    "alltime": False,
    "artist": "Metronomy",
    "country": "UK",
    "id": "2277",
    "pollyear": 2011,
    "position": 77,
    "releaseyear": "2011",
    "track": "The Look"
    },
    {
    "alltime": False,
    "artist": "Husky",
    "country": "Australia",
    "id": "2278",
    "pollyear": 2011,
    "position": 78,
    "releaseyear": "2011",
    "track": "History's Door"
    },
    {
    "alltime": False,
    "artist": "SBTRKT",
    "country": "UK",
    "id": "2279",
    "pollyear": 2011,
    "position": 79,
    "releaseyear": "2011",
    "track": "Wildfire {ft. Little Dragon}"
    },
    {
    "alltime": False,
    "artist": "Pnau",
    "country": "Australia",
    "id": "2280",
    "pollyear": 2011,
    "position": 80,
    "releaseyear": "2011",
    "track": "The Truth"
    },
    {
    "alltime": False,
    "artist": "Busby Marou",
    "country": "Australia",
    "id": "2281",
    "pollyear": 2011,
    "position": 81,
    "releaseyear": "2011",
    "track": "Biding My Time"
    },
    {
    "alltime": False,
    "artist": "Little Dragon",
    "country": "Sweden",
    "id": "2282",
    "pollyear": 2011,
    "position": 82,
    "releaseyear": "2011",
    "track": "Ritual Union"
    },
    {
    "alltime": False,
    "artist": "The Kills",
    "country": "UK",
    "id": "2283",
    "pollyear": 2011,
    "position": 83,
    "releaseyear": "2011",
    "track": "Future Starts Slow"
    },
    {
    "alltime": False,
    "artist": "360",
    "country": "Australia",
    "id": "2284",
    "pollyear": 2011,
    "position": 84,
    "releaseyear": "2011",
    "track": "Throw It Away {ft. Josh Pyke}"
    },
    {
    "alltime": False,
    "artist": "Cosmo Jarvis",
    "country": "UK",
    "id": "2285",
    "pollyear": 2011,
    "position": 85,
    "releaseyear": "2011",
    "track": "Gay Pirates"
    },
    {
    "alltime": False,
    "artist": "Seeker Lover Keeper",
    "country": "Australia",
    "id": "2286",
    "pollyear": 2011,
    "position": 86,
    "releaseyear": "2011",
    "track": "Light All My Lights"
    },
    {
    "alltime": False,
    "artist": "Gotye",
    "country": "Australia",
    "id": "2287",
    "pollyear": 2011,
    "position": 87,
    "releaseyear": "2011",
    "track": "In Your Light"
    },
    {
    "alltime": False,
    "artist": "Bombay Bicycle Club",
    "country": "UK",
    "id": "2288",
    "pollyear": 2011,
    "position": 88,
    "releaseyear": "2011",
    "track": "Shuffle"
    },
    {
    "alltime": False,
    "artist": "Beirut",
    "country": "USA",
    "id": "2289",
    "pollyear": 2011,
    "position": 89,
    "releaseyear": "2011",
    "track": "Santa Fe"
    },
    {
    "alltime": False,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "2290",
    "pollyear": 2011,
    "position": 90,
    "releaseyear": "2011",
    "track": "Make Some Noise"
    },
    {
    "alltime": False,
    "artist": "City and Colour",
    "country": "Canada",
    "id": "2291",
    "pollyear": 2011,
    "position": 91,
    "releaseyear": "2011",
    "track": "Fragile Bird"
    },
    {
    "alltime": False,
    "artist": "James Blake",
    "country": "UK",
    "id": "2292",
    "pollyear": 2011,
    "position": 92,
    "releaseyear": "2011",
    "track": "The Wilhelm Scream"
    },
    {
    "alltime": False,
    "artist": "Kimbra",
    "country": "New Zealand",
    "id": "2293",
    "pollyear": 2011,
    "position": 93,
    "releaseyear": "2011",
    "track": "Two Way Street"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2294",
    "pollyear": 2011,
    "position": 94,
    "releaseyear": "2011",
    "track": "Our Perfect Disease"
    },
    {
    "alltime": False,
    "artist": "Grouplove",
    "country": "USA",
    "id": "2295",
    "pollyear": 2011,
    "position": 95,
    "releaseyear": "2011",
    "track": "Naked Kids"
    },
    {
    "alltime": False,
    "artist": "The Strokes",
    "country": "USA",
    "id": "2296",
    "pollyear": 2011,
    "position": 96,
    "releaseyear": "2011",
    "track": "Machu Picchu"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "2297",
    "pollyear": 2011,
    "position": 97,
    "releaseyear": "2011",
    "track": "Arlandria"
    },
    {
    "alltime": False,
    "artist": "Jay-Z & Kanye West",
    "country": "USA",
    "id": "2298",
    "pollyear": 2011,
    "position": 98,
    "releaseyear": "2011",
    "track": "Niggas in Paris"
    },
    {
    "alltime": False,
    "artist": "The Beards",
    "country": "Australia",
    "id": "2299",
    "pollyear": 2011,
    "position": 99,
    "releaseyear": "2011",
    "track": "You Should Consider Having Sex with a Bearded Man"
    },
    {
    "alltime": False,
    "artist": "Mr Little Jeans",
    "country": "Norway",
    "id": "2300",
    "pollyear": 2011,
    "position": 100,
    "releaseyear": "2011",
    "track": "The Suburbs"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2302",
    "pollyear": 2011,
    "position": 1,
    "releaseyear": "",
    "track": "Odyssey Number Five"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2303",
    "pollyear": 2011,
    "position": 2,
    "releaseyear": "",
    "track": "Frogstomp"
    },
    {
    "alltime": True,
    "artist": "AC/DC",
    "country": "Australia",
    "id": "2304",
    "pollyear": 2011,
    "position": 3,
    "releaseyear": "",
    "track": "Back in Black"
    },
    {
    "alltime": True,
    "artist": "The Living End",
    "country": "Australia",
    "id": "2305",
    "pollyear": 2011,
    "position": 4,
    "releaseyear": "",
    "track": "The Living End"
    },
    {
    "alltime": True,
    "artist": "INXS",
    "country": "Australia",
    "id": "2306",
    "pollyear": 2011,
    "position": 5,
    "releaseyear": "",
    "track": "Kick"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2307",
    "pollyear": 2011,
    "position": 6,
    "releaseyear": "",
    "track": "Internationalist"
    },
    {
    "alltime": True,
    "artist": "The Presets",
    "country": "Australia",
    "id": "2308",
    "pollyear": 2011,
    "position": 7,
    "releaseyear": "",
    "track": "Apocalypso"
    },
    {
    "alltime": True,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "2309",
    "pollyear": 2011,
    "position": 8,
    "releaseyear": "",
    "track": "Wolfmother"
    },
    {
    "alltime": True,
    "artist": "The Avalanches",
    "country": "Australia",
    "id": "2310",
    "pollyear": 2011,
    "position": 9,
    "releaseyear": "",
    "track": "Since I Left You"
    },
    {
    "alltime": True,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "2311",
    "pollyear": 2011,
    "position": 10,
    "releaseyear": "",
    "track": "Unit"
    },
    {
    "alltime": True,
    "artist": "Gotye",
    "country": "Australia",
    "id": "2312",
    "pollyear": 2011,
    "position": 11,
    "releaseyear": "",
    "track": "Like Drawing Blood"
    },
    {
    "alltime": True,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "2313",
    "pollyear": 2011,
    "position": 12,
    "releaseyear": "",
    "track": "Guide to Better Living"
    },
    {
    "alltime": True,
    "artist": "Crowded House",
    "country": "Australia",
    "id": "2314",
    "pollyear": 2011,
    "position": 13,
    "releaseyear": "",
    "track": "Crowded House"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2315",
    "pollyear": 2011,
    "position": 14,
    "releaseyear": "",
    "track": "Vulture Street"
    },
    {
    "alltime": True,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "2316",
    "pollyear": 2011,
    "position": 15,
    "releaseyear": "",
    "track": "Slightly Odway"
    },
    {
    "alltime": True,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2317",
    "pollyear": 2011,
    "position": 16,
    "releaseyear": "",
    "track": "The Hard Road"
    },
    {
    "alltime": True,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "2318",
    "pollyear": 2011,
    "position": 17,
    "releaseyear": "",
    "track": "Eternal Nightcap"
    },
    {
    "alltime": True,
    "artist": "Crowded House",
    "country": "Australia",
    "id": "2319",
    "pollyear": 2011,
    "position": 18,
    "releaseyear": "",
    "track": "Woodface"
    },
    {
    "alltime": True,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2320",
    "pollyear": 2011,
    "position": 19,
    "releaseyear": "",
    "track": "Innerspeaker"
    },
    {
    "alltime": True,
    "artist": "The Temper Trap",
    "country": "Australia",
    "id": "2321",
    "pollyear": 2011,
    "position": 20,
    "releaseyear": "",
    "track": "Conditions"
    },
    {
    "alltime": True,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "2322",
    "pollyear": 2011,
    "position": 21,
    "releaseyear": "",
    "track": "10,9,8,7,6,5,4,3,2,1"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2323",
    "pollyear": 2011,
    "position": 22,
    "releaseyear": "",
    "track": "Diorama"
    },
    {
    "alltime": True,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2324",
    "pollyear": 2011,
    "position": 23,
    "releaseyear": "",
    "track": "The Calling"
    },
    {
    "alltime": True,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "2325",
    "pollyear": 2011,
    "position": 24,
    "releaseyear": "",
    "track": "Sunrise Over Sea"
    },
    {
    "alltime": True,
    "artist": "Jet",
    "country": "Australia",
    "id": "2326",
    "pollyear": 2011,
    "position": 25,
    "releaseyear": "",
    "track": "Get Born"
    },
    {
    "alltime": True,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2327",
    "pollyear": 2011,
    "position": 26,
    "releaseyear": "",
    "track": "Hourly, Daily"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2328",
    "pollyear": 2011,
    "position": 27,
    "releaseyear": "",
    "track": "Neon Ballroom"
    },
    {
    "alltime": True,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "2329",
    "pollyear": 2011,
    "position": 28,
    "releaseyear": "",
    "track": "The Cat Empire"
    },
    {
    "alltime": True,
    "artist": "Missy Higgins",
    "country": "Australia",
    "id": "2330",
    "pollyear": 2011,
    "position": 29,
    "releaseyear": "",
    "track": "The Sound of White"
    },
    {
    "alltime": True,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "2331",
    "pollyear": 2011,
    "position": 30,
    "releaseyear": "",
    "track": "Themata"
    },
    {
    "alltime": True,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "2332",
    "pollyear": 2011,
    "position": 31,
    "releaseyear": "",
    "track": "Down the Way"
    },
    {
    "alltime": True,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "2333",
    "pollyear": 2011,
    "position": 32,
    "releaseyear": "",
    "track": "Universes"
    },
    {
    "alltime": True,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "2334",
    "pollyear": 2011,
    "position": 33,
    "releaseyear": "",
    "track": "Diesel and Dust"
    },
    {
    "alltime": True,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "2335",
    "pollyear": 2011,
    "position": 34,
    "releaseyear": "",
    "track": "Memories & Dust"
    },
    {
    "alltime": True,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2336",
    "pollyear": 2011,
    "position": 35,
    "releaseyear": "",
    "track": "Hi Fi Way"
    },
    {
    "alltime": True,
    "artist": "Cut Copy",
    "country": "Australia",
    "id": "2337",
    "pollyear": 2011,
    "position": 36,
    "releaseyear": "",
    "track": "In Ghost Colours"
    },
    {
    "alltime": True,
    "artist": "The Vines",
    "country": "Australia",
    "id": "2338",
    "pollyear": 2011,
    "position": 37,
    "releaseyear": "",
    "track": "Highly Evolved"
    },
    {
    "alltime": True,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "2339",
    "pollyear": 2011,
    "position": 38,
    "releaseyear": "",
    "track": "A Book Like This"
    },
    {
    "alltime": True,
    "artist": "Birds of Tokyo",
    "country": "Australia",
    "id": "2340",
    "pollyear": 2011,
    "position": 39,
    "releaseyear": "",
    "track": "Birds of Tokyo"
    },
    {
    "alltime": True,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "2341",
    "pollyear": 2011,
    "position": 40,
    "releaseyear": "",
    "track": "Echolalia"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2342",
    "pollyear": 2011,
    "position": 41,
    "releaseyear": "",
    "track": "Double Allergic"
    },
    {
    "alltime": True,
    "artist": "Cold Chisel",
    "country": "Australia",
    "id": "2343",
    "pollyear": 2011,
    "position": 42,
    "releaseyear": "",
    "track": "East"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2344",
    "pollyear": 2011,
    "position": 43,
    "releaseyear": "",
    "track": "Freak Show"
    },
    {
    "alltime": True,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "2345",
    "pollyear": 2011,
    "position": 44,
    "releaseyear": "",
    "track": "Tu-Plang"
    },
    {
    "alltime": True,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "2346",
    "pollyear": 2011,
    "position": 45,
    "releaseyear": "",
    "track": "Sound Awake"
    },
    {
    "alltime": True,
    "artist": "Empire of the Sun",
    "country": "Australia",
    "id": "2347",
    "pollyear": 2011,
    "position": 46,
    "releaseyear": "",
    "track": "Walking on a Dream"
    },
    {
    "alltime": True,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "2348",
    "pollyear": 2011,
    "position": 47,
    "releaseyear": "",
    "track": "Black Fingernails, Red Wine"
    },
    {
    "alltime": True,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "2349",
    "pollyear": 2011,
    "position": 48,
    "releaseyear": "",
    "track": "Ivy and the Big Apples"
    },
    {
    "alltime": True,
    "artist": "John Farnham",
    "country": "Australia",
    "id": "2350",
    "pollyear": 2011,
    "position": 49,
    "releaseyear": "",
    "track": "Whispering Jack"
    },
    {
    "alltime": True,
    "artist": "Cog",
    "country": "Australia",
    "id": "2351",
    "pollyear": 2011,
    "position": 50,
    "releaseyear": "",
    "track": "The New Normal"
    },
    {
    "alltime": True,
    "artist": "Washington",
    "country": "Australia",
    "id": "2352",
    "pollyear": 2011,
    "position": 51,
    "releaseyear": "",
    "track": "I Believe You Liar"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2353",
    "pollyear": 2011,
    "position": 52,
    "releaseyear": "",
    "track": "Murder Ballads"
    },
    {
    "alltime": True,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "2354",
    "pollyear": 2011,
    "position": 53,
    "releaseyear": "",
    "track": "Three"
    },
    {
    "alltime": True,
    "artist": "Bernard Fanning",
    "country": "Australia",
    "id": "2355",
    "pollyear": 2011,
    "position": 54,
    "releaseyear": "",
    "track": "Tea & Sympathy"
    },
    {
    "alltime": True,
    "artist": "Midnight Oil",
    "country": "Australia",
    "id": "2356",
    "pollyear": 2011,
    "position": 55,
    "releaseyear": "",
    "track": "Blue Sky Mining"
    },
    {
    "alltime": True,
    "artist": "Cloud Control",
    "country": "Australia",
    "id": "2357",
    "pollyear": 2011,
    "position": 56,
    "releaseyear": "",
    "track": "Bliss Release"
    },
    {
    "alltime": True,
    "artist": "The Cruel Sea",
    "country": "Australia",
    "id": "2358",
    "pollyear": 2011,
    "position": 57,
    "releaseyear": "",
    "track": "The Honeymoon Is Over"
    },
    {
    "alltime": True,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "2359",
    "pollyear": 2011,
    "position": 58,
    "releaseyear": "",
    "track": "New Detention"
    },
    {
    "alltime": True,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "2360",
    "pollyear": 2011,
    "position": 59,
    "releaseyear": "",
    "track": "As Day Follows Night"
    },
    {
    "alltime": True,
    "artist": "Sia",
    "country": "Australia",
    "id": "2361",
    "pollyear": 2011,
    "position": 60,
    "releaseyear": "",
    "track": "We Are Born"
    },
    {
    "alltime": True,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "2362",
    "pollyear": 2011,
    "position": 61,
    "releaseyear": "",
    "track": "Hold Your Colour"
    },
    {
    "alltime": True,
    "artist": "The Panics",
    "country": "Australia",
    "id": "2363",
    "pollyear": 2011,
    "position": 62,
    "releaseyear": "",
    "track": "Cruel Guards"
    },
    {
    "alltime": True,
    "artist": "The John Butler Trio",
    "country": "Australia",
    "id": "2364",
    "pollyear": 2011,
    "position": 63,
    "releaseyear": "",
    "track": "Grand National"
    },
    {
    "alltime": True,
    "artist": "george",
    "country": "Australia",
    "id": "2365",
    "pollyear": 2011,
    "position": 64,
    "releaseyear": "",
    "track": "Polyserena"
    },
    {
    "alltime": True,
    "artist": "Cold Chisel",
    "country": "Australia",
    "id": "2366",
    "pollyear": 2011,
    "position": 65,
    "releaseyear": "",
    "track": "Cold Chisel"
    },
    {
    "alltime": True,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "2367",
    "pollyear": 2011,
    "position": 66,
    "releaseyear": "",
    "track": "Running on Air"
    },
    {
    "alltime": True,
    "artist": "Bliss n Eso",
    "country": "Australia",
    "id": "2368",
    "pollyear": 2011,
    "position": 67,
    "releaseyear": "",
    "track": "Flying Colours"
    },
    {
    "alltime": True,
    "artist": "Art vs. Science",
    "country": "Australia",
    "id": "2369",
    "pollyear": 2011,
    "position": 68,
    "releaseyear": "",
    "track": "The Experiment"
    },
    {
    "alltime": True,
    "artist": "Paul Kelly and The Coloured Girls",
    "country": "Australia",
    "id": "2370",
    "pollyear": 2011,
    "position": 69,
    "releaseyear": "",
    "track": "Gossip"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2371",
    "pollyear": 2011,
    "position": 70,
    "releaseyear": "",
    "track": "Young Modern"
    },
    {
    "alltime": True,
    "artist": "The Presets",
    "country": "Australia",
    "id": "2372",
    "pollyear": 2011,
    "position": 71,
    "releaseyear": "",
    "track": "Beams"
    },
    {
    "alltime": True,
    "artist": "Something for Kate",
    "country": "Australia",
    "id": "2373",
    "pollyear": 2011,
    "position": 72,
    "releaseyear": "",
    "track": "Beautiful Sharks"
    },
    {
    "alltime": True,
    "artist": "AC/DC",
    "country": "Australia",
    "id": "2374",
    "pollyear": 2011,
    "position": 73,
    "releaseyear": "",
    "track": "Highway to Hell"
    },
    {
    "alltime": True,
    "artist": "Sarah Blasko",
    "country": "Australia",
    "id": "2375",
    "pollyear": 2011,
    "position": 74,
    "releaseyear": "",
    "track": "The Overture & the Underscore"
    },
    {
    "alltime": True,
    "artist": "Skyhooks",
    "country": "Australia",
    "id": "2376",
    "pollyear": 2011,
    "position": 75,
    "releaseyear": "",
    "track": "Living in the 70's"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "2377",
    "pollyear": 2011,
    "position": 76,
    "releaseyear": "",
    "track": "Human Frailty"
    },
    {
    "alltime": True,
    "artist": "Pendulum",
    "country": "Australia",
    "id": "2378",
    "pollyear": 2011,
    "position": 77,
    "releaseyear": "",
    "track": "Immersion"
    },
    {
    "alltime": True,
    "artist": "The Sleepy Jackson",
    "country": "Australia",
    "id": "2379",
    "pollyear": 2011,
    "position": 78,
    "releaseyear": "",
    "track": "Lovers"
    },
    {
    "alltime": True,
    "artist": "The Grates",
    "country": "Australia",
    "id": "2380",
    "pollyear": 2011,
    "position": 79,
    "releaseyear": "",
    "track": "Gravity Won't Get You High"
    },
    {
    "alltime": True,
    "artist": "The Saints",
    "country": "Australia",
    "id": "2381",
    "pollyear": 2011,
    "position": 80,
    "releaseyear": "",
    "track": "(I'm) Stranded"
    },
    {
    "alltime": True,
    "artist": "Pete Murray",
    "country": "Australia",
    "id": "2382",
    "pollyear": 2011,
    "position": 81,
    "releaseyear": "",
    "track": "Feeler"
    },
    {
    "alltime": True,
    "artist": "The Waifs",
    "country": "Australia",
    "id": "2383",
    "pollyear": 2011,
    "position": 82,
    "releaseyear": "",
    "track": "Up All Night"
    },
    {
    "alltime": True,
    "artist": "Lisa Mitchell",
    "country": "Australia",
    "id": "2384",
    "pollyear": 2011,
    "position": 83,
    "releaseyear": "",
    "track": "Wonder"
    },
    {
    "alltime": True,
    "artist": "The Go-Betweens",
    "country": "Australia",
    "id": "2385",
    "pollyear": 2011,
    "position": 84,
    "releaseyear": "",
    "track": "16 Lovers Lane"
    },
    {
    "alltime": True,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2386",
    "pollyear": 2011,
    "position": 85,
    "releaseyear": "",
    "track": "State of the Art"
    },
    {
    "alltime": True,
    "artist": "Dead Letter Circus",
    "country": "Australia",
    "id": "2387",
    "pollyear": 2011,
    "position": 86,
    "releaseyear": "",
    "track": "This Is the Warning"
    },
    {
    "alltime": True,
    "artist": "Eskimo Joe",
    "country": "Australia",
    "id": "2388",
    "pollyear": 2011,
    "position": 87,
    "releaseyear": "",
    "track": "A Song Is a City"
    },
    {
    "alltime": True,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "2389",
    "pollyear": 2011,
    "position": 88,
    "releaseyear": "",
    "track": "Imago"
    },
    {
    "alltime": True,
    "artist": "Pnau",
    "country": "Australia",
    "id": "2390",
    "pollyear": 2011,
    "position": 89,
    "releaseyear": "",
    "track": "Pnau"
    },
    {
    "alltime": True,
    "artist": "Children Collide",
    "country": "Australia",
    "id": "2391",
    "pollyear": 2011,
    "position": 90,
    "releaseyear": "",
    "track": "The Long Now"
    },
    {
    "alltime": True,
    "artist": "Gypsy & The Cat",
    "country": "Australia",
    "id": "2392",
    "pollyear": 2011,
    "position": 91,
    "releaseyear": "",
    "track": "Gilgamesh"
    },
    {
    "alltime": True,
    "artist": "Frenzal Rhomb",
    "country": "Australia",
    "id": "2393",
    "pollyear": 2011,
    "position": 92,
    "releaseyear": "",
    "track": "A Man's Not a Camel"
    },
    {
    "alltime": True,
    "artist": "Augie March",
    "country": "Australia",
    "id": "2394",
    "pollyear": 2011,
    "position": 93,
    "releaseyear": "",
    "track": "Moo, You Bloody Choir"
    },
    {
    "alltime": True,
    "artist": "Paul Dempsey",
    "country": "Australia",
    "id": "2395",
    "pollyear": 2011,
    "position": 94,
    "releaseyear": "",
    "track": "Everything Is True"
    },
    {
    "alltime": True,
    "artist": "Hoodoo Gurus",
    "country": "Australia",
    "id": "2396",
    "pollyear": 2011,
    "position": 95,
    "releaseyear": "",
    "track": "Stoneage Romeos"
    },
    {
    "alltime": True,
    "artist": "Machine Gun Fellatio",
    "country": "Australia",
    "id": "2397",
    "pollyear": 2011,
    "position": 96,
    "releaseyear": "",
    "track": "Paging Mr. Strike"
    },
    {
    "alltime": True,
    "artist": "The Butterfly Effect",
    "country": "Australia",
    "id": "2398",
    "pollyear": 2011,
    "position": 97,
    "releaseyear": "",
    "track": "Begins Here"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2399",
    "pollyear": 2011,
    "position": 98,
    "releaseyear": "",
    "track": "The Boatman's Call"
    },
    {
    "alltime": True,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "2400",
    "pollyear": 2011,
    "position": 99,
    "releaseyear": "",
    "track": "Thrills, Kills & Sunday Pills"
    },
    {
    "alltime": True,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "2401",
    "pollyear": 2011,
    "position": 100,
    "releaseyear": "",
    "track": "Two Shoes"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "2402",
    "pollyear": 1998,
    "position": 1,
    "releaseyear": "1991",
    "track": "Smells Like Teen Spirit"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "2403",
    "pollyear": 1998,
    "position": 2,
    "releaseyear": "1985",
    "track": "Throw Your Arms Around Me"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "2404",
    "pollyear": 1998,
    "position": 3,
    "releaseyear": "1991",
    "track": "Alive"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "2405",
    "pollyear": 1998,
    "position": 4,
    "releaseyear": "1994",
    "track": "Last Goodbye"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "2406",
    "pollyear": 1998,
    "position": 5,
    "releaseyear": "1992",
    "track": "Creep"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "2407",
    "pollyear": 1998,
    "position": 6,
    "releaseyear": "1971",
    "track": "Stairway To Heaven"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "2408",
    "pollyear": 1998,
    "position": 7,
    "releaseyear": "1988",
    "track": "One"
    },
    {
    "alltime": True,
    "artist": "Queen",
    "country": "UK",
    "id": "2409",
    "pollyear": 1998,
    "position": 8,
    "releaseyear": "1975",
    "track": "Bohemian Rhapsody"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "2410",
    "pollyear": 1998,
    "position": 9,
    "releaseyear": "1991",
    "track": "Enter Sandman"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "2411",
    "pollyear": 1998,
    "position": 10,
    "releaseyear": "1991",
    "track": "Black"
    },
    {
    "alltime": True,
    "artist": "U2",
    "country": "Ireland",
    "id": "2412",
    "pollyear": 1998,
    "position": 11,
    "releaseyear": "1992",
    "track": "One"
    },
    {
    "alltime": True,
    "artist": "Marilyn Manson",
    "country": "USA",
    "id": "2413",
    "pollyear": 1998,
    "position": 12,
    "releaseyear": "1996",
    "track": "The Beautiful People"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "2414",
    "pollyear": 1998,
    "position": 13,
    "releaseyear": "1997",
    "track": "Paranoid Android"
    },
    {
    "alltime": True,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "2415",
    "pollyear": 1998,
    "position": 14,
    "releaseyear": "1994",
    "track": "Closer"
    },
    {
    "alltime": True,
    "artist": "Violent Femmes",
    "country": "USA",
    "id": "2416",
    "pollyear": 1998,
    "position": 15,
    "releaseyear": "1982",
    "track": "Blister In The Sun"
    },
    {
    "alltime": True,
    "artist": "Joy Division",
    "country": "UK",
    "id": "2417",
    "pollyear": 1998,
    "position": 16,
    "releaseyear": "1980",
    "track": "Love Will Tear Us Apart"
    },
    {
    "alltime": True,
    "artist": "Rage Against The Machine",
    "country": "USA",
    "id": "2418",
    "pollyear": 1998,
    "position": 17,
    "releaseyear": "1992",
    "track": "Killing In The Name"
    },
    {
    "alltime": True,
    "artist": "The Living End",
    "country": "Australia",
    "id": "2419",
    "pollyear": 1998,
    "position": 18,
    "releaseyear": "1997",
    "track": "Prisoner Of Society"
    },
    {
    "alltime": True,
    "artist": "Faith No More",
    "country": "USA",
    "id": "2420",
    "pollyear": 1998,
    "position": 19,
    "releaseyear": "1990",
    "track": "Epic"
    },
    {
    "alltime": True,
    "artist": "Blink-182",
    "country": "USA",
    "id": "2421",
    "pollyear": 1998,
    "position": 20,
    "releaseyear": "1997",
    "track": "Dammit (Growing Up)"
    },
    {
    "alltime": True,
    "artist": "Live",
    "country": "USA",
    "id": "2422",
    "pollyear": 1998,
    "position": 21,
    "releaseyear": "1995",
    "track": "Lightning Crashes"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "2423",
    "pollyear": 1998,
    "position": 22,
    "releaseyear": "1994",
    "track": "Better Man"
    },
    {
    "alltime": True,
    "artist": "U2",
    "country": "Ireland",
    "id": "2424",
    "pollyear": 1998,
    "position": 23,
    "releaseyear": "1987",
    "track": "With Or Without You"
    },
    {
    "alltime": True,
    "artist": "Tool",
    "country": "USA",
    "id": "2425",
    "pollyear": 1998,
    "position": 24,
    "releaseyear": "1996",
    "track": "Stinkfist"
    },
    {
    "alltime": True,
    "artist": "Soft Cell",
    "country": "UK",
    "id": "2426",
    "pollyear": 1998,
    "position": 25,
    "releaseyear": "1981",
    "track": "Tainted Love"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2427",
    "pollyear": 1998,
    "position": 26,
    "releaseyear": "1990",
    "track": "The Ship Song"
    },
    {
    "alltime": True,
    "artist": "Tori Amos",
    "country": "USA",
    "id": "2428",
    "pollyear": 1998,
    "position": 27,
    "releaseyear": "1994",
    "track": "Cornflake Girl"
    },
    {
    "alltime": True,
    "artist": "The Smiths",
    "country": "UK",
    "id": "2429",
    "pollyear": 1998,
    "position": 28,
    "releaseyear": "1985",
    "track": "How Soon Is Now?"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "2430",
    "pollyear": 1998,
    "position": 29,
    "releaseyear": "1994",
    "track": "Grace"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "2431",
    "pollyear": 1998,
    "position": 30,
    "releaseyear": "1983",
    "track": "Blue Monday"
    },
    {
    "alltime": True,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "2432",
    "pollyear": 1998,
    "position": 31,
    "releaseyear": "1991",
    "track": "Under The Bridge"
    },
    {
    "alltime": True,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "2433",
    "pollyear": 1998,
    "position": 32,
    "releaseyear": "1997",
    "track": "Brick"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "2434",
    "pollyear": 1998,
    "position": 33,
    "releaseyear": "1995",
    "track": "Bullet with Butterfly Wings"
    },
    {
    "alltime": True,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "2435",
    "pollyear": 1998,
    "position": 34,
    "releaseyear": "1991",
    "track": "Unfinished Sympathy"
    },
    {
    "alltime": True,
    "artist": "Faith No More",
    "country": "USA",
    "id": "2436",
    "pollyear": 1998,
    "position": 35,
    "releaseyear": "1997",
    "track": "Ashes To Ashes"
    },
    {
    "alltime": True,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "2437",
    "pollyear": 1998,
    "position": 36,
    "releaseyear": "1998",
    "track": "No Aphrodisiac"
    },
    {
    "alltime": True,
    "artist": "The B-52's",
    "country": "USA",
    "id": "2438",
    "pollyear": 1998,
    "position": 37,
    "releaseyear": "1989",
    "track": "Love Shack"
    },
    {
    "alltime": True,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "2439",
    "pollyear": 1998,
    "position": 38,
    "releaseyear": "1987",
    "track": "(You Gotta) Fight for Your Right (To Party!)"
    },
    {
    "alltime": True,
    "artist": "The Stone Roses",
    "country": "UK",
    "id": "2440",
    "pollyear": 1998,
    "position": 39,
    "releaseyear": "1989",
    "track": "Fools Gold"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "2441",
    "pollyear": 1998,
    "position": 40,
    "releaseyear": "1993",
    "track": "Today"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "2442",
    "pollyear": 1998,
    "position": 41,
    "releaseyear": "1975",
    "track": "Wish You Were Here"
    },
    {
    "alltime": True,
    "artist": "Andy Prieboy",
    "country": "USA",
    "id": "2443",
    "pollyear": 1998,
    "position": 42,
    "releaseyear": "1990",
    "track": "Tomorrow Wendy"
    },
    {
    "alltime": True,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "2444",
    "pollyear": 1998,
    "position": 43,
    "releaseyear": "1998",
    "track": "You Sound Like Louis Burdett"
    },
    {
    "alltime": True,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "2445",
    "pollyear": 1998,
    "position": 44,
    "releaseyear": "1994",
    "track": "Sabotage"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "2446",
    "pollyear": 1998,
    "position": 45,
    "releaseyear": "1991",
    "track": "Lithium"
    },
    {
    "alltime": True,
    "artist": "Blur",
    "country": "UK",
    "id": "2447",
    "pollyear": 1998,
    "position": 46,
    "releaseyear": "1997",
    "track": "Song 2"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "2448",
    "pollyear": 1998,
    "position": 47,
    "releaseyear": "1994",
    "track": "Lover, You Should've Come Over"
    },
    {
    "alltime": True,
    "artist": "Tool",
    "country": "USA",
    "id": "2449",
    "pollyear": 1998,
    "position": 48,
    "releaseyear": "1993",
    "track": "Sober"
    },
    {
    "alltime": True,
    "artist": "The Beatles",
    "country": "UK",
    "id": "2450",
    "pollyear": 1998,
    "position": 49,
    "releaseyear": "1967",
    "track": "A Day In The Life"
    },
    {
    "alltime": True,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "2451",
    "pollyear": 1998,
    "position": 50,
    "releaseyear": "1997",
    "track": "Leaving Home"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "2452",
    "pollyear": 1998,
    "position": 51,
    "releaseyear": "1992",
    "track": "Everybody Hurts"
    },
    {
    "alltime": True,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "2453",
    "pollyear": 1998,
    "position": 52,
    "releaseyear": "1996",
    "track": "Underground"
    },
    {
    "alltime": True,
    "artist": "Deee-Lite",
    "country": "USA",
    "id": "2454",
    "pollyear": 1998,
    "position": 53,
    "releaseyear": "1990",
    "track": "Groove Is In The Heart"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "2455",
    "pollyear": 1998,
    "position": 54,
    "releaseyear": "1997",
    "track": "Karma Police"
    },
    {
    "alltime": True,
    "artist": "The Offspring",
    "country": "USA",
    "id": "2456",
    "pollyear": 1998,
    "position": 55,
    "releaseyear": "1994",
    "track": "Come Out And Play"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "2457",
    "pollyear": 1998,
    "position": 56,
    "releaseyear": "1993",
    "track": "Rearviewmirror"
    },
    {
    "alltime": True,
    "artist": "Tool",
    "country": "USA",
    "id": "2458",
    "pollyear": 1998,
    "position": 57,
    "releaseyear": "1997",
    "track": "Forty-Six & 2"
    },
    {
    "alltime": True,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "2459",
    "pollyear": 1998,
    "position": 58,
    "releaseyear": "1994",
    "track": "Black Hole Sun"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2460",
    "pollyear": 1998,
    "position": 59,
    "releaseyear": "1994",
    "track": "Tomorrow"
    },
    {
    "alltime": True,
    "artist": "New Order",
    "country": "UK",
    "id": "2461",
    "pollyear": 1998,
    "position": 60,
    "releaseyear": "1986",
    "track": "Bizarre Love Triangle"
    },
    {
    "alltime": True,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2462",
    "pollyear": 1998,
    "position": 61,
    "releaseyear": "1994",
    "track": "Berlin Chair"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "2463",
    "pollyear": 1998,
    "position": 62,
    "releaseyear": "1992",
    "track": "Come As You Are"
    },
    {
    "alltime": True,
    "artist": "Led Zeppelin",
    "country": "UK",
    "id": "2464",
    "pollyear": 1998,
    "position": 63,
    "releaseyear": "1975",
    "track": "Kashmir"
    },
    {
    "alltime": True,
    "artist": "Cake",
    "country": "USA",
    "id": "2465",
    "pollyear": 1998,
    "position": 64,
    "releaseyear": "1996",
    "track": "I Will Survive"
    },
    {
    "alltime": True,
    "artist": "The Eagles",
    "country": "USA",
    "id": "2466",
    "pollyear": 1998,
    "position": 65,
    "releaseyear": "1977",
    "track": "Hotel California"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2467",
    "pollyear": 1998,
    "position": 66,
    "releaseyear": "1983",
    "track": "The Lovecats"
    },
    {
    "alltime": True,
    "artist": "Sex Pistols",
    "country": "UK",
    "id": "2468",
    "pollyear": 1998,
    "position": 67,
    "releaseyear": "1976",
    "track": "Anarchy In The UK"
    },
    {
    "alltime": True,
    "artist": "Hunters & Collectors",
    "country": "Australia",
    "id": "2469",
    "pollyear": 1998,
    "position": 68,
    "releaseyear": "1992",
    "track": "Holy Grail"
    },
    {
    "alltime": True,
    "artist": "Jane's Addiction",
    "country": "USA",
    "id": "2470",
    "pollyear": 1998,
    "position": 69,
    "releaseyear": "1990",
    "track": "Been Caught Stealing"
    },
    {
    "alltime": True,
    "artist": "The Jimi Hendrix Experience",
    "country": "USA",
    "id": "2471",
    "pollyear": 1998,
    "position": 70,
    "releaseyear": "1968",
    "track": "All Along the Watchtower"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "2472",
    "pollyear": 1998,
    "position": 71,
    "releaseyear": "1996",
    "track": "1979"
    },
    {
    "alltime": True,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "2473",
    "pollyear": 1998,
    "position": 72,
    "releaseyear": "1997",
    "track": "The Perfect Drug"
    },
    {
    "alltime": True,
    "artist": "R.E.M.",
    "country": "USA",
    "id": "2474",
    "pollyear": 1998,
    "position": 73,
    "releaseyear": "1991",
    "track": "Losing My Religion"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "USA",
    "id": "2475",
    "pollyear": 1998,
    "position": 74,
    "releaseyear": "1980",
    "track": "A Forest"
    },
    {
    "alltime": True,
    "artist": "Portishead",
    "country": "UK",
    "id": "2476",
    "pollyear": 1998,
    "position": 75,
    "releaseyear": "1995",
    "track": "Glory Box"
    },
    {
    "alltime": True,
    "artist": "Crowded House",
    "country": "Australia",
    "id": "2477",
    "pollyear": 1998,
    "position": 76,
    "releaseyear": "1986",
    "track": "Don't Dream It's Over"
    },
    {
    "alltime": True,
    "artist": "Guns N' Roses",
    "country": "USA",
    "id": "2478",
    "pollyear": 1998,
    "position": 77,
    "releaseyear": "1988",
    "track": "Sweet Child O' Mine"
    },
    {
    "alltime": True,
    "artist": "They Might Be Giants",
    "country": "USA",
    "id": "2479",
    "pollyear": 1998,
    "position": 78,
    "releaseyear": "1990",
    "track": "Birdhouse In Your Soul"
    },
    {
    "alltime": True,
    "artist": "The Buggles",
    "country": "UK",
    "id": "2480",
    "pollyear": 1998,
    "position": 79,
    "releaseyear": "1979",
    "track": "Video Killed The Radio Star"
    },
    {
    "alltime": True,
    "artist": "The Offspring",
    "country": "USA",
    "id": "2481",
    "pollyear": 1998,
    "position": 80,
    "releaseyear": "1994",
    "track": "Self Esteem"
    },
    {
    "alltime": True,
    "artist": "Blind Melon",
    "country": "USA",
    "id": "2482",
    "pollyear": 1998,
    "position": 81,
    "releaseyear": "1992",
    "track": "No Rain"
    },
    {
    "alltime": True,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "2483",
    "pollyear": 1998,
    "position": 82,
    "releaseyear": "1996",
    "track": "Jerks Of Attention"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2484",
    "pollyear": 1998,
    "position": 83,
    "releaseyear": "1997",
    "track": "Abuse Me"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2485",
    "pollyear": 1998,
    "position": 84,
    "releaseyear": "1997",
    "track": "Into My Arms"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2486",
    "pollyear": 1998,
    "position": 85,
    "releaseyear": "1987",
    "track": "Just Like Heaven"
    },
    {
    "alltime": True,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "2487",
    "pollyear": 1998,
    "position": 86,
    "releaseyear": "1996",
    "track": "Buy Me A Pony"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "2488",
    "pollyear": 1998,
    "position": 87,
    "releaseyear": "1996",
    "track": "Aneurysm"
    },
    {
    "alltime": True,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "2489",
    "pollyear": 1998,
    "position": 88,
    "releaseyear": "1998",
    "track": "Just Ace"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2490",
    "pollyear": 1998,
    "position": 89,
    "releaseyear": "1985",
    "track": "Close To Me"
    },
    {
    "alltime": True,
    "artist": "Pink Floyd",
    "country": "UK",
    "id": "2491",
    "pollyear": 1998,
    "position": 90,
    "releaseyear": "1979",
    "track": "Comfortably Numb"
    },
    {
    "alltime": True,
    "artist": "Metallica",
    "country": "USA",
    "id": "2492",
    "pollyear": 1998,
    "position": 91,
    "releaseyear": "1991",
    "track": "The Unforgiven"
    },
    {
    "alltime": True,
    "artist": "Pauline Pantsdown",
    "country": "Australia",
    "id": "2493",
    "pollyear": 1998,
    "position": 92,
    "releaseyear": "1997",
    "track": "Backdoor Man"
    },
    {
    "alltime": True,
    "artist": "U2",
    "country": "Ireland",
    "id": "2494",
    "pollyear": 1998,
    "position": 93,
    "releaseyear": "1987",
    "track": "I Still Haven't Found What I'm Looking For"
    },
    {
    "alltime": True,
    "artist": "Cold Chisel",
    "country": "Australia",
    "id": "2495",
    "pollyear": 1998,
    "position": 94,
    "releaseyear": "1978",
    "track": "Khe Sanh"
    },
    {
    "alltime": True,
    "artist": "Prodigy",
    "country": "UK",
    "id": "2496",
    "pollyear": 1998,
    "position": 95,
    "releaseyear": "1996",
    "track": "Breathe"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2497",
    "pollyear": 1998,
    "position": 96,
    "releaseyear": "1994",
    "track": "Red Right Hand"
    },
    {
    "alltime": True,
    "artist": "Beck",
    "country": "USA",
    "id": "2498",
    "pollyear": 1998,
    "position": 97,
    "releaseyear": "1993",
    "track": "Loser"
    },
    {
    "alltime": True,
    "artist": "The Cure",
    "country": "UK",
    "id": "2499",
    "pollyear": 1998,
    "position": 98,
    "releaseyear": "1980",
    "track": "Boys Don't Cry"
    },
    {
    "alltime": True,
    "artist": "The Verve",
    "country": "UK",
    "id": "2500",
    "pollyear": 1998,
    "position": 99,
    "releaseyear": "1997",
    "track": "Bitter Sweet Symphony"
    },
    {
    "alltime": True,
    "artist": "David Bowie",
    "country": "UK",
    "id": "2501",
    "pollyear": 1998,
    "position": 100,
    "releaseyear": "1977",
    "track": "Heroes"
    },
    {
    "alltime": False,
    "artist": "Macklemore & Ryan Lewis",
    "country": "USA",
    "id": "2502",
    "pollyear": 2012,
    "position": 1,
    "releaseyear": "2012",
    "track": "Thrift Shop {ft. Wanz}"
    },
    {
    "alltime": False,
    "artist": "Of Monsters And Men",
    "country": "Iceland",
    "id": "2503",
    "pollyear": 2012,
    "position": 2,
    "releaseyear": "2012",
    "track": "Little Talks"
    },
    {
    "alltime": False,
    "artist": "alt-J",
    "country": "UK",
    "id": "2504",
    "pollyear": 2012,
    "position": 3,
    "releaseyear": "2012",
    "track": "Breezeblocks"
    },
    {
    "alltime": False,
    "artist": "Flume",
    "country": "Australia",
    "id": "2505",
    "pollyear": 2012,
    "position": 4,
    "releaseyear": "2012",
    "track": "Holdin On"
    },
    {
    "alltime": False,
    "artist": "Mumford & Sons",
    "country": "UK",
    "id": "2506",
    "pollyear": 2012,
    "position": 5,
    "releaseyear": "2012",
    "track": "I Will Wait"
    },
    {
    "alltime": False,
    "artist": "Major Lazer",
    "country": "USA",
    "id": "2507",
    "pollyear": 2012,
    "position": 6,
    "releaseyear": "2012",
    "track": "Get Free {ft. Amber Coffman}"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2508",
    "pollyear": 2012,
    "position": 7,
    "releaseyear": "2012",
    "track": "Elephant"
    },
    {
    "alltime": False,
    "artist": "Frank Ocean",
    "country": "USA",
    "id": "2509",
    "pollyear": 2012,
    "position": 8,
    "releaseyear": "2012",
    "track": "Lost"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2510",
    "pollyear": 2012,
    "position": 9,
    "releaseyear": "2012",
    "track": "Feels Like We Only Go Backwards"
    },
    {
    "alltime": False,
    "artist": "The Rubens",
    "country": "Australia",
    "id": "2511",
    "pollyear": 2012,
    "position": 10,
    "releaseyear": "2012",
    "track": "My Gun"
    },
    {
    "alltime": False,
    "artist": "Calvin Harris",
    "country": "UK",
    "id": "2512",
    "pollyear": 2012,
    "position": 11,
    "releaseyear": "2012",
    "track": "Sweet Nothing {ft. Florence Welch}"
    },
    {
    "alltime": False,
    "artist": "Flume",
    "country": "Australia",
    "id": "2513",
    "pollyear": 2012,
    "position": 12,
    "releaseyear": "2012",
    "track": "Sleepless {ft. Jezzabell Doran}"
    },
    {
    "alltime": False,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "2514",
    "pollyear": 2012,
    "position": 13,
    "releaseyear": "2012",
    "track": "Gold On The Ceiling"
    },
    {
    "alltime": False,
    "artist": "Icona Pop",
    "country": "Sweden",
    "id": "2515",
    "pollyear": 2012,
    "position": 14,
    "releaseyear": "2012",
    "track": "I Love It {ft. Charli XCX}"
    },
    {
    "alltime": False,
    "artist": "Macklemore & Ryan Lewis",
    "country": "USA",
    "id": "2516",
    "pollyear": 2012,
    "position": 15,
    "releaseyear": "2012",
    "track": "Same Love {ft. Mary Lambert}"
    },
    {
    "alltime": False,
    "artist": "Rudimental",
    "country": "UK",
    "id": "2517",
    "pollyear": 2012,
    "position": 16,
    "releaseyear": "2012",
    "track": "Not Giving In {ft. John Newman & Alex Clare}"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2518",
    "pollyear": 2012,
    "position": 17,
    "releaseyear": "2012",
    "track": "Clair De Lune {ft. Christine Hoberg}"
    },
    {
    "alltime": False,
    "artist": "Hermitude",
    "country": "Australia",
    "id": "2519",
    "pollyear": 2012,
    "position": 18,
    "releaseyear": "2012",
    "track": "HyperParadise {Flume Remix}"
    },
    {
    "alltime": False,
    "artist": "The xx",
    "country": "UK",
    "id": "2520",
    "pollyear": 2012,
    "position": 19,
    "releaseyear": "2012",
    "track": "Angels"
    },
    {
    "alltime": False,
    "artist": "Rudimental",
    "country": "UK",
    "id": "2521",
    "pollyear": 2012,
    "position": 20,
    "releaseyear": "2012",
    "track": "Feel The Love {ft. John Newman}"
    },
    {
    "alltime": False,
    "artist": "Disclosure",
    "country": "UK",
    "id": "2522",
    "pollyear": 2012,
    "position": 21,
    "releaseyear": "2012",
    "track": "Latch {ft. Sam Smith}"
    },
    {
    "alltime": False,
    "artist": "The Temper Trap",
    "country": "Australia",
    "id": "2523",
    "pollyear": 2012,
    "position": 22,
    "releaseyear": "2012",
    "track": "Trembling Hands"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2524",
    "pollyear": 2012,
    "position": 23,
    "releaseyear": "2012",
    "track": "Coming Down"
    },
    {
    "alltime": False,
    "artist": "Chet Faker",
    "country": "Australia",
    "id": "2525",
    "pollyear": 2012,
    "position": 24,
    "releaseyear": "2012",
    "track": "I'm Into You"
    },
    {
    "alltime": False,
    "artist": "Skrillex",
    "country": "USA",
    "id": "2526",
    "pollyear": 2012,
    "position": 25,
    "releaseyear": "2012",
    "track": "Bangarang {ft. Sirah}"
    },
    {
    "alltime": False,
    "artist": "Seth Sentry",
    "country": "Australia",
    "id": "2527",
    "pollyear": 2012,
    "position": 26,
    "releaseyear": "2012",
    "track": "Dear Science"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2528",
    "pollyear": 2012,
    "position": 27,
    "releaseyear": "2012",
    "track": "Surrender"
    },
    {
    "alltime": False,
    "artist": "Django Django",
    "country": "UK",
    "id": "2529",
    "pollyear": 2012,
    "position": 28,
    "releaseyear": "2012",
    "track": "Default"
    },
    {
    "alltime": False,
    "artist": "Loon Lake",
    "country": "Australia",
    "id": "2530",
    "pollyear": 2012,
    "position": 29,
    "releaseyear": "2012",
    "track": "Cherry Lips"
    },
    {
    "alltime": False,
    "artist": "Bat For Lashes",
    "country": "UK",
    "id": "2531",
    "pollyear": 2012,
    "position": 30,
    "releaseyear": "2012",
    "track": "Laura"
    },
    {
    "alltime": False,
    "artist": "Alpine",
    "country": "Australia",
    "id": "2532",
    "pollyear": 2012,
    "position": 31,
    "releaseyear": "2012",
    "track": "Gasoline"
    },
    {
    "alltime": False,
    "artist": "Florence + The Machine",
    "country": "UK",
    "id": "2533",
    "pollyear": 2012,
    "position": 32,
    "releaseyear": "2012",
    "track": "Spectrum (Say My Name) {Calvin Harris Remix}"
    },
    {
    "alltime": False,
    "artist": "Parachute Youth",
    "country": "Australia",
    "id": "2534",
    "pollyear": 2012,
    "position": 33,
    "releaseyear": "2012",
    "track": "Can't Get Better Than This"
    },
    {
    "alltime": False,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2535",
    "pollyear": 2012,
    "position": 34,
    "releaseyear": "2012",
    "track": "Born To Die"
    },
    {
    "alltime": False,
    "artist": "360",
    "country": "Australia",
    "id": "2536",
    "pollyear": 2012,
    "position": 35,
    "releaseyear": "2012",
    "track": "Run Alone"
    },
    {
    "alltime": False,
    "artist": "Miike Snow",
    "country": "Sweden",
    "id": "2537",
    "pollyear": 2012,
    "position": 36,
    "releaseyear": "2012",
    "track": "Paddling Out"
    },
    {
    "alltime": False,
    "artist": "Two Door Cinema Club",
    "country": "UK",
    "id": "2538",
    "pollyear": 2012,
    "position": 37,
    "releaseyear": "2012",
    "track": "Sun"
    },
    {
    "alltime": False,
    "artist": "Grimes",
    "country": "Canada",
    "id": "2539",
    "pollyear": 2012,
    "position": 38,
    "releaseyear": "2012",
    "track": "Oblivion"
    },
    {
    "alltime": False,
    "artist": "Alabama Shakes",
    "country": "USA",
    "id": "2540",
    "pollyear": 2012,
    "position": 39,
    "releaseyear": "2012",
    "track": "Hold On"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "2541",
    "pollyear": 2012,
    "position": 40,
    "releaseyear": "2012",
    "track": "R U Mine?"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "2542",
    "pollyear": 2012,
    "position": 41,
    "releaseyear": "2012",
    "track": "I Can Make You Love Me"
    },
    {
    "alltime": False,
    "artist": "MS MR",
    "country": "USA",
    "id": "2543",
    "pollyear": 2012,
    "position": 42,
    "releaseyear": "2012",
    "track": "Hurricane"
    },
    {
    "alltime": False,
    "artist": "The Lumineers",
    "country": "USA",
    "id": "2544",
    "pollyear": 2012,
    "position": 43,
    "releaseyear": "2012",
    "track": "Ho Hey"
    },
    {
    "alltime": False,
    "artist": "Xavier Rudd",
    "country": "Australia",
    "id": "2545",
    "pollyear": 2012,
    "position": 44,
    "releaseyear": "2012",
    "track": "Follow The Sun"
    },
    {
    "alltime": False,
    "artist": "Chance Waters",
    "country": "Australia",
    "id": "2546",
    "pollyear": 2012,
    "position": 45,
    "releaseyear": "2012",
    "track": "Young & Dumb {ft. Bertie Blackman}"
    },
    {
    "alltime": False,
    "artist": "Passion Pit",
    "country": "USA",
    "id": "2547",
    "pollyear": 2012,
    "position": 46,
    "releaseyear": "2012",
    "track": "Take A Walk"
    },
    {
    "alltime": False,
    "artist": "Of Monsters And Men",
    "country": "Iceland",
    "id": "2548",
    "pollyear": 2012,
    "position": 47,
    "releaseyear": "2012",
    "track": "Mountain Sound"
    },
    {
    "alltime": False,
    "artist": "San Cisco",
    "country": "Australia",
    "id": "2549",
    "pollyear": 2012,
    "position": 48,
    "releaseyear": "2012",
    "track": "Fred Astaire"
    },
    {
    "alltime": False,
    "artist": "Thundamentals",
    "country": "Australia",
    "id": "2550",
    "pollyear": 2012,
    "position": 49,
    "releaseyear": "2012",
    "track": "Brother {Like A Version}"
    },
    {
    "alltime": False,
    "artist": "Asta",
    "country": "Australia",
    "id": "2551",
    "pollyear": 2012,
    "position": 50,
    "releaseyear": "2012",
    "track": "My Heart Is On Fire"
    },
    {
    "alltime": False,
    "artist": "Birds Of Tokyo",
    "country": "Australia",
    "id": "2552",
    "pollyear": 2012,
    "position": 51,
    "releaseyear": "2012",
    "track": "This Fire"
    },
    {
    "alltime": False,
    "artist": "The Presets",
    "country": "Australia",
    "id": "2553",
    "pollyear": 2012,
    "position": 52,
    "releaseyear": "2012",
    "track": "Ghosts"
    },
    {
    "alltime": False,
    "artist": "San Cisco",
    "country": "Australia",
    "id": "2554",
    "pollyear": 2012,
    "position": 53,
    "releaseyear": "2012",
    "track": "Wild Things"
    },
    {
    "alltime": False,
    "artist": "The Bamboos",
    "country": "Australia",
    "id": "2555",
    "pollyear": 2012,
    "position": 54,
    "releaseyear": "2012",
    "track": "I Got Burned {ft. Tim Rogers}"
    },
    {
    "alltime": False,
    "artist": "Knife Party",
    "country": "Australia",
    "id": "2556",
    "pollyear": 2012,
    "position": 55,
    "releaseyear": "2012",
    "track": "Internet Friends"
    },
    {
    "alltime": False,
    "artist": "Frank Ocean",
    "country": "USA",
    "id": "2557",
    "pollyear": 2012,
    "position": 56,
    "releaseyear": "2012",
    "track": "Thinkin Bout You"
    },
    {
    "alltime": False,
    "artist": "Seth Sentry",
    "country": "Australia",
    "id": "2558",
    "pollyear": 2012,
    "position": 57,
    "releaseyear": "2012",
    "track": "Float Away"
    },
    {
    "alltime": False,
    "artist": "Mumford & Sons",
    "country": "UK",
    "id": "2559",
    "pollyear": 2012,
    "position": 58,
    "releaseyear": "2012",
    "track": "Babel"
    },
    {
    "alltime": False,
    "artist": "Cosmo Jarvis",
    "country": "UK",
    "id": "2560",
    "pollyear": 2012,
    "position": 59,
    "releaseyear": "2012",
    "track": "Love This"
    },
    {
    "alltime": False,
    "artist": "Jack White",
    "country": "USA",
    "id": "2561",
    "pollyear": 2012,
    "position": 60,
    "releaseyear": "2012",
    "track": "Love Interruption"
    },
    {
    "alltime": False,
    "artist": "Sticky Fingers",
    "country": "Australia",
    "id": "2562",
    "pollyear": 2012,
    "position": 61,
    "releaseyear": "2012",
    "track": "Caress Your Soul"
    },
    {
    "alltime": False,
    "artist": "Kid Cudi",
    "country": "USA",
    "id": "2563",
    "pollyear": 2012,
    "position": 62,
    "releaseyear": "2012",
    "track": "Just What I Am {ft. King Chip}"
    },
    {
    "alltime": False,
    "artist": "First Aid Kit",
    "country": "Sweden",
    "id": "2564",
    "pollyear": 2012,
    "position": 63,
    "releaseyear": "2012",
    "track": "Wolf"
    },
    {
    "alltime": False,
    "artist": "alt-J",
    "country": "UK",
    "id": "2565",
    "pollyear": 2012,
    "position": 64,
    "releaseyear": "2012",
    "track": "Tessellate"
    },
    {
    "alltime": False,
    "artist": "Grimes",
    "country": "Canada",
    "id": "2566",
    "pollyear": 2012,
    "position": 65,
    "releaseyear": "2012",
    "track": "Genesis"
    },
    {
    "alltime": False,
    "artist": "The Rubens",
    "country": "Australia",
    "id": "2567",
    "pollyear": 2012,
    "position": 66,
    "releaseyear": "2012",
    "track": "The Best We Got"
    },
    {
    "alltime": False,
    "artist": "Flume",
    "country": "Australia",
    "id": "2568",
    "pollyear": 2012,
    "position": 67,
    "releaseyear": "2012",
    "track": "On Top {ft. T-Shirt}"
    },
    {
    "alltime": False,
    "artist": "Avicii",
    "country": "Sweden",
    "id": "2569",
    "pollyear": 2012,
    "position": 68,
    "releaseyear": "2012",
    "track": "Silhouettes"
    },
    {
    "alltime": False,
    "artist": "Matt Corby",
    "country": "Australia",
    "id": "2570",
    "pollyear": 2012,
    "position": 69,
    "releaseyear": "2012",
    "track": "Lonely Boy {Like A Version}"
    },
    {
    "alltime": False,
    "artist": "The Presets",
    "country": "Australia",
    "id": "2571",
    "pollyear": 2012,
    "position": 70,
    "releaseyear": "2012",
    "track": "Promises"
    },
    {
    "alltime": False,
    "artist": "Kendrick Lamar",
    "country": "USA",
    "id": "2572",
    "pollyear": 2012,
    "position": 71,
    "releaseyear": "2012",
    "track": "Swimming Pools (Drank)"
    },
    {
    "alltime": False,
    "artist": "Regina Spektor",
    "country": "USA",
    "id": "2573",
    "pollyear": 2012,
    "position": 72,
    "releaseyear": "2012",
    "track": "All The Rowboats"
    },
    {
    "alltime": False,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "2574",
    "pollyear": 2012,
    "position": 73,
    "releaseyear": "2012",
    "track": "Draw A Crowd"
    },
    {
    "alltime": False,
    "artist": "The Shins",
    "country": "USA",
    "id": "2575",
    "pollyear": 2012,
    "position": 74,
    "releaseyear": "2012",
    "track": "Simple Song"
    },
    {
    "alltime": False,
    "artist": "Muse",
    "country": "UK",
    "id": "2576",
    "pollyear": 2012,
    "position": 75,
    "releaseyear": "2012",
    "track": "Madness"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "2577",
    "pollyear": 2012,
    "position": 76,
    "releaseyear": "2012",
    "track": "Heard It All"
    },
    {
    "alltime": False,
    "artist": "Feed Me & Crystal Fighters",
    "country": "UK",
    "id": "2578",
    "pollyear": 2012,
    "position": 77,
    "releaseyear": "2012",
    "track": "Love Is All I Got"
    },
    {
    "alltime": False,
    "artist": "Totally Enormous Extinct Dinosaurs",
    "country": "UK",
    "id": "2579",
    "pollyear": 2012,
    "position": 78,
    "releaseyear": "2012",
    "track": "Household Goods"
    },
    {
    "alltime": False,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "2580",
    "pollyear": 2012,
    "position": 79,
    "releaseyear": "2012",
    "track": "Little Black Submarines"
    },
    {
    "alltime": False,
    "artist": "Frank Ocean",
    "country": "USA",
    "id": "2581",
    "pollyear": 2012,
    "position": 80,
    "releaseyear": "2012",
    "track": "Super Rich Kids {ft. Earl Sweatshirt}"
    },
    {
    "alltime": False,
    "artist": "alt-J",
    "country": "UK",
    "id": "2582",
    "pollyear": 2012,
    "position": 81,
    "releaseyear": "2012",
    "track": "Something Good"
    },
    {
    "alltime": False,
    "artist": "Santigold",
    "country": "USA",
    "id": "2583",
    "pollyear": 2012,
    "position": 82,
    "releaseyear": "2012",
    "track": "Disparate Youth"
    },
    {
    "alltime": False,
    "artist": "The Jungle Giants",
    "country": "Australia",
    "id": "2584",
    "pollyear": 2012,
    "position": 83,
    "releaseyear": "2012",
    "track": "She's A Riot"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2585",
    "pollyear": 2012,
    "position": 84,
    "releaseyear": "2012",
    "track": "Rattling The Keys To The Kingdom"
    },
    {
    "alltime": False,
    "artist": "Purity Ring",
    "country": "Canada",
    "id": "2586",
    "pollyear": 2012,
    "position": 85,
    "releaseyear": "2012",
    "track": "Fineshrine"
    },
    {
    "alltime": False,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2587",
    "pollyear": 2012,
    "position": 86,
    "releaseyear": "2012",
    "track": "Summertime Sadness"
    },
    {
    "alltime": False,
    "artist": "The Bloody Beetroots & Greta Svabo Bech",
    "country": "Italy",
    "id": "2588",
    "pollyear": 2012,
    "position": 87,
    "releaseyear": "2012",
    "track": "Chronicles Of A Fallen Love"
    },
    {
    "alltime": False,
    "artist": "C2C",
    "country": "France",
    "id": "2589",
    "pollyear": 2012,
    "position": 88,
    "releaseyear": "2012",
    "track": "Down The Road"
    },
    {
    "alltime": False,
    "artist": "Chance Waters",
    "country": "Australia",
    "id": "2590",
    "pollyear": 2012,
    "position": 89,
    "releaseyear": "2012",
    "track": "Maybe Tomorrow {ft. Lilian Blue}"
    },
    {
    "alltime": False,
    "artist": "Two Door Cinema Club",
    "country": "UK",
    "id": "2591",
    "pollyear": 2012,
    "position": 90,
    "releaseyear": "2012",
    "track": "Sleep Alone"
    },
    {
    "alltime": False,
    "artist": "Allday x C1",
    "country": "Australia",
    "id": "2592",
    "pollyear": 2012,
    "position": 91,
    "releaseyear": "2012",
    "track": "So Good"
    },
    {
    "alltime": False,
    "artist": "Lisa Mitchell",
    "country": "Australia",
    "id": "2593",
    "pollyear": 2012,
    "position": 92,
    "releaseyear": "2012",
    "track": "Spiritus"
    },
    {
    "alltime": False,
    "artist": "Snakadaktal",
    "country": "Australia",
    "id": "2594",
    "pollyear": 2012,
    "position": 93,
    "releaseyear": "2012",
    "track": "Dance Bear"
    },
    {
    "alltime": False,
    "artist": "The Gaslight Anthem",
    "country": "USA",
    "id": "2595",
    "pollyear": 2012,
    "position": 94,
    "releaseyear": "2012",
    "track": "45"
    },
    {
    "alltime": False,
    "artist": "Last Dinosaurs",
    "country": "Australia",
    "id": "2596",
    "pollyear": 2012,
    "position": 95,
    "releaseyear": "2012",
    "track": "Andy"
    },
    {
    "alltime": False,
    "artist": "Kanye West, JAY Z & Big Sean",
    "country": "USA",
    "id": "2597",
    "pollyear": 2012,
    "position": 96,
    "releaseyear": "2012",
    "track": "Clique"
    },
    {
    "alltime": False,
    "artist": "Jack White",
    "country": "USA",
    "id": "2598",
    "pollyear": 2012,
    "position": 97,
    "releaseyear": "2012",
    "track": "I'm Shakin'"
    },
    {
    "alltime": False,
    "artist": "Kimbra",
    "country": "New Zealand",
    "id": "2599",
    "pollyear": 2012,
    "position": 98,
    "releaseyear": "2012",
    "track": "Warrior {ft. Mark Foster & A-Trak}"
    },
    {
    "alltime": False,
    "artist": "M.I.A.",
    "country": "UK",
    "id": "2600",
    "pollyear": 2012,
    "position": 99,
    "releaseyear": "2012",
    "track": "Bad Girls"
    },
    {
    "alltime": False,
    "artist": "Everything Everything",
    "country": "UK",
    "id": "2601",
    "pollyear": 2012,
    "position": 100,
    "releaseyear": "2012",
    "track": "Cough Cough"
    },
    {
    "alltime": True,
    "artist": "Oasis",
    "country": "UK",
    "id": "2602",
    "pollyear": 2013,
    "position": 1,
    "releaseyear": "1995",
    "track": "Wonderwall"
    },
    {
    "alltime": True,
    "artist": "The White Stripes",
    "country": "USA",
    "id": "2603",
    "pollyear": 2013,
    "position": 2,
    "releaseyear": "2003",
    "track": "Seven Nation Army"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "2604",
    "pollyear": 2013,
    "position": 3,
    "releaseyear": "1995",
    "track": "Last Goodbye"
    },
    {
    "alltime": True,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2605",
    "pollyear": 2013,
    "position": 4,
    "releaseyear": "2003",
    "track": "The Nosebleed Section"
    },
    {
    "alltime": True,
    "artist": "The Verve",
    "country": "UK",
    "id": "2606",
    "pollyear": 2013,
    "position": 5,
    "releaseyear": "1997",
    "track": "Bitter Sweet Symphony"
    },
    {
    "alltime": True,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "2607",
    "pollyear": 2013,
    "position": 6,
    "releaseyear": "1997",
    "track": "Everlong"
    },
    {
    "alltime": True,
    "artist": "The Killers",
    "country": "USA",
    "id": "2608",
    "pollyear": 2013,
    "position": 7,
    "releaseyear": "2004",
    "track": "Mr. Brightside"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2609",
    "pollyear": 2013,
    "position": 8,
    "releaseyear": "1999",
    "track": "These Days"
    },
    {
    "alltime": True,
    "artist": "Gotye",
    "country": "Australia",
    "id": "2610",
    "pollyear": 2013,
    "position": 9,
    "releaseyear": "2011",
    "track": "Somebody That I Used to Know {ft. Kimbra}"
    },
    {
    "alltime": True,
    "artist": "Powderfinger",
    "country": "Australia",
    "id": "2611",
    "pollyear": 2013,
    "position": 10,
    "releaseyear": "2000",
    "track": "My Happiness"
    },
    {
    "alltime": True,
    "artist": "Queens of the Stone Age",
    "country": "USA",
    "id": "2612",
    "pollyear": 2013,
    "position": 11,
    "releaseyear": "2002",
    "track": "No One Knows"
    },
    {
    "alltime": True,
    "artist": "Gotye",
    "country": "Australia",
    "id": "2613",
    "pollyear": 2013,
    "position": 12,
    "releaseyear": "2006",
    "track": "Hearts a Mess"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "2614",
    "pollyear": 2013,
    "position": 13,
    "releaseyear": "1997",
    "track": "Paranoid Android"
    },
    {
    "alltime": True,
    "artist": "Mumford & Sons",
    "country": "UK",
    "id": "2615",
    "pollyear": 2013,
    "position": 14,
    "releaseyear": "2009",
    "track": "Little Lion Man"
    },
    {
    "alltime": True,
    "artist": "The Prodigy",
    "country": "UK",
    "id": "2616",
    "pollyear": 2013,
    "position": 15,
    "releaseyear": "1996",
    "track": "Breathe"
    },
    {
    "alltime": True,
    "artist": "Bon Iver",
    "country": "USA",
    "id": "2617",
    "pollyear": 2013,
    "position": 16,
    "releaseyear": "2008",
    "track": "Skinny Love"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2618",
    "pollyear": 2013,
    "position": 17,
    "releaseyear": "1994",
    "track": "Tomorrow"
    },
    {
    "alltime": True,
    "artist": "OutKast",
    "country": "USA",
    "id": "2619",
    "pollyear": 2013,
    "position": 18,
    "releaseyear": "2003",
    "track": "Hey Ya!"
    },
    {
    "alltime": True,
    "artist": "blink-182",
    "country": "Australia",
    "id": "2620",
    "pollyear": 2013,
    "position": 19,
    "releaseyear": "1997",
    "track": "Dammit  "
    },
    {
    "alltime": True,
    "artist": "The Living End",
    "country": "Australia",
    "id": "2621",
    "pollyear": 2013,
    "position": 20,
    "releaseyear": "1997",
    "track": "Prisoner of Society"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "2622",
    "pollyear": 2013,
    "position": 21,
    "releaseyear": "1996",
    "track": "1979"
    },
    {
    "alltime": True,
    "artist": "Blur",
    "country": "UK",
    "id": "2623",
    "pollyear": 2013,
    "position": 22,
    "releaseyear": "1997",
    "track": "Song 2"
    },
    {
    "alltime": True,
    "artist": "Muse",
    "country": "UK",
    "id": "2624",
    "pollyear": 2013,
    "position": 23,
    "releaseyear": "2007",
    "track": "Knights of Cydonia"
    },
    {
    "alltime": True,
    "artist": "Augie March",
    "country": "Australia",
    "id": "2625",
    "pollyear": 2013,
    "position": 24,
    "releaseyear": "2006",
    "track": "One Crowded Hour"
    },
    {
    "alltime": True,
    "artist": "The Smashing Pumpkins",
    "country": "USA",
    "id": "2626",
    "pollyear": 2013,
    "position": 25,
    "releaseyear": "1995",
    "track": "Bullet With Butterfly Wings"
    },
    {
    "alltime": True,
    "artist": "System Of A Down",
    "country": "USA",
    "id": "2627",
    "pollyear": 2013,
    "position": 26,
    "releaseyear": "2001",
    "track": "Chop Suey!"
    },
    {
    "alltime": True,
    "artist": "The Avalanches",
    "country": "Australia",
    "id": "2628",
    "pollyear": 2013,
    "position": 27,
    "releaseyear": "2000",
    "track": "Frontier Psychiatrist"
    },
    {
    "alltime": True,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "2629",
    "pollyear": 2013,
    "position": 28,
    "releaseyear": "1999",
    "track": "Scar Tissue"
    },
    {
    "alltime": True,
    "artist": "Franz Ferdinand",
    "country": "UK",
    "id": "2630",
    "pollyear": 2013,
    "position": 29,
    "releaseyear": "2004",
    "track": "Take Me Out"
    },
    {
    "alltime": True,
    "artist": "Red Hot Chili Peppers",
    "country": "USA",
    "id": "2631",
    "pollyear": 2013,
    "position": 30,
    "releaseyear": "2000",
    "track": "Californication"
    },
    {
    "alltime": True,
    "artist": "Massive Attack",
    "country": "UK",
    "id": "2632",
    "pollyear": 2013,
    "position": 31,
    "releaseyear": "1998",
    "track": "Teardrop"
    },
    {
    "alltime": True,
    "artist": "Tool",
    "country": "USA",
    "id": "2633",
    "pollyear": 2013,
    "position": 32,
    "releaseyear": "1996",
    "track": "Stinkfist"
    },
    {
    "alltime": True,
    "artist": "The Cranberries",
    "country": "UK",
    "id": "2634",
    "pollyear": 2013,
    "position": 33,
    "releaseyear": "1994",
    "track": "Zombie"
    },
    {
    "alltime": True,
    "artist": "Ben Folds Five",
    "country": "USA",
    "id": "2635",
    "pollyear": 2013,
    "position": 34,
    "releaseyear": "1998",
    "track": "Brick"
    },
    {
    "alltime": True,
    "artist": "Radiohead",
    "country": "UK",
    "id": "2636",
    "pollyear": 2013,
    "position": 35,
    "releaseyear": "1997",
    "track": "Karma Police"
    },
    {
    "alltime": True,
    "artist": "Jeff Buckley",
    "country": "USA",
    "id": "2637",
    "pollyear": 2013,
    "position": 36,
    "releaseyear": "1994",
    "track": "Hallelujah"
    },
    {
    "alltime": True,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "2638",
    "pollyear": 2013,
    "position": 37,
    "releaseyear": "1994",
    "track": "Sabotage"
    },
    {
    "alltime": True,
    "artist": "The Temper Trap",
    "country": "Australia",
    "id": "2639",
    "pollyear": 2013,
    "position": 38,
    "releaseyear": "2008",
    "track": "Sweet Disposition"
    },
    {
    "alltime": True,
    "artist": "Nirvana",
    "country": "USA",
    "id": "2640",
    "pollyear": 2013,
    "position": 39,
    "releaseyear": "1993",
    "track": "Heart Shaped Box"
    },
    {
    "alltime": True,
    "artist": "Nine Inch Nails",
    "country": "USA",
    "id": "2641",
    "pollyear": 2013,
    "position": 40,
    "releaseyear": "1994",
    "track": "Closer"
    },
    {
    "alltime": True,
    "artist": "Coldplay",
    "country": "UK",
    "id": "2642",
    "pollyear": 2013,
    "position": 41,
    "releaseyear": "2000",
    "track": "Yellow"
    },
    {
    "alltime": True,
    "artist": "Matt Corby",
    "country": "Australia",
    "id": "2643",
    "pollyear": 2013,
    "position": 42,
    "releaseyear": "2011",
    "track": "Brother"
    },
    {
    "alltime": True,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "2644",
    "pollyear": 2013,
    "position": 43,
    "releaseyear": "2001",
    "track": "Betterman"
    },
    {
    "alltime": True,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2645",
    "pollyear": 2013,
    "position": 44,
    "releaseyear": "2001",
    "track": "One More Time"
    },
    {
    "alltime": True,
    "artist": "Modest Mouse",
    "country": "USA",
    "id": "2646",
    "pollyear": 2013,
    "position": 45,
    "releaseyear": "2004",
    "track": "Float On"
    },
    {
    "alltime": True,
    "artist": "Nick Cave & The Bad Seeds",
    "country": "Australia",
    "id": "2647",
    "pollyear": 2013,
    "position": 46,
    "releaseyear": "1997",
    "track": "Into My Arms"
    },
    {
    "alltime": True,
    "artist": "The Offspring",
    "country": "USA",
    "id": "2648",
    "pollyear": 2013,
    "position": 47,
    "releaseyear": "1994",
    "track": "Self Esteem"
    },
    {
    "alltime": True,
    "artist": "The Strokes",
    "country": "USA",
    "id": "2649",
    "pollyear": 2013,
    "position": 48,
    "releaseyear": "2001",
    "track": "Last Nite"
    },
    {
    "alltime": True,
    "artist": "Florence + the Machine",
    "country": "UK",
    "id": "2650",
    "pollyear": 2013,
    "position": 49,
    "releaseyear": "2009",
    "track": "Dog Days Are Over"
    },
    {
    "alltime": True,
    "artist": "Pearl Jam",
    "country": "USA",
    "id": "2651",
    "pollyear": 2013,
    "position": 50,
    "releaseyear": "1995",
    "track": "Better Man"
    },
    {
    "alltime": True,
    "artist": "The Dandy Warhols",
    "country": "USA",
    "id": "2652",
    "pollyear": 2013,
    "position": 51,
    "releaseyear": "2000",
    "track": "Bohemian Like You"
    },
    {
    "alltime": True,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "2653",
    "pollyear": 2013,
    "position": 52,
    "releaseyear": "2005",
    "track": "Feel Good Inc"
    },
    {
    "alltime": True,
    "artist": "Placebo",
    "country": "UK",
    "id": "2654",
    "pollyear": 2013,
    "position": 53,
    "releaseyear": "1999",
    "track": "Every You Every Me"
    },
    {
    "alltime": True,
    "artist": "Kings Of Leon",
    "country": "USA",
    "id": "2655",
    "pollyear": 2013,
    "position": 54,
    "releaseyear": "2008",
    "track": "Sex On Fire"
    },
    {
    "alltime": True,
    "artist": "Fatboy Slim",
    "country": "UK",
    "id": "2656",
    "pollyear": 2013,
    "position": 55,
    "releaseyear": "1999",
    "track": "Praise You"
    },
    {
    "alltime": True,
    "artist": "Underworld",
    "country": "UK",
    "id": "2657",
    "pollyear": 2013,
    "position": 56,
    "releaseyear": "1996",
    "track": "Born Slippy .NUXX"
    },
    {
    "alltime": True,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "2658",
    "pollyear": 2013,
    "position": 57,
    "releaseyear": "2004",
    "track": "Banquet"
    },
    {
    "alltime": True,
    "artist": "The Whitlams",
    "country": "Australia",
    "id": "2659",
    "pollyear": 2013,
    "position": 58,
    "releaseyear": "1997",
    "track": "No Aphrodisiac"
    },
    {
    "alltime": True,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2660",
    "pollyear": 2013,
    "position": 59,
    "releaseyear": "1997",
    "track": "Around The World"
    },
    {
    "alltime": True,
    "artist": "Bush",
    "country": "UK",
    "id": "2661",
    "pollyear": 2013,
    "position": 60,
    "releaseyear": "1996",
    "track": "Glycerine"
    },
    {
    "alltime": True,
    "artist": "The Black Keys",
    "country": "USA",
    "id": "2662",
    "pollyear": 2013,
    "position": 61,
    "releaseyear": "2011",
    "track": "Lonely Boy"
    },
    {
    "alltime": True,
    "artist": "Spiderbait",
    "country": "Australia",
    "id": "2663",
    "pollyear": 2013,
    "position": 62,
    "releaseyear": "1996",
    "track": "Buy Me A Pony"
    },
    {
    "alltime": True,
    "artist": "Grinspoon",
    "country": "Australia",
    "id": "2664",
    "pollyear": 2013,
    "position": 63,
    "releaseyear": "2002",
    "track": "Chemical Heart"
    },
    {
    "alltime": True,
    "artist": "MGMT",
    "country": "USA",
    "id": "2665",
    "pollyear": 2013,
    "position": 64,
    "releaseyear": "2008",
    "track": "Kids"
    },
    {
    "alltime": True,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2666",
    "pollyear": 2013,
    "position": 65,
    "releaseyear": "2001",
    "track": "Harder, Better, Faster, Stronger"
    },
    {
    "alltime": True,
    "artist": "You Am I",
    "country": "Australia",
    "id": "2667",
    "pollyear": 2013,
    "position": 66,
    "releaseyear": "1994",
    "track": "Berlin Chair"
    },
    {
    "alltime": True,
    "artist": "alt-J",
    "country": "UK",
    "id": "2668",
    "pollyear": 2013,
    "position": 67,
    "releaseyear": "2012",
    "track": "Breezeblocks"
    },
    {
    "alltime": True,
    "artist": "Jet",
    "country": "Australia",
    "id": "2669",
    "pollyear": 2013,
    "position": 68,
    "releaseyear": "2003",
    "track": "Are You Gonna Be My Girl"
    },
    {
    "alltime": True,
    "artist": "Eminem",
    "country": "USA",
    "id": "2670",
    "pollyear": 2013,
    "position": 69,
    "releaseyear": "2002",
    "track": "Lose Yourself"
    },
    {
    "alltime": True,
    "artist": "Regurgitator",
    "country": "Australia",
    "id": "2671",
    "pollyear": 2013,
    "position": 70,
    "releaseyear": "1998",
    "track": "! (The Song Formerly Known As)"
    },
    {
    "alltime": True,
    "artist": "Gorillaz",
    "country": "UK",
    "id": "2672",
    "pollyear": 2013,
    "position": 71,
    "releaseyear": "2001",
    "track": "Clint Eastwood"
    },
    {
    "alltime": True,
    "artist": "Wolfmother",
    "country": "Australia",
    "id": "2673",
    "pollyear": 2013,
    "position": 72,
    "releaseyear": "2005",
    "track": "Joker And The Thief"
    },
    {
    "alltime": True,
    "artist": "Edward Sharpe & The Magnetic Zeros",
    "country": "USA",
    "id": "2674",
    "pollyear": 2013,
    "position": 73,
    "releaseyear": "2009",
    "track": "Home"
    },
    {
    "alltime": True,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2675",
    "pollyear": 2013,
    "position": 74,
    "releaseyear": "2007",
    "track": "Let's Dance To Joy Division"
    },
    {
    "alltime": True,
    "artist": "The Killers",
    "country": "USA",
    "id": "2676",
    "pollyear": 2013,
    "position": 75,
    "releaseyear": "2004",
    "track": "Somebody Told Me"
    },
    {
    "alltime": True,
    "artist": "MGMT",
    "country": "USA",
    "id": "2677",
    "pollyear": 2013,
    "position": 76,
    "releaseyear": "2008",
    "track": "Electric Feel"
    },
    {
    "alltime": True,
    "artist": "The Presets",
    "country": "Australia",
    "id": "2678",
    "pollyear": 2013,
    "position": 77,
    "releaseyear": "2007",
    "track": "My People"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2679",
    "pollyear": 2013,
    "position": 78,
    "releaseyear": "1997",
    "track": "Freak"
    },
    {
    "alltime": True,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "2680",
    "pollyear": 2013,
    "position": 79,
    "releaseyear": "2005",
    "track": "I Bet You Look Good On The Dancefloor"
    },
    {
    "alltime": True,
    "artist": "Rage Against The Machine",
    "country": "USA",
    "id": "2681",
    "pollyear": 2013,
    "position": 80,
    "releaseyear": "1996",
    "track": "Bulls On Parade"
    },
    {
    "alltime": True,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "2682",
    "pollyear": 2013,
    "position": 81,
    "releaseyear": "2010",
    "track": "Big Jet Plane"
    },
    {
    "alltime": True,
    "artist": "Wheatus",
    "country": "USA",
    "id": "2683",
    "pollyear": 2013,
    "position": 82,
    "releaseyear": "2000",
    "track": "Teenage Dirtbag"
    },
    {
    "alltime": True,
    "artist": "Pulp",
    "country": "UK",
    "id": "2684",
    "pollyear": 2013,
    "position": 83,
    "releaseyear": "1995",
    "track": "Common People"
    },
    {
    "alltime": True,
    "artist": "Kanye West",
    "country": "USA",
    "id": "2685",
    "pollyear": 2013,
    "position": 84,
    "releaseyear": "2005",
    "track": "Gold Digger {ft. Jamie Foxx}"
    },
    {
    "alltime": True,
    "artist": "Coolio",
    "country": "USA",
    "id": "2686",
    "pollyear": 2013,
    "position": 85,
    "releaseyear": "1995",
    "track": "Gangsta's Paradise"
    },
    {
    "alltime": True,
    "artist": "The Killers",
    "country": "USA",
    "id": "2687",
    "pollyear": 2013,
    "position": 86,
    "releaseyear": "2006",
    "track": "When You Were Young"
    },
    {
    "alltime": True,
    "artist": "The Kooks",
    "country": "UK",
    "id": "2688",
    "pollyear": 2013,
    "position": 87,
    "releaseyear": "2006",
    "track": "Naive"
    },
    {
    "alltime": True,
    "artist": "Something For Kate",
    "country": "Australia",
    "id": "2689",
    "pollyear": 2013,
    "position": 88,
    "releaseyear": "2001",
    "track": "Monsters"
    },
    {
    "alltime": True,
    "artist": "TV On The Radio",
    "country": "USA",
    "id": "2690",
    "pollyear": 2013,
    "position": 89,
    "releaseyear": "2006",
    "track": "Wolf Like Me"
    },
    {
    "alltime": True,
    "artist": "Silverchair",
    "country": "Australia",
    "id": "2691",
    "pollyear": 2013,
    "position": 90,
    "releaseyear": "2007",
    "track": "Straight Lines"
    },
    {
    "alltime": True,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "2692",
    "pollyear": 2013,
    "position": 91,
    "releaseyear": "1998",
    "track": "Harpoon"
    },
    {
    "alltime": True,
    "artist": "Of Monsters And Men",
    "country": "Iceland",
    "id": "2693",
    "pollyear": 2013,
    "position": 92,
    "releaseyear": "2012",
    "track": "Little Talks"
    },
    {
    "alltime": True,
    "artist": "Soundgarden",
    "country": "USA",
    "id": "2694",
    "pollyear": 2013,
    "position": 93,
    "releaseyear": "1994",
    "track": "Black Hole Sun"
    },
    {
    "alltime": True,
    "artist": "Foster The People",
    "country": "USA",
    "id": "2695",
    "pollyear": 2013,
    "position": 94,
    "releaseyear": "2010",
    "track": "Pumped Up Kicks"
    },
    {
    "alltime": True,
    "artist": "Ben Lee",
    "country": "Australia",
    "id": "2696",
    "pollyear": 2013,
    "position": 95,
    "releaseyear": "1998",
    "track": "Cigarettes Will Kill You"
    },
    {
    "alltime": True,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "2697",
    "pollyear": 2013,
    "position": 96,
    "releaseyear": "2003",
    "track": "Hello"
    },
    {
    "alltime": True,
    "artist": "M.I.A.",
    "country": "UK",
    "id": "2698",
    "pollyear": 2013,
    "position": 97,
    "releaseyear": "2007",
    "track": "Paper Planes"
    },
    {
    "alltime": True,
    "artist": "Jebediah",
    "country": "Australia",
    "id": "2699",
    "pollyear": 2013,
    "position": 98,
    "releaseyear": "1997",
    "track": "Leaving Home"
    },
    {
    "alltime": True,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2700",
    "pollyear": 2013,
    "position": 99,
    "releaseyear": "2011",
    "track": "Video Games"
    },
    {
    "alltime": True,
    "artist": "Beastie Boys",
    "country": "USA",
    "id": "2701",
    "pollyear": 2013,
    "position": 100,
    "releaseyear": "1998",
    "track": "Intergalactic"
    },
    {
    "alltime": False,
    "artist": "Vance Joy",
    "country": "Australia",
    "id": "2702",
    "pollyear": 2013,
    "position": 1,
    "releaseyear": "2013",
    "track": "Riptide"
    },
    {
    "alltime": False,
    "artist": "Lorde",
    "country": "New Zealand",
    "id": "2703",
    "pollyear": 2013,
    "position": 2,
    "releaseyear": "2013",
    "track": "Royals"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2704",
    "pollyear": 2013,
    "position": 3,
    "releaseyear": "2013",
    "track": "Get Lucky {Ft. Pharrell Williams & Nile Rodgers}"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "2705",
    "pollyear": 2013,
    "position": 4,
    "releaseyear": "2013",
    "track": "Do I Wanna Know?"
    },
    {
    "alltime": False,
    "artist": "Flume & Chet Faker",
    "country": "Australia",
    "id": "2706",
    "pollyear": 2013,
    "position": 5,
    "releaseyear": "2013",
    "track": "Drop The Game"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "2707",
    "pollyear": 2013,
    "position": 6,
    "releaseyear": "2013",
    "track": "Why'd You Only Call Me When You're High?"
    },
    {
    "alltime": False,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2708",
    "pollyear": 2013,
    "position": 7,
    "releaseyear": "2013",
    "track": "Young And Beautiful"
    },
    {
    "alltime": False,
    "artist": "Matt Corby",
    "country": "Australia",
    "id": "2709",
    "pollyear": 2013,
    "position": 8,
    "releaseyear": "2013",
    "track": "Resolution"
    },
    {
    "alltime": False,
    "artist": "The Preatures",
    "country": "Australia",
    "id": "2710",
    "pollyear": 2013,
    "position": 9,
    "releaseyear": "2013",
    "track": "Is This How You Feel?"
    },
    {
    "alltime": False,
    "artist": "London Grammar",
    "country": "UK",
    "id": "2711",
    "pollyear": 2013,
    "position": 10,
    "releaseyear": "2013",
    "track": "Strong"
    },
    {
    "alltime": False,
    "artist": "HAIM",
    "country": "USA",
    "id": "2712",
    "pollyear": 2013,
    "position": 11,
    "releaseyear": "2013",
    "track": "The Wire"
    },
    {
    "alltime": False,
    "artist": "Lorde",
    "country": "New Zealand",
    "id": "2713",
    "pollyear": 2013,
    "position": 12,
    "releaseyear": "2013",
    "track": "Tennis Court"
    },
    {
    "alltime": False,
    "artist": "James Blake",
    "country": "UK",
    "id": "2714",
    "pollyear": 2013,
    "position": 13,
    "releaseyear": "2013",
    "track": "Retrograde"
    },
    {
    "alltime": False,
    "artist": "Violent Soho",
    "country": "Australia",
    "id": "2715",
    "pollyear": 2013,
    "position": 14,
    "releaseyear": "2013",
    "track": "Covered In Chrome"
    },
    {
    "alltime": False,
    "artist": "Lorde",
    "country": "New Zealand",
    "id": "2716",
    "pollyear": 2013,
    "position": 15,
    "releaseyear": "2013",
    "track": "Team"
    },
    {
    "alltime": False,
    "artist": "Arcade Fire",
    "country": "Canada",
    "id": "2717",
    "pollyear": 2013,
    "position": 16,
    "releaseyear": "2013",
    "track": "Reflektor"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2718",
    "pollyear": 2013,
    "position": 17,
    "releaseyear": "2013",
    "track": "Lose Yourself To Dance {Ft. Pharrell Williams}"
    },
    {
    "alltime": False,
    "artist": "Arctic Monkeys",
    "country": "UK",
    "id": "2719",
    "pollyear": 2013,
    "position": 18,
    "releaseyear": "2013",
    "track": "Arabella"
    },
    {
    "alltime": False,
    "artist": "The Kite String Tangle",
    "country": "Australia",
    "id": "2720",
    "pollyear": 2013,
    "position": 19,
    "releaseyear": "2013",
    "track": "Given The Chance"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "2721",
    "pollyear": 2013,
    "position": 20,
    "releaseyear": "2013",
    "track": "Black Skinhead"
    },
    {
    "alltime": False,
    "artist": "RUFUS",
    "country": "Australia",
    "id": "2722",
    "pollyear": 2013,
    "position": 21,
    "releaseyear": "2013",
    "track": "Take Me"
    },
    {
    "alltime": False,
    "artist": "Birds Of Tokyo",
    "country": "Australia",
    "id": "2723",
    "pollyear": 2013,
    "position": 22,
    "releaseyear": "2013",
    "track": "Lanterns"
    },
    {
    "alltime": False,
    "artist": "Disclosure",
    "country": "UK",
    "id": "2724",
    "pollyear": 2013,
    "position": 23,
    "releaseyear": "2013",
    "track": "When A Fire Starts To Burn"
    },
    {
    "alltime": False,
    "artist": "Rudimental",
    "country": "UK",
    "id": "2725",
    "pollyear": 2013,
    "position": 24,
    "releaseyear": "2013",
    "track": "Waiting All Night {Ft. Ella Eyre}"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2726",
    "pollyear": 2013,
    "position": 25,
    "releaseyear": "2013",
    "track": "Your Body Is A Weapon"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "2727",
    "pollyear": 2013,
    "position": 26,
    "releaseyear": "2013",
    "track": "Step"
    },
    {
    "alltime": False,
    "artist": "HAIM",
    "country": "USA",
    "id": "2728",
    "pollyear": 2013,
    "position": 27,
    "releaseyear": "2013",
    "track": "Falling"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2729",
    "pollyear": 2013,
    "position": 28,
    "releaseyear": "2013",
    "track": "Recover"
    },
    {
    "alltime": False,
    "artist": "Foals",
    "country": "UK",
    "id": "2730",
    "pollyear": 2013,
    "position": 29,
    "releaseyear": "2013",
    "track": "My Number"
    },
    {
    "alltime": False,
    "artist": "Empire Of The Sun",
    "country": "Australia",
    "id": "2731",
    "pollyear": 2013,
    "position": 30,
    "releaseyear": "2013",
    "track": "Alive"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "2732",
    "pollyear": 2013,
    "position": 31,
    "releaseyear": "2013",
    "track": "Diane Young"
    },
    {
    "alltime": False,
    "artist": "Thundamentals",
    "country": "Australia",
    "id": "2733",
    "pollyear": 2013,
    "position": 32,
    "releaseyear": "2013",
    "track": "Smiles Don't Lie"
    },
    {
    "alltime": False,
    "artist": "Grouplove",
    "country": "USA",
    "id": "2734",
    "pollyear": 2013,
    "position": 33,
    "releaseyear": "2013",
    "track": "Ways To Go"
    },
    {
    "alltime": False,
    "artist": "RUFUS",
    "country": "Australia",
    "id": "2735",
    "pollyear": 2013,
    "position": 34,
    "releaseyear": "2013",
    "track": "Desert Night"
    },
    {
    "alltime": False,
    "artist": "London Grammar",
    "country": "UK",
    "id": "2736",
    "pollyear": 2013,
    "position": 35,
    "releaseyear": "2013",
    "track": "Hey Now"
    },
    {
    "alltime": False,
    "artist": "Bloc Party",
    "country": "UK",
    "id": "2737",
    "pollyear": 2013,
    "position": 36,
    "releaseyear": "2013",
    "track": "Ratchet"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2738",
    "pollyear": 2013,
    "position": 37,
    "releaseyear": "2013",
    "track": "Gun"
    },
    {
    "alltime": False,
    "artist": "Touch Sensitive",
    "country": "Australia",
    "id": "2739",
    "pollyear": 2013,
    "position": 38,
    "releaseyear": "2013",
    "track": "Pizza Guy"
    },
    {
    "alltime": False,
    "artist": "San Cisco",
    "country": "Australia",
    "id": "2740",
    "pollyear": 2013,
    "position": 39,
    "releaseyear": "2013",
    "track": "Get Lucky {Like A Version}"
    },
    {
    "alltime": False,
    "artist": "The Amity Affliction",
    "country": "Australia",
    "id": "2741",
    "pollyear": 2013,
    "position": 40,
    "releaseyear": "2013",
    "track": "Born To Die"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "2742",
    "pollyear": 2013,
    "position": 41,
    "releaseyear": "2013",
    "track": "Southern Sun"
    },
    {
    "alltime": False,
    "artist": "Max Frost",
    "country": "USA",
    "id": "2743",
    "pollyear": 2013,
    "position": 42,
    "releaseyear": "2013",
    "track": "White Lies"
    },
    {
    "alltime": False,
    "artist": "Childish Gambino",
    "country": "USA",
    "id": "2744",
    "pollyear": 2013,
    "position": 43,
    "releaseyear": "2013",
    "track": "3005"
    },
    {
    "alltime": False,
    "artist": "Dustin Tebbutt",
    "country": "Australia",
    "id": "2745",
    "pollyear": 2013,
    "position": 44,
    "releaseyear": "2013",
    "track": "The Breach"
    },
    {
    "alltime": False,
    "artist": "Robert Delong",
    "country": "USA",
    "id": "2746",
    "pollyear": 2013,
    "position": 45,
    "releaseyear": "2013",
    "track": "Global Concepts"
    },
    {
    "alltime": False,
    "artist": "Queens Of The Stone Age",
    "country": "USA",
    "id": "2747",
    "pollyear": 2013,
    "position": 46,
    "releaseyear": "2013",
    "track": "If I Had A Tail"
    },
    {
    "alltime": False,
    "artist": "Rudimental",
    "country": "UK",
    "id": "2748",
    "pollyear": 2013,
    "position": 47,
    "releaseyear": "2013",
    "track": "Free {Ft. Emeli Sande}"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2749",
    "pollyear": 2013,
    "position": 48,
    "releaseyear": "2013",
    "track": "Stand Still {Ft. Micky Green}"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2750",
    "pollyear": 2013,
    "position": 49,
    "releaseyear": "2013",
    "track": "Doin' It Right {Ft. Panda Bear}"
    },
    {
    "alltime": False,
    "artist": "John Newman",
    "country": "UK",
    "id": "2751",
    "pollyear": 2013,
    "position": 50,
    "releaseyear": "2013",
    "track": "Love Me Again"
    },
    {
    "alltime": False,
    "artist": "Fatboy Slim & Riva Starr",
    "country": "UK",
    "id": "2752",
    "pollyear": 2013,
    "position": 51,
    "releaseyear": "2013",
    "track": "Eat Sleep Rave Repeat"
    },
    {
    "alltime": False,
    "artist": "Cloud Control",
    "country": "Australia",
    "id": "2753",
    "pollyear": 2013,
    "position": 52,
    "releaseyear": "2013",
    "track": "Scar"
    },
    {
    "alltime": False,
    "artist": "Kingswood",
    "country": "Australia",
    "id": "2754",
    "pollyear": 2013,
    "position": 53,
    "releaseyear": "2013",
    "track": "Ohio"
    },
    {
    "alltime": False,
    "artist": "Arcade Fire",
    "country": "Canada",
    "id": "2755",
    "pollyear": 2013,
    "position": 54,
    "releaseyear": "2013",
    "track": "Afterlife"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "2756",
    "pollyear": 2013,
    "position": 55,
    "releaseyear": "2013",
    "track": "Harlequin Dream"
    },
    {
    "alltime": False,
    "artist": "HAIM",
    "country": "USA",
    "id": "2757",
    "pollyear": 2013,
    "position": 56,
    "releaseyear": "2013",
    "track": "If I Could Change Your Mind"
    },
    {
    "alltime": False,
    "artist": "Andy Bull",
    "country": "Australia",
    "id": "2758",
    "pollyear": 2013,
    "position": 57,
    "releaseyear": "2013",
    "track": "Keep On Running"
    },
    {
    "alltime": False,
    "artist": "Daft Punk",
    "country": "France",
    "id": "2759",
    "pollyear": 2013,
    "position": 58,
    "releaseyear": "2013",
    "track": "Instant Crush {Ft. Julian Casablancas}"
    },
    {
    "alltime": False,
    "artist": "Kanye West",
    "country": "USA",
    "id": "2760",
    "pollyear": 2013,
    "position": 59,
    "releaseyear": "2013",
    "track": "Bound 2"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2761",
    "pollyear": 2013,
    "position": 60,
    "releaseyear": "2013",
    "track": "Lies"
    },
    {
    "alltime": False,
    "artist": "London Grammar",
    "country": "UK",
    "id": "2762",
    "pollyear": 2013,
    "position": 61,
    "releaseyear": "2013",
    "track": "Wasting My Young Years"
    },
    {
    "alltime": False,
    "artist": "Goldroom",
    "country": "USA",
    "id": "2763",
    "pollyear": 2013,
    "position": 62,
    "releaseyear": "2013",
    "track": "Embrace"
    },
    {
    "alltime": False,
    "artist": "Disclosure",
    "country": "UK",
    "id": "2764",
    "pollyear": 2013,
    "position": 63,
    "releaseyear": "2013",
    "track": "You & Me {Flume Remix}"
    },
    {
    "alltime": False,
    "artist": "The National",
    "country": "USA",
    "id": "2765",
    "pollyear": 2013,
    "position": 64,
    "releaseyear": "2013",
    "track": "Graceless"
    },
    {
    "alltime": False,
    "artist": "Chet Faker",
    "country": "Australia",
    "id": "2766",
    "pollyear": 2013,
    "position": 65,
    "releaseyear": "2013",
    "track": "Melt {Ft. Kilo Kish}"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "2767",
    "pollyear": 2013,
    "position": 66,
    "releaseyear": "2013",
    "track": "Ausmusic Month Medley {Like A Version}"
    },
    {
    "alltime": False,
    "artist": "Bliss N Eso",
    "country": "Australia",
    "id": "2768",
    "pollyear": 2013,
    "position": 67,
    "releaseyear": "2013",
    "track": "Act Your Age"
    },
    {
    "alltime": False,
    "artist": "Something For Kate",
    "country": "Australia",
    "id": "2769",
    "pollyear": 2013,
    "position": 68,
    "releaseyear": "2013",
    "track": "Sweet Nothing {Like A Version}"
    },
    {
    "alltime": False,
    "artist": "Disclosure",
    "country": "UK",
    "id": "2770",
    "pollyear": 2013,
    "position": 69,
    "releaseyear": "2013",
    "track": "White Noise {Ft. AlunaGeorge}"
    },
    {
    "alltime": False,
    "artist": "Sticky Fingers",
    "country": "Australia",
    "id": "2771",
    "pollyear": 2013,
    "position": 70,
    "releaseyear": "2013",
    "track": "Australia Street"
    },
    {
    "alltime": False,
    "artist": "Two Door Cinema Club",
    "country": "UK",
    "id": "2772",
    "pollyear": 2013,
    "position": 71,
    "releaseyear": "2013",
    "track": "Changing Of The Seasons"
    },
    {
    "alltime": False,
    "artist": "Queens Of The Stone Age",
    "country": "USA",
    "id": "2773",
    "pollyear": 2013,
    "position": 72,
    "releaseyear": "2013",
    "track": "I Sat By The Ocean"
    },
    {
    "alltime": False,
    "artist": "Busta Rhymes",
    "country": "USA",
    "id": "2774",
    "pollyear": 2013,
    "position": 73,
    "releaseyear": "2013",
    "track": "Thank You {Ft. Q-Tip, Kanye West & Lil Wayne}"
    },
    {
    "alltime": False,
    "artist": "Major Lazer",
    "country": "USA",
    "id": "2775",
    "pollyear": 2013,
    "position": 74,
    "releaseyear": "2013",
    "track": "Jessica {Ft. Ezra Koenig}"
    },
    {
    "alltime": False,
    "artist": "Mikhael Paskalev",
    "country": "Norway",
    "id": "2776",
    "pollyear": 2013,
    "position": 75,
    "releaseyear": "2013",
    "track": "I Spy"
    },
    {
    "alltime": False,
    "artist": "SAFIA",
    "country": "Australia",
    "id": "2777",
    "pollyear": 2013,
    "position": 76,
    "releaseyear": "2013",
    "track": "Listen To Soul, Listen To Blues"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "2778",
    "pollyear": 2013,
    "position": 77,
    "releaseyear": "2013",
    "track": "Youngbloods {Ft. Ahren Stringer}"
    },
    {
    "alltime": False,
    "artist": "MS MR",
    "country": "USA",
    "id": "2779",
    "pollyear": 2013,
    "position": 78,
    "releaseyear": "2013",
    "track": "Fantasy"
    },
    {
    "alltime": False,
    "artist": "A$AP Rocky",
    "country": "USA",
    "id": "2780",
    "pollyear": 2013,
    "position": 79,
    "releaseyear": "2013",
    "track": "F**kin' Problems {Ft. Drake, 2 Chainz & Kendrick Lamar}"
    },
    {
    "alltime": False,
    "artist": "Panama",
    "country": "Australia",
    "id": "2781",
    "pollyear": 2013,
    "position": 80,
    "releaseyear": "2013",
    "track": "Always"
    },
    {
    "alltime": False,
    "artist": "Andy Bull",
    "country": "Australia",
    "id": "2782",
    "pollyear": 2013,
    "position": 81,
    "releaseyear": "2013",
    "track": "Baby I Am Nobody Now"
    },
    {
    "alltime": False,
    "artist": "Cloud Control",
    "country": "Australia",
    "id": "2783",
    "pollyear": 2013,
    "position": 82,
    "releaseyear": "2013",
    "track": "Dojo Rising"
    },
    {
    "alltime": False,
    "artist": "The Jezabels",
    "country": "Australia",
    "id": "2784",
    "pollyear": 2013,
    "position": 83,
    "releaseyear": "2013",
    "track": "The End"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "2785",
    "pollyear": 2013,
    "position": 84,
    "releaseyear": "2013",
    "track": "Summer Forgive Me"
    },
    {
    "alltime": False,
    "artist": "Remi",
    "country": "Australia",
    "id": "2786",
    "pollyear": 2013,
    "position": 85,
    "releaseyear": "2013",
    "track": "Sangria"
    },
    {
    "alltime": False,
    "artist": "Bring Me The Horizon",
    "country": "UK",
    "id": "2787",
    "pollyear": 2013,
    "position": 86,
    "releaseyear": "2013",
    "track": "Sleepwalking"
    },
    {
    "alltime": False,
    "artist": "John Butler Trio",
    "country": "Australia",
    "id": "2788",
    "pollyear": 2013,
    "position": 87,
    "releaseyear": "2013",
    "track": "Only One"
    },
    {
    "alltime": False,
    "artist": "Josh Pyke",
    "country": "Australia",
    "id": "2789",
    "pollyear": 2013,
    "position": 88,
    "releaseyear": "2013",
    "track": "Leeward Side"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "2790",
    "pollyear": 2013,
    "position": 89,
    "releaseyear": "2013",
    "track": "Brighter Than Gold"
    },
    {
    "alltime": False,
    "artist": "Vampire Weekend",
    "country": "USA",
    "id": "2791",
    "pollyear": 2013,
    "position": 90,
    "releaseyear": "2013",
    "track": "Unbelievers"
    },
    {
    "alltime": False,
    "artist": "RUFUS",
    "country": "Australia",
    "id": "2792",
    "pollyear": 2013,
    "position": 91,
    "releaseyear": "2013",
    "track": "Tonight"
    },
    {
    "alltime": False,
    "artist": "Bring Me The Horizon",
    "country": "UK",
    "id": "2793",
    "pollyear": 2013,
    "position": 92,
    "releaseyear": "2013",
    "track": "Shadow Moses"
    },
    {
    "alltime": False,
    "artist": "St Lucia",
    "country": "USA",
    "id": "2794",
    "pollyear": 2013,
    "position": 93,
    "releaseyear": "2013",
    "track": "Elevate"
    },
    {
    "alltime": False,
    "artist": "Bliss N Eso",
    "country": "Australia",
    "id": "2795",
    "pollyear": 2013,
    "position": 94,
    "releaseyear": "2013",
    "track": "House Of Dreams"
    },
    {
    "alltime": False,
    "artist": "Vance Joy",
    "country": "Australia",
    "id": "2796",
    "pollyear": 2013,
    "position": 95,
    "releaseyear": "2013",
    "track": "Play With Fire"
    },
    {
    "alltime": False,
    "artist": "Big Scary",
    "country": "Australia",
    "id": "2797",
    "pollyear": 2013,
    "position": 96,
    "releaseyear": "2013",
    "track": "Luck Now"
    },
    {
    "alltime": False,
    "artist": "Queens Of The Stone Age",
    "country": "USA",
    "id": "2798",
    "pollyear": 2013,
    "position": 97,
    "releaseyear": "2013",
    "track": "My God Is The Sun"
    },
    {
    "alltime": False,
    "artist": "Horrorshow",
    "country": "Australia",
    "id": "2799",
    "pollyear": 2013,
    "position": 98,
    "releaseyear": "2013",
    "track": "Dead Star Shine"
    },
    {
    "alltime": False,
    "artist": "Dillon Francis",
    "country": "USA",
    "id": "2800",
    "pollyear": 2013,
    "position": 99,
    "releaseyear": "2013",
    "track": "Without You {Ft. Totally Enormous Extinct Dinosaurs}"
    },
    {
    "alltime": False,
    "artist": "Karnivool",
    "country": "Australia",
    "id": "2801",
    "pollyear": 2013,
    "position": 100,
    "releaseyear": "2013",
    "track": "We Are"
    },
    {
    "alltime": False,
    "artist": "Chet Faker",
    "country": "Australia",
    "id": "2802",
    "pollyear": 2014,
    "position": 1,
    "releaseyear": "2014",
    "track": "Talk Is Cheap"
    },
    {
    "alltime": False,
    "artist": "Peking Duk",
    "country": "Australia",
    "id": "2803",
    "pollyear": 2014,
    "position": 2,
    "releaseyear": "2014",
    "track": "High {Ft. Nicole Millar}"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2804",
    "pollyear": 2014,
    "position": 3,
    "releaseyear": "2014",
    "track": "Cosby Sweater"
    },
    {
    "alltime": False,
    "artist": "Milky Chance",
    "country": "Germany",
    "id": "2805",
    "pollyear": 2014,
    "position": 4,
    "releaseyear": "2014",
    "track": "Stolen Dance"
    },
    {
    "alltime": False,
    "artist": "Peking Duk",
    "country": "Australia",
    "id": "2806",
    "pollyear": 2014,
    "position": 5,
    "releaseyear": "2014",
    "track": "Take Me Over {Ft. SAFIA}"
    },
    {
    "alltime": False,
    "artist": "Mark Ronson",
    "country": "UK",
    "id": "2807",
    "pollyear": 2014,
    "position": 6,
    "releaseyear": "2014",
    "track": "Uptown Funk {Ft. Bruno Mars}"
    },
    {
    "alltime": False,
    "artist": "Chet Faker",
    "country": "Australia",
    "id": "2808",
    "pollyear": 2014,
    "position": 7,
    "releaseyear": "2014",
    "track": "Gold"
    },
    {
    "alltime": False,
    "artist": "Chet Faker",
    "country": "Australia",
    "id": "2809",
    "pollyear": 2014,
    "position": 8,
    "releaseyear": "2014",
    "track": "1998"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "2810",
    "pollyear": 2014,
    "position": 9,
    "releaseyear": "2014",
    "track": "Chandelier"
    },
    {
    "alltime": False,
    "artist": "Asgeir",
    "country": "Iceland",
    "id": "2811",
    "pollyear": 2014,
    "position": 10,
    "releaseyear": "2014",
    "track": "King And Cross"
    },
    {
    "alltime": False,
    "artist": "ZHU",
    "country": "USA",
    "id": "2812",
    "pollyear": 2014,
    "position": 11,
    "releaseyear": "2014",
    "track": "Faded"
    },
    {
    "alltime": False,
    "artist": "Glass Animals",
    "country": "UK",
    "id": "2813",
    "pollyear": 2014,
    "position": 12,
    "releaseyear": "2014",
    "track": "Gooey"
    },
    {
    "alltime": False,
    "artist": "Vance Joy",
    "country": "Australia",
    "id": "2814",
    "pollyear": 2014,
    "position": 13,
    "releaseyear": "2014",
    "track": "Mess Is Mine"
    },
    {
    "alltime": False,
    "artist": "alt-J",
    "country": "UK",
    "id": "2815",
    "pollyear": 2014,
    "position": 14,
    "releaseyear": "2014",
    "track": "Every Other Freckle"
    },
    {
    "alltime": False,
    "artist": "The Kite String Tangle",
    "country": "Australia",
    "id": "2816",
    "pollyear": 2014,
    "position": 15,
    "releaseyear": "2014",
    "track": "Arcadia"
    },
    {
    "alltime": False,
    "artist": "alt-J",
    "country": "UK",
    "id": "2817",
    "pollyear": 2014,
    "position": 16,
    "releaseyear": "2014",
    "track": "Left Hand Free"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "2818",
    "pollyear": 2014,
    "position": 17,
    "releaseyear": "2014",
    "track": "Tightrope {Ft. Scarlett Stevens}"
    },
    {
    "alltime": False,
    "artist": "Lorde",
    "country": "New Zealand",
    "id": "2819",
    "pollyear": 2014,
    "position": 18,
    "releaseyear": "2014",
    "track": "Yellow Flicker Beat"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2820",
    "pollyear": 2014,
    "position": 19,
    "releaseyear": "2014",
    "track": "She Only Loves Me When I'm There"
    },
    {
    "alltime": False,
    "artist": "Sticky Fingers",
    "country": "Australia",
    "id": "2821",
    "pollyear": 2014,
    "position": 20,
    "releaseyear": "2014",
    "track": "Gold Snafu"
    },
    {
    "alltime": False,
    "artist": "Chet Faker",
    "country": "Australia",
    "id": "2822",
    "pollyear": 2014,
    "position": 21,
    "releaseyear": "2014",
    "track": "(Lover) You Don't Treat Me No Good {Like A Version 2014}"
    },
    {
    "alltime": False,
    "artist": "The Amity Affliction",
    "country": "Australia",
    "id": "2823",
    "pollyear": 2014,
    "position": 22,
    "releaseyear": "2014",
    "track": "Pittsburgh"
    },
    {
    "alltime": False,
    "artist": "Future Islands",
    "country": "USA",
    "id": "2824",
    "pollyear": 2014,
    "position": 23,
    "releaseyear": "2014",
    "track": "Seasons (Waiting On You)"
    },
    {
    "alltime": False,
    "artist": "Meg Mac",
    "country": "Australia",
    "id": "2825",
    "pollyear": 2014,
    "position": 24,
    "releaseyear": "2014",
    "track": "Roll Up Your Sleeves"
    },
    {
    "alltime": False,
    "artist": "Bluejuice",
    "country": "Australia",
    "id": "2826",
    "pollyear": 2014,
    "position": 25,
    "releaseyear": "2014",
    "track": "I'll Go Crazy"
    },
    {
    "alltime": False,
    "artist": "alt-J",
    "country": "UK",
    "id": "2827",
    "pollyear": 2014,
    "position": 26,
    "releaseyear": "2014",
    "track": "Hunger Of The Pine"
    },
    {
    "alltime": False,
    "artist": "Banks",
    "country": "USA",
    "id": "2828",
    "pollyear": 2014,
    "position": 27,
    "releaseyear": "2014",
    "track": "Beggin For Thread"
    },
    {
    "alltime": False,
    "artist": "The Griswolds",
    "country": "Australia",
    "id": "2829",
    "pollyear": 2014,
    "position": 28,
    "releaseyear": "2014",
    "track": "Beware The Dog"
    },
    {
    "alltime": False,
    "artist": "The Preatures",
    "country": "Australia",
    "id": "2830",
    "pollyear": 2014,
    "position": 29,
    "releaseyear": "2014",
    "track": "Somebody's Talking"
    },
    {
    "alltime": False,
    "artist": "Thundamentals",
    "country": "Australia",
    "id": "2831",
    "pollyear": 2014,
    "position": 30,
    "releaseyear": "2014",
    "track": "Something I Said {Ft. Thom Crawford}"
    },
    {
    "alltime": False,
    "artist": "Childish Gambino",
    "country": "USA",
    "id": "2832",
    "pollyear": 2014,
    "position": 31,
    "releaseyear": "2014",
    "track": "Sober"
    },
    {
    "alltime": False,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2833",
    "pollyear": 2014,
    "position": 32,
    "releaseyear": "2014",
    "track": "West Coast"
    },
    {
    "alltime": False,
    "artist": "San Cisco",
    "country": "Australia",
    "id": "2834",
    "pollyear": 2014,
    "position": 33,
    "releaseyear": "2014",
    "track": "RUN"
    },
    {
    "alltime": False,
    "artist": "SBTRKT",
    "country": "UK",
    "id": "2835",
    "pollyear": 2014,
    "position": 34,
    "releaseyear": "2014",
    "track": "NEW DORP. NEW YORK {Ft. Ezra Koenig}"
    },
    {
    "alltime": False,
    "artist": "Allday",
    "country": "Australia",
    "id": "2836",
    "pollyear": 2014,
    "position": 35,
    "releaseyear": "2014",
    "track": "You Always Know The DJ"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2837",
    "pollyear": 2014,
    "position": 36,
    "releaseyear": "2014",
    "track": "Won't Let You Down {Ft. Maverick Sabre}"
    },
    {
    "alltime": False,
    "artist": "Alison Wonderland",
    "country": "Australia",
    "id": "2838",
    "pollyear": 2014,
    "position": 37,
    "releaseyear": "2014",
    "track": "I Want U"
    },
    {
    "alltime": False,
    "artist": "First Aid Kit",
    "country": "Sweden",
    "id": "2839",
    "pollyear": 2014,
    "position": 38,
    "releaseyear": "2014",
    "track": "My Silver Lining"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2840",
    "pollyear": 2014,
    "position": 39,
    "releaseyear": "2014",
    "track": "Two Bodies {Ft. Emma Louise}"
    },
    {
    "alltime": False,
    "artist": "Broods",
    "country": "New Zealand",
    "id": "2841",
    "pollyear": 2014,
    "position": 40,
    "releaseyear": "2014",
    "track": "Mother & Father"
    },
    {
    "alltime": False,
    "artist": "Carmada",
    "country": "Australia",
    "id": "2842",
    "pollyear": 2014,
    "position": 41,
    "releaseyear": "2014",
    "track": "Maybe"
    },
    {
    "alltime": False,
    "artist": "Kim Churchill",
    "country": "Australia",
    "id": "2843",
    "pollyear": 2014,
    "position": 42,
    "releaseyear": "2014",
    "track": "Window To The Sky"
    },
    {
    "alltime": False,
    "artist": "Jamie T",
    "country": "UK",
    "id": "2844",
    "pollyear": 2014,
    "position": 43,
    "releaseyear": "2014",
    "track": "Zombie"
    },
    {
    "alltime": False,
    "artist": "Milky Chance",
    "country": "Germany",
    "id": "2845",
    "pollyear": 2014,
    "position": 44,
    "releaseyear": "2014",
    "track": "Flashed Junk Mind"
    },
    {
    "alltime": False,
    "artist": "FKA twigs",
    "country": "UK",
    "id": "2846",
    "pollyear": 2014,
    "position": 45,
    "releaseyear": "2014",
    "track": "Two Weeks"
    },
    {
    "alltime": False,
    "artist": "Meg Mac",
    "country": "Australia",
    "id": "2847",
    "pollyear": 2014,
    "position": 46,
    "releaseyear": "2014",
    "track": "Grandma's Hands"
    },
    {
    "alltime": False,
    "artist": "Lorde",
    "country": "New Zealand",
    "id": "2848",
    "pollyear": 2014,
    "position": 47,
    "releaseyear": "2014",
    "track": "Tennis Court (Flume Remix)"
    },
    {
    "alltime": False,
    "artist": "DMA's",
    "country": "Australia",
    "id": "2849",
    "pollyear": 2014,
    "position": 48,
    "releaseyear": "2014",
    "track": "Delete"
    },
    {
    "alltime": False,
    "artist": "TV On The Radio",
    "country": "USA",
    "id": "2850",
    "pollyear": 2014,
    "position": 49,
    "releaseyear": "2014",
    "track": "Happy Idiot"
    },
    {
    "alltime": False,
    "artist": "Vance Joy",
    "country": "Australia",
    "id": "2851",
    "pollyear": 2014,
    "position": 50,
    "releaseyear": "2014",
    "track": "First Time"
    },
    {
    "alltime": False,
    "artist": "Courtney Barnett",
    "country": "Australia",
    "id": "2852",
    "pollyear": 2014,
    "position": 51,
    "releaseyear": "2014",
    "track": "Pickles From The Jar"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2853",
    "pollyear": 2014,
    "position": 52,
    "releaseyear": "2014",
    "track": "Sunshine {Ft. Reggie Watts}"
    },
    {
    "alltime": False,
    "artist": "Kendrick Lamar",
    "country": "USA",
    "id": "2854",
    "pollyear": 2014,
    "position": 53,
    "releaseyear": "2014",
    "track": "i"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2855",
    "pollyear": 2014,
    "position": 54,
    "releaseyear": "2014",
    "track": "Do I Wanna Know? {Like A Version 2014}"
    },
    {
    "alltime": False,
    "artist": "Caribou",
    "country": "Canada",
    "id": "2856",
    "pollyear": 2014,
    "position": 55,
    "releaseyear": "2014",
    "track": "Can't Do Without You"
    },
    {
    "alltime": False,
    "artist": "Kingswood",
    "country": "Australia",
    "id": "2857",
    "pollyear": 2014,
    "position": 56,
    "releaseyear": "2014",
    "track": "I Can Feel That You Don't Love Me"
    },
    {
    "alltime": False,
    "artist": "Hilltop Hoods",
    "country": "Australia",
    "id": "2858",
    "pollyear": 2014,
    "position": 57,
    "releaseyear": "2014",
    "track": "Walking Under Stars"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2859",
    "pollyear": 2014,
    "position": 58,
    "releaseyear": "2014",
    "track": "Everything Is Shit Except My Friendship With You"
    },
    {
    "alltime": False,
    "artist": "Röyksopp",
    "country": "Norway",
    "id": "2860",
    "pollyear": 2014,
    "position": 59,
    "releaseyear": "2014",
    "track": "Monument (The Inevitable End Version) {Ft. Robyn}"
    },
    {
    "alltime": False,
    "artist": "Childish Gambino",
    "country": "USA",
    "id": "2861",
    "pollyear": 2014,
    "position": 60,
    "releaseyear": "2014",
    "track": "Sweatpants"
    },
    {
    "alltime": False,
    "artist": "Andy Bull",
    "country": "Australia",
    "id": "2862",
    "pollyear": 2014,
    "position": 61,
    "releaseyear": "2014",
    "track": "Talk Too Much"
    },
    {
    "alltime": False,
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "id": "2863",
    "pollyear": 2014,
    "position": 62,
    "releaseyear": "2014",
    "track": "Heart Beats Slow"
    },
    {
    "alltime": False,
    "artist": "The War On Drugs",
    "country": "USA",
    "id": "2864",
    "pollyear": 2014,
    "position": 63,
    "releaseyear": "2014",
    "track": "Red Eyes"
    },
    {
    "alltime": False,
    "artist": "The Amity Affliction",
    "country": "Australia",
    "id": "2865",
    "pollyear": 2014,
    "position": 64,
    "releaseyear": "2014",
    "track": "Don't Lean On Me"
    },
    {
    "alltime": False,
    "artist": "Allday",
    "country": "Australia",
    "id": "2866",
    "pollyear": 2014,
    "position": 65,
    "releaseyear": "2014",
    "track": "Right Now"
    },
    {
    "alltime": False,
    "artist": "clipping.",
    "country": "USA",
    "id": "2867",
    "pollyear": 2014,
    "position": 66,
    "releaseyear": "2014",
    "track": "Work Work {Ft. Cocc Pistol Cree}"
    },
    {
    "alltime": False,
    "artist": "Jungle",
    "country": "UK",
    "id": "2868",
    "pollyear": 2014,
    "position": 67,
    "releaseyear": "2014",
    "track": "Busy Earnin'"
    },
    {
    "alltime": False,
    "artist": "Bring Me The Horizon",
    "country": "UK",
    "id": "2869",
    "pollyear": 2014,
    "position": 68,
    "releaseyear": "2014",
    "track": "Drown"
    },
    {
    "alltime": False,
    "artist": "The Smith Street Band",
    "country": "Australia",
    "id": "2870",
    "pollyear": 2014,
    "position": 69,
    "releaseyear": "2014",
    "track": "Surrender"
    },
    {
    "alltime": False,
    "artist": "Odd Mob",
    "country": "Australia",
    "id": "2871",
    "pollyear": 2014,
    "position": 70,
    "releaseyear": "2014",
    "track": "Is It A Banger?"
    },
    {
    "alltime": False,
    "artist": "The Amity Affliction",
    "country": "Australia",
    "id": "2872",
    "pollyear": 2014,
    "position": 71,
    "releaseyear": "2014",
    "track": "The Weigh Down"
    },
    {
    "alltime": False,
    "artist": "Run The Jewels",
    "country": "USA",
    "id": "2873",
    "pollyear": 2014,
    "position": 72,
    "releaseyear": "2014",
    "track": "Close Your Eyes (And Count To Fuck) {Ft. Zack De La Rocha}"
    },
    {
    "alltime": False,
    "artist": "Röyksopp & Robyn",
    "country": "Norway",
    "id": "2874",
    "pollyear": 2014,
    "position": 73,
    "releaseyear": "2014",
    "track": "Do It Again"
    },
    {
    "alltime": False,
    "artist": "Duke Dumont",
    "country": "UK",
    "id": "2875",
    "pollyear": 2014,
    "position": 74,
    "releaseyear": "2014",
    "track": "I Got U {Ft. Jax Jones}"
    },
    {
    "alltime": False,
    "artist": "360",
    "country": "Australia",
    "id": "2876",
    "pollyear": 2014,
    "position": 75,
    "releaseyear": "2014",
    "track": "Live It Up {Ft. Pez}"
    },
    {
    "alltime": False,
    "artist": "Kingswood",
    "country": "Australia",
    "id": "2877",
    "pollyear": 2014,
    "position": 76,
    "releaseyear": "2014",
    "track": "Micro Wars"
    },
    {
    "alltime": False,
    "artist": "Highasakite",
    "country": "Norway",
    "id": "2878",
    "pollyear": 2014,
    "position": 77,
    "releaseyear": "2014",
    "track": "Since Last Wednesday"
    },
    {
    "alltime": False,
    "artist": "Thundamentals",
    "country": "Australia",
    "id": "2879",
    "pollyear": 2014,
    "position": 78,
    "releaseyear": "2014",
    "track": "Quit Your Job"
    },
    {
    "alltime": False,
    "artist": "Jack White",
    "country": "USA",
    "id": "2880",
    "pollyear": 2014,
    "position": 79,
    "releaseyear": "2014",
    "track": "Lazaretto"
    },
    {
    "alltime": False,
    "artist": "Rise Against",
    "country": "USA",
    "id": "2881",
    "pollyear": 2014,
    "position": 80,
    "releaseyear": "2014",
    "track": "I Don't Want To Be Here Anymore"
    },
    {
    "alltime": False,
    "artist": "The Avener",
    "country": "France",
    "id": "2882",
    "pollyear": 2014,
    "position": 81,
    "releaseyear": "2014",
    "track": "Fade Out Lines"
    },
    {
    "alltime": False,
    "artist": "Hopium",
    "country": "Australia",
    "id": "2883",
    "pollyear": 2014,
    "position": 82,
    "releaseyear": "2014",
    "track": "Dreamers {Ft. Phoebe Lou}"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "2884",
    "pollyear": 2014,
    "position": 83,
    "releaseyear": "2014",
    "track": "Wrong Direction"
    },
    {
    "alltime": False,
    "artist": "Foo Fighters",
    "country": "USA",
    "id": "2885",
    "pollyear": 2014,
    "position": 84,
    "releaseyear": "2014",
    "track": "Something From Nothing"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2886",
    "pollyear": 2014,
    "position": 85,
    "releaseyear": "2014",
    "track": "Get Away"
    },
    {
    "alltime": False,
    "artist": "Sticky Fingers",
    "country": "Australia",
    "id": "2887",
    "pollyear": 2014,
    "position": 86,
    "releaseyear": "2014",
    "track": "Just For You"
    },
    {
    "alltime": False,
    "artist": "Briggs",
    "country": "Australia",
    "id": "2888",
    "pollyear": 2014,
    "position": 87,
    "releaseyear": "2014",
    "track": "Bad Apples"
    },
    {
    "alltime": False,
    "artist": "DZ Deathrays",
    "country": "Australia",
    "id": "2889",
    "pollyear": 2014,
    "position": 88,
    "releaseyear": "2014",
    "track": "Gina Works At Hearts"
    },
    {
    "alltime": False,
    "artist": "Cold War Kids",
    "country": "USA",
    "id": "2890",
    "pollyear": 2014,
    "position": 89,
    "releaseyear": "2014",
    "track": "First"
    },
    {
    "alltime": False,
    "artist": "Thundamentals",
    "country": "Australia",
    "id": "2891",
    "pollyear": 2014,
    "position": 90,
    "releaseyear": "2014",
    "track": "Got Love {Ft. Solo}"
    },
    {
    "alltime": False,
    "artist": "Meg Mac",
    "country": "Australia",
    "id": "2892",
    "pollyear": 2014,
    "position": 91,
    "releaseyear": "2014",
    "track": "Bridges {Like A Version 2014}"
    },
    {
    "alltime": False,
    "artist": "One Day",
    "country": "Australia",
    "id": "2893",
    "pollyear": 2014,
    "position": 92,
    "releaseyear": "2014",
    "track": "Love Me Less"
    },
    {
    "alltime": False,
    "artist": "Vance Joy",
    "country": "Australia",
    "id": "2894",
    "pollyear": 2014,
    "position": 93,
    "releaseyear": "2014",
    "track": "Georgia"
    },
    {
    "alltime": False,
    "artist": "Sticky Fingers",
    "country": "Australia",
    "id": "2895",
    "pollyear": 2014,
    "position": 94,
    "releaseyear": "2014",
    "track": "Liquorlip Loaded Gun"
    },
    {
    "alltime": False,
    "artist": "Thelma Plum",
    "country": "Australia",
    "id": "2896",
    "pollyear": 2014,
    "position": 95,
    "releaseyear": "2014",
    "track": "How Much Does Your Love Cost?"
    },
    {
    "alltime": False,
    "artist": "SAFIA",
    "country": "Australia",
    "id": "2897",
    "pollyear": 2014,
    "position": 96,
    "releaseyear": "2014",
    "track": "Paranoia, Ghosts & Other Sounds"
    },
    {
    "alltime": False,
    "artist": "Japanese Wallpaper",
    "country": "Australia",
    "id": "2898",
    "pollyear": 2014,
    "position": 97,
    "releaseyear": "2014",
    "track": "Between Friends {Ft. Jesse Davidson}"
    },
    {
    "alltime": False,
    "artist": "Bombay Bicycle Club",
    "country": "UK",
    "id": "2899",
    "pollyear": 2014,
    "position": 98,
    "releaseyear": "2014",
    "track": "Luna"
    },
    {
    "alltime": False,
    "artist": "Ball Park Music",
    "country": "Australia",
    "id": "2900",
    "pollyear": 2014,
    "position": 99,
    "releaseyear": "2014",
    "track": "Trippin' The Light Fantastic"
    },
    {
    "alltime": False,
    "artist": "Tkay Maidza",
    "country": "Australia",
    "id": "2901",
    "pollyear": 2014,
    "position": 100,
    "releaseyear": "2014",
    "track": "Switch Lanes {Prod. Paces}"
    },
    {
    "alltime": False,
    "artist": "The Rubens",
    "country": "Australia",
    "id": "2902",
    "pollyear": 2015,
    "position": 1,
    "releaseyear": "2015",
    "track": "Hoops"
    },
    {
    "alltime": False,
    "artist": "Kendrick Lamar",
    "country": "USA",
    "id": "2903",
    "pollyear": 2015,
    "position": 2,
    "releaseyear": "2015",
    "track": "King Kunta"
    },
    {
    "alltime": False,
    "artist": "Major Lazer",
    "country": "USA",
    "id": "2904",
    "pollyear": 2015,
    "position": 3,
    "releaseyear": "2015",
    "track": "Lean On {Ft. M¯/DJ Snake}"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2905",
    "pollyear": 2015,
    "position": 4,
    "releaseyear": "2015",
    "track": "The Less I Know The Better"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2906",
    "pollyear": 2015,
    "position": 5,
    "releaseyear": "2015",
    "track": "Let It Happen"
    },
    {
    "alltime": False,
    "artist": "Marcus Marr & Chet Faker",
    "country": "Australia",
    "id": "2907",
    "pollyear": 2015,
    "position": 6,
    "releaseyear": "2015",
    "track": "The Trouble With Us"
    },
    {
    "alltime": False,
    "artist": "Jarryd James",
    "country": "Australia",
    "id": "2908",
    "pollyear": 2015,
    "position": 7,
    "releaseyear": "2015",
    "track": "Do You Remember"
    },
    {
    "alltime": False,
    "artist": "Hermitude",
    "country": "Australia",
    "id": "2909",
    "pollyear": 2015,
    "position": 8,
    "releaseyear": "2015",
    "track": "The Buzz {Ft. Mataya/Young Tapz}"
    },
    {
    "alltime": False,
    "artist": "The Weeknd",
    "country": "Canada",
    "id": "2910",
    "pollyear": 2015,
    "position": 9,
    "releaseyear": "2015",
    "track": "Can't Feel My Face"
    },
    {
    "alltime": False,
    "artist": "Disclosure",
    "country": "UK",
    "id": "2911",
    "pollyear": 2015,
    "position": 10,
    "releaseyear": "2015",
    "track": "Magnets {Ft. Lorde}"
    },
    {
    "alltime": False,
    "artist": "Meg Mac",
    "country": "Australia",
    "id": "2912",
    "pollyear": 2015,
    "position": 11,
    "releaseyear": "2015",
    "track": "Never Be"
    },
    {
    "alltime": False,
    "artist": "RÜFÜS",
    "country": "Australia",
    "id": "2913",
    "pollyear": 2015,
    "position": 12,
    "releaseyear": "2015",
    "track": "You Were Right"
    },
    {
    "alltime": False,
    "artist": "Duke Dumont",
    "country": "UK",
    "id": "2914",
    "pollyear": 2015,
    "position": 13,
    "releaseyear": "2015",
    "track": "Ocean Drive"
    },
    {
    "alltime": False,
    "artist": "Drake",
    "country": "Canada",
    "id": "2915",
    "pollyear": 2015,
    "position": 14,
    "releaseyear": "2015",
    "track": "Hotline Bling"
    },
    {
    "alltime": False,
    "artist": "Violent Soho",
    "country": "Australia",
    "id": "2916",
    "pollyear": 2015,
    "position": 15,
    "releaseyear": "2015",
    "track": "Like Soda"
    },
    {
    "alltime": False,
    "artist": "Vance Joy",
    "country": "Australia",
    "id": "2917",
    "pollyear": 2015,
    "position": 16,
    "releaseyear": "2015",
    "track": "Fire And The Flood"
    },
    {
    "alltime": False,
    "artist": "DJ Snake",
    "country": "France",
    "id": "2918",
    "pollyear": 2015,
    "position": 17,
    "releaseyear": "2015",
    "track": "Middle {Ft. Bipolar Sunshine}"
    },
    {
    "alltime": False,
    "artist": "Macklemore & Ryan Lewis",
    "country": "USA",
    "id": "2919",
    "pollyear": 2015,
    "position": 18,
    "releaseyear": "2015",
    "track": "DOWNTOWN {Ft. Eric Nally/Melle Mel/Kool Moe Dee/Grandmaster Caz}"
    },
    {
    "alltime": False,
    "artist": "The Weeknd",
    "country": "Canada",
    "id": "2920",
    "pollyear": 2015,
    "position": 19,
    "releaseyear": "2015",
    "track": "The Hills"
    },
    {
    "alltime": False,
    "artist": "Foals",
    "country": "UK",
    "id": "2921",
    "pollyear": 2015,
    "position": 20,
    "releaseyear": "2015",
    "track": "Mountain At My Gates"
    },
    {
    "alltime": False,
    "artist": "Gang Of Youths",
    "country": "Australia",
    "id": "2922",
    "pollyear": 2015,
    "position": 21,
    "releaseyear": "2015",
    "track": "Magnolia"
    },
    {
    "alltime": False,
    "artist": "L D R U",
    "country": "Australia",
    "id": "2923",
    "pollyear": 2015,
    "position": 22,
    "releaseyear": "2015",
    "track": "Keeping Score {Ft. Paige IV}"
    },
    {
    "alltime": False,
    "artist": "SAFIA",
    "country": "Australia",
    "id": "2924",
    "pollyear": 2015,
    "position": 23,
    "releaseyear": "2015",
    "track": "Embracing Me"
    },
    {
    "alltime": False,
    "artist": "Flume",
    "country": "Australia",
    "id": "2925",
    "pollyear": 2015,
    "position": 24,
    "releaseyear": "2015",
    "track": "Some Minds {Ft. Andrew Wyatt}"
    },
    {
    "alltime": False,
    "artist": "The Amity Affliction",
    "country": "Australia",
    "id": "2926",
    "pollyear": 2015,
    "position": 25,
    "releaseyear": "2015",
    "track": "Shine On"
    },
    {
    "alltime": False,
    "artist": "Jamie xx",
    "country": "UK",
    "id": "2927",
    "pollyear": 2015,
    "position": 26,
    "releaseyear": "2015",
    "track": "I Know There's Gonna Be (Good Times) {Ft. Young Thug/Popcaan}"
    },
    {
    "alltime": False,
    "artist": "Vallis Alps",
    "country": "Australia",
    "id": "2928",
    "pollyear": 2015,
    "position": 27,
    "releaseyear": "2015",
    "track": "Young"
    },
    {
    "alltime": False,
    "artist": "RÜFÜS",
    "country": "Australia",
    "id": "2929",
    "pollyear": 2015,
    "position": 28,
    "releaseyear": "2015",
    "track": "Like An Animal"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2930",
    "pollyear": 2015,
    "position": 29,
    "releaseyear": "2015",
    "track": "Greek Tragedy"
    },
    {
    "alltime": False,
    "artist": "Peking Duk",
    "country": "Australia",
    "id": "2931",
    "pollyear": 2015,
    "position": 30,
    "releaseyear": "2015",
    "track": "Say My Name {Ft. Benjamin Joseph}"
    },
    {
    "alltime": False,
    "artist": "Jamie xx",
    "country": "UK",
    "id": "2932",
    "pollyear": 2015,
    "position": 31,
    "releaseyear": "2015",
    "track": "Loud Places {Ft. Romy}"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2933",
    "pollyear": 2015,
    "position": 32,
    "releaseyear": "2015",
    "track": "Leave A Trace"
    },
    {
    "alltime": False,
    "artist": "Urthboy",
    "country": "Australia",
    "id": "2934",
    "pollyear": 2015,
    "position": 33,
    "releaseyear": "2015",
    "track": "Long Loud Hours {Ft. Bertie Blackman}"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2935",
    "pollyear": 2015,
    "position": 34,
    "releaseyear": "2015",
    "track": "Eventually"
    },
    {
    "alltime": False,
    "artist": "SAFIA",
    "country": "Australia",
    "id": "2936",
    "pollyear": 2015,
    "position": 35,
    "releaseyear": "2015",
    "track": "Counting Sheep"
    },
    {
    "alltime": False,
    "artist": "Snakehips",
    "country": "UK",
    "id": "2937",
    "pollyear": 2015,
    "position": 36,
    "releaseyear": "2015",
    "track": "All My Friends {Ft. Tinashe/Chance The Rapper}"
    },
    {
    "alltime": False,
    "artist": "Kendrick Lamar",
    "country": "USA",
    "id": "2938",
    "pollyear": 2015,
    "position": 37,
    "releaseyear": "2015",
    "track": "Alright"
    },
    {
    "alltime": False,
    "artist": "Florence + The Machine",
    "country": "UK",
    "id": "2939",
    "pollyear": 2015,
    "position": 38,
    "releaseyear": "2015",
    "track": "Delilah"
    },
    {
    "alltime": False,
    "artist": "Illy",
    "country": "Australia",
    "id": "2940",
    "pollyear": 2015,
    "position": 39,
    "releaseyear": "2015",
    "track": "Swear Jar"
    },
    {
    "alltime": False,
    "artist": "Florence + The Machine",
    "country": "UK",
    "id": "2941",
    "pollyear": 2015,
    "position": 40,
    "releaseyear": "2015",
    "track": "Ship To Wreck"
    },
    {
    "alltime": False,
    "artist": "Claptone",
    "country": "Germany",
    "id": "2942",
    "pollyear": 2015,
    "position": 41,
    "releaseyear": "2015",
    "track": "Puppet Theatre {Ft. Peter Bjorn & John}"
    },
    {
    "alltime": False,
    "artist": "Halsey",
    "country": "USA",
    "id": "2943",
    "pollyear": 2015,
    "position": 42,
    "releaseyear": "2015",
    "track": "Hold Me Down"
    },
    {
    "alltime": False,
    "artist": "Courtney Barnett",
    "country": "Australia",
    "id": "2944",
    "pollyear": 2015,
    "position": 43,
    "releaseyear": "2015",
    "track": "Pedestrian At Best"
    },
    {
    "alltime": False,
    "artist": "Hayden James",
    "country": "Australia",
    "id": "2945",
    "pollyear": 2015,
    "position": 44,
    "releaseyear": "2015",
    "track": "Something About You"
    },
    {
    "alltime": False,
    "artist": "Bring Me The Horizon",
    "country": "UK",
    "id": "2946",
    "pollyear": 2015,
    "position": 45,
    "releaseyear": "2015",
    "track": "Throne"
    },
    {
    "alltime": False,
    "artist": "The Chemical Brothers",
    "country": "UK",
    "id": "2947",
    "pollyear": 2015,
    "position": 46,
    "releaseyear": "2015",
    "track": "Go {Ft. Q-Tip}"
    },
    {
    "alltime": False,
    "artist": "Asta",
    "country": "Australia",
    "id": "2948",
    "pollyear": 2015,
    "position": 47,
    "releaseyear": "2015",
    "track": "Dynamite {Ft. Allday}"
    },
    {
    "alltime": False,
    "artist": "Parkway Drive",
    "country": "Australia",
    "id": "2949",
    "pollyear": 2015,
    "position": 48,
    "releaseyear": "2015",
    "track": "Crushed"
    },
    {
    "alltime": False,
    "artist": "San Cisco",
    "country": "Australia",
    "id": "2950",
    "pollyear": 2015,
    "position": 49,
    "releaseyear": "2015",
    "track": "Too Much Time Together"
    },
    {
    "alltime": False,
    "artist": "BOO SEEKA",
    "country": "Australia",
    "id": "2951",
    "pollyear": 2015,
    "position": 50,
    "releaseyear": "2015",
    "track": "Deception Bay"
    },
    {
    "alltime": False,
    "artist": "Chvrches",
    "country": "UK",
    "id": "2952",
    "pollyear": 2015,
    "position": 51,
    "releaseyear": "2015",
    "track": "Clearest Blue"
    },
    {
    "alltime": False,
    "artist": "Ratatat",
    "country": "USA",
    "id": "2953",
    "pollyear": 2015,
    "position": 52,
    "releaseyear": "2015",
    "track": "Cream On Chrome"
    },
    {
    "alltime": False,
    "artist": "Matt Corby",
    "country": "Australia",
    "id": "2954",
    "pollyear": 2015,
    "position": 53,
    "releaseyear": "2015",
    "track": "Monday"
    },
    {
    "alltime": False,
    "artist": "ZHU x Skrillex x THEY.",
    "country": "USA",
    "id": "2955",
    "pollyear": 2015,
    "position": 54,
    "releaseyear": "2015",
    "track": "Working For It"
    },
    {
    "alltime": False,
    "artist": "Unknown Mortal Orchestra",
    "country": "New Zealand",
    "id": "2956",
    "pollyear": 2015,
    "position": 55,
    "releaseyear": "2015",
    "track": "Multi-Love"
    },
    {
    "alltime": False,
    "artist": "Sia",
    "country": "Australia",
    "id": "2957",
    "pollyear": 2015,
    "position": 56,
    "releaseyear": "2015",
    "track": "Alive"
    },
    {
    "alltime": False,
    "artist": "Alpine",
    "country": "Australia",
    "id": "2958",
    "pollyear": 2015,
    "position": 57,
    "releaseyear": "2015",
    "track": "Foolish"
    },
    {
    "alltime": False,
    "artist": "Parkway Drive",
    "country": "Australia",
    "id": "2959",
    "pollyear": 2015,
    "position": 58,
    "releaseyear": "2015",
    "track": "Vice Grip"
    },
    {
    "alltime": False,
    "artist": "Alison Wonderland",
    "country": "Australia",
    "id": "2960",
    "pollyear": 2015,
    "position": 59,
    "releaseyear": "2015",
    "track": "Run"
    },
    {
    "alltime": False,
    "artist": "MØ",
    "country": "Denmark",
    "id": "2961",
    "pollyear": 2015,
    "position": 60,
    "releaseyear": "2015",
    "track": "Kamikaze"
    },
    {
    "alltime": False,
    "artist": "Tame Impala",
    "country": "Australia",
    "id": "2962",
    "pollyear": 2015,
    "position": 61,
    "releaseyear": "2015",
    "track": "Cause I'm A Man"
    },
    {
    "alltime": False,
    "artist": "Disclosure",
    "country": "UK",
    "id": "2963",
    "pollyear": 2015,
    "position": 62,
    "releaseyear": "2015",
    "track": "Omen {Ft. Sam Smith}"
    },
    {
    "alltime": False,
    "artist": "Boy & Bear",
    "country": "Australia",
    "id": "2964",
    "pollyear": 2015,
    "position": 63,
    "releaseyear": "2015",
    "track": "Walk The Wire"
    },
    {
    "alltime": False,
    "artist": "A$AP Rocky",
    "country": "USA",
    "id": "2965",
    "pollyear": 2015,
    "position": 64,
    "releaseyear": "2015",
    "track": "L$D"
    },
    {
    "alltime": False,
    "artist": "Alabama Shakes",
    "country": "USA",
    "id": "2966",
    "pollyear": 2015,
    "position": 65,
    "releaseyear": "2015",
    "track": "Don't Wanna Fight"
    },
    {
    "alltime": False,
    "artist": "Tkay Maidza",
    "country": "Australia",
    "id": "2967",
    "pollyear": 2015,
    "position": 66,
    "releaseyear": "2015",
    "track": "M.O.B."
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2968",
    "pollyear": 2015,
    "position": 67,
    "releaseyear": "2015",
    "track": "Give Me A Try"
    },
    {
    "alltime": False,
    "artist": "Skepta",
    "country": "UK",
    "id": "2969",
    "pollyear": 2015,
    "position": 68,
    "releaseyear": "2015",
    "track": "Shutdown"
    },
    {
    "alltime": False,
    "artist": "Japanese Wallpaper",
    "country": "Australia",
    "id": "2970",
    "pollyear": 2015,
    "position": 69,
    "releaseyear": "2015",
    "track": "Forces {Ft. Airling}"
    },
    {
    "alltime": False,
    "artist": "Florence + The Machine",
    "country": "UK",
    "id": "2971",
    "pollyear": 2015,
    "position": 70,
    "releaseyear": "2015",
    "track": "What Kind Of Man"
    },
    {
    "alltime": False,
    "artist": "Grimes",
    "country": "Canada",
    "id": "2972",
    "pollyear": 2015,
    "position": 71,
    "releaseyear": "2015",
    "track": "Flesh Without Blood"
    },
    {
    "alltime": False,
    "artist": "Birds Of Tokyo",
    "country": "Australia",
    "id": "2973",
    "pollyear": 2015,
    "position": 72,
    "releaseyear": "2015",
    "track": "Anchor"
    },
    {
    "alltime": False,
    "artist": "Ngaiire",
    "country": "Australia",
    "id": "2974",
    "pollyear": 2015,
    "position": 73,
    "releaseyear": "2015",
    "track": "Once"
    },
    {
    "alltime": False,
    "artist": "Major Lazer",
    "country": "USA",
    "id": "2975",
    "pollyear": 2015,
    "position": 74,
    "releaseyear": "2015",
    "track": "Powerful {Ft. Ellie Goulding/Tarrus Riley}"
    },
    {
    "alltime": False,
    "artist": "Courtney Barnett",
    "country": "Australia",
    "id": "2976",
    "pollyear": 2015,
    "position": 75,
    "releaseyear": "2015",
    "track": "Elevator Operator"
    },
    {
    "alltime": False,
    "artist": "British India",
    "country": "Australia",
    "id": "2977",
    "pollyear": 2015,
    "position": 76,
    "releaseyear": "2015",
    "track": "Suddenly"
    },
    {
    "alltime": False,
    "artist": "DMA's",
    "country": "Australia",
    "id": "2978",
    "pollyear": 2015,
    "position": 77,
    "releaseyear": "2015",
    "track": "Lay Down"
    },
    {
    "alltime": False,
    "artist": "Jack Garratt",
    "country": "UK",
    "id": "2979",
    "pollyear": 2015,
    "position": 78,
    "releaseyear": "2015",
    "track": "Weathered"
    },
    {
    "alltime": False,
    "artist": "The Cat Empire",
    "country": "Australia",
    "id": "2980",
    "pollyear": 2015,
    "position": 79,
    "releaseyear": "2015",
    "track": "Wolves"
    },
    {
    "alltime": False,
    "artist": "A$AP Rocky",
    "country": "USA",
    "id": "2981",
    "pollyear": 2015,
    "position": 80,
    "releaseyear": "2015",
    "track": "Everyday {Ft. Rod Stewart/Miguel/Mark Ronson}"
    },
    {
    "alltime": False,
    "artist": "Tuka",
    "country": "Australia",
    "id": "2982",
    "pollyear": 2015,
    "position": 81,
    "releaseyear": "2015",
    "track": "Big Jet Plane {triple j Like A Version}"
    },
    {
    "alltime": False,
    "artist": "Courtney Barnett",
    "country": "Australia",
    "id": "2983",
    "pollyear": 2015,
    "position": 82,
    "releaseyear": "2015",
    "track": "Depreston"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2984",
    "pollyear": 2015,
    "position": 83,
    "releaseyear": "2015",
    "track": "Down To Earth {Radio Edit}"
    },
    {
    "alltime": False,
    "artist": "Sticky Fingers",
    "country": "Australia",
    "id": "2985",
    "pollyear": 2015,
    "position": 84,
    "releaseyear": "2015",
    "track": "Delete {triple j Like A Version}"
    },
    {
    "alltime": False,
    "artist": "Flight Facilities",
    "country": "Australia",
    "id": "2986",
    "pollyear": 2015,
    "position": 85,
    "releaseyear": "2015",
    "track": "Heart Attack {Ft. Owl Eyes} {Radio Edit}"
    },
    {
    "alltime": False,
    "artist": "Bring Me The Horizon",
    "country": "UK",
    "id": "2987",
    "pollyear": 2015,
    "position": 86,
    "releaseyear": "2015",
    "track": "Happy Song"
    },
    {
    "alltime": False,
    "artist": "Purity Ring",
    "country": "Canada",
    "id": "2988",
    "pollyear": 2015,
    "position": 87,
    "releaseyear": "2015",
    "track": "Begin Again"
    },
    {
    "alltime": False,
    "artist": "The Bennies",
    "country": "Australia",
    "id": "2989",
    "pollyear": 2015,
    "position": 88,
    "releaseyear": "2015",
    "track": "Party Machine"
    },
    {
    "alltime": False,
    "artist": "Lana Del Rey",
    "country": "USA",
    "id": "2990",
    "pollyear": 2015,
    "position": 89,
    "releaseyear": "2015",
    "track": "High By The Beach"
    },
    {
    "alltime": False,
    "artist": "What So Not",
    "country": "Australia",
    "id": "2991",
    "pollyear": 2015,
    "position": 90,
    "releaseyear": "2015",
    "track": "Gemini {Ft. George Maple}"
    },
    {
    "alltime": False,
    "artist": "The Wombats",
    "country": "UK",
    "id": "2992",
    "pollyear": 2015,
    "position": 91,
    "releaseyear": "2015",
    "track": "Be Your Shadow"
    },
    {
    "alltime": False,
    "artist": "Golden Features",
    "country": "Australia",
    "id": "2993",
    "pollyear": 2015,
    "position": 92,
    "releaseyear": "2015",
    "track": "No One {Ft. Thelma Plum}"
    },
    {
    "alltime": False,
    "artist": "Jai Wolf",
    "country": "USA",
    "id": "2994",
    "pollyear": 2015,
    "position": 93,
    "releaseyear": "2015",
    "track": "Indian Summer"
    },
    {
    "alltime": False,
    "artist": "Halsey",
    "country": "USA",
    "id": "2995",
    "pollyear": 2015,
    "position": 94,
    "releaseyear": "2015",
    "track": "Ghost"
    },
    {
    "alltime": False,
    "artist": "Courtney Barnett",
    "country": "Australia",
    "id": "2996",
    "pollyear": 2015,
    "position": 95,
    "releaseyear": "2015",
    "track": "Nobody Really Cares If You Don't Go To The Party"
    },
    {
    "alltime": False,
    "artist": "Rudimental",
    "country": "UK",
    "id": "2997",
    "pollyear": 2015,
    "position": 96,
    "releaseyear": "2015",
    "track": "Rumour Mill {Ft. Anne-Marie/Will Heard}"
    },
    {
    "alltime": False,
    "artist": "Methyl Ethel",
    "country": "Australia",
    "id": "2998",
    "pollyear": 2015,
    "position": 97,
    "releaseyear": "2015",
    "track": "Twilight Driving"
    },
    {
    "alltime": False,
    "artist": "Major Lazer",
    "country": "USA",
    "id": "2999",
    "pollyear": 2015,
    "position": 98,
    "releaseyear": "2015",
    "track": "Be Together {Ft. Wild Belle}"
    },
    {
    "alltime": False,
    "artist": "Bring Me The Horizon",
    "country": "UK",
    "id": "3000",
    "pollyear": 2015,
    "position": 99,
    "releaseyear": "2015",
    "track": "True Friends"
    },
    {
    "alltime": False,
    "artist": "Seth Sentry",
    "country": "Australia",
    "id": "3001",
    "pollyear": 2015,
    "position": 100,
    "releaseyear": "2015",
    "track": "Hell Boy"
    },
    
    {
    "id": "3002",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 1,
    "artist": "Flume",
    "track": "Never Be Like You {Ft. Kai}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3003",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 2,
    "artist": "Amy Shark",
    "track": "Adore",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3004",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 3,
    "artist": "Tash Sultana",
    "track": "Jungle",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3005",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 4,
    "artist": "Hilltop Hoods",
    "track": "1955 {Ft. Montaigne/Tom Thum}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3006",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 5,
    "artist": "Childish Gambino",
    "track": "Redbone",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3007",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 6,
    "artist": "DMA'S",
    "track": "Believe {triple j Like A Version 2016}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3008",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 7,
    "artist": "Illy",
    "track": "Papercuts {Ft. Vera Blue}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3009",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 8,
    "artist": "Flume",
    "track": "Say It {Ft. Tove Lo}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3010",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 9,
    "artist": "Peking Duk",
    "track": "Stranger {Ft. Elliphant}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3011",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 10,
    "artist": "The Weeknd",
    "track": "Starboy {Ft. Daft Punk}",
    "country": "Canada",
    "alltime": False
    },
    {
    "id": "3012",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 11,
    "artist": "Pnau",
    "track": "Chameleon",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3013",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 12,
    "artist": "Milky Chance",
    "track": "Cocoon",
    "country": "Germany",
    "alltime": False
    },
    {
    "id": "3014",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 13,
    "artist": "Mura Masa",
    "track": "Love$ick {Ft. A$AP Rocky}",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3015",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 14,
    "artist": "Violent Soho",
    "track": "Viceroy",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3016",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 15,
    "artist": "Miike Snow",
    "track": "Genghis Khan",
    "country": "Sweden",
    "alltime": False
    },
    {
    "id": "3017",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 16,
    "artist": "A.B. Original",
    "track": "January 26 {Ft. Dan Sultan}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3018",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 17,
    "artist": "Big Scary",
    "track": "The Opposite Of Us",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3019",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 18,
    "artist": "Chance The Rapper",
    "track": "All Night {Ft. Knox Fortune}",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3020",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 19,
    "artist": "Catfish And The Bottlemen",
    "track": "7",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3021",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 20,
    "artist": "The xx",
    "track": "On Hold",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3022",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 21,
    "artist": "The Smith Street Band",
    "track": "Death To The Lads",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3023",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 22,
    "artist": "Kanye West",
    "track": "Ultralight Beam",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3024",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 23,
    "artist": "Illy",
    "track": "Catch 22 {Ft. Anne-Marie}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3025",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 24,
    "artist": "Cub Sport",
    "track": "Come On Mess Me Up",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3026",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 25,
    "artist": "Montaigne",
    "track": "Because I Love You",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3027",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 26,
    "artist": "SAFIA",
    "track": "Make Them Wheels Roll",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3028",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 27,
    "artist": "Gretta Ray",
    "track": "Drive",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3029",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 28,
    "artist": "The Avalanches",
    "track": "Frankie Sinatra",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3030",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 29,
    "artist": "Sticky Fingers",
    "track": "Our Town",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3031",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 30,
    "artist": "R\u00dcF\u00dcS",
    "track": "Innerbloom {What So Not Remix}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3032",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 31,
    "artist": "Drake",
    "track": "One Dance {Ft. Wizkid/Kyla}",
    "country": "Canada",
    "alltime": False
    },
    {
    "id": "3033",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 32,
    "artist": "Tash Sultana",
    "track": "Notion",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3034",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 33,
    "artist": "Dune Rats",
    "track": "Bullshit",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3035",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 34,
    "artist": "Dune Rats",
    "track": "Scott Green",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3036",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 35,
    "artist": "Client Liaison",
    "track": "World Of Our Love",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3037",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 36,
    "artist": "Sticky Fingers",
    "track": "Sad Songs",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3038",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 37,
    "artist": "Flume",
    "track": "Smoke & Retribution {Ft. Vince Staples/KUCKA}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3039",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 38,
    "artist": "Glass Animals",
    "track": "Youth",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3040",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 39,
    "artist": "DMA'S",
    "track": "Step Up The Morphine",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3041",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 40,
    "artist": "Kid Cudi",
    "track": "Surfin' {Ft. Pharrell Williams}",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3042",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 41,
    "artist": "The Weeknd",
    "track": "I Feel It Coming {Ft. Daft Punk}",
    "country": "Canada",
    "alltime": False
    },
    {
    "id": "3043",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 42,
    "artist": "Broods",
    "track": "Heartlines",
    "country": "New Zealand",
    "alltime": False
    },
    {
    "id": "3044",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 43,
    "artist": "M\u00d8",
    "track": "Final Song",
    "country": "Denmark",
    "alltime": False
    },
    {
    "id": "3045",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 44,
    "artist": "D.D Dumbo",
    "track": "Satan",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3046",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 45,
    "artist": "A.B. Original",
    "track": "Dumb Things {Ft. Paul Kelly/Dan Sultan} {Like A Version 2016}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3047",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 46,
    "artist": "Mac Miller",
    "track": "Dang! {Ft. Anderson .Paak}",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3048",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 47,
    "artist": "D.D Dumbo",
    "track": "Walrus",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3049",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 48,
    "artist": "Kingswood",
    "track": "Creepin",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3050",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 49,
    "artist": "Hilltop Hoods",
    "track": "Higher {Ft. James Chatburn}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3051",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 50,
    "artist": "Gang Of Youths",
    "track": "Strange Diseases",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3052",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 51,
    "artist": "Sticky Fingers",
    "track": "Outcast At Last",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3053",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 52,
    "artist": "Halsey",
    "track": "Love Yourself {triple j Like A Version 2016}",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3054",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 53,
    "artist": "Violent Soho",
    "track": "Blanket",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3055",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 54,
    "artist": "Blink-182",
    "track": "Bored To Death",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3056",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 55,
    "artist": "R\u00dcF\u00dcS",
    "track": "Say A Prayer For Me",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3057",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 56,
    "artist": "Paces",
    "track": "Keeping Score {Ft. Guy Sebastian} {triple j Like A Version 2016}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3058",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 57,
    "artist": "Catfish And The Bottlemen",
    "track": "Twice",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3059",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 58,
    "artist": "Ali Barter",
    "track": "Girlie Bits",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3060",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 59,
    "artist": "Frank Ocean",
    "track": "Solo",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3061",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 60,
    "artist": "Sofi Tukker",
    "track": "Drinkee",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3062",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 61,
    "artist": "King Gizzard & The Lizard Wizard",
    "track": "Gamma Knife",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3063",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 62,
    "artist": "DOPE LEMON",
    "track": "Marinade",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3064",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 63,
    "artist": "Glass Animals",
    "track": "Life Itself",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3065",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 64,
    "artist": "Maggie Rogers",
    "track": "Alaska",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3066",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 65,
    "artist": "The Amity Affliction",
    "track": "All Fucked Up",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3067",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 66,
    "artist": "Beyonc\u00e9",
    "track": "Hold Up",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3068",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 67,
    "artist": "The Amity Affliction",
    "track": "I Bring The Weather With Me",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3069",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 68,
    "artist": "L D R U",
    "track": "Next To You {Ft. Savoi}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3070",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 69,
    "artist": "Violent Soho",
    "track": "So Sentimental",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3071",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 70,
    "artist": "Golden Features",
    "track": "Wolfie {Ft. Julia Stone}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3072",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 71,
    "artist": "Broods",
    "track": "Free",
    "country": "New Zealand",
    "alltime": False
    },
    {
    "id": "3073",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 72,
    "artist": "Kanye West",
    "track": "Famous",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3074",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 73,
    "artist": "Violent Soho",
    "track": "No Shade",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3075",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 74,
    "artist": "Camp Cope",
    "track": "Lost: Season One",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3076",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 75,
    "artist": "The Avalanches",
    "track": "Because I'm Me",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3077",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 76,
    "artist": "The Amity Affliction",
    "track": "This Could Be Heartbreak",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3078",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 77,
    "artist": "Catfish And The Bottlemen",
    "track": "Soundcheck",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3079",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 78,
    "artist": "Vera Blue",
    "track": "Settle",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3080",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 79,
    "artist": "Radiohead",
    "track": "Burn The Witch",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3081",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 80,
    "artist": "Banks",
    "track": "Gemini Feed",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3082",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 81,
    "artist": "Desiigner",
    "track": "Panda",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3083",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 82,
    "artist": "Thundamentals",
    "track": "Think About It {Ft. Peta & The Wolves}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3084",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 83,
    "artist": "Tkay Maidza",
    "track": "Simulation",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3085",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 84,
    "artist": "Frank Ocean",
    "track": "Pink + White",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3086",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 85,
    "artist": "SAFIA",
    "track": "My Love Is Gone",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3087",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 86,
    "artist": "Bliss N Eso",
    "track": "Dopamine {Ft. Thief}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3088",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 87,
    "artist": "DOPE LEMON",
    "track": "Uptown Folks",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3089",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 88,
    "artist": "Childish Gambino",
    "track": "Me And Your Mama",
    "country": "USA",
    "alltime": False
    },
    {
    "id": "3090",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 89,
    "artist": "SAFIA",
    "track": "Over You",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3091",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 90,
    "artist": "Luca Brasi",
    "track": "Anything Near Conviction",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3092",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 91,
    "artist": "The Avalanches",
    "track": "Subways",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3093",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 92,
    "artist": "Violent Soho",
    "track": "How To Taste",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3094",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 93,
    "artist": "Empire Of The Sun",
    "track": "High And Low",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3095",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 94,
    "artist": "Vallis Alps",
    "track": "Fading",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3096",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 95,
    "artist": "Flume",
    "track": "Lose It {Ft. Vic Mensa}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3097",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 96,
    "artist": "Elk Road",
    "track": "Hanging By A Thread {Ft. Natalie Foster}",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3098",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 97,
    "artist": "Alex Lahey",
    "track": "You Don't Think You Like People Like Me",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "3099",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 98,
    "artist": "Glass Animals",
    "track": "Season 2 Episode 3",
    "country": "UK",
    "alltime": False
    },
    {
    "id": "3100",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 99,
    "artist": "Drake",
    "track": "Too Good {Ft. Rihanna}",
    "country": "Canada",
    "alltime": False
    },
    {
    "id": "3101",
    "pollyear": 2016,
    "releaseyear": "2016",
    
    "position": 100,
    "artist": "Birds Of Tokyo",
    "track": "Brace",
    "country": "Australia",
    "alltime": False
    },
    {
    "id": "910",
    "position": 1,
    "track": "HUMBLE.",
    "artist": "Kendrick Lamar",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "618",
    "position": 2,
    "track": "Let Me Down Easy",
    "artist": "Gang Of Youths",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "96",
    "position": 3,
    "track": "Chateau",
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1167",
    "position": 4,
    "track": "Ubu",
    "artist": "Methyl Ethel",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "624",
    "position": 5,
    "track": "The Deepest Sighs, The Frankest Shadows",
    "artist": "Gang Of Youths",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1073",
    "position": 6,
    "track": "Green Light",
    "artist": "Lorde",
    "country": "New Zealand",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1393",
    "position": 7,
    "track": "Go Bang",
    "artist": "PNAU",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1701",
    "position": 8,
    "track": "Sally {Ft. Mataya}",
    "artist": "Thundamentals",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1796",
    "position": 9,
    "track": "Lay It On Me",
    "artist": "Vance Joy",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "617",
    "position": 10,
    "track": "What Can I Do If The Fire Goes Out?",
    "artist": "Gang Of Youths",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "279",
    "position": 11,
    "track": "SWEET",
    "artist": "BROCKHAMPTON",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1360",
    "position": 12,
    "track": "Fake Magic",
    "artist": "Peking Duk & AlunaGeorge",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "929",
    "position": 13,
    "track": "Young Dumb & Broke",
    "artist": "Khalid",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1077",
    "position": 14,
    "track": "Homemade Dynamite",
    "artist": "Lorde",
    "country": "New Zealand",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1804",
    "position": 15,
    "track": "Regular Touch",
    "artist": "Vera Blue",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "867",
    "position": 16,
    "track": "Feel The Way I Do",
    "artist": "The Jungle Giants",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "163",
    "position": 17,
    "track": "Marryuna {Ft. Yirrmal}",
    "artist": "Baker Boy",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "164",
    "position": 18,
    "track": "Exactly How You Are",
    "artist": "Ball Park Music",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "932",
    "position": 19,
    "track": "The Man",
    "artist": "The Killers",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1359",
    "position": 20,
    "track": "Let You Down {Ft. Icona Pop}",
    "artist": "Peking Duk",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1592",
    "position": 21,
    "track": "Birthdays",
    "artist": "The Smith Street Band",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1876",
    "position": 22,
    "track": "Lemon To A Knife Fight",
    "artist": "The Wombats",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "46",
    "position": 23,
    "track": "Not Worth Hiding",
    "artist": "Alex The Astronaut",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "10004",
    "position": 24,
    "track": "rockstar {Ft. 21 Savage}",
    "artist": "Post Malone",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "88",
    "position": 25,
    "track": "Weekends",
    "artist": "Amy Shark",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1417",
    "position": 26,
    "track": "Feel It Still",
    "artist": "Portugal. The Man",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1856",
    "position": 27,
    "track": "Be About You",
    "artist": "Winston Surfshirt",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1685",
    "position": 28,
    "track": "Mystik",
    "artist": "Tash Sultana",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1801",
    "position": 29,
    "track": "Mended",
    "artist": "Vera Blue",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1155",
    "position": 30,
    "track": "Low Blows",
    "artist": "Meg Mac",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1759",
    "position": 31,
    "track": "Lay Down",
    "artist": "Touch Sensitive",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "729",
    "position": 32,
    "track": "NUMB {Ft. GRAACE}",
    "artist": "Hayden James",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "94",
    "position": 33,
    "track": "Slow Mover",
    "artist": "Angie McMahon",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "912",
    "position": 34,
    "track": "DNA.",
    "artist": "Kendrick Lamar",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "459",
    "position": 35,
    "track": "Passionfruit",
    "artist": "Drake",
    "country": "Canada",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "38",
    "position": 36,
    "track": "I Haven't Been Taking Care Of Myself",
    "artist": "Alex Lahey",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "308",
    "position": 37,
    "track": "Slide {Ft. Frank Ocean/Migos}",
    "artist": "Calvin Harris",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "10001",
    "position": 38,
    "track": "Bellyache",
    "artist": "Billie Eilish",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "10006",
    "position": 39,
    "track": "Got On My Skateboard",
    "artist": "Skegss",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "748",
    "position": 40,
    "track": "True Lovers",
    "artist": "Holy Holy",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "628",
    "position": 41,
    "track": "Blood {triple j Like A Version 2017}",
    "artist": "Gang Of Youths",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "310",
    "position": 42,
    "track": "Cola",
    "artist": "CamelPhat & Elderbrook",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1684",
    "position": 43,
    "track": "Murder To The Mind",
    "artist": "Tash Sultana",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "64",
    "position": 44,
    "track": "In Motion {Ft. Japanese Wallpaper}",
    "artist": "Allday",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "37",
    "position": 45,
    "track": "Every Day's The Weekend",
    "artist": "Alex Lahey",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1126",
    "position": 46,
    "track": "Better",
    "artist": "Mallrat",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "703",
    "position": 47,
    "track": "Want You Back",
    "artist": "HAIM",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1315",
    "position": 48,
    "track": "The Comedown",
    "artist": "Ocean Alley",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1595",
    "position": 49,
    "track": "Passiona",
    "artist": "The Smith Street Band",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "868",
    "position": 50,
    "track": "On Your Way Down",
    "artist": "The Jungle Giants",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "206",
    "position": 51,
    "track": "Man's Not Hot",
    "artist": "Big Shaq",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1107",
    "position": 52,
    "track": "Glorious {Ft. Skylar Grey}",
    "artist": "Macklemore",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "236",
    "position": 53,
    "track": "Moments {Ft. Gavin James}",
    "artist": "Bliss N Eso",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "743",
    "position": 54,
    "track": "Homely Feeling",
    "artist": "Hockey Dad",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "482",
    "position": 55,
    "track": "6 Pack",
    "artist": "Dune Rats",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1328",
    "position": 56,
    "track": "Watch Me Read You",
    "artist": "Odette",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "869",
    "position": 57,
    "track": "Bad Dream",
    "artist": "The Jungle Giants",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "313",
    "position": 58,
    "track": "The Opener",
    "artist": "Camp Cope",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "870",
    "position": 59,
    "track": "Used To Be In Love",
    "artist": "The Jungle Giants",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "322",
    "position": 60,
    "track": "Boys",
    "artist": "Charli XCX",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1705",
    "position": 61,
    "track": "21 Grams {Ft. Hilltop Hoods}",
    "artist": "Thundamentals",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "926",
    "position": 62,
    "track": "Saved",
    "artist": "Khalid",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "492",
    "position": 63,
    "track": "Life Goes On",
    "artist": "E^ST",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "798",
    "position": 64,
    "track": "Fool's Gold",
    "artist": "Jack River",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "117",
    "position": 65,
    "track": "Everything Now",
    "artist": "Arcade Fire",
    "country": "Canada",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1254",
    "position": 66,
    "track": "Lemon",
    "artist": "N.E.R.D. & Rihanna",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "490",
    "position": 67,
    "track": "Shred For Summer",
    "artist": "DZ Deathrays",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "966",
    "position": 68,
    "track": "Golden",
    "artist": "Kingswood",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1911",
    "position": 69,
    "track": "I Love You, Will You Marry Me",
    "artist": "Yungblud",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1305",
    "position": 70,
    "track": "Amsterdam",
    "artist": "Nothing But Thieves",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1075",
    "position": 71,
    "track": "Perfect Places",
    "artist": "Lorde",
    "country": "New Zealand",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "68",
    "position": 72,
    "track": "In Cold Blood",
    "artist": "alt-J",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "945",
    "position": 73,
    "track": "Nuclear Fusion",
    "artist": "King Gizzard & The Lizard Wizard",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1043",
    "position": 74,
    "track": "XO TOUR Llif3",
    "artist": "Lil Uzi Vert",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "484",
    "position": 75,
    "track": "Braindead",
    "artist": "Dune Rats",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "162",
    "position": 76,
    "track": "Cloud 9 {Ft. Kian}",
    "artist": "Baker Boy",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1489",
    "position": 77,
    "track": "Million Man",
    "artist": "The Rubens",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1683",
    "position": 78,
    "track": "Electric Feel {triple j Like A Version 2017}",
    "artist": "Tash Sultana",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1523",
    "position": 79,
    "track": "Hey, Did I Do You Wrong?",
    "artist": "San Cisco",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1883",
    "position": 80,
    "track": "Say Something Loving",
    "artist": "The xx",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "10003",
    "position": 81,
    "track": "Liability",
    "artist": "Lorde",
    "country": "New Zealand",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1062",
    "position": 82,
    "track": "1-800-273-8255 {Ft. Alessia Cara/Khalid}",
    "artist": "Logic",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "90",
    "position": 83,
    "track": "Blood Brothers",
    "artist": "Amy Shark",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1794",
    "position": 84,
    "track": "Oceans",
    "artist": "Vallis Alps",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "251",
    "position": 85,
    "track": "Does This Last",
    "artist": "Boo Seeka",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1156",
    "position": 86,
    "track": "Maybe It's My First Time",
    "artist": "Meg Mac",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1439",
    "position": 87,
    "track": "The Way You Used To Do",
    "artist": "Queens Of The Stone Age",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1357",
    "position": 88,
    "track": "Edge Of Town {triple j Like A Version 2017}",
    "artist": "Paul Dempsey",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "457",
    "position": 89,
    "track": "Dawning",
    "artist": "DMA's",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "577",
    "position": 90,
    "track": "Hyperreal {Ft. KU&#x10C;KA}",
    "artist": "Flume",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1634",
    "position": 91,
    "track": "Big For Your Boots",
    "artist": "Stormzy",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "919",
    "position": 92,
    "track": "LOVE. {Ft. ZACARI}",
    "artist": "Kendrick Lamar",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1423",
    "position": 93,
    "track": "Do What You Want",
    "artist": "The Presets",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "940",
    "position": 94,
    "track": "Second Hand Car",
    "artist": "Kim Churchill",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "613",
    "position": 95,
    "track": "Mask Off",
    "artist": "Future",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "386",
    "position": 96,
    "track": "Chasin'",
    "artist": "Cub Sport",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "916",
    "position": 97,
    "track": "LOYALTY. {Ft. RIHANNA}",
    "artist": "Kendrick Lamar",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "95",
    "position": 98,
    "track": "Snow",
    "artist": "Angus & Julia Stone",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "568",
    "position": 99,
    "track": "Arty Boy {Ft. Emma Louise}",
    "artist": "Flight Facilities",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1600",
    "position": 100,
    "track": "Don't Leave",
    "artist": "Snakehips & M&Oslash;",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2017,
    "alltime": False
    },
    {
    "id": "1140",
    "position": 1,
    "artist": "Ocean Alley",
    "track": "Confidence",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "564",
    "position": 2,
    "artist": "FISHER",
    "track": "Losing It",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1501",
    "position": 3,
    "artist": "Travis Scott",
    "track": "SICKO MODE",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "325",
    "position": 4,
    "artist": "Childish Gambino",
    "track": "This Is America",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "87",
    "position": 5,
    "artist": "Amy Shark",
    "track": "I Said Hi",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "425",
    "position": 6,
    "artist": "Dean Lewis",
    "track": "Be Alright",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "987",
    "position": 7,
    "artist": "Mallrat",
    "track": "Groceries",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "209",
    "position": 8,
    "artist": "Billie Eilish",
    "track": "when the party's over",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1290",
    "position": 9,
    "artist": "Ruby Fields",
    "track": "Dinosaurs",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1143",
    "position": 10,
    "artist": "Ocean Alley",
    "track": "Knees",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1357",
    "position": 11,
    "artist": "Skegss",
    "track": "Up In The Clouds",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1591",
    "position": 12,
    "artist": "The Wombats",
    "track": "Turn",
    "country": "UK",
    "releaseyear": 2017,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "23",
    "position": 13,
    "artist": "A$AP Rocky",
    "track": "Praise The Lord (Da Shine) {Ft. Skepta}",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1562",
    "position": 14,
    "artist": "Wafia",
    "track": "I'm Good",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "683",
    "position": 15,
    "artist": "Hayden James",
    "track": "Just Friends {Ft. Boy Matthews}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "2006",
    "position": 16,
    "artist": "Ocean Alley",
    "track": "Baby Come Back {triple j Like A Version 2018}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "208",
    "position": 17,
    "artist": "Billie Eilish",
    "track": "lovely {with Khalid}",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "705",
    "position": 18,
    "artist": "Hockey Dad",
    "track": "Join The Club",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "268",
    "position": 19,
    "artist": "Broods",
    "track": "Peach",
    "country": "New Zealand",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "846",
    "position": 20,
    "artist": "KIAN",
    "track": "Waiting",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1289",
    "position": 21,
    "artist": "The Rubens",
    "track": "Never Ever {Ft. Sarah}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1302",
    "position": 22,
    "artist": "RÃœFÃœS DU SOL",
    "track": "Underwater",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1301",
    "position": 23,
    "artist": "RÃœFÃœS DU SOL",
    "track": "Treat You Better",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "698",
    "position": 24,
    "artist": "Hilltop Hoods",
    "track": "Leave Me Lonely",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1460",
    "position": 25,
    "artist": "Thundamentals",
    "track": "I Miss You",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1551",
    "position": 26,
    "artist": "Vera Blue",
    "track": "All The Pretty Girls",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1225",
    "position": 27,
    "artist": "Post Malone & Swae Lee",
    "track": "Sunflower",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "834",
    "position": 28,
    "artist": "Kendrick Lamar & SZA",
    "track": "All The Stars",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1196",
    "position": 29,
    "artist": "Peking Duk",
    "track": "Fire",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "408",
    "position": 30,
    "artist": "Cub Sport",
    "track": "Sometimes",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "58",
    "position": 31,
    "artist": "Alison Wonderland",
    "track": "Church",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1287",
    "position": 32,
    "artist": "The Rubens",
    "track": "God Forgot",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1220",
    "position": 33,
    "artist": "Post Malone",
    "track": "Better Now",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "860",
    "position": 34,
    "artist": "King Princess",
    "track": "1950",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "974",
    "position": 35,
    "artist": "Mac Miller",
    "track": "Ladders",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "83",
    "position": 36,
    "artist": "Amy Shark",
    "track": "All Loved Up",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1627",
    "position": 37,
    "artist": "Ziggy Alberts",
    "track": "Love Me Now",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "594",
    "position": 38,
    "artist": "G Flip",
    "track": "About You",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "176",
    "position": 39,
    "artist": "Ball Park Music",
    "track": "The Perfect Life Does Not Exist",
    "country": "Australia",
    "releaseyear": 2017,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "474",
    "position": 40,
    "artist": "Drake",
    "track": "Nice For What",
    "country": "Canada",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "460",
    "position": 41,
    "artist": "DMA'S",
    "track": "In The Air",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1626",
    "position": 42,
    "artist": "Ziggy Alberts",
    "track": "Laps Around The Sun",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "471",
    "position": 43,
    "artist": "Drake",
    "track": "God's Plan",
    "country": "Canada",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "697",
    "position": 44,
    "artist": "Hilltop Hoods",
    "track": "Clark Griswold {Ft. Adrian Eagle}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "252",
    "position": 45,
    "artist": "Bring Me The Horizon",
    "track": "MANTRA",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "210",
    "position": 46,
    "artist": "Billie Eilish",
    "track": "you should see me in a crown",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "499",
    "position": 47,
    "artist": "DZ Deathrays",
    "track": "Like People",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1324",
    "position": 48,
    "artist": "San Cisco",
    "track": "When I Dream",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "109",
    "position": 49,
    "artist": "Angie McMahon",
    "track": "Missing Me",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1300",
    "position": 50,
    "artist": "RÃœFÃœS DU SOL",
    "track": "No Place",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "167",
    "position": 51,
    "artist": "Baker Boy",
    "track": "Mr La Di Da Di",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "841",
    "position": 52,
    "artist": "Khalid",
    "track": "Better",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1546",
    "position": 53,
    "artist": "Vance Joy",
    "track": "We're Going Home",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1544",
    "position": 54,
    "artist": "Vance Joy",
    "track": "Saturday Sun",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1197",
    "position": 55,
    "artist": "Peking Duk",
    "track": "Wasted",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "665",
    "position": 56,
    "artist": "Halsey",
    "track": "Without Me",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1230",
    "position": 57,
    "artist": "The Presets",
    "track": "Martini",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "197",
    "position": 58,
    "artist": "Bene",
    "track": "Soaked",
    "country": "New Zealand",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1016",
    "position": 59,
    "artist": "Meg Mac",
    "track": "Give Me My Name Back",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "462",
    "position": 60,
    "artist": "DMA'S",
    "track": "The End",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "704",
    "position": 61,
    "artist": "Hockey Dad",
    "track": "I Wanna Be Everybody",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "595",
    "position": 62,
    "artist": "G Flip",
    "track": "Killing My Time",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "257",
    "position": 63,
    "artist": "BROCKHAMPTON",
    "track": "BOOGIE",
    "country": "USA",
    "releaseyear": 2017,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "2004",
    "position": 64,
    "artist": "Middle Kids",
    "track": "Mistake",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1022",
    "position": 65,
    "artist": "Methyl Ethel",
    "track": "Scream Whole",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "568",
    "position": 66,
    "artist": "Flight Facilities",
    "track": "Need You {Ft. NÃKA}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "104",
    "position": 67,
    "artist": "Anderson .Paak",
    "track": "Tints {Ft. Kendrick Lamar}",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "199",
    "position": 68,
    "artist": "benny blanco",
    "track": "Eastside {Ft. Halsey/Khalid}",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1588",
    "position": 69,
    "artist": "The Wombats",
    "track": "Cheetah Tongue",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "988",
    "position": 70,
    "artist": "Mallrat",
    "track": "UFO {Ft. Allday}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1355",
    "position": 71,
    "artist": "Skegss",
    "track": "Smogged Out",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1132",
    "position": 72,
    "artist": "Nothing But Thieves",
    "track": "What Can I Do If The Fire Goes Out {triple j Like A Version 2018}",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "707",
    "position": 73,
    "artist": "Hockey Dad",
    "track": "Sweet Release",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "862",
    "position": 74,
    "artist": "King Princess",
    "track": "Pussy Is God",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "2002",
    "position": 75,
    "artist": "Kira Puru",
    "track": "Molotov",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1212",
    "position": 76,
    "artist": "Polish Club",
    "track": "Clarity",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "340",
    "position": 77,
    "artist": "CHVRCHES",
    "track": "Miracle",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "682",
    "position": 78,
    "artist": "Hayden James",
    "track": "Better Together {Ft. Running Touch}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1450",
    "position": 79,
    "artist": "Thelma Plum",
    "track": "Clumsy Love",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1004",
    "position": 80,
    "artist": "Mark Ronson",
    "track": "Nothing Breaks Like A Heart {Ft. Miley Cyrus}",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "757",
    "position": 81,
    "artist": "Jack River",
    "track": "Ballroom",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "572",
    "position": 82,
    "artist": "Florence + The Machine",
    "track": "Hunger",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "254",
    "position": 83,
    "artist": "BROCKHAMPTON",
    "track": "1999 WILDFIRE",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1431",
    "position": 84,
    "artist": "Tash Sultana",
    "track": "Cigarettes",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "99",
    "position": 85,
    "artist": "Anderson .Paak",
    "track": "Bubblin'",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "934",
    "position": 86,
    "artist": "Lime Cordiale",
    "track": "Dirt Cheap",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1296",
    "position": 87,
    "artist": "Ruel",
    "track": "Younger",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1561",
    "position": 88,
    "artist": "WAAX",
    "track": "Labrador",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1295",
    "position": 89,
    "artist": "Ruel",
    "track": "Dazed & Confused {Prod. M-Phazes}",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1222",
    "position": 90,
    "artist": "Post Malone",
    "track": "Psycho {Ft. Ty Dolla $ign}",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "24",
    "position": 91,
    "artist": "A$AP Rocky",
    "track": "Sundress",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1458",
    "position": 92,
    "artist": "Thundamentals",
    "track": "Everybody But You",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1513",
    "position": 93,
    "artist": "Trophy Eyes",
    "track": "You Can Count On Me",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "81",
    "position": 94,
    "artist": "The Amity Affliction",
    "track": "Ivy (Doomsday)",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "132",
    "position": 95,
    "artist": "Arctic Monkeys",
    "track": "Four Out Of Five",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1155",
    "position": 96,
    "artist": "Odette",
    "track": "Take It To The Heart",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "458",
    "position": 97,
    "artist": "DMA'S",
    "track": "Do I Need You Now?",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "822",
    "position": 98,
    "artist": "Kanye West",
    "track": "Ghost Town",
    "country": "USA",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "2008",
    "position": 99,
    "artist": "YUNGBLUD",
    "track": "Polygraph Eyes",
    "country": "UK",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    {
    "id": "1142",
    "position": 100,
    "artist": "Ocean Alley",
    "track": "Happy Sad",
    "country": "Australia",
    "releaseyear": 2018,
    "pollyear": 2018,
    "alltime": False
    },
    
    
    
    {
    "id": "edc6f2",
    "artist": "Billie Eilish",
    "position": 1,
    "track": "bad guy",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "712eca",
    "artist": "Flume",
    "position": 2,
    "track": "Rushing Back {Ft. Vera Blue}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "3a2246",
    "artist": "Mallrat",
    "position": 3,
    "track": "Charlie",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "561a62",
    "artist": "Tones and I",
    "position": 4,
    "track": "Dance Monkey",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "44e566",
    "artist": "Denzel Curry",
    "position": 5,
    "track": "Bulls On Parade {triple j Like A Version 2019}",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "8370cb",
    "artist": "G Flip",
    "position": 6,
    "track": "Drink Too Much",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "e4373d",
    "artist": "Lime Cordiale",
    "position": 7,
    "track": "Robbery",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "d619e9",
    "artist": "The Jungle Giants",
    "position": 8,
    "track": "Heavy Hearted",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "550a4d",
    "artist": "Thelma Plum",
    "position": 9,
    "track": "Better In Blak",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "a75942",
    "artist": "Hilltop Hoods",
    "position": 10,
    "track": "Exit Sign {Ft. Illy/Ecca Vandal}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "70be85",
    "artist": "Post Malone",
    "position": 11,
    "track": "Circles",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "8964d4",
    "artist": "FIDLAR",
    "position": 12,
    "track": "By Myself",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "2d81e0",
    "artist": "Lime Cordiale",
    "position": 13,
    "track": "Inappropriate Behaviour",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "0caca6",
    "artist": "Sofi Tukker",
    "position": 14,
    "track": "Purple Hat",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "723678",
    "artist": "Tones and I",
    "position": 15,
    "track": "Never Seen The Rain",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "1a859e",
    "artist": "Billie Eilish",
    "position": 16,
    "track": "everything i wanted",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "cf2c05",
    "artist": "Lime Cordiale",
    "position": 17,
    "track": "I Touch Myself {triple j Like A Version 2019}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "debfea",
    "artist": "Tame Impala",
    "position": 18,
    "track": "Borderline",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "e4d3e2",
    "artist": "BENEE",
    "position": 19,
    "track": "Glitter",
    "pollyear": 2019,
    "alltime": False,
    "country": "New Zealand"
    },
    {
    "id": "b10acf",
    "artist": "DMA'S",
    "position": 20,
    "track": "Silver",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "b02c08",
    "artist": "The Chats",
    "position": 21,
    "track": "Pub Feed",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "442e35",
    "artist": "Ruel",
    "position": 22,
    "track": "Painkiller",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "241a9c",
    "artist": "Tyler, The Creator",
    "position": 23,
    "track": "EARFQUAKE",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "2d71b9",
    "artist": "Ocean Alley",
    "position": 24,
    "track": "Infinity",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "8a8a73",
    "artist": "BENEE",
    "position": 25,
    "track": "Find An Island",
    "pollyear": 2019,
    "alltime": False,
    "country": "New Zealand"
    },
    {
    "id": "71c6e3",
    "artist": "Tones and I",
    "position": 26,
    "track": "Johnny Run Away",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "428174",
    "artist": "Stormzy",
    "position": 27,
    "track": "Vossi Bop",
    "pollyear": 2019,
    "alltime": False,
    "country": "UK"
    },
    {
    "id": "c45101",
    "artist": "Lizzo",
    "position": 28,
    "track": "Juice",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "404a5d",
    "artist": "MEDUZA",
    "position": 29,
    "track": "Piece Of Your Heart {Ft. Goodboys}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Italy"
    },
    {
    "id": "cc78d2",
    "artist": "Flume",
    "position": 30,
    "track": "Friends {Ft. Reo Cragun}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "3ed20c",
    "artist": "Skegss",
    "position": 31,
    "track": "Save It For The Weekend",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "aaa90e",
    "artist": "Lime Cordiale",
    "position": 32,
    "track": "Money",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "2a62c5",
    "artist": "Dom Dolla",
    "position": 33,
    "track": "San Frandisco",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "802ecc",
    "artist": "Glass Animals",
    "position": 34,
    "track": "Tokyo Drifting {Ft. Denzel Curry}",
    "pollyear": 2019,
    "alltime": False,
    "country": "UK"
    },
    {
    "id": "68ce6c",
    "artist": "Billie Eilish",
    "position": 35,
    "track": "bury a friend",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "d97f06",
    "artist": "PNAU",
    "position": 36,
    "track": "Solid Gold {Ft. Kira Divine/Marques Toliver}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "d81a1a",
    "artist": "Duke Dumont",
    "position": 37,
    "track": "Red Light Green Light {Ft. Shaun Ross}",
    "pollyear": 2019,
    "alltime": False,
    "country": "UK"
    },
    {
    "id": "a01911",
    "artist": "Ruel",
    "position": 38,
    "track": "Face To Face",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "210a61",
    "artist": "Catfish and the Bottlemen",
    "position": 39,
    "track": "Longshot",
    "pollyear": 2019,
    "alltime": False,
    "country": "UK"
    },
    {
    "id": "1633ab",
    "artist": "Halsey",
    "position": 40,
    "track": "Graveyard",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "9401af",
    "artist": "Travis Scott",
    "position": 41,
    "track": "HIGHEST IN THE ROOM",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "8bf331",
    "artist": "Juice WRLD",
    "position": 42,
    "track": "Robbery",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "a49060",
    "artist": "Tame Impala",
    "position": 43,
    "track": "It Might Be Time",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "caebbe",
    "artist": "Baker Boy",
    "position": 44,
    "track": "Cool As Hell",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "e44b30",
    "artist": "Denzel Curry",
    "position": 45,
    "track": "RICKY",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "4daab4",
    "artist": "Dean Lewis",
    "position": 46,
    "track": "7 Minutes",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "92f801",
    "artist": "BROCKHAMPTON",
    "position": 47,
    "track": "SUGAR",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "c876ea",
    "artist": "Ziggy Alberts",
    "position": 48,
    "track": "Intentions (22)",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "94aa6f",
    "artist": "Ruel",
    "position": 49,
    "track": "Free Time",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "50faec",
    "artist": "Holy Holy",
    "position": 50,
    "track": "Teach Me About Dying",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "472692",
    "artist": "BENEE",
    "position": 51,
    "track": "Evil Spider",
    "pollyear": 2019,
    "alltime": False,
    "country": "New Zealand"
    },
    {
    "id": "46a61c",
    "artist": "Tame Impala",
    "position": 52,
    "track": "Patience",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "244c6a",
    "artist": "FISHER",
    "position": 53,
    "track": "You Little Beauty",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "1e1e6e",
    "artist": "Ocean Alley",
    "position": 54,
    "track": "Stained Glass",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "306b0e",
    "artist": "Khalid",
    "position": 55,
    "track": "Talk {Ft. Disclosure}",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "721e5d",
    "artist": "J. Cole",
    "position": 56,
    "track": "MIDDLE CHILD",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "01e77f",
    "artist": "Slowly Slowly",
    "position": 57,
    "track": "Jellyfish",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "24efb6",
    "artist": "G Flip",
    "position": 58,
    "track": "Lover",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "6ae92a",
    "artist": "Mallrat x Basenji",
    "position": 59,
    "track": "Nobody's Home",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "70285a",
    "artist": "Hockey Dad",
    "position": 60,
    "track": "I Missed Out",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "6a7818",
    "artist": "Holy Holy",
    "position": 61,
    "track": "Maybe You Know",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "faffdf",
    "artist": "Bakar",
    "position": 62,
    "track": "Hell N Back",
    "pollyear": 2019,
    "alltime": False,
    "country": "UK"
    },
    {
    "id": "fc73e3",
    "artist": "Halsey",
    "position": 63,
    "track": "Nightmare",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "698bfd",
    "artist": "George Alice",
    "position": 64,
    "track": "Circles",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "66404c",
    "artist": "Thelma Plum",
    "position": 65,
    "track": "Homecoming Queen",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "f95fe4",
    "artist": "G Flip",
    "position": 66,
    "track": "Stupid",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "a1afa7",
    "artist": "Billie Eilish",
    "position": 67,
    "track": "wish you were gay",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "d569fe",
    "artist": "Illy",
    "position": 68,
    "track": "Then What",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "27b5a3",
    "artist": "Violent Soho",
    "position": 69,
    "track": "Vacation Forever",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "8eeb73",
    "artist": "E^ST",
    "position": 70,
    "track": "Talk Deep",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "0bc440",
    "artist": "The Weeknd",
    "position": 71,
    "track": "Blinding Lights",
    "pollyear": 2019,
    "alltime": False,
    "country": "Canada"
    },
    {
    "id": "2f7f65",
    "artist": "Angie McMahon",
    "position": 72,
    "track": "Pasta",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "0a081b",
    "artist": "Cub Sport",
    "position": 73,
    "track": "Party Pill",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "2b3346",
    "artist": "Hayden James and NAATIONS",
    "position": 74,
    "track": "Nowhere To Go",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "dd4cb9",
    "artist": "Golden Features x The Presets",
    "position": 75,
    "track": "Paradise",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "839a8a",
    "artist": "Meg Mac",
    "position": 76,
    "track": "Something Tells Me",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "844544",
    "artist": "G Flip",
    "position": 77,
    "track": "I Am Not Afraid",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "8c21b5",
    "artist": "Thelma Plum",
    "position": 78,
    "track": "Not Angry Anymore",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "a1ecc0",
    "artist": "Dean Lewis",
    "position": 79,
    "track": "Stay Awake",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "c78d7e",
    "artist": "Spacey Jane",
    "position": 80,
    "track": "Good For You",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "a876a8",
    "artist": "Flume",
    "position": 81,
    "track": "Let You Know {Ft. London Grammar}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "20e448",
    "artist": "Peking Duk & Jack River",
    "position": 82,
    "track": "Sugar",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "2c1d2d",
    "artist": "Alex Lahey",
    "position": 83,
    "track": "Welcome To The Black Parade {triple j Like A Version 2019}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "787468",
    "artist": "DOPE LEMON",
    "position": 84,
    "track": "Hey You",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "323c88",
    "artist": "Lana Del Rey",
    "position": 85,
    "track": "Doin' Time",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "0ada8c",
    "artist": "Slipknot",
    "position": 86,
    "track": "Unsainted",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "7bf01d",
    "artist": "Kanye West",
    "position": 87,
    "track": "Follow God",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "3b3d6d",
    "artist": "Meduza x Becky Hill x Goodboys",
    "position": 88,
    "track": "Lose Control",
    "pollyear": 2019,
    "alltime": False,
    "country": "Italy"
    },
    {
    "id": "9cd5cd",
    "artist": "Sampa the Great",
    "position": 89,
    "track": "Final Form",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "9e75d8",
    "artist": "Skegss",
    "position": 90,
    "track": "Here Comes Your Man {triple j Like A Version 2019}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "68136f",
    "artist": "Billie Eilish",
    "position": 91,
    "track": "all the good girls go to hell",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "3e3d22",
    "artist": "Client Liaison",
    "position": 92,
    "track": "The Real Thing",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "bc58a7",
    "artist": "Post Malone",
    "position": 93,
    "track": "Wow.",
    "pollyear": 2019,
    "alltime": False,
    "country": "USA"
    },
    {
    "id": "d6ca8c",
    "artist": "Allday",
    "position": 94,
    "track": "Protection",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "82093b",
    "artist": "Adrian Eagle",
    "position": 95,
    "track": "A.O.K.",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "1903a6",
    "artist": "Bring Me The Horizon",
    "position": 96,
    "track": "Ludens",
    "pollyear": 2019,
    "alltime": False,
    "country": "UK"
    },
    {
    "id": "83860e",
    "artist": "San Cisco",
    "position": 97,
    "track": "Skin",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "00d188",
    "artist": "Baker Boy",
    "position": 98,
    "track": "Meditjin {Ft. JessB}",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "118dbf",
    "artist": "Cosmo's Midnight",
    "position": 99,
    "track": "C.U.D.I. (Can U Dig It)",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "id": "6b8c44",
    "artist": "Dune Rats",
    "position": 100,
    "track": "No Plans",
    "pollyear": 2019,
    "alltime": False,
    "country": "Australia"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "f1229c",
    "pollyear": 2020,
    "position": 1,
    "artist": "Tame Impala",
    "track": "The Less I Know The Better",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "9b65a2",
    "pollyear": 2020,
    "position": 2,
    "artist": "Gotye",
    "track": "Somebody That I Used To Know {Ft. Kimbra}",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "9cf437",
    "pollyear": 2020,
    "position": 3,
    "artist": "Arctic Monkeys",
    "track": "Do I Wanna Know?",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "ad2769",
    "pollyear": 2020,
    "position": 4,
    "artist": "Violent Soho",
    "track": "Covered In Chrome",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "95b60e",
    "pollyear": 2020,
    "position": 5,
    "artist": "RÜFÜS DU SOL",
    "track": "Innerbloom",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "df67f1",
    "pollyear": 2020,
    "position": 6,
    "artist": "Gang of Youths",
    "track": "Magnolia",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "da8363",
    "pollyear": 2020,
    "position": 7,
    "artist": "Foster The People",
    "track": "Pumped Up Kicks",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "148c18",
    "pollyear": 2020,
    "position": 8,
    "artist": "Flume",
    "track": "Never Be Like You {Ft. Kai}",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "3cd218",
    "pollyear": 2020,
    "position": 9,
    "artist": "Angus & Julia Stone",
    "track": "Big Jet Plane",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "bcdc3c",
    "pollyear": 2020,
    "position": 10,
    "artist": "Matt Corby",
    "track": "Brother",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "cf6cb9",
    "pollyear": 2020,
    "position": 11,
    "artist": "Nick Murphy / Chet Faker",
    "track": "Talk Is Cheap",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "8fca00",
    "pollyear": 2020,
    "position": 12,
    "artist": "alt-J",
    "track": "Breezeblocks",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "7f121e",
    "pollyear": 2020,
    "position": 13,
    "artist": "Vance Joy",
    "track": "Riptide",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "512bc5",
    "pollyear": 2020,
    "position": 14,
    "artist": "Kanye West",
    "track": "Runaway {ft. Pusha T}",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "005ac5",
    "pollyear": 2020,
    "position": 15,
    "artist": "Sticky Fingers",
    "track": "Australia Street",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "New Zealand",
    "id": "4af209",
    "pollyear": 2020,
    "position": 16,
    "artist": "Lorde",
    "track": "Royals",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "fa296d",
    "pollyear": 2020,
    "position": 17,
    "artist": "Ball Park Music",
    "track": "It's Nice To Be Alive",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "8dedca",
    "pollyear": 2020,
    "position": 18,
    "artist": "Flume",
    "track": "Holdin On",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "0e9c3f",
    "pollyear": 2020,
    "position": 19,
    "artist": "Gang of Youths",
    "track": "Let Me Down Easy",
    "releaseyear": "2017"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "68d958",
    "pollyear": 2020,
    "position": 20,
    "artist": "Hilltop Hoods",
    "track": "Cosby Sweater",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "a48763",
    "pollyear": 2020,
    "position": 21,
    "artist": "DMA'S",
    "track": "Delete",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "4038a0",
    "pollyear": 2020,
    "position": 22,
    "artist": "M83",
    "track": "Midnight City",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "16ec08",
    "pollyear": 2020,
    "position": 23,
    "artist": "Kendrick Lamar",
    "track": "King Kunta",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "49b201",
    "pollyear": 2020,
    "position": 24,
    "artist": "JAY-Z & Kanye West",
    "track": "Ni**as In Paris",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "f2c0d8",
    "pollyear": 2020,
    "position": 25,
    "artist": "Flight Facilities",
    "track": "Clair De Lune {Ft. Christine Hoberg}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "f99b63",
    "pollyear": 2020,
    "position": 26,
    "artist": "Tame Impala",
    "track": "Let It Happen",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "6270ba",
    "pollyear": 2020,
    "position": 27,
    "artist": "Childish Gambino",
    "track": "3005",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "66d9cd",
    "pollyear": 2020,
    "position": 28,
    "artist": "Childish Gambino",
    "track": "Redbone",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "e12f8e",
    "pollyear": 2020,
    "position": 29,
    "artist": "Lana Del Rey",
    "track": "Video Games",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Iceland",
    "id": "f899df",
    "pollyear": 2020,
    "position": 30,
    "artist": "Of Monsters and Men",
    "track": "Little Talks",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "75cb71",
    "pollyear": 2020,
    "position": 31,
    "artist": "The Wombats",
    "track": "Tokyo (Vampires & Wolves)",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "546aa9",
    "pollyear": 2020,
    "position": 32,
    "artist": "Peking Duk",
    "track": "High {Ft. Nicole Millar}",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "c1d49c",
    "pollyear": 2020,
    "position": 33,
    "artist": "Sticky Fingers",
    "track": "Rum Rage",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "8a5bfc",
    "pollyear": 2020,
    "position": 34,
    "artist": "Frank Ocean",
    "track": "Lost",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "3f6ac7",
    "pollyear": 2020,
    "position": 35,
    "artist": "Ocean Alley",
    "track": "Confidence",
    "releaseyear": "2018"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "906d4a",
    "pollyear": 2020,
    "position": 36,
    "artist": "Hilltop Hoods",
    "track": "1955 {Ft. Montaigne & Tom Thum}",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "Germany",
    "id": "84b866",
    "pollyear": 2020,
    "position": 37,
    "artist": "Milky Chance",
    "track": "Stolen Dance",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "Sweden",
    "id": "996d3c",
    "pollyear": 2020,
    "position": 38,
    "artist": "Avicii",
    "track": "Levels",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "9b59d3",
    "pollyear": 2020,
    "position": 39,
    "artist": "Flight Facilities",
    "track": "Crave You {ft. Giselle}",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "c97a49",
    "pollyear": 2020,
    "position": 40,
    "artist": "Disclosure",
    "track": "Latch {Ft. Sam Smith}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "36093f",
    "pollyear": 2020,
    "position": 41,
    "artist": "DMA'S",
    "track": "Believe {triple j Like A Version 2016}",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "e26ba6",
    "pollyear": 2020,
    "position": 42,
    "artist": "Arctic Monkeys",
    "track": "R U Mine?",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "4d84d9",
    "pollyear": 2020,
    "position": 43,
    "artist": "Angus & Julia Stone",
    "track": "Chateau",
    "releaseyear": "2017"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "54156d",
    "pollyear": 2020,
    "position": 44,
    "artist": "Florence + The Machine",
    "track": "Shake It Out",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "9d7ccc",
    "pollyear": 2020,
    "position": 45,
    "artist": "The Black Keys",
    "track": "Lonely Boy",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "437db6",
    "pollyear": 2020,
    "position": 46,
    "artist": "The Rubens",
    "track": "Hoops",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "3e74c3",
    "pollyear": 2020,
    "position": 47,
    "artist": "Mumford & Sons",
    "track": "I Will Wait",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "36e9e5",
    "pollyear": 2020,
    "position": 48,
    "artist": "Hermitude",
    "track": "HyperParadise {Flume Remix}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "ebaf8c",
    "pollyear": 2020,
    "position": 49,
    "artist": "Tash Sultana",
    "track": "Jungle",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "France",
    "id": "ee9491",
    "pollyear": 2020,
    "position": 50,
    "artist": "Daft Punk",
    "track": "Get Lucky {Ft. Pharrell Williams & Nile Rodgers}",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "0052f9",
    "pollyear": 2020,
    "position": 51,
    "artist": "Amy Shark",
    "track": "Adore",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "a46ccd",
    "pollyear": 2020,
    "position": 52,
    "artist": "Gang of Youths",
    "track": "The Deepest Sighs, The Frankest Shadows",
    "releaseyear": "2017"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "ddc545",
    "pollyear": 2020,
    "position": 53,
    "artist": "Sia",
    "track": "Chandelier",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "1f3806",
    "pollyear": 2020,
    "position": 54,
    "artist": "Grouplove",
    "track": "Tongue Tied",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "a2cb7e",
    "pollyear": 2020,
    "position": 55,
    "artist": "Skrillex",
    "track": "Bangarang {Ft. Sirah}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "7d61ab",
    "pollyear": 2020,
    "position": 56,
    "artist": "Macklemore & Ryan Lewis, Wanz",
    "track": "Thrift Shop {Ft. Wanz}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "7a2f4e",
    "pollyear": 2020,
    "position": 57,
    "artist": "Kendrick Lamar",
    "track": "HUMBLE.",
    "releaseyear": "2017"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "439aeb",
    "pollyear": 2020,
    "position": 58,
    "artist": "Sticky Fingers",
    "track": "Gold Snafu",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "Sweden",
    "id": "5877ca",
    "pollyear": 2020,
    "position": 59,
    "artist": "Adrian Lux",
    "track": "Teenage Crime",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "58a855",
    "pollyear": 2020,
    "position": 60,
    "artist": "Kendrick Lamar",
    "track": "Swimming Pools (Drank)",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "New Zealand",
    "id": "6b3bdc",
    "pollyear": 2020,
    "position": 61,
    "artist": "Lorde",
    "track": "Green Light",
    "releaseyear": "2017"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "15a035",
    "pollyear": 2020,
    "position": 62,
    "artist": "Frank Ocean",
    "track": "Thinkin Bout You",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "fd7816",
    "pollyear": 2020,
    "position": 63,
    "artist": "Hermitude",
    "track": "The Buzz {Ft. Mataya & Young Tapz}",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "99a401",
    "pollyear": 2020,
    "position": 64,
    "artist": "RÜFÜS DU SOL",
    "track": "Innerbloom {What So Not Remix}",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "79ab17",
    "pollyear": 2020,
    "position": 65,
    "artist": "Tame Impala",
    "track": "Feels Like We Only Go Backwards",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "ae8690",
    "pollyear": 2020,
    "position": 66,
    "artist": "Tame Impala",
    "track": "Elephant",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "d802d6",
    "pollyear": 2020,
    "position": 67,
    "artist": "Hilltop Hoods",
    "track": "I Love It {Ft. Sia}",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "5b3fa9",
    "pollyear": 2020,
    "position": 68,
    "artist": "Azealia Banks",
    "track": "212 {Ft. Lazy Jay}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "866402",
    "pollyear": 2020,
    "position": 69,
    "artist": "Flume & Nick Murphy / Chet Faker",
    "track": "Drop The Game",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "2df3c5",
    "pollyear": 2020,
    "position": 70,
    "artist": "Catfish and the Bottlemen",
    "track": "7",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "9f7070",
    "pollyear": 2020,
    "position": 71,
    "artist": "Billie Eilish",
    "track": "bad guy",
    "releaseyear": "2019"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "f700c5",
    "pollyear": 2020,
    "position": 72,
    "artist": "Kanye West",
    "track": "Monster {ft. Jay-Z, Rick Ross, Nicki Minaj & Bon Iver}",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "e046d0",
    "pollyear": 2020,
    "position": 73,
    "artist": "Arctic Monkeys",
    "track": "Why'd You Only Call Me When You're High?",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Sweden",
    "id": "9c326c",
    "pollyear": 2020,
    "position": 74,
    "artist": "Robyn",
    "track": "Dancing On My Own",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "e8e603",
    "pollyear": 2020,
    "position": 75,
    "artist": "Calvin Harris",
    "track": "Feel So Close",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "c70bdb",
    "pollyear": 2020,
    "position": 76,
    "artist": "Travis Scott",
    "track": "SICKO MODE",
    "releaseyear": "2018"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "e06398",
    "pollyear": 2020,
    "position": 77,
    "artist": "Kanye West",
    "track": "Black Skinhead",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "a3788b",
    "pollyear": 2020,
    "position": 78,
    "artist": "San Cisco",
    "track": "Awkward",
    "releaseyear": "2011"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "9ee086",
    "pollyear": 2020,
    "position": 79,
    "artist": "Mallrat",
    "track": "Charlie",
    "releaseyear": "2019"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "8e8bdc",
    "pollyear": 2020,
    "position": 80,
    "artist": "Kanye West",
    "track": "Ultralight Beam {Ft. Chance The Rapper, The-Dream, Kelly Price & Kirk Franklin}",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "086eb1",
    "pollyear": 2020,
    "position": 81,
    "artist": "Cub Sport",
    "track": "Come On Mess Me Up",
    "releaseyear": "2016"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "132d39",
    "pollyear": 2020,
    "position": 82,
    "artist": "Flume",
    "track": "On Top {Ft. T-Shirt}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "89ceb9",
    "pollyear": 2020,
    "position": 83,
    "artist": "Ruel",
    "track": "Painkiller",
    "releaseyear": "2019"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "e3a222",
    "pollyear": 2020,
    "position": 84,
    "artist": "Ruby Fields",
    "track": "Dinosaurs",
    "releaseyear": "2018"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "09f37d",
    "pollyear": 2020,
    "position": 85,
    "artist": "J. Cole",
    "track": "No Role Modelz",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "0534b9",
    "pollyear": 2020,
    "position": 86,
    "artist": "The Wombats",
    "track": "Greek Tragedy",
    "releaseyear": "2015"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "e1006a",
    "pollyear": 2020,
    "position": 87,
    "artist": "Matt Corby",
    "track": "Resolution",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "274c14",
    "pollyear": 2020,
    "position": 88,
    "artist": "Glass Animals",
    "track": "Gooey",
    "releaseyear": "2014"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "ac5d54",
    "pollyear": 2020,
    "position": 89,
    "artist": "Two Door Cinema Club",
    "track": "Undercover Martyn",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "714512",
    "pollyear": 2020,
    "position": 90,
    "artist": "Childish Gambino",
    "track": "This Is America",
    "releaseyear": "2018"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "266cbf",
    "pollyear": 2020,
    "position": 91,
    "artist": "Rex Orange County",
    "track": "Loving Is Easy {Ft. Benny Sings}",
    "releaseyear": "2017"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "064558",
    "pollyear": 2020,
    "position": 92,
    "artist": "Kendrick Lamar",
    "track": "m.A.A.d city {Ft. MC Eiht}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "76ab1e",
    "pollyear": 2020,
    "position": 93,
    "artist": "Flume",
    "track": "Sleepless {Ft. Jezzabell Doran}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "569fbe",
    "pollyear": 2020,
    "position": 94,
    "artist": "The Preatures",
    "track": "Is This How You Feel?",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "86c471",
    "pollyear": 2020,
    "position": 95,
    "artist": "FISHER",
    "track": "Losing It",
    "releaseyear": "2018"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "3fed73",
    "pollyear": 2020,
    "position": 96,
    "artist": "Major Lazer",
    "track": "Get Free {Ft. Amber Coffman}",
    "releaseyear": "2012"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "39da7c",
    "pollyear": 2020,
    "position": 97,
    "artist": "Adele",
    "track": "Rolling In The Deep",
    "releaseyear": "2010"
    },
    {
    "alltime": True,
    "country": "UK",
    "id": "320d54",
    "pollyear": 2020,
    "position": 98,
    "artist": "Disclosure",
    "track": "You & Me {Ft. Eliza Doolittle} {Flume Remix}",
    "releaseyear": "2013"
    },
    {
    "alltime": True,
    "country": "Australia",
    "id": "3d70e5",
    "pollyear": 2020,
    "position": 99,
    "artist": "Ruel",
    "track": "Dazed & Confused {Prod. M-Phazes}",
    "releaseyear": "2018"
    },
    {
    "alltime": True,
    "country": "USA",
    "id": "20792f",
    "pollyear": 2020,
    "position": 100,
    "artist": "Bon Iver",
    "track": "Holocene",
    "releaseyear": "2011"
    }
]

column_names = ["alltime", "country", "id", "pollyear", "position", "artist", "track", "releaseyear"]
df = pd.DataFrame(columns = column_names)

for i in tracks:
    df = df.append(i, ignore_index=True)

print('Writing to file...')
'''with open('linkDict.csv', 'w', encoding='utf-8') as link_dict_file:
    w = csv.DictWriter(link_dict_file, song_link_dict.keys())
    w.writeheader()
    w.writerow(song_link_dict)
    link_dict_file.close()
'''
df.to_csv('hot100.csv', encoding='utf-8', index=False)

print(df)
