<summary><b>ᴅᴇᴘʟᴏʏ ᴛᴏ ʜᴇʀᴏᴋᴜ</b></summary>
<br>
<h4> ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴅᴇᴘʟᴏʏ tpx ᴏɴ ʜᴇʀᴏᴋᴜ</h4>    
<p><a href="http://dashboard.heroku.com/new?template=https://github.com/BtwUnnati/New"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-red?style=for-the-badge&logo=heroku" width="200"/></a></p>
<br>




<h1 align="center"><b>𝖳𝗈𝗑𝗂𝖼 𝖡𝗈𝗍</b></h1>

### 💻 𝖳𝗈𝗑𝗂𝖼 𝖡𝗈𝗍 ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ɢᴜɪᴅᴇ ᴏɴ ʟᴏᴄᴀʟ sᴇʀᴠᴇʀ ᴏʀ ᴠᴘs 🗄️
<br>
<details>
<summary><strong>Ubuntu 20.04 / 22.04 Setup</strong></summary>

#### 🧩 Step-by-Step Installation

**1. Update & Upgrade the System**
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

**2. Install Required Packages**
```bash
sudo apt-get install python3-pip ffmpeg -y
```

**3. Upgrade pip**
```bash
sudo pip3 install -U pip
```

**4. Clone the Repository**
```bash
git clone https://github.com/BtwUnnati/12 && cd 12
```

**5. Install Python Requirements**
```bash
pip3 install -U -r requirements.txt
```

**6. Create `.env` File**
```bash
cp sample.env .env
```
> Now edit `.env` with your configuration variables.

**7. Edit Environment Variables**
```bash
vi .env
```
> - Press `I` to start editing.  
> - Press `Ctrl + C`, then type `:wq` to save and exit.  
> - Use `:qa` to quit without saving.

**8. Install and Start Tmux**
```bash
sudo apt install tmux && tmux
```

**9. Start the Bot**
```bash
bash toxic 
```
</details>

<br>
<details>
<summary><strong>Ubuntu 24.04 Setup</strong></summary>

#### 🧩 Step-by-Step Installation

**1. Update & Upgrade the System**
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

**2. Install Required Packages**
```bash
sudo apt-get install python3-pip ffmpeg -y
```

**3. Upgrade pip**
```bash
sudo pip3 install -U pip
```

**4. Clone the Repository**
```bash
git clone  https://github.com/BtwUnnati/12 && cd 12
```

**5. Install Python Requirements (Ubuntu 24 specific)**
```bash
pip install -r requirements.txt --break-system-packages
```

**6. Create `.env` File**
```bash
cp sample.env .env
```
> Edit `.env` with your bot configuration.

**7. Edit Environment Variables**
```bash
vi .env
```
> - Press `I` to edit.  
> - Press `Ctrl + C`, then type `:wq` to save.  
> - Use `:qa` to quit without saving.

**8. Install and Start Tmux**
```bash
sudo apt install tmux && tmux
```

**9. Start the Bot**
```bash
bash toxic 
```





