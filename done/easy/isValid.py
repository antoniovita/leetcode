class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # nossa pilha
        pair = {')': '(', ']': '[', '}': '{'}  # mapa de fechamento → abertura

        for char in s:
            if char in "({[":
                stack.append(char)  # empilha aberturas
            elif char in ")}]":
                if not stack or stack[-1] != pair[char]:
                    # se a pilha está vazia ou o topo não bate com o que precisa fechar
                    return False
                stack.pop()  # remove o par correspondente

        # se a pilha está vazia no final, está tudo certo
        return len(stack) == 0
    

## entender como funciona a stack nesse leetcode!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
