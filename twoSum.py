class Solution(object):
    def twoSum(self, nums, target):
        """
        整数数组中两数之和等于指定数，找出它们并返回下标
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        for i, num in enumerate(nums):
            if target - num in hashtable:
        # 如果存在就返回字典记录索引和当前索引
                return [hashtable[target - num], i]
        # 如果不存在就放入哈希表里
            hashtable[num] = i
        return []
