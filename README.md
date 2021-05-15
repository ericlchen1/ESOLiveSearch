# ESOLiveSearch

Attempt at creating a live search feature to be used on TamrielTradeCentre.com
Used to bypass website reCaptcha v3 to fetch data in realtime using direct HTTP requests.

Currently implemented:
- Dynamic user-agents for http requests
- Dynamic captcha keys that were pre-generated
- Variable delay between searches (~2 minutes)
- Location and item information parsing

Current Issues to be solved:
- Dynamic IP through proxies
- Decoding protobuf request to generate ReCaptcha keys
- More than one search option

To be implemented in the future:
- UI to add more filters to be livesearched
