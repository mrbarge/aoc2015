import copy

class Fighter:

    def __init__(self, name, hp=100, damage=0, armor=0, mana=0, boss=False):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = 0
        self.mana = mana
        self.effects = []
        self.mana_spend = 0
        self.turn = 0
        self.spellhistory = []
        self.boss = boss

    def can_cast(self, spell):
        return self.mana > spell.cost and (spell.name not in [s.name for s in self.effects])

    def apply(self, spell):
        s = copy.deepcopy(spell)
        self.mana -= spell.cost
        self.mana_spend += spell.cost
        self.effects.append(s)
        self.spellhistory.append(s.name)

    def prepare(self):

        if not self.boss:
            self.damage = 0
            self.armor = 0

        for effect in self.effects:
            #print(f"Applying buff {effect.name} (turns left: {effect.turns})")
            self.hp += effect.hp
            self.damage += effect.damage
            self.mana += effect.mana
            self.armor += effect.armor

            effect.turns -= 1

        #self.show()
        self.effects = [e for e in self.effects if e.turns > 0]

    def show(self):
        #print(f"{self.name} HP: {self.hp} Damage: {self.damage} Armor: {self.armor} Mana: {self.mana}")
        return

class Spell:

    def __init__(self, name, cost=0, damage=0, hp=0, armor=0, turns=0, mana=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.hp = hp
        self.armor = armor
        self.turns = turns
        self.mana = mana

spells = [
    Spell('missile', cost=53, damage=4, hp=0, armor=0, turns=1, mana=0),
    Spell('drain', cost=73, damage=2, hp=2, armor=0, turns=1, mana=0),
    Spell('shield', cost=113, damage=0, hp=0, armor=7, turns=6, mana=0),
    Spell('poison', cost=173, damage=3, hp=0, armor=0, turns=6, mana=0),
    Spell('recharge', cost=229, damage=0, hp=0, armor=0, turns=5, mana=101)
]

least_mana_cost = 5000

def round(player,boss,turn,playerTurn=True,part2=False):
    global least_mana_cost

    # apply existing effects
    player.prepare()
    boss.prepare()
    boss.hp -= player.damage

    if boss.hp <= 0:
        goodmanas.append(player.mana_spend)
        #print(f"Winning spell history: {player.mana_spend} {player.spellhistory}")
        least_mana_cost = min(player.mana_spend,least_mana_cost)
        return


    if part2 and playerTurn:
        player.hp -= 1

    if player.hp <= 0:
        return

    # we know from testing that this is at least one winning solution, ignore any mana spends above it
    if player.mana_spend > least_mana_cost:
        return

    if playerTurn:
        #print(f"*** Turn {turn}: Boss hit for {player.damage} and is now {boss.hp}")

        valid_spells = [s for s in spells if player.can_cast(s)]
        if len(valid_spells) == 0:
            prospect_player = copy.deepcopy(player)
            prospect_boss = copy.deepcopy(boss)
            prospect_player.turn += 1
            round(prospect_player, prospect_boss, turn + 1, False,part2)
        else:
            for spell in valid_spells:
                prospect_player = copy.deepcopy(player)
                prospect_boss = copy.deepcopy(boss)
                prospect_player.apply(spell)
                prospect_player.turn += 1
                #print(f"Turn {turn}: Player using {spell.name}")
                round(prospect_player,prospect_boss,turn+1,False,part2)
    else:
        prospect_player = copy.deepcopy(player)
        prospect_boss = copy.deepcopy(boss)
        prospect_player.hp -= max(boss.damage - player.armor, 1)

        #print(f"*** Turn {turn}: Boss hits for {boss.damage - player.armor}, player hp now {player.hp}")
        if prospect_player.hp > 0:
            round(prospect_player,prospect_boss,turn+1,True,part2)

goodmanas = []

player = Fighter('player', hp=50, damage=0, armor=0, mana=500)
boss = Fighter('boss', hp=58, damage=9, armor=0, mana=0,boss=True)

round(player,boss,0,True,True)
goodmanas = sorted(goodmanas)

print(goodmanas)

