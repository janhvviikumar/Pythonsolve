class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dist1=0
        dist2=0
        for i in range(min(start,destination),max(start,destination)):
            dist1+=distance[i]
        flag=True
        while flag!=False:
            for i in range(max(start,destination),len(distance)):
                dist2+=distance[i]
            for j in range(min(start,destination)):
                dist2+=distance[j]
            flag=False
        if dist1<dist2:
            return dist1
        else:
            return dist2
        