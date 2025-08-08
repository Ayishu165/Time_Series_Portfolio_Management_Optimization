
import os
import pandas as pd
import configparser
from datetime import datetime
from getpass import getpass
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

# Load config from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']
phone_number = config['Telegram']['phone']
TELEGRAM_CHANNELS = [
    '@shageronlinestore',
    '@ZemenExpress',
    '@meneshayeofficial',
    '@Shewabrand',
    '@Fashiontera'
]
# === Folder to save output CSV files ===
DATA_FOLDER = r'D:\kaimtenx\project\week4\Amharic-Ecommerce-Data-Extractor\data1'

# === Message limits per channel ===
MIN_MESSAGES = 2000
MAX_MESSAGES = 7000

# === Helper: Ensure output directory exists ===
def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Created directory: {path}")
    else:
        print(f"📁 Directory already exists: {path}")

# === Helper: Extract metadata from Telegram message ===
def extract_message_data(msg):
    return {
        'channel': msg.peer_id.channel_id if msg.peer_id else None,
        'date': msg.date,
        'message': msg.message,
        'views': msg.views or msg.forwards,
        'sender_id': getattr(msg, 'sender_id', None),
        'media_type': (
            'photo' if isinstance(msg.media, MessageMediaPhoto)
            else 'document' if isinstance(msg.media, MessageMediaDocument)
            else None
        )
    }

# === Main script ===
def main():
    print("🚀 Starting Telegram scraping...")
    ensure_directory(DATA_FOLDER)

    client = TelegramClient('session', api_id, api_hash)

    try:
        print("🔗 Connecting to Telegram...")
        client.connect()

        # Authentication if not yet logged in
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            code = input("📲 Enter the code sent to your Telegram: ")
            try:
                client.sign_in(phone_number, code)
            except SessionPasswordNeededError:
                password = getpass("🔒 Two-step password: ")
                client.sign_in(password=password)

        print("✅ Connected successfully!")

        all_data = []

        for channel in TELEGRAM_CHANNELS:
            print(f"\n📡 Fetching messages from {channel} ...")
            channel_data = []

            try:
                entity = client.get_entity(channel)

                for i, msg in enumerate(client.iter_messages(entity, limit=MAX_MESSAGES)):
                    if msg.message:
                        channel_data.append(extract_message_data(msg))
                    if (i + 1) % 500 == 0:
                        print(f"  ✅ Fetched {i+1} messages...")
                    if len(channel_data) >= MAX_MESSAGES:
                        break

                # Save only if enough data
                if len(channel_data) < MIN_MESSAGES:
                    print(f"⚠️ Warning: Only {len(channel_data)} messages from {channel} (minimum required: {MIN_MESSAGES})")
                else:
                    print(f"✅ Total messages from {channel}: {len(channel_data)}")

                if channel_data:
                    df = pd.DataFrame(channel_data)
                    df['date'] = pd.to_datetime(df['date'])
                    df['channel'] = channel
                    file_path = os.path.join(DATA_FOLDER, f"{channel[1:]}_data.csv")  # remove @ from filename
                    df.to_csv(file_path, index=False, encoding='utf-8')
                    print(f"💾 Saved to {file_path}")
                    all_data.append(df)

            except Exception as e:
                print(f"❌ Error fetching {channel}: {e}")

    finally:
        if client.is_connected():
            client.disconnect()
            print("🔌 Disconnected from Telegram.")

if __name__ == "__main__":
    main()