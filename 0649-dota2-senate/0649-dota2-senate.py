class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Radiant=deque()
        Dire=deque()
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=="R":
                Radiant.append(i)
            else:
                Dire.append(i)
        print("Radiant:",Radiant)
        print(f'Dire {Dire}')
        print(f'n is {n}')
        # "DDDRR"
        # Radiant: []
        # Dire [2,5,6]
        # R=4
        # J=1
        # n=5
        while Radiant and Dire:
            R=Radiant.popleft()
            J=Dire.popleft()
            if R<J:
                Radiant.append(R+n)
            else:
                Dire.append(J+n)
        return "Dire" if Dire else "Radiant"