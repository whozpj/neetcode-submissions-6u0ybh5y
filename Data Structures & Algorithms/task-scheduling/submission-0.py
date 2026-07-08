class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #we should use the most frequent values first.
        #remove from maxheap and then reinsert after cooldown is done


        hashmap = {}
        max_heap = []
        for task in tasks:
            hashmap[task] = 1 + hashmap.get(task, 0)

        # create a maxHeap of just unique vars

        for letter in hashmap:
            frequency = hashmap[letter]
            heapq.heappush(max_heap, [-frequency, letter])

        #use a queue as a cooldown counter. keep track of time, and if
        #time permits reuse, repush to heap

        time = 0
        cooldown = []

        while max_heap or cooldown:
            time += 1
            if max_heap:
                frequency, letter = heapq.heappop(max_heap)
                frequency = -frequency #need to reconvert from negative

                frequency -= 1 # reduce by one cuz used

                if frequency > 0:
                    cooldown.append([-frequency, letter, time + n]) #time + n = cooldown done

            #check cooldown for anythign to put in now:
            if cooldown:
                cf, cl, ct = cooldown[0]

                if ct == time:
                    heapq.heappush(max_heap, [cf,cl])
                    cooldown.pop(0)
                

        return time






