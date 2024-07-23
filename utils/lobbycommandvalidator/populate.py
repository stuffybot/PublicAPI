import json
import logging
import time

logging.basicConfig(level=logging.WARNING)


def main():
  file_path = "../../apis/lobbies.json"
  logging.debug("Loading file")
  with open(file_path, 'r') as file:
    data = json.load(file)
  logging.debug("Loaded file")

  lobbies = []

  for game in data["lobby_commands"]:
    gameName = game["lobby"]
    aliases = 0
    for _ in game["identifiers"]:
      aliases += 1
      lobbies.append(_)
      logging.debug(f"Added {_} to list")

    logging.debug(f"{aliases} identifiers for {gameName}")

  lobbies = sorted(lobbies)
  data["lobbiesRaw"] = lobbies

  current_time = int(time.time())
  data["lastUpdated"] = current_time

  response = input(f"Generated {len(lobbies)} identifiers. Input `push` to merge list with source.\n")
  if response == "push":
    with open(file_path, 'w') as file:
      json.dump(data, file)
    logging.debug(f"Pushed {len(lobbies)} identifiers.")

if __name__ == '__main__':
    main()
