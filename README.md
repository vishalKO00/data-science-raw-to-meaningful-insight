# Instagram Profile Data Parser & Analysis (Python)

## Overview

This project simulates parsing and analyzing Instagram-style profile data using pure Python.
The dataset contains raw text profiles formatted similarly to how information appears on a social media page.

The goal of the project was to practice **data cleaning, parsing, transformation, and analysis** using Python without relying on external libraries like pandas.

Each profile contains:

* Username
* Name
* Posts
* Followers
* Following
* Bio

The raw data is stored as text and then processed into structured Python dictionaries.

---

## Dataset Format

Each profile follows this structure:

```
username
Name
123 posts
12.5K followers
345 following
Bio text
```

Profiles are separated by a blank line.

Example:

```
alpha_trader
Rohit Mehra
1,204 posts
78.4K followers
412 following
Stock market trader | Options
```

---

## What This Project Demonstrates

### Data Parsing

Splitting raw text data into structured records using newline patterns.

### Data Cleaning

Converting values like:

* `23.4K` → `23400`
* `1.4M` → `1400000`
* `1,204` → `1204`

### Data Structuring

Each profile is converted into a dictionary:

```
{
 "Username": "alpha_trader",
 "Name": "Rohit Mehra",
 "posts": 1204,
 "followers": 78400,
 "following": 412,
 "bio": "Stock market trader | Options"
}
```

### Data Analysis

The project performs several analyses:

* Find account with **maximum posts**
* Extract **unique bios**
* Calculate **Top Influencers**
* Sort profiles by followers
* Compute **Follower / Following influence score**

---

## Influence Score

Influence is estimated using:

```
Influence Score = followers / (following + 1)
```

The `+1` prevents division by zero when an account follows nobody.

Example result:

```
Top 5 Most Influential Accounts

1. hustle_aman
   Followers: 1400000
   Following: 301
   Influence Score: 4635.76
```

---

## Key Python Concepts Used

* String parsing
* `.split()` for structured text processing
* List comprehensions
* Dictionary storage
* Sorting with `key=lambda`
* `max()` and `min()` functions
* Set operations for unique values

---

## Project Structure

```
instagram-parser/
│
├── main.py
├── README.md
└── raw_data.txt (optional)
```

---

## Learning Outcome

This project helped practice how raw messy text data can be converted into structured datasets suitable for analysis.
It also reinforced fundamental Python skills like string manipulation, iteration, and custom metrics.

---

## Future Improvements

Possible extensions:

* Visualizing follower distributions
* Detecting outliers
* Categorizing bios automatically
* Using pandas for large datasets
* Creating graphs using matplotlib

---

## Author


Student project for practicing **data parsing and basic data analysis using Python**.
