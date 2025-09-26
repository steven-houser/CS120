# Steven Houser
# Choose Your Own Adventure Game
# 09/26/25

def main():
    game = getGame()
    keepGoing = True
    nextNode = "start"
    while keepGoing:
        nextNode = playNode(game, nextNode)
        if nextNode == "quit":
            keepGoing = False


def getGame():
    game = {
        "start": ["You stand at the entrance to the ancient Shadowmere Caverns. Local legends speak of a dragon's treasure hidden deep within, but many adventurers have never returned.", "Enter through the main tunnel", "main_tunnel", "Climb down the narrow side passage", "side_passage"],
        
        "main_tunnel": ["The wide tunnel stretches ahead, lit by glowing crystals. You hear the distant sound of dripping water and something else... growling.", "Follow the growling sound", "beast_chamber", "Head toward the water sounds", "underground_lake"],
        
        "side_passage": ["The narrow passage opens into a small chamber filled with ancient runes carved into the walls. A faint magical aura emanates from them.", "Touch the glowing runes", "magic_chamber", "Search for hidden passages", "secret_door"],
        
        "beast_chamber": ["You enter a large cavern where a massive cave bear blocks your path. Its eyes glow red with unnatural hunger.", "Try to sneak past the bear", "sneak_success", "Stand your ground and fight", "bear_fight"],
        
        "underground_lake": ["You reach a vast underground lake with crystal-clear water. An old wooden boat is tied to a small dock.", "Take the boat across the lake", "treasure_island", "Swim across to save time", "lake_monster"],
        
        "magic_chamber": ["The runes activate as you touch them, revealing you are the chosen one. Ancient magic flows through you, granting you power.", "Use magic to explore deeper", "wizard_path", "Seek the source of the magic", "ancient_altar"],
        
        "secret_door": ["Behind a loose stone, you discover a hidden passage that leads to the dragon's back entrance. You can hear heavy breathing.", "Sneak toward the dragon's lair", "dragon_encounter", "Look for another way around", "treasure_victory"],
        
        "sneak_success": ["You successfully sneak past the sleeping bear and find yourself in a chamber filled with old adventurer gear and bones.", "Take the magical sword from the bones", "dragon_encounter", "Search through the adventurer packs", "treasure_victory"],
        
        "bear_fight": ["You engage the cave bear in fierce combat. Your blade finds its mark, and the beast falls. You are wounded but victorious.", "Rest and tend your wounds", "treasure_island", "Press on despite your injuries", "dragon_encounter"],
        
        "treasure_island": ["The boat carries you to a small island in the center of the lake. Here stands an ancient shrine with a glowing gem.", "Take the gem of power", "wizard_path", "Leave the gem and explore the shrine", "ancient_altar"],
        
        "lake_monster": ["As you swim, a massive serpent rises from the depths! Its coils wrap around you as it drags you underwater.", "Fight the serpent with your dagger", "treasure_victory", "Try to escape to the surface", "start"],
        
        "wizard_path": ["With newfound magical power, you can sense the dragon's presence and the location of its greatest treasure.", "Confront the dragon with magic", "dragon_encounter", "Use magic to claim treasure secretly", "treasure_victory"],
        
        "ancient_altar": ["At the heart of the magical chamber lies an altar with an ancient crown. Wearing it would grant you dominion over the caves.", "Claim the crown of the caverns", "treasure_victory", "Leave the crown and continue exploring", "dragon_encounter"],
        
        "dragon_encounter": ["You face the ancient red dragon in its lair. Mountains of gold and jewels surround its massive sleeping form.", "Challenge the dragon to single combat", "treasure_victory", "Try to steal treasure while it sleeps", "quit"],
        
        "treasure_victory": ["You have successfully claimed the dragon's treasure! Gold, jewels, and magical artifacts are now yours. You are rich beyond measure!", "Leave the caves with your fortune", "quit", "Stay and rule the underground realm", "quit"]
    }
    
    return game


def playNode(game, currentNode):
    (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]
    
    print(f"""
    {desc}
    1) {menuA}
    2) {menuB}
    """)
    userChoice = input("Your choice: ")
    
    if userChoice == "1":
        nextNode = nodeA
    elif userChoice == "2":
        nextNode = nodeB
    else:
        print("Not a valid input. Please enter '1' or '2.'")
        nextNode = currentNode
    
    return nextNode


main() 