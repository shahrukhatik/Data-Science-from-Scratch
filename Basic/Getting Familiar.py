###Just Random "Getting Feels"

users = [
{"id" : 0, "name": "Shahrukh"},
{"id" : 1, "name": "Mazy"},
{"id" : 2, "name": "Sartaj"},
{"id" : 3, "name": "Emily"},
{"id" : 4, "name": "Sierra"},
{"id" : 5, "name": "Andy"},
{"id" : 6, "name": "Rob"},
{"id" : 7, "name": "Janak"},
{"id" : 8, "name": "Wasil"},
{"id" : 9, "name": "Kartik"}
]

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

## Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

#Loop over friendship pairs to populate it
for i, j in friendship_pairs:
    friendships[i].append(j) ## add j as a friend of user i
    friendships[j].append(i) ## add i as a friend of user j

def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
total_connections = sum(number_of_friends(user) for user in users)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key = lambda id_and_friends: id_and_friends[1],reverse=True)

######