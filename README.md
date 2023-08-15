# daily quotes
Gets a quote from a website and posts it as an instagram note.
After posting, it waits between 18 and 28 hours and loops.
## how to use
1. Follow the instagrapi tutorial to get a permanent session (session.json).
2. copy `session.json` to this folder
## Locally
1. Run `python -m pip install -r requirements.txt` to install the requirements
2. Run with `QUOTES_API_KEY` environment variable, which is the API key for API ninja website, where you get the quotes.
## With docker compose
1. Set `QUOTES_API_KEY` in `docker-compose.yml`
2. `docker compose up -d`