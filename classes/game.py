import random
import pprint
from .magic import Spell


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "    ACTIONS" + Bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        '''
        print(self.magic)
        for i in self.magic:
            print(i.name)
        return False
        '''
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    MAGIC" + Bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "    ITEMS:" + Bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" +
                  str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        print("                        _________________________           __________ ")
        print(Bcolors.BOLD + str(self.name) + "       " +
              str(self.hp) + "/" + str(self.maxhp) + " |" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + "|   " +
              str(self.mp) + "/" + str(self.maxmp) + " |" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC + "|")