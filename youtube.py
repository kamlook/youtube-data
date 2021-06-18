from googleapiclient.discovery import build 

api_key = 'AIzaSyD_-bnanDMKT97zt5DtBEUvxDs1RP05RbQ'

youtube = build('youtube', 'v3', developerKey = api_key)

channel_request = youtube.channels().list(
	part = 'snippet', #'statistics', 'contentDetails'
	forUsername = 'Atrioc',
	)
playlist_request = youtube.playlistItems().list(
	part = 'contentDetails',
	playlistId = 'UUgv4dPk_qZNAbUW9WkuLPSA'
	)
video_request = youtube.videos().list(
	part = 'statistics',
	chart= 'mostPopular'
	#maxResults = int
	)


#channel_response = channel_request.execute()
playlist_response = playlist_request.execute()
video_response = video_request.execute()

# print(channel_response)
# print(playlist_response)
print(video_response)