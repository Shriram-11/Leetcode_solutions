class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Returns the intersection of two integer arrays.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # Define a helper function to find intersection
        def find_intersection(p, q):
            return [i for i in q if i in p]
        
        # Convert arrays to sets to eliminate duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Choose the smaller set for efficiency
        # Find intersection using the helper function
        return find_intersection(set1, set2) if len(set1) > len(set2) else find_intersection(set2, set1)
