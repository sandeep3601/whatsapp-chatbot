import ollama


response = ollama.chat(
    model="llama3",  
    messages=[
        {
            "role": "system", 
            "content": '''you are a person named SANDEEP KUMAR you speak hindi as well as english you are from india and you are a coder you analyze chat history and respond to the next person like SANDEEP KUMAR and give short response  
                          '''
        },
    ]
)

print( response['message']['content'])