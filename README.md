## Documentation

Documentation for this API is a Work in Progress. Until then, hopefully exploring the endpoints yourself is self explanatory. Otherwise, feel free to reach out via discord: @stuffy.

## Usage

This API can be used by any projects or mods that may have use for any of it's data. Endpoints are formatted as json objects. See table below for endpoints.

| Endpoint | Link | Description |
| - | - | - |
| Stuffy Bot Statistics | [bot](https://raw.githubusercontent.com/stuffybot/PublicAPI/main/apis/bot.json) | Stats for the operation of Stuffy Bot, total commands run, etc. |
| Hypixel Tournaments | [tournaments](https://raw.githubusercontent.com/stuffybot/PublicAPI/main/apis/tournaments.json) | Data on all historical hypixel tournaments, start and end times in Unix, and json objects for where stats are located in the Hypixel API |
| Play Commands | [playcommands](https://raw.githubusercontent.com/stuffybot/PublicAPI/main/apis/playcommands.json) | All known play commands and aliases for Hypixel, constantly updating. Can also be used as a more complete resources endpoint than [Hypixel](https://api.hypixel.net/v2/resources/games)'s |
| Lobby Commands | [lobbies](https://raw.githubusercontent.com/stuffybot/PublicAPI/main/apis/lobbies.json) | All known lobby commands and aliases for Hypixel, constantly updating. |

## Contributing

Note that not all endpoints will accept contributions. Endpoints whose contributions will be considered are the following:
* tournaments
* playcommands
* lobbies

To contribute data to endpoints that support it, make a [Pull Request](https://github.com/stuffybot/PublicAPI/pulls) and provide sufficient evidence.

If you notice information missing and are unable to submit a pull request, create a [new issue](https://github.com/stuffybot/PublicAPI/issues) on the Issues page with as much information from the following list as you can provide:
1. Where information is missing from
2. What information is missing
3. The date and time of when you last confirmed this information to be missing