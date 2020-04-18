import typing
from functools import reduce

import numpy as np
from gork.structs import RGB, Color


SENSITIVITY = 10
COLORS = [
    Color("#000000", name="Black"),
    Color("#800000", name="Maroon"),
    Color("#008000", name="Green"),
    Color("#808000", name="Olive"),
    Color("#000080", name="Navy"),
    Color("#800080", name="Purple"),
    Color("#008080", name="Teal"),
    Color("#c0c0c0", name="Silver"),
    Color("#808080", name="Grey"),
    Color("#ff0000", name="Red"),
    Color("#00ff00", name="Lime"),
    Color("#ffff00", name="Yellow"),
    Color("#0000ff", name="Blue"),
    Color("#ff00ff", name="Fuchsia"),
    Color("#00ffff", name="Aqua"),
    Color("#ffffff", name="White"),
    Color("#000000", name="Grey0"),
    Color("#00005f", name="NavyBlue"),
    Color("#000087", name="DarkBlue"),
    Color("#0000af", name="Blue3"),
    Color("#0000d7", name="Blue3"),
    Color("#0000ff", name="Blue1"),
    Color("#005f00", name="DarkGreen"),
    Color("#005f5f", name="DeepSkyBlue4"),
    Color("#005f87", name="DeepSkyBlue4"),
    Color("#005faf", name="DeepSkyBlue4"),
    Color("#005fd7", name="DodgerBlue3"),
    Color("#005fff", name="DodgerBlue2"),
    Color("#008700", name="Green4"),
    Color("#00875f", name="SpringGreen4"),
    Color("#008787", name="Turquoise4"),
    Color("#0087af", name="DeepSkyBlue3"),
    Color("#0087d7", name="DeepSkyBlue3"),
    Color("#0087ff", name="DodgerBlue1"),
    Color("#00af00", name="Green3"),
    Color("#00af5f", name="SpringGreen3"),
    Color("#00af87", name="DarkCyan"),
    Color("#00afaf", name="LightSeaGreen"),
    Color("#00afd7", name="DeepSkyBlue2"),
    Color("#00afff", name="DeepSkyBlue1"),
    Color("#00d700", name="Green3"),
    Color("#00d75f", name="SpringGreen3"),
    Color("#00d787", name="SpringGreen2"),
    Color("#00d7af", name="Cyan3"),
    Color("#00d7d7", name="DarkTurquoise"),
    Color("#00d7ff", name="Turquoise2"),
    Color("#00ff00", name="Green1"),
    Color("#00ff5f", name="SpringGreen2"),
    Color("#00ff87", name="SpringGreen1"),
    Color("#00ffaf", name="MediumSpringGreen"),
    Color("#00ffd7", name="Cyan2"),
    Color("#00ffff", name="Cyan1"),
    Color("#5f0000", name="DarkRed"),
    Color("#5f005f", name="DeepPink4"),
    Color("#5f0087", name="Purple4"),
    Color("#5f00af", name="Purple4"),
    Color("#5f00d7", name="Purple3"),
    Color("#5f00ff", name="BlueViolet"),
    Color("#5f5f00", name="Orange4"),
    Color("#5f5f5f", name="Grey37"),
    Color("#5f5f87", name="MediumPurple4"),
    Color("#5f5faf", name="SlateBlue3"),
    Color("#5f5fd7", name="SlateBlue3"),
    Color("#5f5fff", name="RoyalBlue1"),
    Color("#5f8700", name="Chartreuse4"),
    Color("#5f875f", name="DarkSeaGreen4"),
    Color("#5f8787", name="PaleTurquoise4"),
    Color("#5f87af", name="SteelBlue"),
    Color("#5f87d7", name="SteelBlue3"),
    Color("#5f87ff", name="CornflowerBlue"),
    Color("#5faf00", name="Chartreuse3"),
    Color("#5faf5f", name="DarkSeaGreen4"),
    Color("#5faf87", name="CadetBlue"),
    Color("#5fafaf", name="CadetBlue"),
    Color("#5fafd7", name="SkyBlue3"),
    Color("#5fafff", name="SteelBlue1"),
    Color("#5fd700", name="Chartreuse3"),
    Color("#5fd75f", name="PaleGreen3"),
    Color("#5fd787", name="SeaGreen3"),
    Color("#5fd7af", name="Aquamarine3"),
    Color("#5fd7d7", name="MediumTurquoise"),
    Color("#5fd7ff", name="SteelBlue1"),
    Color("#5fff00", name="Chartreuse2"),
    Color("#5fff5f", name="SeaGreen2"),
    Color("#5fff87", name="SeaGreen1"),
    Color("#5fffaf", name="SeaGreen1"),
    Color("#5fffd7", name="Aquamarine1"),
    Color("#5fffff", name="DarkSlateGray2"),
    Color("#870000", name="DarkRed"),
    Color("#87005f", name="DeepPink4"),
    Color("#870087", name="DarkMagenta"),
    Color("#8700af", name="DarkMagenta"),
    Color("#8700d7", name="DarkViolet"),
    Color("#8700ff", name="Purple"),
    Color("#875f00", name="Orange4"),
    Color("#875f5f", name="LightPink4"),
    Color("#875f87", name="Plum4"),
    Color("#875faf", name="MediumPurple3"),
    Color("#875fd7", name="MediumPurple3"),
    Color("#875fff", name="SlateBlue1"),
    Color("#878700", name="Yellow4"),
    Color("#87875f", name="Wheat4"),
    Color("#878787", name="Grey53"),
    Color("#8787af", name="LightSlateGrey"),
    Color("#8787d7", name="MediumPurple"),
    Color("#8787ff", name="LightSlateBlue"),
    Color("#87af00", name="Yellow4"),
    Color("#87af5f", name="DarkOliveGreen3"),
    Color("#87af87", name="DarkSeaGreen"),
    Color("#87afaf", name="LightSkyBlue3"),
    Color("#87afd7", name="LightSkyBlue3"),
    Color("#87afff", name="SkyBlue2"),
    Color("#87d700", name="Chartreuse2"),
    Color("#87d75f", name="DarkOliveGreen3"),
    Color("#87d787", name="PaleGreen3"),
    Color("#87d7af", name="DarkSeaGreen3"),
    Color("#87d7d7", name="DarkSlateGray3"),
    Color("#87d7ff", name="SkyBlue1"),
    Color("#87ff00", name="Chartreuse1"),
    Color("#87ff5f", name="LightGreen"),
    Color("#87ff87", name="LightGreen"),
    Color("#87ffaf", name="PaleGreen1"),
    Color("#87ffd7", name="Aquamarine1"),
    Color("#87ffff", name="DarkSlateGray1"),
    Color("#af0000", name="Red3"),
    Color("#af005f", name="DeepPink4"),
    Color("#af0087", name="MediumVioletRed"),
    Color("#af00af", name="Magenta3"),
    Color("#af00d7", name="DarkViolet"),
    Color("#af00ff", name="Purple"),
    Color("#af5f00", name="DarkOrange3"),
    Color("#af5f5f", name="IndianRed"),
    Color("#af5f87", name="HotPink3"),
    Color("#af5faf", name="MediumOrchid3"),
    Color("#af5fd7", name="MediumOrchid"),
    Color("#af5fff", name="MediumPurple2"),
    Color("#af8700", name="DarkGoldenrod"),
    Color("#af875f", name="LightSalmon3"),
    Color("#af8787", name="RosyBrown"),
    Color("#af87af", name="Grey63"),
    Color("#af87d7", name="MediumPurple2"),
    Color("#af87ff", name="MediumPurple1"),
    Color("#afaf00", name="Gold3"),
    Color("#afaf5f", name="DarkKhaki"),
    Color("#afaf87", name="NavajoWhite3"),
    Color("#afafaf", name="Grey69"),
    Color("#afafd7", name="LightSteelBlue3"),
    Color("#afafff", name="LightSteelBlue"),
    Color("#afd700", name="Yellow3"),
    Color("#afd75f", name="DarkOliveGreen3"),
    Color("#afd787", name="DarkSeaGreen3"),
    Color("#afd7af", name="DarkSeaGreen2"),
    Color("#afd7d7", name="LightCyan3"),
    Color("#afd7ff", name="LightSkyBlue1"),
    Color("#afff00", name="GreenYellow"),
    Color("#afff5f", name="DarkOliveGreen2"),
    Color("#afff87", name="PaleGreen1"),
    Color("#afffaf", name="DarkSeaGreen2"),
    Color("#afffd7", name="DarkSeaGreen1"),
    Color("#afffff", name="PaleTurquoise1"),
    Color("#d70000", name="Red3"),
    Color("#d7005f", name="DeepPink3"),
    Color("#d70087", name="DeepPink3"),
    Color("#d700af", name="Magenta3"),
    Color("#d700d7", name="Magenta3"),
    Color("#d700ff", name="Magenta2"),
    Color("#d75f00", name="DarkOrange3"),
    Color("#d75f5f", name="IndianRed"),
    Color("#d75f87", name="HotPink3"),
    Color("#d75faf", name="HotPink2"),
    Color("#d75fd7", name="Orchid"),
    Color("#d75fff", name="MediumOrchid1"),
    Color("#d78700", name="Orange3"),
    Color("#d7875f", name="LightSalmon3"),
    Color("#d78787", name="LightPink3"),
    Color("#d787af", name="Pink3"),
    Color("#d787d7", name="Plum3"),
    Color("#d787ff", name="Violet"),
    Color("#d7af00", name="Gold3"),
    Color("#d7af5f", name="LightGoldenrod3"),
    Color("#d7af87", name="Tan"),
    Color("#d7afaf", name="MistyRose3"),
    Color("#d7afd7", name="Thistle3"),
    Color("#d7afff", name="Plum2"),
    Color("#d7d700", name="Yellow3"),
    Color("#d7d75f", name="Khaki3"),
    Color("#d7d787", name="LightGoldenrod2"),
    Color("#d7d7af", name="LightYellow3"),
    Color("#d7d7d7", name="Grey84"),
    Color("#d7d7ff", name="LightSteelBlue1"),
    Color("#d7ff00", name="Yellow2"),
    Color("#d7ff5f", name="DarkOliveGreen1"),
    Color("#d7ff87", name="DarkOliveGreen1"),
    Color("#d7ffaf", name="DarkSeaGreen1"),
    Color("#d7ffd7", name="Honeydew2"),
    Color("#d7ffff", name="LightCyan1"),
    Color("#ff0000", name="Red1"),
    Color("#ff005f", name="DeepPink2"),
    Color("#ff0087", name="DeepPink1"),
    Color("#ff00af", name="DeepPink1"),
    Color("#ff00d7", name="Magenta2"),
    Color("#ff00ff", name="Magenta1"),
    Color("#ff5f00", name="OrangeRed1"),
    Color("#ff5f5f", name="IndianRed1"),
    Color("#ff5f87", name="IndianRed1"),
    Color("#ff5faf", name="HotPink"),
    Color("#ff5fd7", name="HotPink"),
    Color("#ff5fff", name="MediumOrchid1"),
    Color("#ff8700", name="DarkOrange"),
    Color("#ff875f", name="Salmon1"),
    Color("#ff8787", name="LightCoral"),
    Color("#ff87af", name="PaleVioletRed1"),
    Color("#ff87d7", name="Orchid2"),
    Color("#ff87ff", name="Orchid1"),
    Color("#ffaf00", name="Orange1"),
    Color("#ffaf5f", name="SandyBrown"),
    Color("#ffaf87", name="LightSalmon1"),
    Color("#ffafaf", name="LightPink1"),
    Color("#ffafd7", name="Pink1"),
    Color("#ffafff", name="Plum1"),
    Color("#ffd700", name="Gold1"),
    Color("#ffd75f", name="LightGoldenrod2"),
    Color("#ffd787", name="LightGoldenrod2"),
    Color("#ffd7af", name="NavajoWhite1"),
    Color("#ffd7d7", name="MistyRose1"),
    Color("#ffd7ff", name="Thistle1"),
    Color("#ffff00", name="Yellow1"),
    Color("#ffff5f", name="LightGoldenrod1"),
    Color("#ffff87", name="Khaki1"),
    Color("#ffffaf", name="Wheat1"),
    Color("#ffffd7", name="Cornsilk1"),
    Color("#ffffff", name="Grey100"),
    Color("#080808", name="Grey3"),
    Color("#121212", name="Grey7"),
    Color("#1c1c1c", name="Grey11"),
    Color("#262626", name="Grey15"),
    Color("#303030", name="Grey19"),
    Color("#3a3a3a", name="Grey23"),
    Color("#444444", name="Grey27"),
    Color("#4e4e4e", name="Grey30"),
    Color("#585858", name="Grey35"),
    Color("#626262", name="Grey39"),
    Color("#6c6c6c", name="Grey42"),
    Color("#767676", name="Grey46"),
    Color("#808080", name="Grey50"),
    Color("#8a8a8a", name="Grey54"),
    Color("#949494", name="Grey58"),
    Color("#9e9e9e", name="Grey62"),
    Color("#a8a8a8", name="Grey66"),
    Color("#b2b2b2", name="Grey70"),
    Color("#bcbcbc", name="Grey74"),
    Color("#c6c6c6", name="Grey78"),
    Color("#d0d0d0", name="Grey82"),
    Color("#dadada", name="Grey85"),
    Color("#e4e4e4", name="Grey89"),
    Color("#eeeeee", name="Grey93"),
]
PALETTE = [c.as_rgb for c in COLORS]


def get_palette() -> np.ndarray:
    palette = np.empty((2 ** 8, 3), dtype=np.int64)
    for index, color in enumerate(PALETTE):
        palette[index] = color[::-1]
    return palette


def get_flat_palette() -> typing.Tuple[int, ...]:
    palette = PALETTE
    for _ in range(256 - len(palette)):
        palette.append((0, 0, 0))
    return reduce(lambda a, b: a + b, palette)


def get_nearest_color(rgb: RGB) -> Color:
    """
    We find the nearest color calculating the Euclidian distance. But here, there's a bit different implementation:
    https://www.compuphase.com/cmetric.htm
    """

    # TODO: need to write a unit test.
    distances = []

    for color in palette:
        mean = (rgb.red + color.red) / 2
        dist_red = rgb.red - color.red
        dist_green = rgb.green - color.green
        dist_blue = rgb.blue - color.blue
        distance = ((512 + mean) * dist_red ** 2 >> 8) ** 2 + 4 * dist_green ** 2 + (767 - mean * dist_blue ** 2) >> 8
        distances.append(distance)

    return palette.index(distances.index(min(distances[0])))
