def chatbox():    
    print("Welcome to the ChatBox! Type your questions below:")
    while True:
        query = input("Enter your query:").lower().strip()
        if query == "hello":
            print("Hello! How can I assist you today?")
        elif query == "how are you?":
            print("I'm just a program, but thanks for asking!")
        elif query == "what is your name?":
            print("I'm ChatBot, your virtual assistant.")
        else:  
            print("I'm sorry, I don't understand that question.")
            break

if __name__ == "__main__":
    chatbox()