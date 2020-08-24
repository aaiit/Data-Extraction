import json

import requests as req

api = 'AIzaSyCPYehigrYNp7TkN12zTmwu3cDRt2CM4ZE'


class VideoComments:
    '''
    This class is going to be used to retrieve the following informations about comments of the video_id:

        snippet(canReply,totalReplyCount,
                    topLevelComment(
                            snippet(authorDisplayName,textDisplay,likeCount,publishedAt,updatedAt)
                            ))
        replies
    '''

    def __init__(self, api):
        self.link = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet,replies'
        self.api = '&key=' + api
        self.nextPage = None
        self.prevPage = None
        self.fields = {}

    def next_page(self):
        if self.nextPage:
            self.fields['&pageToken='] = self.nextPage
            return 1
        return 0

    def prev_page(self, begin=False):
        '''
        :param begin: To search over from the first page.
        '''
        if begin:
            self.fields.pop('&pageToken=', None)
            return 1
        elif self.prevPage:
            self.fields['&pageToken='] = self.prevPage
            return 1
        return 0

    def related_to_keywords(self, keywords=''):
        '''
        :param keywords: Filter the comments that are related to keywords.
        '''
        if keywords == '':
            self.fields.pop('&searchTerms=', None)
        else:
            self.fields['&searchTerms='] = keywords
        return self

    def related_to_video(self, video_id=''):
        '''
        :param video_id: Retrieve comments associated with the video_id
        '''
        if video_id == '':
            self.fields.pop('&videoId=', None)
        else:
            self.fields['&videoId='] = video_id
        return self

    def related_to_channel(self, channel_id=''):
        '''
        :param channel_id: Retrieve comments associated with the channel_id
        '''
        if channel_id == '':
            self.fields.pop('&allThreadsRelatedToChannelId=', None)
        else:
            self.fields['&allThreadsRelatedToChannelId='] = channel_id
        return self

    def sort(self, criteria=''):
        '''
        :param criteria: Sort the comments based on ['relevance','time']; order from better to worse.
        '''
        if criteria == '':
            self.fields.pop('&order=', None)
        else:
            self.fields['&order='] = criteria.strip()
        return self

    def max_comments(self, max=0):
        '''
        :param max: Retrieve the first 'max' comments if they exist.
        '''
        if max > 0:
            self.fields['&maxResults='] = str(max)
        else:
            self.fields.pop('&maxResults=', None)
        return self

    def filter(self, info=True):
        '''
        :param info: To retrieve only the values of the attributes that we target.
        '''
        if not info:
            self.fields.pop('&fields=', None)
        else:
            self.fields[
                '&fields='] = 'items(replies(comments(snippet(authorDisplayName,textDisplay,likeCount,publishedAt,updatedAt))),' \
                              'snippet(canReply,totalReplyCount,' \
                              'topLevelComment(' \
                              'snippet(authorDisplayName,textDisplay,likeCount,publishedAt,updatedAt)' \
                              ')))'
        return self

    def format(self, text=True):
        '''
        :param text: if false the text is contains html syntax..
        '''
        if text:
            self.fields['&textFormat='] = 'plainText'
        else:
            self.fields['&textFormat='] = 'html'
        return self

    def request(self):
        link = self.link + self.api + ''.join([k + v for k, v in self.fields.items()])
        result = req.get(link, timeout=2)
        print('Video Comments: ', result)
        if result.status_code != 200:
            return []
        data = json.loads(result.content)
        self.nextPage = data['nextPageToken'] if 'nextPageToken' in data else None
        self.prevPage = data['prevPageToken'] if 'prevPageToken' in data else None

        return data['items'] if 'items' in data else []
