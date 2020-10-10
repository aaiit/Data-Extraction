import json

import pandas

from youtubeApp.Youtube.YoutubeSearchByKeywords import SearchRequest
from youtubeApp.Youtube.YoutubeVideoComments import VideoComments
from youtubeApp.Youtube.YoutubeVideoInformations import VideoContent

api = 'AIzaSyCPYehigrYNp7TkN12zTmwu3cDRt2CM4ZE'

search = SearchRequest(api)
video_infos = VideoContent(api).filter()
comments = VideoComments(api).filter()

fields_search = {'q': 'vaccine corona', 'max_results': '60', 'by_channel': '', 'order_by': 'relevance',
                 'related_to': '',
                 'before_time': '2020-08-23T00:00:00Z', 'after_time': '2020-08-22T00:00:00Z'}


fields_comments = {'sort': 'relevance', 'count': '30', 'format': True, 'video_id': 'gAiDp0_525U',
          'keywords': ''}


def search_videos(fields):
    count = int(fields.pop('max_results', 50))
    search.type('video') \
        .query(fields.pop('q', '')) \
        .location(fields.pop('lat', ''), fields.pop('long', ''), fields.pop('radius', '')) \
        .max_results(count if count <= 50 else 50) \
        .by_channel(fields.pop('by_channel', '')) \
        .order_by(fields.pop('order_by', '')) \
        .related_to(fields.pop('related_to', '')) \
        .before_time(fields.pop('before_time', None)) \
        .after_time(fields.pop('after_time', None)) \
        .filter_snippet(fields.pop('filter_snippet', True)) \
        .region(fields.pop('region', ''))
    videos = search.request()
    while count > 50 and search.nextPage:
        count -= 50
        search.max_results(count if count <= 50 else 50)
        search.next_page()
        videos.extend(search.request())
    if not videos:
        return []
    i = 0
    while i < len(videos):
        vid = videos[i]
        # Try to get more informations about the video as well as its comments.
        video_id = vid['id']['videoId']

        # Add the new informations to the list of the videos.
        if vid['id']['kind'] == 'video':
            video = video_infos.request(video_id)
            if not video:
                # In case of any error remove this video from the results and go next.
                videos.remove(vid)
                continue
            add_video_newInfos(vid, video)
        i += 1


    BN=[]
    for d in videos:
        N={}
        print(type(d))
        for bk in d:
            if type(d[bk]) is dict:
                for k in d[bk]:
                    N[k]=d[bk][k]
            else:
                N[bk]=d[bk]
        BN.append(N)
        
    return json.dumps(BN, indent=3, default=str) 


def search_comments(fields):
    count = int(fields.pop('count', 50))
    comments.max_comments(count if count <= 50 else 50) \
        .format(fields.pop('format', True)) \
        .sort(fields.pop('sort', '')) \
        .related_to_video(fields.pop('video_id', '')) \
        .related_to_keywords(fields.pop('keywords', ''))
    results = comments.request()
    while count > 50 and comments.nextPage:
        count -= 50
        comments.max_comments(count if count <= 50 else 50)
        comments.next_page()
        results.extend(comments.request())
    BN=[]
    for d in results:
        N={}
        print(type(d))
        for bk in d:
            if type(d[bk]) is dict:
                for k in d[bk]:
                    N[k]=d[bk][k]
            else:
                N[bk]=d[bk]
        BN.append(N)
    return json.dumps(BN, indent=3, default=str) 


##################################################################  HELPER FUNCTION
def add_video_newInfos(old, new):
    # Beware of not having a key in the returned data.
    old['snippet'].update(new['snippet'] if 'snippet' in new else {})
    old['statistics'] = new['statistics'] if 'statistics' in new else {}
    old['topicCategories'] = new['topicCategories'] if 'topicCategories' in new else {}


with open('result2.json', 'w') as f:
    f.write(search_comments(fields_comments))
