USER_KEYS = ['id', 'screen_name', 'created_at', 'description', 'verified', 'followers_count', 'friends_count', 'lang',
             'time_zone', 'withheld_in_countries']
TWEET_KEYS = ['created_at', 'id_str', 'full_text', 'truncated', 'user.id', 'retweet_count', 'reply_count',
              'favorite_count', 'lang']
REPLIES_KEYS = TWEET_KEYS
FRIENDSHIP_KEYS = ['id_str', 'following', 'followed_by']
TWEET_VIDEOS_KEYS = TWEET_KEYS + ['extended_entities.media.' + t for t in
                                  ['id', 'media_url_https', 'type','video_info.variants']]
TWEET_IMAGES_KEYS = TWEET_VIDEOS_KEYS+ ['entities.media', 'entities.urls']
TWEET_VIDEOS_REDUCED_KEYS=['extended_entities.media.video_info.variants']