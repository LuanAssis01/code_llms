import ollama

client = ollama.Client()

context = f"""Em uma vila charmosa, os irmãos Jack e Jill partem em viagem. 
uma missão para buscar água no topo de uma colina 
bem. Enquanto subiam, cantando alegremente, infortúnio  
atingido - Jack tropeçou em uma pedra e caiu 
descendo a colina, com Jill seguindo o exemplo. 
Embora um pouco machucados, a dupla voltou para casa para  
abraços reconfortantes. Apesar do acidente, 
seus espíritos aventureiros permaneceram intactos, e eles 
continuou explorando com prazer.
"""

instruction = f""" 
Conte-me sobre a escova de dentes inteligente AeroGlide UltraSlim da Boieexit
"""

prompt = f"Context: {context}\n\nQuestion: {instruction}"

response = client.generate(model="llama3.2", prompt=prompt)

# imprime a resposta
print("Resposta do Llama 3.2:\n", response['response'])