# Forza Horizon 5 Skill Point, Forzathon Point, CR/XP, Wheelspin, AuctionHouse Sniping Macro

## Introduction
This project provides a macro to automate the process of earning skill points, forzathon points, CR/XP, wheelspins, and auction house sniping in Forza Horizon 5.

## Features
- Automates skill point farming (in EventLab)
- Automates forzathon point farming (BMW M5 1995 or Lexus SC300 or Jaguar E-type Perk)
- ~~Automates wheelspin farming (Peel Trident Perk)~~
  - The Peel Trident's skill point tree was nerfed one week after I started using this script. :(
- half-auto CR/XP farming
- Automates gift dropping
- Auction House Sniping

## How to use
### Skill Point
> [!TIP]
> Watch the entire guide here [@NiceDriving](https://www.youtube.com/@NiceDriving/videos)  
1. Enter your Farming EventLab. (145 828 346 or Search the GamerTag "KarmaDriving")
2. In the "Start Race Event Button" showing menu, Start the macro script.
3. The macro will automatically start farming.

### Forzathon Point
1. In the "Garage" menu, start the macro script.
2. The macro will automatically repeat buying the car and unlocking perks.

### Wheelspin
1. In the "Garage" menu, start the macro script.
2. The macro will automatically repeat buying a Peel Trident and unlocking perks.

### CR and XP
1. In the game, not in the menu, start the macro script.
2. the macro will automatically start farming.
3. but you should put the front wheels in the tunnel manually.

### GiftDrop
1. In the "GiftDrop" menu, start the macro script.
2. The macro will automatically send all Peel cars.

> [!WARNING]
> Since it sends all Peel cars, it will also send the Peel P50.

> [!NOTE]
> If you send the Peel Trident, the recipient can also do the Wheelspin farming since the perks will be restored. Well, that's just the spirit of Horizon, isn't it?

### AuctionHouse Sniper
1. Be in solo mode, stock Peel Trident and main festival site.
2. Open the Search menu in the Auction House and change the settings to your desired configuration.
3. Confirm your configuration and back out from the search result.
4. Configure the script (advanced search, half-auto and etc.) and start it.

\* Tested in FHD 120FPS. You can change the (x, y) if you use another resolution.

### Discord Notify Bot
1. Make your empty bot in [here](https://discord.com/developers).
2. Make the new server and invite the bot.
3. Add your token in `/src/config.py`
4. Run any macro script.
   ```python
   # /src/config.py
   DISCORD_BOT_TOKEN = "your_token"
   ```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please open an issue on GitHub.