from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='[Insert Webex API Token]')


rooms = api.rooms.list()

for room in rooms:
	if 'My Room' in room.title:
		roomId = room.id
		break

api.messages.create(roomId, text='Hello World')
