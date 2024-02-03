class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        suggestions= []
        for i in range(len(searchWord)):
            suggestions.append([])
            for j in products:
                if j[0:i+1]==searchWord[0:i+1]:
                    suggestions[i].append(j)
            suggestions[i]= sorted(suggestions[i])[:3]
        return suggestions
                