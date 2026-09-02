# krzbot

A lightweight Slack bot for custom slash commands, AI generation, and weather lookups. Built with Python, `slack-bolt`, and Socket Mode.

## Features

- `/krzbot-ask-ai [prompt]` - Send prompts to LLMs via OpenRouter.
- `/weather [city]` - Fetch current weather metrics from Open-Meteo (no API key required).
- `/krzbot-tell-joke` - Output a random dev joke.

## Environment Variables

The bot requires three environment variables to run:

```bash
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
OPENROUTER_API_KEY=sk-or-...
