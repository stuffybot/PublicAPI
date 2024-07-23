import requests
import logging
import json

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG for detailed logs

def getUUID(ign):
  try:
    resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}")
    return resp.json()["id"]
  except:
    logging.warning("Failed to fetch uuid")

def main():
  logging.debug("Starting...")
  try:
    resource_response = requests.get("https://api.hypixel.net/v2/resources/achievements")
    
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

    resourceGenerated = []
    for x in resource["achievements"]:
      for _ in resource["achievements"][x]["one_time"]:
        resourceGenerated.append(f"{x}_{(_).lower()}")

    logging.debug(f"Generated {len(resourceGenerated)} from resource data")

    key = input("Enter your API Key: ")
    checked = 0
    fullList = []
    while(True):
      ign = input("Next ign to check (type 'STOP' to stop): ")
      if(ign == "STOP"):
        break
      uuid = getUUID(ign)
      playerEndpoint = f"https://api.hypixel.net/v2/player?uuid={uuid}&key={key}" 
      response = requests.get(playerEndpoint)
      if response.status_code != 200:
        logging.error("Failed to load API data.")
      else:
        object = response.json()
        try:
          for _ in object["player"]["achievementsOneTime"]:
            if not isinstance(_, str):
              logging.warning(f"Found object of incorrect type in achievements array: '{_}'")
              continue
            if _ not in fullList:
              fullList.append(_)
          checked += 1
        except:
          logging.warning("Error finding achievements in object, API disabled?")

      logging.debug(f"Generated {len(fullList)} from input data")

    diff2 = set(fullList) - set(resourceGenerated)

    logging.debug(f"Found {len(diff2)} in player generated not in resources.")
    logging.debug(diff2)

    
    logging.debug("Ending...")
  
  except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching data: {e}")

if __name__ == '__main__':
  main()
