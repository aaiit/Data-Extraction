import json

import requests as req


class SearchRequest:
    def __init__(self, api):
        self.nextPage = None
        self.prevPage = None
        self.link = 'https://www.googleapis.com/youtube/v3/search?part=snippet'
        self.api = '&key=' + api
        self.fields = {}

    def type(self, types=None):
        '''
        :param types: a string containing any combination of these separated by commas:
                        ['video','channel','playlist']
        '''
        # check validity of types variable.
        if types is not None:
            types = types.lower()
            if not {x.strip() for x in types.split(',')}.issubset({'channel', 'video', 'playlist'}):
                raise ValueError('The value of "types" isn\'t valid.')
            self.fields['&type='] = '&type='.join([x.strip() for x in types.split(',')])
        else:
            self.fields.pop('&type=', None)
        return self

    def location(self, lat='', long=None, radius=None):
        '''
        :param lat: 10.3333
        :param long: -12.0004
        :param radius: cannot exceed 1000 km. You can adjust the unit: mi,km,ft,m. (e.g: 0.5mi)
                ----> radius Is mandatory.
        '''
        if lat =='':
            self.fields.pop('&location=', '')
        else:
            self.fields['&location='] = str(lat) + '%2C' + str(long) + '&locationRadius=' + str(radius) + 'mi'
        return self

    def query(self, q=''):
        '''
        :param q: list of keywords to search by.
                -----> can include | (pipe) to search for results associated with either parts. (e.g: nike|adidas)
                            ----->Should encode it in url using %7C.
                -----> can include - (dash) to exclude the following part from the results. (e.g: nike-adidas puma)
                            exclude any result related to adidas or puma.
        '''
        if q == '':
            self.fields.pop('&q=', None)
        else:
            self.fields['&q='] = q
        return self

    def max_results(self, max=0):
        '''
        :param max: the number of results to return in each page( per request).
        '''
        if max == 0:
            self.fields.pop('&maxResults=', None)
        else:
            self.fields['&maxResults='] = str(max)
        return self

    def order_by(self, order=''):
        '''
        :param order:['date','rating','relevance','title','videoCount','viewCount']
                ----> all criterias are sorted from better to worst.
                ----> videoCount: sort channel based on the number of the uploaded videos.
        '''
        if order == '':
            self.fields.pop('&order=', None)
        else:
            self.fields['&order='] = order
        return self

    def by_channel(self, channel=''):
        '''
        :param channel: id of the channel that you want to search inside of it.
        '''
        if channel == '':
            self.fields.pop('&channelId=', None)
        else:
            self.fields['&channelId='] = channel
        return self

    def related_to(self, video_id=''):
        '''
        :param video_id: id of a video
        '''
        if video_id == '':
            self.fields.pop('&relatedToVideoId=', None)
        else:
            self.fields['&relatedToVideoId='] = video_id
        return self

    def region(self, region=''):
        '''
        :param region:  ISO 3166-1 alpha-2 country code: MA,US,UK ...
        '''
        if region == '':
            self.fields.pop('&regionCode=', None)
        else:
            self.fields['&regionCode='] = region
        return self

    def next_page(self):
        if self.nextPage is None:
            self.fields.pop('&pageToken=', None)
        else:
            self.fields['&pageToken='] = self.nextPage
        return self

    def prev_page(self):
        if self.prevPage is None:
            self.fields.pop('&pageToken=', None)
        else:
            self.fields['&pageToken='] = self.prevPage
        return self

    def after_time(self, date=None):
        # date variable should be like this: yyyy-dd-mmThh:mm:ssZ
        if date is None:
            self.fields.pop('&publishedAfter=', None)
        else:
            self.fields['&publishedAfter='] = str(date)
        return self

    def before_time(self, date=None):
        # date variable should be like this: yyyy-dd-mmThh:mm:ssZ
        if date is None:
            self.fields.pop('&publishedBefore=', None)
        else:
            self.fields['&publishedBefore='] = str(date)
        return self

    def filter_snippet(self, snippet=True):
        '''
        :param snippet: True if you want to include only:
                 nextPageToken,prevPageToken,items(id,snippet(publishedAt,channelId,title))
                 in your results
        '''
        if not snippet:
            self.fields.pop('&fields=', None)
        else:
            self.fields['&fields='] = \
                'nextPageToken,prevPageToken,' \
                'items(id,snippet(publishedAt,channelId,title))'
        return self

    def request(self):
        """
        The function request data from youtube using the query built
        :return: a list containing the information about the results;
                the results are a list of dictionaries.
                ---> In case of error, the list is going to be empty.
        """
        link = self.link + self.api + ''.join([key + val for key, val in self.fields.items()])
        res = req.get(link)
        print(link)
        print('Videos Retrieval: ', res)
        if res.status_code != 200:
            raise ValueError("The request wasn't done: ", res.status_code)
        data = json.loads(res.content)
        self.nextPage = data['nextPageToken'] if 'nextPageToken' in data else None
        self.prevPage = data['prevPageToken'] if 'prevPageToken' in data else None
        if 'items' in data and len(data['items']) > 0:
            data = data['items']
            for i in range(len(data)):
                data[i]['id']['kind'] = data[i]['id']['kind'].split('#')[-1]
        else:
            data = []
        return data
