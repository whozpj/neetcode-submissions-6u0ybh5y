from collections import defaultdict

class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value), kept sorted
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.m[key]

        # --- find correct insert position (binary search) ---
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid

        # insert while maintaining sorted order
        arr.insert(left, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m.get(key, [])
        if not arr:
            return ""

        # --- binary search for floor(timestamp) ---
        left, right = 0, len(arr) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans