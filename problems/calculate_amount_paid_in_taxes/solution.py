class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = prev = 0

        for stage, percent in brackets:
            if income >= stage:
                tax += (stage - prev) * (percent/100)
                prev = stage
            else:
                tax += (income - prev) * (percent/100)
                return tax
        
        return tax
