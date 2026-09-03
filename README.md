# krzbot

A custom Slack bot built with Python (`slack-bolt`) using Socket Mode. Features AI integrations, real-time weather reports via Open-Meteo.

---

## Features & Commands

* **`/krzbot-ask-ai <prompt>`**  
  Queries language models through the OpenRouter API and posts the answer directly to the channel.

* **`/weather <city>`**  
  Looks up coordinates using Open-Meteo Geocoding, then fetches current metrics including temperature, feels-like temperature, humidity, wind speed, and precipitation.

* **`/krzbot-tell-joke`**  
  Returns a random programming joke.

* **Socket Mode Architecture**  
  Uses WebSocket connections so the bot operates behind firewalls without public HTTP endpoints, webhooks, or reverse proxies.

---

## Environment Variables

The application requires three keys set in its environment:

* `SLACK_BOT_TOKEN`: OAuth token
* `SLACK_APP_TOKEN`: Socket Mode app-level token
* `OPENROUTER_API_KEY`: API key for OpenRouter AI

---

## Requirements & Dependencies

* Python 3.10 or newer
  * `slack-bolt`
  * `slack-sdk`
  * `openrouter`
  * `requests`

```bash
pip3 install slack-bolt slack-sdk openrouter requests
