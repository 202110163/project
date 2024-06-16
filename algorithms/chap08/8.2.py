def knapSack_fractional_greedy(obj, W):
    obj.sort(key=lambda o: o[2]/o[1], reverse=True)

    totalValue = 0
    for o in obj:
        if W <= 0:
            break
        if W - o[1] >= 0:
            W -= o[1]
            totalValue += o[2]
        else:
            fraction = W / o[1]
            totalValue += o[2] * fraction
            W = int(W-o[1]*fraction) 
    return totalValue

obj1 = [("A", 10, 90), ("B", 12, 140), ("C", 8, 90)]
print("배낭 용량: 18")
print("부분적인 배낭 최대 가치 (용량 18):", knapSack_fractional_greedy(obj1, 18), end='\n\n')

obj2 = [("A", 20, 70), ("B", 40, 40), ("C", 20, 100), ("D", 30, 100)]
print("배낭 용량: 50")
print("부분적인 배낭 최대 가치 (용량 50):", knapSack_fractional_greedy(obj2, 50))