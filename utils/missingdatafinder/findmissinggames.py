import requests
import logging
import json

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG for detailed logs

def main():
  logging.debug("Starting...")
  try:
    resource_response = requests.get("https://api.hypixel.net/v2/resources/games")
    
    if resource_response.status_code != 200:
      logging.error("Failed to load API data.")
      return
    
    resource = resource_response.json()
    file_path = "../../apis/playcommands.json"
    with open(file_path, 'r') as file:
      games = json.load(file)
    
    if not resource["success"] or not games["success"]:
      logging.error("API request not successful.")
      return
    
    playerGenerated = []

    for x in games["gameData"]:
      current = x["game"]
      for _ in x["modes"]:
        playerGenerated.append((current, _["modeName"]))

    
    logging.debug(f"Generated {len(playerGenerated)} from local data")


    resourceGenerated = []
    for x in resource["games"]:
      if "modeNames" in resource["games"][x]:
        for _ in resource["games"][x]["modeNames"]:
          resourceGenerated.append((x, _))

    logging.debug(f"Generated {len(resourceGenerated)} from resource data")

    diff1 = set(resourceGenerated) - set(playerGenerated)
    diff2 = set(playerGenerated) - set(resourceGenerated)

    logging.debug(f"Found {len(diff1)} in resources not in player generated and {len(diff2)} in player generated not in resources.")
    logging.debug(diff2)

    
    logging.debug("Ending...")
  
  except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching data: {e}")

if __name__ == '__main__':
  main()
