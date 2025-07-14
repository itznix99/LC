class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0])-96)%2==0:
            return (False if int(coordinates[1])%2==0 else True)
        else:
            return (True if int(coordinates[1])%2==0 else False)
        