# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import webbrowser  # 🚀 For website opening
import wikipedia  # 📝 For Wikipedia search
import pyttsx3     # 🗣️ For speech synthesis
import pywhatkit   # 🎵 For playing YouTube

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def say(text):
    print(f"Chatbot: {text}")
    engine.say(text)
    engine.runAndWait()

# ==========================
# 1️⃣ Create Sample Data
# ==========================
data = {
    "question": [
        "What are your opening hours?",
        "When does the store open?",
        "Where is my order?",
        "How can I return an item?",
        "Do you have discounts available?",
        "I want to speak to a human.",
        "Can I cancel my order?",
        "What payment methods do you accept?",
        "How do I track my order?",
        "Do you ship internationally?",
        "When will I get my refund?",
        "Are there any loyalty programs?",
        "How long does shipping take?",
        "How can I change my shipping address?",
        "Can I get free shipping?"
    ],
    "category": [
        "opening_hours",
        "opening_hours",
        "order_status",
        "returns",
        "discounts",
        "human_agent",
        "order_cancellation",
        "payment_methods",
        "order_tracking",
        "shipping",
        "returns",
        "discounts",
        "shipping",
        "shipping",
        "shipping"
    ]
}

df = pd.DataFrame(data)

# ==========================
# 2️⃣ Train the Model
# ==========================
X = df["question"]
y = df["category"]

model = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english')),
    ('classifier', LogisticRegression(max_iter=1000))
])

model.fit(X, y)
say("✅ Model trained successfully!")

# ==========================
# 3️⃣ Chatbot Interaction
# ==========================
def chatbot_response(user_input):
    category = model.predict([user_input])[0]
    if category == "opening_hours":
        return "Our store is open from 9 AM to 6 PM every day!"
    elif category == "order_status":
        return "Please provide your order ID, and I'll look it up for you."
    elif category == "returns":
        return "You can return items within 30 days. Please visit our Returns Center."
    elif category == "discounts":
        return "We have seasonal discounts — check our website for current offers!"
    elif category == "human_agent":
        return "Connecting you to a human agent. Please hold on."
    elif category == "order_cancellation":
        return "You can cancel your order within 2 hours of purchase."
    elif category == "payment_methods":
        return "We accept Visa, MasterCard, PayPal, and UPI."
    elif category == "order_tracking":
        return "Please provide your order ID, and I'll help you track it."
    elif category == "shipping":
        return "Shipping times vary, but typically orders arrive within 3-5 business days."
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# ==========================
# 4️⃣ Handle 'play' Commands
# ==========================
def run_vivo(command):
    if 'play' in command:
        song = command.replace('play', '').strip()
        if song:
            say(f'Playing {song}')
            pywhatkit.playonyt(song)
        else:
            say("Please tell me which song to play.")
    else:
        say("Sorry, I can only play songs in Vivo mode right now.")

# ==========================
# 5️⃣ Chatbot Loop
# ==========================
say("\n💬 Welcome to the Customer Service Chatbot!")
say("Type 'exit' or 'quit' to end the conversation.")
say("Type 'open <platform>' to open a website (e.g., 'open YouTube').")
say("You can also ask 'who is <person>' to get information from Wikipedia.")
say("Type 'play <song>' to play a song on YouTube.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        say("Goodbye! 👋")
        break
    elif user_input.lower().startswith("open "):
        platform = user_input[5:].strip().lower()
        if platform == "website":
            say("Opening our official website...")
            webbrowser.open("https://www.example.com")
        elif platform == "youtube":
            say("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif platform == "instagram":
            say("Opening Instagram...")
            webbrowser.open("https://www.instagram.com")
        elif platform == "whatsapp":
            say("Opening WhatsApp...")
            webbrowser.open("https://web.whatsapp.com")
        elif platform == "facebook":
            say("Opening Facebook...")
            webbrowser.open("https://www.facebook.com")
        elif platform == "linkedin":
            say("Opening LinkedIn...")
            webbrowser.open("https://www.linkedin.com")
        elif platform == "github":
            say("Opening GitHub...")
            webbrowser.open("https://www.github.com")
        elif platform == "amazon":
            say("Opening Amazon...")
            webbrowser.open("https://www.amazon.in")
        elif platform == "flipkart":
            say("Opening Flipkart...")
            webbrowser.open("https://www.flipkart.com")
        elif platform == "wikipedia":
            say("Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.org")
        else:
            say("Sorry, I don't have that link saved. Please specify another platform.")
        continue
    elif user_input.lower().startswith("who is "):
        person = user_input[7:].strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            say(info)
        except wikipedia.exceptions.DisambiguationError:
            say("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            say("I couldn't find information on that.")
        continue
    elif user_input.lower().startswith("play "):
        run_vivo(user_input)
        continue
    else:
        response = chatbot_response(user_input)
        say(response)
