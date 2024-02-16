from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

API_KEY = 'YOUR_API_KEY'

def search_youtube(query, max_results = 10):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    try:
        search_response = youtube.search().list(
            q=query,
            part='id_snippet',
            maxResults = max_results
        ).execute()

        videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append({
                    'title': search_result['snippet']['title'],
                    'video_id': search_result['id']['videoId'],
                    'thumbnail_url': search_result['snippet']['thumbnails']['default']['url']
                })

        return videos
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))

search_query = input("Enter search query: ")
search_results = search_youtube(search_query)

print("Search Results:")
for idx, video in enumerate(search_results, start=1):
    print(f"{idx}. {video['title']} - https://www.youtube.com/watch?v={video['video_id']}")
