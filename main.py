from ColorHunt import ColorHunt
from FlatUIColors import FlatUIColors

if __name__ == '__main__':

    colorHunt = ColorHunt()
    colorHunt.get_all_palettes()
    colorHunt.print_stats()
    colorHunt.save_to_csv()

    # flatUI = FlatUIColors()
    # flatUI.get_all_palettes()
    # flatUI.save_to_csv()



