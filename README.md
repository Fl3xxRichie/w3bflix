# 🎬 W3BFLIX - Auto Claim Bot (FlexxRichie Version)

An automated bot for claiming rewards and watching videos on W3BFLIX platform.

## 🔗 Join W3BFLIX

Join using our referral link to get started:
- 🎁 [Join W3BFLIX](https://t.me/W3BFLIXBot?start=iv8114cb84a0)

## 📱 Contact & Support

Join our Telegram channel for updates and support:
- 📢 [FlexxRichie Channel](https://t.me/airdrop3arn)

## ✨ Features

| Feature | Status | Description |
|---------|--------|-------------|
| 🎲 Auto Daily Lucky Draw | ✅ Active | Automatically claims your daily lucky draw rewards |
| 🎥 Auto Watch Videos | ✅ Active | Watches videos and claims rewards automatically |
| ⏱️ Auto Scheduling | ✅ Active | Runs every 12 hours automatically |
| 👥 Multi-Account Support | ✅ Active | Supports multiple accounts through data.txt |

## 🚀 Installation & Setup

1. **Install Python**
   - Download and install Python 3.8+ from [python.org](https://python.org)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Git**
   - Download and install Git from [git-scm.com](https://git-scm.com)

3. **Clone the Repository**
   ```bash
   git clone https://github.com/fl3xxrichie/w3bflix.git
   cd w3bflix
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Configuration

1. **Get Your Auth Data**
   - Open W3BFLIX bot in Telegram
   - Open DevTools (F12) in your browser
   - Go to Network tab
   - Click any action in the bot
   - Find request with auth data
   - Copy the full query string starting with `query_id=`

2. **Setup data.txt**
   - Open data.txt
   - Paste your auth data
   - For multiple accounts, add each auth data on a new line

Example `data.txt`:
```
query_id=AAGrDJdeAgAAAKsMl16dPzhv&user=%7B%22id%22%3A123...
query_id=BBHrKJdeAgBBBKsMl16dPzhv&user=%7B%22id%22%3A456...
```

## 🖥️ Usage

1. **Start the Bot**
   ```bash
   python bot.py
   ```

2. **Auto-Claiming Process**
   - Bot will automatically:
     - Claim daily lucky draw
     - Watch videos
     - Generate claim codes
   - Runs every 12 hours automatically
   - Press Ctrl+C to stop safely

## ⚙️ Features Detail

- **Daily Lucky Draw**
  - Auto-claims once per day
  - Shows rewards or waiting time

- **Video Watching**
  - Simulates video watching
  - Auto-generates claim codes
  - Handles multiple videos
  - Tracks claimed status

- **Auto Scheduling**
  - Runs every 12 hours
  - Shows next scheduled run time
  - Continues running until stopped

## ⚠️ Important Notes

1. **Auth Data Security**
   - Keep your auth data private
   - Don't share your data.txt
   - Regularly update auth data if needed

2. **Running the Bot**
   - Keep the terminal window open
   - Check logs for any errors
   - Make sure your internet is stable

3. **Manual Claiming**
   - If auto-claim fails, copy `/watch` commands
   - Send them manually to W3BFLIX bot

## 🔍 Troubleshooting

Common issues and solutions:

1. **Git Clone Issues**
   ```bash
   # If you get SSL certificate errors
   git config --global http.sslVerify false
   # Then try cloning again
   git clone https://github.com/fl3xxrichie/w3bflix.git
   ```

2. **Installation Errors**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

3. **Auth Data Issues**
   - Make sure data.txt format is correct
   - Update auth data if expired
   - Check for extra spaces/lines

4. **Bot Not Running**
   - Check Python installation
   - Verify all files are in same folder
   - Check internet connection

## 📄 License

This project is for educational purposes only. Use at your own risk.

## 🤝 Credits

Modified by FlexxRichie
Original W3BFLIX platform rights belong to their respective owners.