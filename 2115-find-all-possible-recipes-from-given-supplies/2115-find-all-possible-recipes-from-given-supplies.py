class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        graph = {}
        in_degree = {}
        
        for recipe in recipes:
            in_degree[recipe] = 0
            graph[recipe] = []
            
        for i, recipe in enumerate(recipes):
            needed_ingredients = 0
            for ingredient in ingredients[i]:
                if ingredient in available:
                    continue
                elif ingredient in graph:
                    graph[ingredient].append(recipe)
                    needed_ingredients += 1
                else:
                    needed_ingredients += 1
            
            in_degree[recipe] = needed_ingredients
        
        queue = []
        for recipe in recipes:
            if in_degree[recipe] == 0:
                queue.append(recipe)
        
        result = []
        while queue:
            recipe = queue.pop(0)
            result.append(recipe)
            
            for dependent in graph[recipe]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        return result