import datetime
from Entities.peopleInfo import peopleInfo
from Entities.friends import get_friends_github_events
from Entities.friends import build_friend
from Entities.friends import save_friends_activities
from Entities.friends import Friends

def Main():
  FIRST_DATE_CHAR_INDEX = 0
  LAST_DATE_CHAR_INDEX = 10

  today = str(datetime.date.today())
  for friend in peopleInfo():
    commited = False
    jsonObject = get_friends_github_events(friend["username"])
    for key in jsonObject:
      eventType = key["type"]
      isToday = key["created_at"][FIRST_DATE_CHAR_INDEX : LAST_DATE_CHAR_INDEX]
      if eventType == "PushEvent" and isToday == today:
        commited = True
        break
    if not commited:
      build_friend(friend["username"], False, friend["discordId"])
    else:
      build_friend(friend["username"], True, friend["discordId"])
  save_friends_activities()