# Day 10: Dictionaries

# Exercises

# Below is a tuple describing an album. Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then another tuple containing the track list.

(
	"The Dark Side of the Moon",
	"Pink Floyd",
	1973,
	(
		"Speak to Me",
		"Breathe",
		"On the Run",
		"Time",
		"The Great Gig in the Sky",
		"Money",
		"Us and Them",
		"Any Colour You Like",
		"Brain Damage",
		"Eclipse"
	)
)

# Convert this outer tuple to a dictionary with four keys.

music = {
	"album": "The Dark Side of the Moon",
	"band": "Pink Floyd",
	"year": 1973, 
    "tracks": (
		"Speak to Me",
		"Breathe",
		"On the Run",
		"Time",
		"The Great Gig in the Sky",
		"Money",
		"Us and Them",
		"Any Colour You Like",
		"Brain Damage",
		"Eclipse"
	)
}

# Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.

for key in music:
    print(f"{key}: {music[key]}")

# Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. 
# The date of release for The Dark Side of the Moon was March 1st, 1973. If you use a different album for the exercises, update the date accordingly.

del music["tracks"]

# Verify delete
for key in music:
    print(f"{key}: {music[key]}")

# Add and verify
music["release"] = "01.03.1973"
print(music["release"])

# Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.

print(music["tracks"]) # KeyError: 'tracks'

print(music.get("tracks")) # None