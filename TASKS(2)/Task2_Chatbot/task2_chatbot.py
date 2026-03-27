def chatbot():
    print('Basic Rule-Based Chatbot (type exit or bye to quit)')

    responses = {
        'hello': 'Hi! How can I help you today?',
        'hi': 'Hello! What can I do for you?',
        'how are you': 'I am just a script, but I am functioning normally! 😊',
        'what is your name': 'I am CodeAlpha Bot.',
        'bye': 'Goodbye! Have a nice day! 🌟',
        'exit': 'Goodbye! Have a nice day! 🌟',
        'thank you': 'You are welcome!'
    }

    while True:
        user = input('You: ').strip().lower()
        if not user:
            continue

        if user in ('bye', 'exit'):
            print('Bot:', responses.get(user))
            break

        matched = False
        for key,pos_resp in responses.items():
            if key in ('bye', 'exit'):
                continue
            if key in user:
                print('Bot:', pos_resp)
                matched = True
                break

        if not matched:
            print('Bot: Sorry, I did not understand that. Can you say it differently?')


if __name__ == '__main__':
    chatbot()
