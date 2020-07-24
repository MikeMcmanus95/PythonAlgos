'''
Leetcode #846: Hand of Straights
https://leetcode.com/problems/hand-of-straights/
Time: O(n log(n)) | Space O(n)
'''

from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        cardCount = {}

        for card in hand:
            if card not in cardCount:
                cardCount[card] = 1
            else:
                cardCount[card] += 1

        cardCountKeys = sorted(cardCount)

        while cardCountKeys:
            minVal = cardCountKeys[0]
            for i in range(minVal, minVal + W):
                if i not in cardCount:
                    return False
                if cardCount[i] == 1:
                    cardCountKeys.remove(i)
                else:
                    cardCount[i] -= 1
        return True
