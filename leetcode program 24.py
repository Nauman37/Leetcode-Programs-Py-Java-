class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # customers coming after closing time
        closed_penalty = customers.count('Y')
        open_penalty = 0

        min_penalty = closed_penalty
        best_hour = 0

        for i in range(n):
            if customers[i] == 'Y':
                closed_penalty -= 1
            else:
                open_penalty += 1

            total_penalty = open_penalty + closed_penalty

            if total_penalty < min_penalty:
                min_penalty = total_penalty
                best_hour = i + 1

        return best_hour
