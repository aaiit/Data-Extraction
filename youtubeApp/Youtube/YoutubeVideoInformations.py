import json

import requests as req

api = 'AIzaSyCPYehigrYNp7TkN12zTmwu3cDRt2CM4ZE'


class VideoContent:
    '''
    This class is going to be used to retrieve the following informations about the video (video_id):
        snippet(description,tags,defaultLanguage)
        topicDetails(topicCategories)
        statistics(viewCount,likeCount,dislikeCount,commentCount)
    '''

    def __init__(self, api):
        self.link = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,topicDetails'
        self.api = '&key=' + api
        self.fields = {}

    def filter(self, info=True):
        if not info:
            self.fields.pop('&fields=', None)
        else:
            self.fields[
                '&fields='] = 'items(topicDetails(topicCategories)' \
                              ',snippet(description,tags,defaultLanguage),statistics(' \
                              'viewCount,likeCount,dislikeCount,commentCount))'
        return self

    def request(self, video_id):
        self.fields['&id='] = video_id
        link = self.link + self.api + ''.join([k + v for k, v in self.fields.items()])
        result = req.get(link)
        print('Video Extra Infos: ', result, video_id)
        if result.status_code != 200:
            return {}
        data = json.loads(result.content)
        data = {} if ('items' not in data or len(data['items']) == 0) else data['items'][0]
        if 'topicDetails' in data and 'topicCategories' in data['topicDetails']:
            data['topicCategories'] = [s.split('/')[-1] for s in
                                       data['topicDetails']['topicCategories']]
            data.pop('topicDetails', None)
        return data
