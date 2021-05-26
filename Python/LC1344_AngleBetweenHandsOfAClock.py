class Solution:
        """
        Basic math
        """
    def angleClock(self, hour: int, minutes: int) -> float:
        offset_hour_angle = 360 * (minutes + (hour % 12)  * 60) / 720
        offset_minutes_angle = 360 * minutes / 60
        
        res = (offset_hour_angle - offset_minutes_angle + 360) % 360
        
        if res > 180:
            res = 180 - (res % 180)
        return res
