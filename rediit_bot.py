import praw
import random
import time

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent',
                     username='your_reddit_username',
                     password='your_reddit_password')

subreddit_name = 'askreddit'

quotes = {
    'motivational': [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs",
        "Don't let the noise of others' opinions drown out your own inner voice. - Steve Jobs",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
        "Life is a journey, not a destination. - Ralph Waldo Emerson",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The best way to predict the future is to create it. - Abraham Lincoln",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Life is either a daring adventure or nothing at all. - Helen Keller",
        "The only thing worse than being blind is having sight but no vision. - Helen Keller",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
    ],
    'funny': [
        "I intend to live forever. So far, so good. - Steven Wright",
        "Why do they call it rush hour when nothing moves? - Robin Williams",
        "A bank is a place that will lend you money if you can prove that you don't need it. - Bob Hope",
        "Why do we park in driveways and drive on parkways? - Unknown",
        "I asked God for a bike, but I know God doesn't work that way. So I stole a bike and asked for forgiveness. - Emo Philips",
        "Some people never go crazy. What truly horrible lives they must lead. - Charles Bukowski",
        "When I die, I want to go peacefully like my grandfather did–in his sleep. Not yelling and screaming like the passengers in his car. - Bob Monkhouse",
        "The road to success is dotted with many tempting parking spaces. - Will Rogers",
        "I'm not superstitious, but I am a little stitious. - Michael Scott",
        "The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it. - Terry Pratchett",
        "I like long walks, especially when they are taken by people who annoy me. - Fred Allen",
        "Clothes make the man. Naked people have little or no influence on society. - Mark Twain",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying. - Woody Allen",
        "The only mystery in life is why the kamikaze pilots wore helmets. - Al McGuire",
        "I'm writing a book. I've got the page numbers done. - Steven Wright",
        "A day without sunshine is like, you know, night. - Steve Martin",
        "If you're going to tell people the truth, be funny or they'll kill you. - Billy Wilder",
        "I cook with wine. Sometimes I even add it to the food. - W.C. Fields",
        "The four most beautiful words in our common language: I told you so. - Gore Vidal",
        "I'm an idealist. I don't know where I'm going, but I'm on my way. - Carl Sandburg"
    ],
    'love': [
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage. - Lao Tzu",
        "Love is that condition in which the happiness of another person is essential to your own. - Robert A. Heinlein",
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - Victor Hugo",
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "Love is like the wind, you can't see it but you can feel it. - Nicholas Sparks",
        "A simple 'I love you' means more than money. - Frank Sinatra",
        "Love is an endless act of forgiveness. - Beyoncé",
        "There is no charm equal to tenderness of heart. - Jane Austen",
        "Love is not about possession, it's all about appreciation. - Unknown",
        "Love is the only gold. - Alfred Lord Tennyson",
        "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
        "You know you're in love when you can't fall asleep because reality is finally better than your dreams. - Dr. Seuss",
        "The best love is the kind that awakens the soul and makes us reach for more, that plants a fire in our hearts and brings peace to our minds. - Nicholas Sparks",
        "I have found the one whom my soul loves. - Song of Solomon 3:4",
        "Love is when the other person's happiness is more important than your own. - H. Jackson Brown, Jr.",
        "Love is the master key that opens the gates of happiness. - Oliver Wendell Holmes, Sr.",
        "The greatest happiness you can have is knowing that you do not necessarily require happiness. - William Saroyan",
        "Love is a canvas furnished by nature and embroidered by imagination. - Voltaire",
        "The best love story is when you fall in love with the most unexpected person at the most unexpected time. - Unknown"
    ]
}

def check_comments():
    subreddit = reddit.subreddit(subreddit_name)
    for comment in subreddit.stream.comments():
        if any(trigger in comment.body.lower() for trigger in ['!quote', '!motivate', '!joke', '!love', '!inspire', '!funny', '!philosophy', '!life']):
            reply_message(comment)

def reply_message(comment):
    response = ''
    if '!quote' in comment.body.lower():
        response = get_random_quote()
    elif '!motivate' in comment.body.lower():
        response = get_random_quote('motivational')
    elif '!joke' in comment.body.lower():
        response = get_random_quote('funny')
    elif '!love' in comment.body.lower():
        response = get_random_quote('love')
    elif '!inspire' in comment.body.lower():
        response = get_random_quote('motivational') + "\n\n" + get_random_quote('love')
    elif '!funny' in comment.body.lower():
        response = get_random_quote('funny')
    elif '!philosophy' in comment.body.lower():
        response = get_random_quote('motivational') + "\n\n" + get_random_quote('love')
    elif '!life' in comment.body.lower():
        response = get_random_quote('motivational') + "\n\n" + get_random_quote('funny') + "\n\n" + get_random_quote('love')
    elif '!advice' in comment.body.lower():
        response = get_advice()

    if response:
        comment.reply(response)

def get_random_quote(category=None):
    if category:
        if category in quotes:
            return random.choice(quotes[category])
        else:
            return "Sorry, I don't have quotes for that category."
    else:
        all_quotes = [quote for sublist in quotes.values() for quote in sublist]
        return random.choice(all_quotes)

def get_advice():
    advices = [
        "Always trust your instincts.",
        "Don't be afraid to ask for help when you need it.",
        "Take care of your physical and mental health.",
        "Learn from your mistakes and use them as opportunities for growth.",
        "Stay true to yourself and your values.",
        "Be kind to yourself and others.",
        "Set goals and work towards them every day.",
        "Don't compare yourself to others; everyone's journey is unique.",
        "Take time to relax and recharge.",
        "Focus on the present moment; the past is gone and the future is yet to come.",
        "Surround yourself with positive and supportive people.",
        "Embrace change and see it as a chance for new beginnings.",
        "Forgive yourself and others; holding onto grudges only hurts you in the end.",
        "Practice gratitude and appreciate the good things in your life.",
        "Believe in yourself and your abilities.",
        "Keep an open mind and be willing to learn from others.",
        "Celebrate your accomplishments, no matter how small.",
        "Be patient; good things take time to happen.",
        "Stay curious and never stop exploring the world around you.",
        "Remember that you are worthy of love and happiness."
    ]
    return random.choice(advices)

def main():
    print("Bot is running...")
    while True:
        try:
            check_comments()
        except praw.exceptions.APIException as api_exception:
            print(f"API Exception: {api_exception.message}")
            # Sleep for a while before retrying
            time.sleep(60)
        except praw.exceptions.PRAWException as praw_exception:
            print(f"PRAW Exception: {praw_exception}")
            # Sleep for a while before retrying
            time.sleep(60)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            # Sleep for a while before retrying
            time.sleep(60)

if __name__ == "__main__":
    main()
