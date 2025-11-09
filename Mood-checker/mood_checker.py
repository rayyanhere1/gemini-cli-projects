import random

def mood_checker():
    """
    Checks the user's mood and responds with a positive or motivational message.
    """
    mood_responses = {
        "sad": [
            "I'm sorry to hear that you're feeling sad. 😢 Remember that it's okay to not be okay. Things will get better. ✨",
            "It's tough feeling sad. 😔 Take a deep breath and know that you're not alone. You've got this! 💪",
            "Sending you a virtual hug! 🤗 Sometimes a little self-care can make a big difference. Maybe watch your favorite movie or listen to some uplifting music? 🎶"
        ],
        "happy": [
            "That's awesome! 😄 I'm so glad you're feeling happy. Keep shining! 🌟",
            "Yay! 🎉 Your happiness is contagious! Keep spreading those good vibes. 😊",
            "It's wonderful to hear you're happy! 🥳 Keep that positive energy flowing. 💃"
        ],
        "anxious": [
            "I understand that you're feeling anxious. 😟 Remember to be kind to yourself. Take some time to relax and focus on your breathing. 🧘",
            "Anxiety can be overwhelming. 😥 Try to focus on the present moment. You are safe and you are strong. 💖",
            "It's okay to feel anxious. 😥 Be patient with yourself. Maybe try some grounding techniques, like naming five things you can see. 👀"
        ],
        "angry": [
            "It's understandable to feel angry sometimes. 🔥 Take a moment to cool down. Maybe some physical activity could help? 🏃",
            "Feeling angry is a valid emotion. 😠 Try to channel that energy into something productive. You have the power to turn this around. 🔄",
            "I'm sorry you're feeling angry. 😡 Remember to take deep breaths and count to ten. This feeling will pass. 💨"
        ],
        "excited": [
            "That's fantastic! 🤩 I'm excited for you! Whatever it is, I hope it's amazing. 🎊",
            "Woo-hoo! 🎉 Your excitement is palpable! Enjoy every moment of it. 🤸",
            "How exciting! 🥳 I'm thrilled to hear that! Keep that amazing energy going. 🚀"
        ],
        "tired": [
            "It sounds like you need some rest. 😴 Make sure to take care of yourself and get some quality sleep. 🛌",
            "Feeling tired is a sign that your body needs to recharge. 🔋 Be kind to yourself and allow yourself to rest. 💤",
            "I'm sorry you're feeling tired. 😩 Remember that rest is productive too. Sweet dreams! 🌌"
        ]
    }

    while True:
        user_input = input("How are you feeling today? (e.g., 'I'm feeling sad') ").lower()

        if "exit" in user_input or "quit" in user_input:
            print("Thank you for sharing your feelings with me. Remember to always be kind to yourself. Goodbye! 👋")
            break

        mood_detected = False
        for mood, responses in mood_responses.items():
            if mood in user_input:
                print(random.choice(responses))
                mood_detected = True
                break
        
        if not mood_detected:
            print("I'm not sure I understand that mood. 🤔 Could you try expressing it differently? Or you can type 'exit' to quit.")

if __name__ == "__main__":
    mood_checker()
