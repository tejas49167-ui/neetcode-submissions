class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l = [] 
        st = [] 
        nd = [] 

        for i in range(len(nums1)) : 

          

            if nums1[i] not in nums2 and nums1[i] not in st : 
                st.append(nums1[i]) 
        for i in range(len(nums2)) : 

            if nums2[i] not in nums1 and nums2[i] not in nd: 
                nd.append(nums2[i]) 

        return [st,nd]
            
           


        