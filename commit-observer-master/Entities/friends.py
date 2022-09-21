from requests import get
import json

DISCORD_EMOJI_WRONG = ":no_entry_sign:"
DISCORD_EMOJI_RIGHT = ":white_check_mark:"

friendsObject = []

messages = []

class Friends(object):
  def __init__ (self, name, commited, discordId):
    self.name = name
    self.commited = "DID COMMIT" if commited else "DID NOT COMMIT"
    self.discordId = discordId

def get_friends_github_events(friend):
  r = get(f"https://api.github.com/users/{friend}/events")
  return json.loads(r.text)

def build_friend(friendName, commited, discordId):
  friends = friends(friendName, commited, discordId)
  friendsObject.append(friends)

def save_friends_activities():
  for friendObject in friendObject:
    emoji = DISCORD_EMOJI_RIGHT if friendObject.commited == "DID COMMIT" else DISCORD_EMOJI_WRONG
    message = ("{} <@{}> **{}** {}".format(emoji, friendObject.discordId, friendObject.commited, emoji))
    messages.append(message)
    print(message)