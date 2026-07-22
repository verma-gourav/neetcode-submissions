class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list) # user_id -> list of [timestamp, tweet_id]
        self.followers = defaultdict(set) # user_id -> set of followee_id

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        self.tweets[userId].append([self.timestamp, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        user_list = list(self.followers[userId]) # making a copy of followees of a userId
        user_list.append(userId) # adding userId to that list as a user can see their own tweets

        # pushing the absolute latest tweet of each followed user into heap
        for u_id in user_list:
            if u_id in self.tweets:
                last_index = len(self.tweets[u_id]) - 1 # index of latest tweet 
                time, t_id = self.tweets[u_id][last_index]

                # storing time, tweet id, user id and new index to look at
                heapq.heappush(min_heap, (time, t_id, u_id, last_index - 1))
        
        # popping from heap 10 times to get 10 latest tweets
        while min_heap and len(res) < 10:
            time, t_id, u_id, next_index = heapq.heappop(min_heap)
            res.append(t_id)
        
            # if the same user has older tweets left, push them into heap
            if next_index >= 0:
                next_time, next_t_id = self.tweets[u_id][next_index]
                heapq.heappush(min_heap, (next_time, next_t_id, u_id, next_index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
