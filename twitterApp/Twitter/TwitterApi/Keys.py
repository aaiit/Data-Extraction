USER_KEYS = ['id_str', 'screen_name', 'created_at', 'description', 'verified', 'followers_count', 'friends_count',
             'lang',
             'time_zone', 'withheld_in_countries']
TWEET_KEYS = ['created_at', 'id_str', 'full_text', 'truncated', 'user.id_str', 'retweet_count', 'reply_count',
              'favorite_count', 'lang', 'source', "geo", "coordinates", "place"] \
             + ['entities.' + t for t in
                ['hashtags.text', 'user_mentions.id_str', 'urls.expanded_url', 'symbols']]
REPLY_KEYS = TWEET_KEYS + ['in_reply_to_status_id_str']
FRIENDSHIP_KEYS = ['id_str', 'following', 'followed_by']
TWEET_IMAGE_KEYS = TWEET_KEYS + ['extended_entities.media.' + t for t in ['id_str', 'type', 'media_url_https']]
TWEET_VIDEO_KEYS = TWEET_KEYS + ['extended_entities.media.' + t for t in
                                 ['id_str', 'media_url_https', 'type', 'video_info.variants.url']]
