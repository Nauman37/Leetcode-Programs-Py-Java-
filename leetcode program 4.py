#You are given an integer numberOfUsers representing the total number of users
#and an array events of size n x 3.
#Each events[i] can be either of the following two types:
#Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
#This event indicates that a set of users was mentioned in a message at timestampi.
#The mentions_stringi string can contain one of the following tokens:
#id<number>: where <number> is an integer in range [0,numberOfUsers - 1].
#There can be multiple ids separated by a single whitespace and may contain duplicates.
#This can mention even the offline users.
#ALL: mentions all users.
#HERE: mentions all online users.
#Offline Event: ["OFFLINE", "timestampi", "idi"]
#This event indicates that the user idi had become offline at timestampi for 60 time units.
#The user will automatically be online again at time timestampi + 60.
#Return an array mentions where mentions[i] represents the number of mentions
#the user with id i has across all MESSAGE events.
#All users are initially online, and if a user goes offline or comes back online,
#their status change is processed before handling any message event
#that occurs at the same timestamp.

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        norm_events =[]
        for e in events:
            etype, ts_str, third = e
            t = int(ts_str)
            if etype == "OFFLINE":
                norm_events.append((t, 0,"OFFLINE", int(third)))
            else:
                norm_events.append((t, 1,"MESSAGE", third))
        norm_events.sort()

        mentions= [0]*numberOfUsers
        online=[True]*numberOfUsers

        offline_until=[]

        for t, _, etype, payload in norm_events:
            while offline_until and offline_until[0][0]<= t:
                end_time,uid=heapq.heappop(offline_until)
                online[uid] = True 

            if etype =="OFFLINE":
                uid=payload
                online[uid] = False
                heapq.heappush(offline_until,(t+60,uid))
            else:
                mention_str =payload
                tokens=mention_str.split()

                has_all = any(tok =="ALL" for tok in tokens)
                has_here = any(tok =="HERE" for tok in tokens)

                if has_all:
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                if has_here:
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                for tok in tokens:
                    if tok.startswith("id"):
                        uid = int(tok[2:])
                        if 0 <= uid <numberOfUsers:
                            mentions[uid] += 1
        return mentions        
