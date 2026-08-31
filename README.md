# krzbot 

A feature-packed, lightweight Slack bot built using Python ([Slack Bolt](https://slack.dev/bolt-python)), integrated with [OpenRouter](https://openrouter.ai) for AI capabilities and [Open-Meteo](https://open-meteo.com/) for real-time weather forecasts.

---

## ✨ Features

- **AI Assistance (`/krzbot-ask-ai`)**: Query large language models (powered by OpenRouter / LLMs) directly from Slack.
- **Weather Forecasts (`/weather`)**: Get current weather metrics (temperature, humidity, wind, precipitation) for any city using Open-Meteo—no external API keys required.
- **Joke Generator (`/krzbot-tell-joke`)**: Delivers developer and programming jokes from a local collection.
- **Socket Mode Integration**: Connects securely to Slack without requiring public endpoints, webhooks, or NGINX/ngrok configuration.
- **Systemd Ready**: Runs easily as a background Linux daemon with automatic restarts.

---

## 🛠️ Slash Commands

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `/krzbot-ask-ai` | `[prompt]` | Asks an AI model a question set up using ai.hackclub.com. |
| `/weather` | `[city_name]` | Returns current weather, temperature, humidity, and wind speed. |
| `/krzbot-tell-joke` | *None* | Sends a random programming or engineering joke to the channel. |

---

## Prerequisite Setup (Slack Dashboard)

Before running the application, set up your bot on the [Slack API Portal](https://api.slack.com/apps):

1. **Create an App**: Click **Create New App** -> **From scratch**.
2. **OAuth & Permissions**:
   * Go to **OAuth & Permissions** -> **Bot Token Scopes** and add:
     * `chat:write`
     * `commands`
   * Scroll up and click **Install to Workspace**.
   * Copy the **Bot User OAuth Token** (`xoxb-...`).
3. **App-Level Token**:
   * Go to **Basic Information** -> **App-Level Tokens** -> **Generate Token and Scopes**.
   * Add the `connections:write` scope.
   * Copy the **App-Level Token** (`xapp-...`).
4. **Enable Socket Mode**:
   * Go to **Socket Mode** in the sidebar and toggle **Enable Socket Mode** to **On**.
5. **Create Slash Commands**:
   * Go to **Slash Commands** and register:
     * `/krzbot-ask-ai`
     * `/weather`
     * `/krzbot-tell-joke`

---

## Local Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/krzbot.git](https://github.com/your-username/krzbot.git)
   cd krzbot
   pip3 install slack-sdk slack-bolt openrouter requests
   python3 main.py
