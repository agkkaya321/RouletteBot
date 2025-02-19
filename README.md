# RouletteBot

## Description
RouletteBot is a web extension that automates betting on an online casino site using a strategy based on a tiered martingale system. Additionally, Python scripts are provided to test this strategy using the `random` library.

The project's goal was to analyze the viability of this approach and determine its profitability.

## Features
- **Web Extension**: Automates betting on the online casino site according to the martingale strategy.
- **Python Scripts**: Allows testing of the strategy with random simulations.
- **Results Analysis**: Statistical evaluation of gains and losses to assess the profitability of the strategy.

## Study Results
After multiple simulations, it was concluded that this strategy **is not profitable** in the long term. In the best cases, the probability of achieving a 30% gain was **0.61** (61%), which does not guarantee a sustainable profit.

## Installation
### Web Extension
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/RouletteBot.git
   ```
2. Load the extension manually into your browser:
   - Go to `chrome://extensions/` (or the equivalent for your browser).
   - Enable developer mode.
   - Click "Load unpacked extension" and select the project folder.

### Python Scripts
1. Install dependencies:
   ```sh
   python rouletteTest.py
   ```

## Disclaimer
⚠️ **This project is for educational purposes only**. Using bots and automated scripts on online casino sites may violate their terms of service and result in account bans. Additionally, gambling involves a high risk of financial loss.

## License
This project is distributed under the MIT license. See the `LICENSE` file for more details.

---

