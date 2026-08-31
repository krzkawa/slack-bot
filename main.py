import os
import re
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from openrouter import OpenRouter
import time
import requests

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "**********")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN", "******")
app = App(token=SLACK_BOT_TOKEN)

openrouter_client = OpenRouter(
    api_key=os.environ.get("OPENROUTER_API_KEY", "***********"),
    server_url=os.environ.get("OPENROUTER_SERVER_URL", "https://ai.hackclub.com/proxy/v1")
)


JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people in the world: Those who understand binary, and those who don't.",
    "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'",
    "How many programmers does it take to change a light bulb? None, it's a hardware problem.",
    "Why did the developer go broke? Because he used up all his cache.",
    "How do you tell an introverted C++ dev from an extroverted one? The extroverted one looks at YOUR shoes while avoiding garbage collection.",
    "How many hardware engineers does it take to change a lightbulb? None. 'It's a software problem.'",
    "Why was the resistor so popular? It offered zero resistance to good vibes.",
    "What is the difference between Mechanical and Civil Engineers? Mechanical engineers build weapons; Civil engineers build targets.",
    "How do mechanical engineers fix things? If it moves and shouldn't: Duct tape. If it doesn't move and should: WD-40.",
    "Why do Java developers wear glasses? Because they can't C#.",
    "Why was the JavaScript developer sad? Because they didn't 'know' how to 'null' their feelings.",
    "Why did the DevOps engineer get kicked out of the concert? They kept trying to deploy to production during the main set.",
    "What is a git developer's favorite drink? A rebase-on-the-rocks.",
    "What is an algorithm? Words used by programmers when they don't want to explain what they did.",
    "How do you know someone uses Linux? Don't worry, they'll tell you in the first 5 seconds.",
    "To understand recursion... You must first understand recursion.",
    "I'd tell you a joke about UDP... But you might not get it.",
    "I'd tell you a joke about TCP... Did you get it? Great, now I can tell you the rest.",
    "How do you center a div in CSS? Nobody knows; it remains an unsolved Millennium Prize Problem.",
    "Why is HTML not considered a programming language? Because it doesn't have class... wait, it does!",
    "Why did the object-oriented program fail its exam? It lost its inheritance.",
    "Why do functional programmers love immutable data? They hate change.",
    "Why do Rust developers sleep so well at night? The compiler checked all their memory safety beforehand.",
    "Why did the Assembly programmer get lost? They missed a JMP instruction.",
    "A quantum computer walks into a bar... It orders a drink, doesn't order a drink, and exists in both states until observed.",
    "Why was the micro-controller so confident? It had high pin-tegrity.",
    "Why did the router cry? It lost its default gateway.",
    "Why do hackers love nature walks? They enjoy finding backdoor paths.",
    "A QA tester walks into a bar, orders 1 beer, 0 beers, 99999 beers, a lizard, -1 beers... The first real customer enters, asks where the bathroom is, and the bar bursts into flames.",
    "A developer had a problem, so they used Regex. Now they have two problems.",
    "Why is Python so easy to learn? Because indentation is mandatory, just like adult responsibilities.",
    "Why did C break up with C++? C couldn't handle C++'s extra weight and classes.",
    "Why do Go developers love concurrency? They can do routine tasks in channels.",
    "Why does PHP get a bad rap? It's like dollar store tools—works fine until you try to build a skyscraper.",
    "Why do embedded engineers hate magic tricks? They prefer deterministic behavior.",
    "What's an aerospace engineer's favorite song? 'Free Falling' (during stress testing).",
    "Why are chemical engineers great at parties? They know how to optimize reaction rates.",
    "Why did the industrial engineer reorder their closet? To minimize throughput time during morning prep.",
    "Real programmers don't comment their code... If it was hard to write, it should be hard to understand!",
    "What is 'the cloud'? Just someone else's computer on fire.",
    "It's not a bug... It's an undocumented feature.",
    "What is refactoring? Taking working code and breaking it until it looks prettier.",
    "Two threads walk into a bar... bartending. ordered a beer The first",
    "What do cryptographers eat for breakfast? Enigma flakes with asymmetric syrup.",
    "Why did the programmer quit their job? They didn't get arrays (a raise) and missed the semicolon.",
    "Why did the frontend dev leave the party early? The UI was too responsive to handle.",
    "Why do backend devs love dark basements? That's where the database queries feel most comfortable.",
    "What is machine learning? Written math until you get funding, then it's AI.",
    "What is a data scientist? Someone who is better at statistics than any software engineer, and better at software engineering than any statistician.",
    "What did git commit say to git push? 'I'm ready when you are, don't origin reject me.'",
    "Why doesn't Python have pointers? Because life is too short to point fingers.",
    "What is a Docker container's favorite holiday? Boxing Day.",
    "Why was Kubernetes stressed? Too many pods to manage and not enough nodes.",
    "Why did the REST API get ghosted? Bad status code 404: Relationship Not Found.",
    "Why did monolith architecture break up into microservices? It needed space to handle its individual issues.",
    "What is code review? Watching someone point out missing whitespace for 45 minutes.",
    "What is technical debt? Taking a loan from your future weekend.",
    "How do senior developers code? Ctrl+C, Ctrl+V from Stack Overflow.",
    "What is code documentation like? Like sex: when it's good, it's very good; when it's bad, it's better than nothing.",
    "Why is clean code like a clean room? It only stays that way until someone actually lives in it.",
    "What is an electrical engineer's favorite exercise? Circuit training.",
    "Why do mechanical engineers love gears? They really mesh well together.",
    "Why did the suspension bridge go to therapy? It was under too much tension.",
    "Why did the beam refuse to bend? It had strong moral moment capacity.",
    "There are 2 hard problems in computer science... Cache invalidation, naming things, and off-by-one errors.",
    "01001000 01101001 — Binary jokes are easy once you get the byte out of them.",
    "Why do floating point numbers fail math? Because 0.1 + 0.2 = 0.30000000000000004.",
    "A string walks into a bar and orders a drink. The bartender says, 'Aren't you a string?' The string replies, 'No, I'm a frayed knot.'",
    "A null pointer exception walks into a bar... Everything crashes.",
    "Why did the developer stay in the shower forever? The shampoo bottle said: 'Lather, Rinse, Repeat.'",
    "Why do Linux users love sudo? Because absolute power corrupts absolutely, and comfortably.",
    "How do you generate a random string? Put a first-time user in Vim and ask them to exit.",
    "Why is Emacs an OS? It just lacks a decent text editor.",
    "What's the difference between hardware and software? Hardware is the part you can kick when software crashes.",
    "What is firmware? Software that thinks it's hardware.",
    "Why was the quantum bit nervous? It was uncertain about its state.",
    "Why is the compiler so harsh? It refuses to overlook your mistakes.",
    "Why did the interpreter cross the road? To execute the code line by line on the other side.",
    "Why did the developer perform git push --force? Because fortune favors the bold (and unemployed).",
    "What is Agile methodology? Paying twice as much to fail in 2-week increments.",
    "Why did the developer hate daily standups? They couldn't sit down with their problems.",
    "What is legacy code? Code written by someone who no longer works here (or you, 3 weeks ago).",
    "Why shouldn't you test in production? Unless you enjoy adrenaline rushes on Friday at 4:55 PM.",
    "Why did the cache clear itself? It needed a fresh start.",
    "Ping! Pong! (Latency: 24ms)",
    "Why is the system down? It's always DNS. Except when it's not, but it actually is.",
    "Why did the internet go down? Someone mistyped a route table entry.",
    "Why do mainframes never die? They're powered by COBOL and sheer inertia.",
    "Why are COBOL programmers always rich? Because all their code runs the world's banks.",
    "Why do Lisp programmers love parentheses? ((Because) (((they) (really) (do))).",
    "Why do Haskell programmers love purity? No side effects means no unexpected consequences.",
    "Why did Prolog win the debate? It derived the answer logically from first principles.",
    "Why do matrix operations scare people? Because dimensions must match, or everything explodes.",
    "Why did the mechanical design crash? The assembly constraints were over-defined.",
    "What is soldering? Welding for people who like fumes and tiny burn marks.",
    "Why is the oscilloscope the coolest tool in the lab? It really knows how to show waves.",
    "Why did the multimeter cross the circuit? To measure the potential difference.",
    "Why do mechanical engineers hate entropy? Because disorder always wins in the end.",
    "Why is CFD called 'Colors For Directors'? Beautiful rainbow contours hide convergence errors.",
    "Why is open-source software like a free puppy? It's free, but you have to feed, maintain, and clean up after it forever."
]

MENTION_PATTERN = re.compile(r"<@([A-Z0-9]+)>")

@app.command("/krzbot-weather")
def handle_weather(ack, command, respond):
    ack()
    city = command.get("text", "").strip()

    if not city:
        respond("Please provide a city name. Example: `/weather Wroclaw`")
        return

    try:
        # Step 1: Geocoding - Convert city name to latitude and longitude
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={requests.utils.quote(city)}&count=1&language=en&format=json"
        geo_res = requests.get(geo_url, timeout=5).json()

        results = geo_res.get("results")
        if not results:
            respond(f"Could not find coordinates for city: `{city}`")
            return

        location = results[0]
        lat = location["latitude"]
        lon = location["longitude"]
        city_name = location.get("name", city)
        country = location.get("country", "")

        # Step 2: Fetch weather using coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m&wind_speed_unit=kmh"
        weather_res = requests.get(weather_url, timeout=5).json()

        current = weather_res.get("current", {})
        temp = current.get("temperature_2m")
        feels_like = current.get("apparent_temperature")
        humidity = current.get("relative_humidity_2m")
        wind = current.get("wind_speed_10m")
        precip = current.get("precipitation")

        # Step 3: Format output message
        location_label = f"{city_name}, {country}" if country else city_name
        
        message = (
            f"🌤️ *Weather in {location_label}*\n"
            f"• *Temperature:* {temp}°C (Feels like {feels_like}°C)\n"
            f"• *Humidity:* {humidity}%\n"
            f"• *Wind Speed:* {wind} km/h\n"
            f"• *Precipitation:* {precip} mm"
        )

        respond(text=message, response_type="in_channel")

    except Exception as e:
        respond(f"Error fetching weather data: {str(e)}")

@app.command("/krzbot-tell-joke")
def handle_tell_joke(ack, respond):
    ack()
    joke = random.choice(JOKES)
    respond(text=joke, response_type="in_channel")


@app.command("/krzbot-ask-ai")
def handle_ask_ai(ack, command, respond):
    ack()
    prompt = command.get("text", "").strip()

    if not prompt:
        respond("Please provide a prompt. Example: `/krzbot-ask-ai Explain recursion`")
        return
    
    respond("Thinking")

    try:
        response = openrouter_client.chat.send(
            model="google/gemini-3.7-flash",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False

        )
        ai_response = response.choices[0].message.content
        respond(text=f"*Q:* {prompt}\n\n*A:* {ai_response}", response_type="in_channel")
    except Exception as e:
        respond(f"Error querying OpenRouter API: {str(e)}")
    


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
