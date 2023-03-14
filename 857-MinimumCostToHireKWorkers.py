import heapq

def MinCostToHireKWorker(quality, wage, K):

    workers = []

    for i in range(len(quality)):
        workers.append((wage[i]/quality[i], quality[i]))
    print(f'workers_before_sort={workers}')
    workers.sort()
    print(workers)

    ans = float('inf')
    sumq = 0
    heap = []

    for ratio, q in workers:
        heapq.heappush(heap, -q) #max heap
        sumq += q 

        if len(heap) > K:
            #remove the worker with the highest quality from the heap 
            # and subtract their quality from the sum of qualities.

            sumq += heapq.heappop(heap)
            

        if len(heap) == K:

            ans = min(ans, ratio*sumq)
        
    return ans

# N log N






print(MinCostToHireKWorker(quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3))


