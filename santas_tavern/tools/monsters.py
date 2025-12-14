from typing import Dict, Optional, Any
import logging
import requests
from datapizza.tools import tool
import json


logger = logging.getLogger(__name__)

BASE_URL = "https://www.dnd5eapi.co/api/2014"

global monsters_list
monsters_list: Optional[Dict[str, Any]] = None

global cache
cache: Dict[str, Any] = {}
# Load cache from disk (optional)
try:
    with open("dnd_cache.json", "r") as f:
        cache = json.load(f)
except FileNotFoundError:
    cache = {}


def _get_item_details(
    category: str, index: str, cache: Dict[str, Any]
) -> Dict[str, Any]:
    """Get detailed information about a specific item, using cache if available."""
    cache_key = f"dnd_item_{category}_{index}"
    cached_data = cache.get(cache_key)

    if cached_data:
        # Add source attribution if not already present
        if isinstance(cached_data, dict) and "source" not in cached_data:
            cached_data["source"] = "D&D 5e API"
        return cached_data

    try:
        response = requests.get(f"{BASE_URL}/{category}/{index}")
        if response.status_code != 200:
            return {
                "error": f"Item '{index}' not found in category '{category}' or API request failed",
                "status_code": response.status_code,
                "message": "Please use only valid D&D 5e API endpoints and parameters",
                "source": "D&D 5e API",
            }

        data = response.json()

        # Add source attribution
        data["source"] = "D&D 5e API"

        # Cache the result
        cache[cache_key] = data
        # Save cache to disk (optional)
        with open("dnd_cache.json", "w") as f:
            json.dump(cache, f)

        return data
    except requests.RequestException as e:
        logger.error(f"Request failed for {category}/{index}: {e}")
        return json.dumps(
            {
                "error": f"Request failed for item '{index}' in category '{category}'",
                "message": str(e),
                "source": "D&D 5e API",
            }
        )


@tool
def find_monsters_by_challenge_rating(
    min_cr: float = 0, max_cr: float = 30
) -> Dict[str, Any]:
    """Find monsters within a specified Challenge Rating (CR) range."""
    logger.info(f"Finding monsters by CR: {min_cr}-{max_cr}")

    crs = []
    if min_cr < 1:
        crs.extend([x * 0.25 for x in range(0, 4)])
    crs.extend(list(range(max(1, int(min_cr)), int(max_cr))))

    response = requests.get(
        f"{BASE_URL}/monsters?challenge_rating={','.join(map(str, crs))}"
    )
    if response.status_code != 200:
        return {
            "error": "Monster' not found or API request failed",
            "status_code": response.status_code,
            "message": "Please use only valid D&D 5e API categories",
            "source": "D&D 5e API",
        }
    monsters_list = response.json()

    if "error" in monsters_list:
        return monsters_list

    # Filter monsters by CR
    results = []
    for item in monsters_list.get("results", []):
        # Get detailed monster info (from cache if available)
        item_index = item["index"]
        monster_details = _get_item_details("monsters", item_index, cache)
        if "error" in monster_details:
            continue

        results.append(
            {
                "name": monster_details["name"],
                "challenge_rating": monster_details.get("challenge_rating", 0),
                "type": monster_details.get("type", "Unknown"),
                "size": monster_details.get("size", "Unknown"),
                "alignment": monster_details.get("alignment", "Unknown"),
                "hit_points": monster_details.get("hit_points", 0),
                "armor_class": monster_details.get("armor_class", [{"value": 0}])[
                    0
                ].get("value", 0),
                "uri": f"resource://dnd/item/monsters/{item_index}",
            }
        )

    # Sort results by CR and name
    results.sort(key=lambda x: (x["challenge_rating"], x["name"]))

    return json.dumps(
        {
            "query": f"Monsters with CR {min_cr}-{max_cr}",
            "items": results,
            "count": len(results),
        }
    )
