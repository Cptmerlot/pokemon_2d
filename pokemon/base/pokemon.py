from typing import Optional, Tuple, Dict, List
import uuid
import random
import operator
from pokemon.attack.base import Attack


class Base:
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int

    def __init__(self, hp: int, attack: int, defense: int, sp_attack: int, sp_defense: int, speed: int) -> None:
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed


class Name:
    english: str
    japanese: str
    chinese: str
    french: str

    def __init__(self, english: str = "", japanese: str = "", chinese: str = "", french: str = "") -> None:
        self.english = english
        self.japanese = japanese
        self.chinese = chinese
        self.french = french


class Type:
    types: List[str]
    weak: List[str]
    strong: List[str]
    resistant: List[str]
    vulnerable: List[str]

    def __init__(self,
                 type: List[str],
                 weak: List[str],
                 strong: List[str],
                 resistant: List[str],
                 vulnerable: List[str]):
        self.type = type
        self.weak = weak
        self.strong = strong
        self.vulnerable = vulnerable
        self.resistant = resistant


class PokemonSchema:
    id: int
    name: Name
    type: Type
    base: Base

    def __init__(self, id: int, name: Name, type: Type, base: Base) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.base = base


class Pokemon():
    _evolves_to: Optional[str] = None
    _evolve_level: Optional[int] = None
    _level = 0
    _hitpoints: int = 0
    _current_hitpoints: int = 0
    _attk_pw: int = 0
    _sp_attk_pw: int = 0
    _defense: int = 0
    _sp_defense: int = 0
    _speed: int = 0
    _experience: int = 0
    _attacks: List[Attack] = []

    def __init__(self, pokemon: PokemonSchema, level_range: Tuple[int, int]) -> None:
        self._info = pokemon
        self._id = uuid.uuid1()
        self._roll_for_level(level_range)
        self._generate_stats()

    def _roll_for_level(self, level_range: Tuple[int, int]) -> None:
        min, max = level_range
        self._level = random.randint(min, max)

    def _generate_stats(self) -> None:
        self._hitpoints = self._generate_stat(self._info.base.hp, 0.30)
        self._attk_pw = self._generate_stat(self._info.base.attack)
        self._sp_attk_pw = self._generate_stat(self._info.base.sp_attack)
        self._speed = self._generate_stat(self._info.base.speed)
        self._defense = self._generate_stat(self._info.base.defense)
        self._sp_defense = self._generate_stat(self._info.base.sp_defense)
        self._current_hitpoints = int(self._hitpoints)

    def _generate_stat(self, base: float, stat_mod: float = 0.10) -> int:
        return int(base * (stat_mod * self._level))

    def evolves_to(self) -> str:
        if self._evolves_to is not None:
            return "{} at level {}".format(self._evolves_to, self._evolve_level)
        return "n/a"

    def level_up(self) -> None:
        self._level = self._level + 1
        if self._evolve_level is not None:
            if self._level >= self._evolve_level:
                answer = input(f"would you like to evolve {self._info.name} to {self.evolves_to}")
                if answer.lower() == "yes":
                    self._evolve()
        self._generate_stats()

    @property
    def alive(self) -> bool:
        return self._current_hitpoints > 0

    def _evolve(self) -> None:
        # evolve pokemon here
        # update base base values
        pass

    def _combat_experience(self) -> None:
        # roll for exp
        # self._experience + get_exp()
        pass

    def take_damage(self, dmg: int) -> None:
        if dmg > 0:
            self._mins_hp(dmg)

    def heal(self, healing: int) -> None:
        if healing > 0:
            self._add_hp(healing)

    def _add_hp(self, healing: int) -> None:
        if (self._hitpoints - self._current_hitpoints) < healing:
            healing = self._hitpoints - self._current_hitpoints
        self._current_hitpoints = self._current_hitpoints + healing

    def _mins_hp(self, dmg: int) -> None:
        if self._current_hitpoints < dmg:
            self._current_hitpoints = 0
            return

        self._current_hitpoints = self._current_hitpoints - dmg
        return

    @property
    def hitpoints(self):
        return self._hitpoints

    @property
    def current_hitpoints(self):
        return self._current_hitpoints

    @property
    def experience(self):
        return self._experience

    @property
    def attack_power(self):
        return self._attk_pw

    @property
    def special_attack_power(self):
        return self._sp_attk_pw

    @property
    def defense(self):
        return self._defense

    @property
    def special_defense(self):
        return self._sp_defense

    @property
    def speed(self):
        return self._speed

    @property
    def level(self):
        return self._level

    @property
    def name(self):
        return self._info.name

    @property
    def type(self):
        return self._info.type.type

    @property
    def weak(self):
        return self._info.type.weak

    @property
    def strong(self):
        return self._info.type.strong

    @property
    def vulnerable(self):
        return self._info.type.vulnerable

    @property
    def resistant(self):
        return self._info.type.resistant

    def get_type(self) -> List[str]:
        return self._info.type.types

    def get_stats(self) -> Dict[str, int]:
        return {
            "attack": self._attk_pw,
            "defense": self._defense,
            "speed": self._speed,
            "hitpoints": self._hitpoints,
            "level": self._level,
            "experience": self._experience,
        }

    def __str__(self) -> str:
        return("name: {1} type: {2} level: {3} id: {0}".format(self._id,
                                                               self._info.name,
                                                               ", ".join(self._info.type.type),
                                                               self.level))
