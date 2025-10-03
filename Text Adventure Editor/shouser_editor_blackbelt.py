# Steven Houser
# Text Adventure Editor: Blackbelt Extension
# 10/03/25

import json

def main():
    # Main program loop
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            keepGoing = False
        elif menuChoice == "1":
            game = getDefaultGame()
        elif menuChoice == "2":
            print("Loading a game")
            game = loadGame()
        elif menuChoice == "3":
            saveGame(game)
        elif menuChoice == "4":
            print("Create or edit a node")
            editNode(game)
        elif menuChoice == "5":
            playGame(game)
        else:
            print("Something went wrong")

def getMenuChoice():
    # Display menu and validate input
    keepGoing = True
    while keepGoing:
        print("""
        0) Exit
        1) Load default game
        2) Load a game file
        3) Save the current game
        4) Edit or add a node
        5) Play the current game""")
        menuChoice = input("What will you do? ")
        if menuChoice in ("0", "1", "2", "3", "4", "5"):
            keepGoing = False
        else:
            print("That is not a valid choice. Pick 0-5")
    return menuChoice

def playGame(game):
    # Keep playing until user quits
    keepGoing = True
    nextNode = "start"
    while keepGoing:
        nextNode = playNode(game, nextNode)
        if nextNode == "quit":
            keepGoing = False

def playNode(game, currentNode):
    # Play a single node and return next node
    nodeNames = game.keys()
    if currentNode in nodeNames:
        # Extract node data using tuple unpacking
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
    else:
        print(f"{currentNode} is not a valid node. Exiting the game")
        nextNode = "quit"
    return nextNode

def getDefaultGame():
    # Create and return default game with one node
    game = {
        "start": ("Default start node", "Start over", "start", "Quit", "quit")
    }
    return game

def editNode(game):
    # Edit existing node or create new one
    print("Current status of entire game:")
    print(json.dumps(game, indent=2))
    print("Current node names:")
    nodeNames = game.keys()
    for nodeName in nodeNames:
        print(f"  {nodeName}")
    newNodeName = input("Choose node to edit or enter new node name: ")
    if newNodeName in nodeNames:
        newNode = game[newNodeName]
    else:
        newNode = ("", "", "", "", "")
    (desc, menuA, nodeA, menuB, nodeB) = newNode
    # Get updated values for each field
    newDesc = getField("Description", desc)
    newMenuA = getField("Menu A", menuA)
    newNodeA = getField("Node A", nodeA)
    newMenuB = getField("Menu B", menuB)
    newNodeB = getField("Node B", nodeB)
    newNode = (newDesc, newMenuA, newNodeA, newMenuB, newNodeB)
    game[newNodeName] = newNode

def getField(fieldName, currentVal):
    # Get field input, keep current value if user presses enter
    field = input(f"{fieldName} ({currentVal}): ")
    if field == "":
        field = currentVal
    return field

def saveGame(game):
    # Save game to JSON file
    fileName = input("Enter filename to save (e.g., game.json): ")
    if fileName == "":
        fileName = "game.json"
    outFile = open(fileName, "w")
    json.dump(game, outFile, indent=4)
    outFile.close()
    print("Saving this file...")
    print(json.dumps(game, indent=4))

def loadGame():
    # Load game from JSON file
    fileName = input("Enter filename to load (e.g., game.json): ")
    if fileName == "":
        fileName = "game.json"
    inFile = open(fileName, "r")
    game = json.load(inFile)
    inFile.close()
    return game

main() 