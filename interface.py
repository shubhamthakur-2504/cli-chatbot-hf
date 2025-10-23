from model_loader import ModelLoader
from chat_history import ChatHistory
from dataclasses import dataclass

@dataclass
class ChatInterface:
    model_name: str
    history_length: int = 10
    temperature: float = 0.7

    def __post_init__(self):
        self.model_loader = ModelLoader(self.model_name)
        self.chat_pipeline = self.model_loader.load_model_and_tokenizer()
        self.chat_history = ChatHistory(self.history_length)

    def get_response(self, user_input: str) -> str:

        try:

            history = self.chat_history.get_history()
            system_prompt = "The following is a conversation between a user and an AI assistant. You are helpful and friendly assistant. Only answer the user's query based on the context provided in short."
            formatted_input = f"{system_prompt}\n"+"\n".join([f"context: {msg['role']}: {msg['content']}" for msg in history])
            prompt = f"{formatted_input}\n query: {user_input}\nBot:"
            self.chat_history.add_message("User", user_input)
            response = self.chat_pipeline(prompt, max_new_tokens=80, do_sample=True, temperature=self.temperature, repetition_penalty=1.2, top_p=0.9, top_k=50)
            if not response or "generated_text" not in response[0]:
                bot_reply = "Sorry, I couldn't generate a response."
            else:
                bot_reply = response[0]["generated_text"].split("Bot:")[-1].strip()
            self.chat_history.add_message("Bot", bot_reply)

            return bot_reply
        
        except Exception as e:
            error_msg = f"Error generating response: {e}"
            self.chat_history.add_message("Bot", error_msg)
            return error_msg
    


def main():
    model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"  
    chat_interface = ChatInterface(model_name=model_name)

    print("Welcome to the CLI Chatbot! Type '/exit' to quit.")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "/exit":
            print("Exiting the chatbot. Goodbye!")
            break

        bot_response = chat_interface.get_response(user_input)
        print(f"Bot: {bot_response}\n")

if __name__ == "__main__":
    main()