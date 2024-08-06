import heapq
class Twitter:
    def __init__(self):
        self.time=0
        self.tweet={}
        self.follo={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            heap=[]
            self.tweet[userId]=heap
        self.tweet[userId]=[(tweetId,self.time)]+self.tweet[userId]
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweet:
            self.tweet[userId] = []
        twee=list(self.tweet[userId])
        if userId in self.follo:
            for followeeId in self.follo[userId]:
                if  followeeId in self.tweet:
                    twee.extend(self.tweet[followeeId])
        twee.sort(key=lambda x:x[1],reverse=True)
        return [tweetId for tweetId, time in twee[:10]]           



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follo:
            self.follo[followerId] = set()
        self.follo[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follo and followeeId in self.follo[followerId]:
            self.follo[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
