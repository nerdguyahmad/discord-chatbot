#### :warning: This code is outdated now, I didn't update it yet, I will do soon when I get some time but for now, This doesn't work. If you want, you can open a pull request to update it with new wrapper [randomstuff.py](https://github.com/nerdguyahmad/randomstuff.py)

# Discord Chatbot

Discord chat bot is a very simple chat bot made in Python using [Discord.py API wrapper](https://github.com/Rapptz/discord.py) and [prsaw](https://github.com/CodeWithSwastik/prsaw) library.

## Prerequisites & Installation

You need [Python 3.6+](https://python.org/)  to use this bot.

#### Libraries required:
- [`discord.py`](https://github.com/Rapptz/discord.py)
- [`prsaw`](https://github.com/CodeWithSwastik/prsaw)
- requests

### Installation:

Installation is pretty simple, Clone this repository. You can use `git clone` for easy cloning.

```git
git clone https://github.com/nerdguyahmad/discord-chat-bot
```

In the cloned directory, run this command to install required modules.

```bash
python -m pip install -r requirements.txt
```
This will install the required modules.

### For Linux Users:

On linux based OS, you might have Python 2 installed with Python 3. In that case, Above command may not work. You should install the libraries for Python 3.
```bash
python3 -m pip install -r requirements.txt
```

## Usage

You need to create an application & bot in the [Discord Developer Portal](https://discord.dev) first and copy it's token.

Follow [this](https://vimeo.com/509933655) guide to do so.

Once you have the token, Simply open the `config.json` file and paste your token in the `token` key. Like so:

```json
{
    "token": "PASTE YOUR TOKEN HERE"
}
```
Finally start the bot by running this command:
```bash
python main.py
```
Or for Linux users:

```bash
python3 main.py
```

Wait a few seconds till you see this output in terminal. :

```html
[ Discord ChatBot ]

Currently Logged in as: BOT NAME
Client ID: 123456789
```

The bot should be started. Use `!!setchannel` to start the setup.

## Hosting

To keep the bot online 24/7, You need to host your bot. This task can be done on your computer but you'll have to keep your PC on 24/7 which is difficult for majority of users. There are many options to host like buying a VPS though here are some options that are recommended for majority of users.

#### Free (But Limited and Unrecommended):
[Heroku](https://heroku.com) is a free option but your bot will stay online for 20-22 days in a month. Every month, you get free dynos which will restart your bot again.

If you add a credit card to Heroku (No need to pay anything, Just add a card). Your bot will stay online 24/7 with no downtime.

One drawback of heroku is that on every push your DB will be wiped. So, If you have multiple servers. You will lost the data of servers.

#### Paid (But Cheap):
[SomethingHost](https://something.host) is another option and is the recommended one. The cheapest plan of Discord Bot Hosting package will be perfect for you.

## Contribution

Pull requests are welcome! Feel free to contribute. For major changes, Open an issue first to discuss.

## Acknowledgment

This bot is perfect to be used on few servers. If you are planning to use it on MANY servers, It would be a bad idea. In that case, Please use a better database like MySQL, MongoDB etc.

## License
[MIT](https://github.com/nerdguyahmad/discord-chatbot/blob/main/LICENSE)
