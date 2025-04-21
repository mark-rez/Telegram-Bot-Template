# Telegram-Bot-Template
This is a simple Telegram bot written in Python, using SQLAlchemy ORM to save user information into an SQLite database.
## Features
- `/start` command saves the user's `chat_id` and `username` into the SQLite database
- Simple and modular design using SQLAlchemy ORM
- Environment variable support via `.env` for token management
## Setup
1. Create a .env file in the root directory with your bot token:

    ```sh
    BOT_TOKEN=your_telegram_bot_token
    ```
2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```
## Running the bot
To start the bot, run the following command:
```sh
python bot.py
```
The bot will start and listen for incoming /start commands. When a user sends /start, their information will be saved into the database.
## Debugging the Database
To inspect the data saved in the SQLite database, you can either:
1. Use Python script to print user data:
    ```sh
    python debug.py
    ```
2. Use an SQLite database viewer to open the `bot.db` file and view the `users` table.
## Commands
### `/start`
When a user starts the bot with `/start`, their information (chat_id and username) will be saved into the database.
## Contributing
Feel free to fork the project, make changes, and submit pull requests!