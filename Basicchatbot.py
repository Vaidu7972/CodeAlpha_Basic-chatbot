def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
