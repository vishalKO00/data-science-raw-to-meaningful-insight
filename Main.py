with open ("raw_data.txt" , encoding = 'utf-8') as f:
    data = f.read()

data

chunks = data.split("\n\n")

chunks

chunks[0]

def converted_numbers(value):
    value = value.replace(",", "").strip()
    
    # normalize case (so K and k both work)
    value = value.upper()

    if "K" in value:
        return int(float(value.replace("K", "")) * 1000)
    elif "M" in value:
        return int(float(value.replace("M", "")) * 1000000)
    else:
        return int(value)

def parse_data(chunk):
    chunk = chunk.strip()
    lines = chunk.split("\n")

    username = lines[0]
    name = lines[1]

    posts = converted_numbers(lines[2].split()[0])
    followers = converted_numbers(lines[3].split()[0])
    following = converted_numbers(lines[4].split()[0])

    bio = lines[5]

    return {
        "username": username,
        "name": name,
        "posts": posts,
        "followers": followers,
        "following": following,
        "bio": bio
    }

all_chunks = []
for chunk in chunks:
    parsed_data= parse_data(chunk)
    all_chunks.append(parsed_data)
print(all_chunks)

import json
s = json.dumps(all_chunks,indent =4)
print(s)

max_posts_account = max(all_chunks, key=lambda x: x["posts"])
print(max_posts_account)

top_5 = sorted(all_chunks, key=lambda x: x["followers"], reverse=True)[:5]

for user in top_5:
    print(user["username"], "-", user["followers"])

least_5 = sorted(all_chunks, key=lambda x: x["following"])[:5]

for user in least_5:
    print(user["username"], "-", user["following"])

# Calculate ratio for each user
for user in all_chunks:
    user["ratio"] = user["followers"] / (user["following"] + 1)

# Sort by ratio (highest first)
ranked_users = sorted(all_chunks, key=lambda x: x["ratio"], reverse=True)

# Print top 5 by influence ratio
print("Top 5 Most Influential Accounts (Followers / (Following + 1)):\n")

for i, user in enumerate(ranked_users[:5], start=1):
    print(f"{i}. {user['username']}")
    print(f"   Followers: {user['followers']}")
    print(f"   Following: {user['following']}")
    print(f"   Influence Score: {round(user['ratio'], 2)}\n")


unique = set(x["bio"] for x in all_chunks)
print("different bio are:")
for bio in unique:
    
    print("\n-",bio)

print("\n\ntotal unique bio are: ",len(unique))

#note this code works for jupyter lab
