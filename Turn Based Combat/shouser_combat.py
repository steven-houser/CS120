# Steven Houser
# Combat Implementation
# 10/17/25

import shouser_tbc as tbc

def main():
    # Create and simulate combat between hero and monster
    # Create hero character
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    
    # Create monster character
    monster = tbc.Character("Monster", 20, 30, 5, 0)
    
    # Print stats
    hero.printStats()
    monster.printStats()
    
    # Fight
    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()

