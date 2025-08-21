# Practice Modifying Objects Attributes And Calling Methods
from prettytable import PrettyTable

# Create table object
table = PrettyTable()

# Set table title
table.title = "🔥 Pokémon Battle Roster 🔥"

# Add columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur", "Jigglypuff"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass", "Fairy"])

# Changing the attributes
table.align = "l"                     # Default alignment for all columns
table.align["Pokemon Name"] = "c"     # Center-align the "Pokemon Name" column
table.align["Type"] = "c"             # Center-align the "Type" column
table.border = True                    # Show borders
table.header = True                    # Show headers
table.hrules = 1                       # Horizontal lines between rows
table.vrules = 1                       # Vertical lines between columns

# Optional: Add rows dynamically
# more_pokemon = [["Eevee", "Normal"], ["Gengar", "Ghost"]]
# for name, type_ in more_pokemon:
#     table.add_row([name, type_])

# Print table
print(table)