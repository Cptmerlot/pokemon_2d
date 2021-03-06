from typing import List, Dict, Any

# FIXME: Enforce Better types
POKEMON_TYPE_DATA: Dict[str, Dict[str, Any]] = {
    "Normal": {
        "Type": "Normal",
        "Strong": [
            "Rock",
            "Ghost",
            "Steel"
        ],
        "Weak": ["Ghost"],
        "Resistant": ["Fighting"]
    },
    "Fighting": {
        "Type": "Fighting",
        "Strong": [
            "Normal",
            "Rock",
            "Steel",
            "Ice",
            "Dark"
        ],
        "Weak": [
            "Flying",
            "Poison",
            "Psychic",
            "Bug",
            "Ghost",
            "Fairy"
        ],
        "Resistant": [
            "Rock",
            "Bug",
            "Dark"
        ],
        "Vulnerable": [
            "Flying",
            "Psychic",
            "Fairy"
        ]
    },
    "Flying": {
        "Type": "Flying",
        "Strong": [
            "Fighting",
            "Bug",
            "Grass"
        ],
        "Weak": [
            "Rock",
            "Steel",
            "Electric"
        ],
        "Resistant": [
            "Fighting",
            "Ground",
            "Bug",
            "Grass"
        ],
        "Vulnerable": [
            "Rock",
            "Electric",
            "Ice"
        ]
    },
    "Poison": {
        "Type": "Poison",
        "Strong": [
            "Grass",
            "Fairy"
        ],
        "Weak": [
            "Poison",
            "Ground",
            "Rock",
            "Ghost",
            "Steel"
        ],
        "Resistant": [
            "Fighting",
            "Poison",
            "Grass",
            "Fairy"
        ],
        "Vulnerable": [
            "Ground",
            "Psychic"
        ]
    },
    "Ground": {
        "Type": "Ground",
        "Strong": [
            "Poison",
            "Rock",
            "Steel",
            "Fire",
            "Electric"
        ],
        "Weak": [
            "Flying",
            "Bug",
            "Grass"
        ],
        "Resistant": [
            "Poison",
            "Rock",
            "Electric"
        ],
        "Vulnerable": [
            "Water",
            "Grass",
            "Ice"
        ]
    },
    "Rock": {
        "Type": "Rock",
        "Strong": [
            "Flying",
            "Bug",
            "Fire",
            "Ice"
        ],
        "Weak": [
            "Fighting",
            "Ground",
            "Steel"
        ],
        "Resistant": [
            "Normal",
            "Flying",
            "Poison",
            "Fire"
        ],
        "Vulnerable": [
            "Fighting",
            "Ground",
            "Steel",
            "Water",
            "Grass"
        ]
    },
    "Bug": {
        "Type": "Bug",
        "Strong": [
            "Grass",
            "Psychic",
            "Dark"
        ],
        "Weak": [
            "Fighting",
            "Flying",
            "Poison",
            "Ghost",
            "Steel",
            "Fire",
            "Fairy"
        ],
        "Resistant": [
            "Fighting",
            "Ground",
            "Grass"
        ],
        "Vulnerable": [
            "Flying",
            "Rock",
            "Fire"
        ]
    },
    "Ghost": {
        "Type": "Ghost",
        "Strong": [
            "Ghost",
            "Psychic"
        ],
        "Weak": [
            "Normal",
            "Dark"
        ],
        "Resistant": [
            "Normal",
            "Fighting",
            "Poison",
            "Bug"
        ],
        "Vulnerable": [
            "Ghost",
            "Dark"
        ]
    },
    "Steel": {
        "Type": "Steel",
        "Strong": [
            "Rock",
            "Ice",
            "Fairy"
        ],
        "Weak": [
            "Steel",
            "Fire",
            "Water",
            "Electric"
        ],
        "Resistant": [
            "Normal",
            "Flying",
            "Poison",
            "Rock",
            "Bug",
            "Steel",
            "Grass",
            "Psychic",
            "Ice",
            "Dragon",
            "Fairy"
        ],
        "Vulnerable": [
            "Fighting",
            "Ground",
            "Fire"
        ]
    },
    "Fire": {
        "Type": "Fire",
        "Strong": [
            "Bug",
            "Steel",
            "Grass",
            "Ice"
        ],
        "Weak": [
            "Rock",
            "Fire",
            "Water",
            "Dragon"
        ],
        "Resistant": [
            "Bug",
            "Steel",
            "Fire",
            "Grass",
            "Ice"
        ],
        "Vulnerable": [
            "Ground",
            "Rock",
            "Water"
        ]
    },
    "Water": {
        "Type": "Water",
        "Strong": [
            "Ground",
            "Rock",
            "Fire"
        ],
        "Weak": [
            "Water",
            "Grass",
            "Dragon"
        ],
        "Resistant": [
            "Steel",
            "Fire",
            "Water",
            "Ice"
        ],
        "Vulnerable": [
            "Grass",
            "Electric"
        ]
    },
    "Grass": {
        "Type": "Grass",
        "Strong": [
            "Ground",
            "Rock",
            "Water"
        ],
        "Weak": [
            "Flying",
            "Poison",
            "Bug",
            "Steel",
            "Fire",
            "Grass",
            "Dragon"
        ],
        "Resistant": [
            "Ground",
            "Water",
            "Grass",
            "Electric"
        ],
        "Vulnerable": [
            "Flying",
            "Poison",
            "Bug",
            "Fire",
            "Ice"
        ]
    },
    "Electric": {
        "Type": "Electric",
        "Strong": [
            "Flying",
            "Water"
        ],
        "Weak": [
            "Ground",
            "Grass",
            "Electric",
            "Dragon"
        ],
        "Resistant": [
            "Flying",
            "Steel",
            "Electric"
        ],
        "Vulnerable": "Ground"
    },
    "Psychic": {
        "Type": "Psychic",
        "Strong": [
            "Fighting",
            "Poison"
        ],
        "Weak": [
            "Steel",
            "Psychic",
            "Dark"
        ],
        "Resistant": [
            "Fighting",
            "Psychic"
        ],
        "Vulnerable": [
            "Bug",
            "Ghost",
            "Dark"
        ]
    },
    "Ice": {
        "Type": "Ice",
        "Strong": [
            "Flying",
            "Ground",
            "Grass",
            "Dragon"
        ],
        "Weak": [
            "Steel",
            "Fire",
            "Water",
            "Ice"
        ],
        "Resistant": "Ice",
        "Vulnerable": [
            "Fighting",
            "Rock",
            "Steel",
            "Fire"
        ]
    },
    "Dragon": {
        "Type": "Dragon",
        "Strong": "Dragon",
        "Weak": [
            "Steel",
            "Fairy"
        ],
        "Resistant": [
            "Fire",
            "Water",
            "Grass",
            "Electric"
        ],
        "Vulnerable": [
            "Ice",
            "Dragon",
            "Fairy"
        ]
    },
    "Fairy": {
        "Type": "Fairy",
        "Strong": [
            "Fighting",
            "Dragon",
            "Dark"
        ],
        "Weak": [
            "Poison",
            "Steel",
            "Fire"
        ],
        "Resistant": [
            "Fighting",
            "Bug",
            "Dragon",
            "Dark"
        ],
        "Vulnerable": [
            "Poison",
            "Steel"
        ]
    },
    "Dark": {
        "Type": "Dark",
        "Strong": [
            "Ghost",
            "Psychic"
        ],
        "Weak": [
            "Fighting",
            "Dark",
            "Fairy"
        ],
        "Resistant": [
            "Ghost",
            "Psychic",
            "Dark"
        ],
        "Vulnerable": [
            "Fighting",
            "Bug",
            "Fairy"
        ]
    }
}
