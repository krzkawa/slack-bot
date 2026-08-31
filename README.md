# krzbot 

A Slack bot built using Python ([Slack Bolt](https://slack.dev/bolt-python)).

---

## Features

- **AI Assistance (`/krzbot-ask-ai`)**: Ask AI straight from slack!!!
- **Weather Forecasts (`/krzbot-weather`)**: Get current weather (temperature, humidity, wind, precipitation) for any city using Open-Meteo!!!
- **Joke Generator (`/krzbot-tell-joke`)**: Sends developer or programming jokes!!!

---

## Slash Commands

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `/krzbot-ask-ai` | `[prompt]` | Asks an AI model a question, set up using ai.hackclub.com. |
| `/krzbot-weather` | `[city_name]` | Returns current weather, temperature, humidity, and wind speed. |
| `/krzbot-tell-joke` | *None* | Sends a random programming or engineering joke to the channel. |

---

## Setup in Slack's Dashboard

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
     * `/krzbot-weather`
     * `/krzbot-tell-joke`

---

## Local Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/krzbot.git](https://github.com/your-username/krzbot.git)
   cd krzbot
   pip3 install slack-sdk slack-bolt openrouter requests
   python3 main.py
