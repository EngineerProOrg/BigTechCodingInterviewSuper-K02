# -*- coding: utf-8 -*-
"""
1. xác định giá trị kết quả [a, b]
2.xác định bài toán cần cực tiểu hoá hay cực đại hoá kết quả.
3. Gọi err là độ sai số chấp nhận được ( đô chia nho nhat) (thường err = 1, hay rời vào th là chặt nhị phân trên số nguyên)
ví dụ: tìm x trong array sorted rồi index từ 0 -> n - 1, 
-> vẽ trục số 0, 1, 2, ..., n - 2, n - 1
3.1 Nếu cực tiểu hoá
    l, r = a - err, b
    while l + err < r:
        m = (l + r) / 2 (chia 2.0 nếu chặt nhị phân trên số thưc, chia 2 là trên số nguyên và lấy phần nguyên)
        if is_valid(...): # hàm is_valid kiểm tra kết quả nằm trong đoạn [l, m]
            r = m
        else: # kết quả phải nằm trong đoạn (m, r]
            l = m
    # kết quả là r
    # thử lại kết quả nếu cần, nếu [a, b] bạn sure là kết quả nằm ở đó thì ko cần thử lại

3.2 Nếu cực đại hoá
    l, r = a, b + err
    while l + err < r:
        m = (l + r) / 2 (chia 2.0 nếu chặt nhị phân trên số thưc, chia 2 là trên số nguyên và lấy phần nguyên)
        if is_valid(...): # hàm is_valid kiểm tra kết quả nằm trong đoạn [m, r]
            l = m
        else:
            r = m
    # kết quả là l
    # thử lại kết quả nếu cần, nếu [a, b] bạn sure là kết quả nằm ở đó thì ko cần thử lại

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. binary search tìm pivot index chia array thành 2 array sort rồi
        0-> pivot_index, pivot_index + 1 -> n - 1 
        sau khi tìm được pivot index rồi thì áp dụng BS để tìm index tương 
ứng với giá trj target
        Time : O(log(n))
        Space: O(1)
        """
        if not nums:
            return -1
        n = len(nums)
        er = 1
        l, r = 0, n
        while l + er < r:
            m = (l + r) // 2
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        
        ans = self.get_index(nums, 0, l, target)
        if ans != -1:
            return ans
        return self.get_index(nums, l + 1, n - 1, target)
        
    def get_index(self, arr, low, high, target) -> int:
        if low > high:
            return -1
        er = 1
        l, r = low, high + er
        while l + er < r:
            m = (l + r) // 2
            if arr[m] <= target:
                l = m
            else:
                r = m
    
        return l if arr[l] == target else -1
        


    

class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        """
        [a, b] = [1, max(bloomDay)], er = 1
        chat theo r.
        """
        if not nums:
            return -1

        l, r = 0, max(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if self.is_valid(nums, m, k, mid):
                r = mid
            else:
                l = mid
        # thu lai
        return r if self.is_valid(nums, m, k, r) else -1
    
    def is_valid(self, nums, m, k, mid):
        # check kq nam trong doan tu [l, mid]
        # time : O(n), space : O(1)
        count = 0
        num_b = 0
        for idx, val in enumerate(nums):
            if val <= mid:
                count += 1
                if count == k:
                    num_b += 1
                    count = 0
            else:
                count = 0
        return num_b >= m


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        f(x) = x ** 2  - 3x + 1 tren [0, 10] 
        [a, b] = [0, n - 1]
        er = 1

        """

        first_index = self.get_first(nums, target)
        last_index = self.get_last(nums, target)
        return [first_index, last_index]

    def get_first(self, arr, target):
        if not arr:
            return -1
        n = len(arr)
        l, r = -1, n - 1
        while l + 1 < r:
            m = (l + r) // 2
            if arr[m] >= target:
                r = m
            else:
                l = m
        return r if arr[r] == target else -1

    def get_last(self, arr, target):
        if not arr:
            return -1
        n = len(arr)
        l, r = 0, n
        while l + 1 < r:
            m = (l + r) // 2
            if arr[m] <= target:
                l = m
            else:
                r = m
        return l if arr[l] == target else -1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        [1] -> index: 0
        l, r = 0, n 
        [l - > m], (m, r]
        if nums[m] < nums[m + 1]:
            ket qua chac chan tim dc o doan [m, r], -> [l, m - 1] mac du 
co kq
        else:
            # l -> m - 1
        """
        n = len(nums)
        l, r = 0, n
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m - 1] < nums[m]:
                l = m
            else:
                r = m
        return l
        
  
