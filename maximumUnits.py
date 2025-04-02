class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0  
        for boxes, units in boxTypes:
            if truckSize == 0: 
                break
            boxes_to_take = min(boxes, truckSize)
            total_units += boxes_to_take * units
            truckSize -= boxes_to_take 
        return total_units