
class UserInfo(object):
    def __init__(self):
        self.followee = set()
        self.tweets = []

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user_map = {} #<user_id, UserInfo>

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.user_map: self.user_map[userId] = UserInfo()
        self.user_map[userId].tweets.append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        if userId not in self.user_map: return []
        heap = []
        for time, tid in self.user_map[userId].tweets:
            heap.append([-time, tid])
        for followeeid in self.user_map[userId].followee:
            if followeeid not in self.user_map: continue
            for time, tid in self.user_map[followeeid].tweets:
                heap.append([-time, tid])
        heapq.heapify(heap)
        res = []
        for i in range(10):
            if len(heap) == 0: break
            time, tid = heapq.heappop(heap)
            res.append(tid)
        return res


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_map: self.user_map[followerId] = UserInfo()
        self.user_map[followerId].followee.add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_map: return
        self.user_map[followerId].followee.remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)