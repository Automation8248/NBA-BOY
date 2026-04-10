import os
import json
import random
import requests
import datetime

# --- CONFIGURATION ---
VIDEO_FOLDER = "videos"
HISTORY_FILE = "history.json"
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

GITHUB_REPO = "Automation8248/Dark-Discipline" 
BRANCH_NAME = "main"

# --- DATA GRID (NBA & USA Hoops Topic Only) ---

# List 1: Titles (69 Options for NBA/Basketball)
TITLES_GRID = [
    "Unreal Hoops Moment 🏀🔥",
    "Did You See That Coming? 🤯",
    "Absolute Menace on the Court 😤",
    "This is Why We Love the Game ❤️🏀",
    "Ankle Breaker Alert ⚠️🥶",
    "Clutch Gene Activated 🧬🧊",
    "Top Tier Basketball IQ 🧠",
    "They Couldn't Stop Him! 🛑🔥",
    "Highlight Reel Material Right Here 🎬",
    "Pure Greatness on Display 👑",
    "The Defense Had No Chance 🤷‍♂️",
    "Wait for the Replay... ⏪👀",
    "Game Winner Energy ⏳🎯",
    "That Bounce is Crazy 🚀",
    "Smooth with It 🧈🏀",
    "Tough Finish Through Traffic 😤💪",
    "Poetry in Motion 📖✨",
    "Rookie vs Veteran Moment 🍿",
    "How Did That Go In?! 🤯🔥",
    "Best Play of the Week? 🤔",
    "Generational Talent 🌟",
    "He Took Flight ✈️💥",
    "Nothing But Net 🎯",
    "Putting the League on Notice 🗣️",
    "Disrespectful in the Best Way 🥶",
    "The Crowd Went WILD 🏟️🔊",
    "Locked In on Both Ends 🔒",
    "That Crossover Was Lethal 💀🏀",
    "Buzzer Beater Vibes 🚨",
    "Unstoppable Force 🚂💨",
    "Bro Glitched on the Court 🎮",
    "Textbook Play Execution 📖",
    "He Owns the Paint 🎨💪",
    "Shooter's Touch 🤌🏀",
    "Not in His House 🚫🏠",
    "Hang Time Was Crazy ⏳✈️",
    "Look at the Footwork 🕺",
    "He is a Walking Bucket 🪣🔥",
    "Posterized Him! 📸💀",
    "Unreal Court Vision 👀",
    "Ice in His Veins 🧊🩸",
    "They Weren't Ready for This 🙅‍♂️",
    "Cheat Code Activated ⬆️⬇️",
    "He Got the Hot Hand 🔥🤚",
    "Coast to Coast Action 🌊",
    "Too Fast for the Camera 🎥💨",
    "Absolute Clinic Out There 🏥",
    "The Rim is Still Shaking 💥",
    "Vintage Move Right There 🍷",
    "Calculated Greatness 🧮",
    "He Makes it Look Too Easy 🥱",
    "Different Breed 🐺🏀",
    "Are You Kidding Me?! 🤯",
    "Showtime Basketball 🍿🎭",
    "Elite Level Defense 🛡️",
    "Off the Glass! 🪟🏀",
    "Splash Warning 💦🎯",
    "The Hops Are Unreal 🦘",
    "You Can't Teach That 🧠",
    "He Took Over the Game 🎮",
    "Silencing the Away Crowd 🤫🏟️",
    "Monster Jam! 👹💥",
    "Precision Passing 🎯",
    "He Put Him on Skates ⛸️",
    "Next Level Athleticism 🚀",
    "Money From Deep 💰🎯",
    "The Energy is Unmatched ⚡",
    "Hall of Fame Play 🏆",
    "Basketball at its Finest 🤌"
]

# List 2: Captions (69 Options for Engagement)
CAPTIONS_GRID = [
    "Rate this play from 1-10 in the comments! 👇",
    "Is he top 5 in the league right now? Let's debate 🗣️🏀",
    "Tag a friend who plays like this 😂👇",
    "Traveling or clean? What do y'all think? 🤔🦓",
    "This was absolutely filthy. 🥶 Drop a 🔥 if you agree!",
    "Who is stopping this man? Seriously. 🤷‍♂️",
    "I've watched this 10 times already. Pure hoops! 🏀🔥",
    "Defense was lost on this one. 🤦‍♂️ Where was the help?",
    "We need more moments like this in the league. 💯",
    "Would you have taken this shot? Let me know below 👇",
    "The athleticism is just unfair. 🚀🤯",
    "Instant classic moment. 🎬 What's your favorite play?",
    "That footwork is textbook! 📖🏀",
    "Comment your favorite team down below! 👇🏀",
    "They really let him get to his spot. Too easy! 🎯",
    "Bro activated takeover mode. 🎮🔥",
    "What goes through your mind defending this? 💀",
    "Cleanest play of the night hands down. 🧼",
    "Tag your hoop squad! 🏃‍♂️💨",
    "The disrespect was loud on this one! 🔊🥶",
    "Can we talk about the assist though?! 👀🤌",
    "If you try this in a pickup game, what happens? 😂",
    "The bench reaction says it all! 🤯🛋️",
    "Shooters gotta shoot. 🎯 Drop a 💦 if you agree.",
    "This angle makes it look even crazier 🎥🔥",
    "Y'all think this is a foul or nah? 🦓👇",
    "He’s been playing out of his mind lately. 🧠🔥",
    "Greatness in the making. Appreciate it. 👑",
    "Look at the hang time! ⏳✈️",
    "Bro put him in a blender! 🌪️💀",
    "This is why basketball is the best sport in the world. 🌍🏀",
    "Who you got winning it all this year? 🏆👇",
    "Coach has to be smiling at that execution. 📋👏",
    "How do you even guard that? Give me your gameplan 👇",
    "Ice cold. 🧊 Name a more clutch player.",
    "He practically dared them to block it. 😤",
    "That crossover needs a warning label. ⚠️ ankles broken.",
    "You just can’t teach that kind of instinct. 🧠💯",
    "This duo is looking scary good right now. 👻🔥",
    "Put some respect on his name! 🗣️😤",
    "He hit the 'too small' celebration on him! 🤏😂",
    "What’s your go-to move on the court? 👇🏀",
    "That was pure muscle memory. 💪🧠",
    "This crowd energy is giving me chills. 🏟️🥶",
    "He knew it was going in before it left his hand. 🎯",
    "Bro thought he had a chance at blocking that 😂🛑",
    "The gravity he pulls on the court is insane. 🪐",
    "This is going straight to the highlight tape. 📼🔥",
    "Who had a better game tonight? Let me know! 👇",
    "He’s playing 2K on Rookie difficulty right now. 🎮🥱",
    "That pass was an absolute laser. 🔫🏀",
    "He got up there QUICK! 🚀👀",
    "This is what hours in the gym looks like. 💯🏋️",
    "Did he carry the ball? Be honest. 🤔",
    "Bro has springs in his shoes! 🦘🔥",
    "The game is just moving too slow for him right now. ⏳",
    "Comment 'HOOPS' letter by letter without getting interrupted! 👇",
    "That fake had everybody jumping! 🐇😂",
    "He’s been a bucket since high school. 🪣🔥",
    "They gotta double team him at this point. 🤷‍♂️",
    "The swagger is off the charts. 📈😎",
    "Pure hustle right there. You love to see it. 🏃‍♂️💨",
    "He let the game come to him. High IQ play. 🧠🏀",
    "Who is the most underrated player right now? 👇",
    "That release is so quick it’s unfair. ⚡🎯",
    "He’s playing chess while everyone else is playing checkers. ♟️",
    "Bro literally floated. 🎈🤯",
    "The definition of a tough bucket. 🪣😤",
    "Hit that share button and send this to a hooper! 📲🏀"
]


# List 3: Fixed Hashtags (USA USA USA)
FIXED_HASHTAGS = """
.
.
.
.
.
#nba #basketball #hoops #nbahighlights #sports #bball #viral #usa #basketballneverstops #dunk #nbanews #ballislife"""

INSTA_HASHTAGS = """
.
.
.
.
"#nbareels #hoopmixtape #basketballtraining #nbaedits #nbamemes #sportsreels #crossover #anklebreaker #explorepage #fyp #instasports"
"""

YOUTUBE_HASHTAGS = """
.
.
.
"#nba #nbashorts #basketballshorts #nbahighlights #sportsshorts #youtubehoops #viralshorts #nbaplays #lebron #stephencurry #michaeljordan #fyp"
"""

FACEBOOK_HASHTAGS = """
.
.
.
"#nbahighlights #basketballgame #nbafans #sportsnews #hoops #gametime #basketballislife #nbaaction #viralvideo #mustwatch"
"""

# --- HELPER FUNCTIONS ---

def load_history():
    if not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0:
        return []
        
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: history.json was corrupted or invalid. Starting fresh.")
        return []

def save_history(data):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- MAIN LOGIC ---

def run_automation():
    # 1. DELETE OLD FILES (15 Days Logic)
    history = load_history()
    today = datetime.date.today()
    new_history = []
    
    print("Checking for expired videos...")
    for entry in history:
        if 'date_sent' in entry:
            sent_date = datetime.date.fromisoformat(entry['date_sent'])
            days_diff = (today - sent_date).days
            
            file_path = os.path.join(VIDEO_FOLDER, entry['filename'])
            
            if days_diff >= 15:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"DELETED EXPIRED: {entry['filename']}")
            else:
                new_history.append(entry)
        else:
            new_history.append(entry)
    
    save_history(new_history)
    history = new_history 

    # 2. PICK NEW VIDEO
    if not os.path.exists(VIDEO_FOLDER):
        os.makedirs(VIDEO_FOLDER)
        
    all_videos = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]
    sent_filenames = [entry.get('filename') for entry in history if 'filename' in entry]
    
    available_videos = [v for v in all_videos if v not in sent_filenames]
    
    if not available_videos:
        print("No new videos to send.")
        return

    video_to_send = random.choice(available_videos)
    video_path = os.path.join(VIDEO_FOLDER, video_to_send)
    
    print(f"Selected Video File: {video_to_send}")

    # 3. RANDOM SELECTION (Grid System)
    selected_title = random.choice(TITLES_GRID)
    selected_caption = random.choice(CAPTIONS_GRID)
    
    # Combine content
    full_telegram_caption = f"{selected_title}\n\n{selected_caption}\n{FIXED_HASHTAGS}"
    
    print(f"Generated Title: {selected_title}")
    print(f"Generated Caption: {selected_caption}")

    # 4. SEND TO TELEGRAM
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        print("Sending to Telegram...")
        
        ist_now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
        time_string = ist_now.strftime("%d %b %I:%M:%S %p %Y").upper()
        
        telegram_caption = f"<b>{time_string}</b>"

        with open(video_path, 'rb') as video_file:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendVideo"
            payload = {
                'chat_id': TELEGRAM_CHAT_ID, 
                'caption': telegram_caption,
                'parse_mode': 'HTML' 
            }
            files = {'video': video_file}
            try:
                requests.post(url, data=payload, files=files)
            except Exception as e:
                print(f"Telegram Error: {e}")

    # 5. SEND TO WEBHOOK
    if WEBHOOK_URL:
        print("Sending to Webhook...")
        raw_video_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{BRANCH_NAME}/{VIDEO_FOLDER}/{video_to_send}"
        raw_video_url = raw_video_url.replace(" ", "%20")
        
        webhook_data = {
            "video_url": raw_video_url,
            "title": selected_title,
            "caption": selected_caption,
            "hashtags": FIXED_HASHTAGS,
            "insta_hashtags": INSTA_HASHTAGS,
            "youtube_hashtags": YOUTUBE_HASHTAGS, 
            "facebook_hashtags": FACEBOOK_HASHTAGS, 
            "source": "AffiliateBot" 
        }
        try:
            requests.post(WEBHOOK_URL, json=webhook_data)
            print(f"Webhook Sent: {raw_video_url}")
        except Exception as e:
            print(f"Webhook Error: {e}")

    # 6. UPDATE HISTORY
    new_history.append({
        "filename": video_to_send,
        "date_sent": today.isoformat()
    })
    save_history(new_history)
    print("Automation Complete.")

if __name__ == "__main__":
    run_automation()
