from ColorHunt import ColorHunt
from FlatUIColors import FlatUIColors

if __name__ == '__main__':

    # Scrape  colorhunt.co
    colorHunt = ColorHunt()
    colorHunt.get_all_palettes()
    colorHunt.print_stats()
    colorHunt.save_to_csv()

    # Scrape flatuicolors.com
    flatUI = FlatUIColors()
    flatUI.get_all_palettes()
    flatUI.save_to_csv()