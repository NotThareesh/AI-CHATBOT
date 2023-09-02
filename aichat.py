import tkinter as tk
import openai
import sys

class GoogleSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Education Chat Bot")

        self.label = tk.Label(root, text="Enter your query:", font=("Helvetica", 20))
        self.label.pack()

        self.query_entry = tk.Entry(root, font=("Helvetica", 18))
        self.query_entry.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.search_button = tk.Button(self.button_frame, text="Search", font=("Helvetica", 16), command=self.perform_search)
        # self.search_button.pack(side=tk.LEFT, padx=10)
        self.search_button.pack()

        self.exit_button = tk.Button(self.button_frame, text="Exit", font=("Helvetica", 16), command=self.exit_app)
        # self.exit_button.pack(side=tk.LEFT)
        self.exit_button.pack()

        self.results_text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 16))
        self.results_text.pack()

        openai.api_key = "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"

    def perform_search(self):
        query = self.query_entry.get()
        response = chat_gpt(query)
        self.results_text.delete(1.0, tk.END)
        
        result_list = response.split('\n')
        bullet_points = "\n".join([f"• {result.strip()}" for result in result_list])
        
        self.results_text.insert(tk.END, bullet_points)
    
    def exit_app(self):
        self.root.destroy()
        sys.exit()

def chat_gpt(query):
    prompt = f"Search the web for information about '{query}' and provide a concise answer:\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleSearchApp(root)
    root.mainloop()
