rom webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='[Insert Webex API Token]')


rooms = api.rooms.list()

for room in rooms:
	if 'My Room' in room.title:
		roomId = room.id
		break
    
file_list = ["./myfile.txt"]

api.messages.create(roomId, text='Hello World')

api.messages.create(roomId=roomId, files=file_list)
