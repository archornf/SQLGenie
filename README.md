## SQLGenie

### What is this project?
The point of these tools is to speed up development by reducing unnecessary choice in favor of quick generation or automation.

### What is the future of this project?

Currently I'm only focusing on implementing SQL development.

### What does it support?
This tool currently only supports [**Trinity Core 3.3.5a Branch**](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) 

Using the following databases:
- [MySQL](https://www.mysql.com/) >= 5.7 
- [MariaDB](https://mariadb.org/) >= 10.4

### What tools are included in this project?
- Item Display Finder
	- Search display ids via item entry/name.
		- Automatically copies it to your clipboard for easy use.
- Item Stat Multiplier
	- Insert a starting entry, a ending entry, and a multiplier value to mod all stats by the multiplier.
	- Stats Modified = stat values 1 - 10, min/max dmg, armor, and block.
	- Multiplier (1.10 is **10%**, 1.20 is **20%**,  2 is **200%** and so on.)
- Wrathful Clone
	- This will clone all Wrathful items and will multiply their stats. 
 	- Make sure your starting entry and the following 208 entries are not in use. 
    	- Prefix is the text that will replace Wrathful in the item name.
       	- Multipliers are float representations of percentages 101% = 1.01, 150% = 1.5, 200% = 2.0, ect.
      	- If you want to reduce a stat, use a number less than 1.0. 50% = 0.5, 25% = 0.25, ect.
      	- Only thing you have to do now is change the display ids.
- Player Start Location
  	- Will set the location of all classes/races to the cordinates supplied.

### Disclaimer
This tool is currently in its early stages of development.

This tool should not affect your data in any negative way. 
- However it is your responsibilty as the end user to ensure you practice good database management and backup your data.
- Should you mess something up using this tool that is on you.

If you notice issues please report them.
