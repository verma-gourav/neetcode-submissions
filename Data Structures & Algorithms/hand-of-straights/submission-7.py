class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)

        for card in hand:
            start = card
            
            # if there exist cards less the current card
            while count[start - 1]:
                start -= 1
            
            while start <= card:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        
        return True