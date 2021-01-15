import geopandas as gpd
import matplotlib.pylab as pylab
from moviepy.editor import *


# TODO: Fix legend to be static
def generate_images():
    # Create output directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    output_dir = r'images\NSW_bushfire_images'
    new_path = r'{}\{}'.format(dir_path, output_dir)
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    # Read in NSW fire history shapefile
    shapefile = gpd.GeoDataFrame.from_file("data/NSW/NPWSFireHistory_17122020.shp")

    # Reformat data to separate year and fire type data
    shapefile[['YEAR', 'FIRETYPE']] = shapefile['Label'].str.split(' ', 1, expand=True)
    shapefile['YEAR'] = shapefile['YEAR'].str[:4]

    # Specify start and end years of dataset
    start_year = 1961
    end_year = 2019

    # Read in map of NSW city councils
    df_map = gpd.read_file("data/NSW/NSW_LGA_POLYGON_GDA2020.shp")

    # Plot data and save images
    for i in range(start_year, end_year + 1):
        ax = df_map.plot(figsize=(24, 18), cmap='Pastel2', edgecolor='black')

        pylab.rcParams['figure.figsize'] = 24, 18
        data = shapefile.query("(FIRETYPE == 'Wildfire' | FIRETYPE == 'Prescribed Burn') & YEAR == '{}'".format(i))
        plot = data.plot(column='FIRETYPE', cmap='jet', ax=ax, legend=True)
        plot.axis([141, 154, -37.5, -28])

        fig = plot.get_figure()
        fig.suptitle("Bushfire Season: {}".format(i + 1), fontsize=30)
        fig.savefig("{}/{}.png".format(output_dir, i + 1), bbox_inches='tight', pad_inches=0.1, metadata=None)
        print("Saved: {}".format(i + 1))

    return output_dir


def generate_video(images_dir):
    base_dir = os.path.realpath(".")
    images_dir = base_dir + '\\' + images_dir + '\\'
    images = sorted(os.listdir(images_dir))

    clips = []
    for filename in images:
        if filename.endswith(".png"):
            clips.append(ImageClip(images_dir + filename).set_duration(1))

    video = concatenate(clips, method="compose")
    video.write_videofile('NSW_bushfires.mp4', fps=3)


def main():
    images_dir = generate_images()
    generate_video(images_dir)


if __name__ == "__main__":
    main()
