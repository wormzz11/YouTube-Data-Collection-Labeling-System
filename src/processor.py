def processing(response):
    processed_data = []
    for item in response.get("items"):
        video_id = item.get("id", {}).get("videoId")
        title = item.get("snippet", {}).get("title")

        if video_id and title:
            video_data = {
                    "title" : title,
                    "videoId" : video_id
                }
                
            processed_data.append(video_data)
            
    return processed_data
            

    
