def simple_customer_chatbot():
    print("Welcome to Customer Service Bot!")
    print("How can I help you today? (Type 'exit' to end the conversation)")
    
    # Dictionary of predefined responses
    responses = {
        "hours": "Our hours are 9am-5pm Monday through Friday.",
        "contact": "You can contact us at support@example.com or call 555-123-4567.",
        "return": "Our return policy allows returns within 30 days of purchase with receipt.",
        "shipping": "Standard shipping takes 3-5 business days. Express shipping is 1-2 business days.",
        "help": "You can ask about: hours, contact, return, shipping, or speak with a representative.",
        "representative": "To speak with a representative, please call 555-123-4567 during business hours.",
        "price": "Prices vary by product. Please visit our website or specify which product."
    }
    
    while True:
        user_input = input("> ").lower()
        
        if user_input == "exit":
            print("Thank you for using our customer service bot. Goodbye!")
            break
        
        # Check if any keywords match
        found_response = False
        for keyword, response in responses.items():
            if keyword in user_input:
                print(response)
                found_response = True
                break
        
        # Default response if no keywords match
        if not found_response:
            print("I'm not sure I understand. For help, type 'help' or try using keywords like 'hours', 'contact', 'return', or 'shipping'.")

if __name__ == "__main__":
    simple_customer_chatbot()