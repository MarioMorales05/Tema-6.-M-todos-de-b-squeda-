def busqueda_secuencial(lista, clave, campo):
    """
    Realiza una búsqueda secuencial en una lista de diccionarios.
    Retorna una lista de tuplas (indice, item, estado).
    """
    # Creamos una lista de estados iniciales, todos "No revisado"
    resultados_paso_a_paso = [(i, item, "No revisado") for i, item in enumerate(lista)]
    
    found_index = -1
    for i, item in enumerate(lista):
        valor_a_comparar = item[campo]
        if isinstance(valor_a_comparar, int):
            try:
                clave_comparable = int(clave)
            except ValueError:
                return resultados_paso_a_paso
        else:
            clave_comparable = str(clave).lower()
            valor_a_comparar = str(valor_a_comparar).lower()

        if valor_a_comparar == clave_comparable:
            resultados_paso_a_paso[i] = (i, item, "Encontrado")
            found_index = i
            break
        else:
            resultados_paso_a_paso[i] = (i, item, "Revisado")

    if found_index != -1:
        for i in range(found_index + 1, len(lista)):
            resultados_paso_a_paso[i] = (i, lista[i], "No revisado")

    return resultados_paso_a_paso

def busqueda_binaria(lista_ordenada, clave, campo):
    """
    Realiza una búsqueda binaria en una lista de diccionarios ordenada.
    Retorna una lista de tuplas (indice, item, estado) del proceso de búsqueda.
    """
    low = 0
    high = len(lista_ordenada) - 1
    
    # Creamos una lista inicial de estados, todos "No revisado"
    resultados = [(i, item, "No revisado") for i, item in enumerate(lista_ordenada)]
    
    while low <= high:
        mid = (low + high) // 2
        mid_item = lista_ordenada[mid]

        # Marcamos el elemento del medio como revisado
        resultados[mid] = (mid, mid_item, "Revisado")
        
        # Intentamos convertir la clave a un tipo comparable (int o str)
        valor_a_comparar = mid_item[campo]
        if isinstance(valor_a_comparar, int):
            try:
                clave_comparable = int(clave)
            except ValueError:
                # Si la clave no es un entero, no se puede comparar
                return resultados
        else:
            clave_comparable = str(clave)

        if valor_a_comparar == clave_comparable:
            # ¡Elemento encontrado!
            resultados[mid] = (mid, mid_item, "Encontrado")
            return resultados
        elif valor_a_comparar < clave_comparable:
            # El elemento está en la mitad superior
            low = mid + 1
        else: # valor_a_comparar > clave_comparable
            # El elemento está en la mitad inferior
            high = mid - 1
            
    # Si el bucle termina y no se encontró el elemento
    return resultados