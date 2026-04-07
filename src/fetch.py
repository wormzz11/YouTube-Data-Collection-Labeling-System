from googleapiclient.errors import HttpError
from config.settings import YOUTUBE_API_KEY
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def title_fetcher(query,  total_quantity):
    all_items = []
    token = None
    while len(all_items) < total_quantity:
        remaining = total_quantity - len(all_items)
        maxResults = min(50, remaining)
        request = youtube.search().list(
            part="snippet",
            maxResults=maxResults,
            q=query,
            relevanceLanguage="en",
            fields="nextPageToken,items(id(videoId),snippet(title, thumbnails))",
            type="video",
            pageToken = token
        )

        try:
            response = request.execute()
        except HttpError as e:
            raise
        token = response.get("nextPageToken")    
        items = response.get("items", [])
        all_items.extend(items)
        if token is None:
            break

    return {"items": all_items}
        
    



