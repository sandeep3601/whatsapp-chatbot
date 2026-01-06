import ollama

# Ensure you've pulled the model first: run `ollama pull llama3` in your terminal
response = ollama.chat(
    model="llama3",  # Fixed typo: "modle" → "model"
    messages=[
        {
            "role": "system", 
            "content": '''you are a person named SANDEEP KUMAR you speak hindi as well as english you are from india and you are a coder you analyze chat history and respond to the next person like SANDEEP KUMAR and give short response  
                          '''
        },
        {
            "role": "user", 
            "content": '''
[9:58 pm, 3/7/2025] Tejinder 9 To 3: bhai tughe konsa gana pasand hai
[11:05 am, 7/7/2025] Tejinder 9 To 3: bata bhai
[8:49 am, 8/7/2025] SANDEEP KUMAR: yrr me tou karan aujla ke gane hi sunta hu bas
[8:50 am, 8/7/2025] SANDEEP KUMAR: mughe to punjabi gane hi pasand hai
[10:38 am, 8/7/2025] Tejinder 9 To 3: mughe bhi pasand hai but tujhe uske gane kyu pasand hai bro
'''
        }
    ]
)

# Print the AI's response
print( response['message']['content'])