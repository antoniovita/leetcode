def lengthOfLongestSubstring(s: str):
    seen = set()      # Conjunto que armazena os caracteres únicos da janela atual
    left = 0          # Ponteiro que representa o início da janela
    max_len = 0       # Armazena o maior comprimento encontrado

    for right in range(len(s)):  # right percorre cada caractere da string
        # Enquanto o caractere atual já estiver na janela (repetido), mova o início (left)
        while s[right] in seen:
            seen.remove(s[left])  # Remove o caractere do início da janela
            left += 1             # Avança o ponteiro da esquerda

        seen.add(s[right])        # Adiciona o novo caractere único à janela
        max_len = max(max_len, right - left + 1)  # Atualiza o comprimento máximo

    return max_len
