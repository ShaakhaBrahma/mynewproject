from instapy import InstaPy

session=InstaPy(username="sublime_camps", password="milkyway@123").login()
session.like_by_tags(["trekking", "hiking"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
