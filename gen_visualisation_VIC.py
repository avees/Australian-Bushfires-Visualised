import geopandas as gpd
import matplotlib.pylab as pylab
from moviepy.editor import *


# Generate and store images of all historic bushfires
def generate_images():
    # Create output directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    output_dir = r'images\VIC_bushfire_images'
    new_path = r'{}\{}'.format(dir_path, output_dir)
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    # Read in VIC fire history shapefile
    shapefile = gpd.GeoDataFrame.from_file("data/VIC/fire_history.shp")

    # Specify start and end years of dataset
    start_year = 1950
    end_year = 2020

    # Read in map of Victorian city councils/wards
    df_map = gpd.read_file("data/VIC/ward_2020.shp")

    # Plot data and save images
    for i in range(start_year, end_year + 1):
        # TODO: Fix legend to use static colours
        ax = df_map.plot(figsize=(24, 18), cmap='Pastel2', edgecolor='black')

        pylab.rcParams['figure.figsize'] = 24, 18
        data = shapefile.query("(FIRETYPE == 'BUSHFIRE' | FIRETYPE == 'BURN') & SEASON == {}".format(i))
        plot = data.plot(column='FIRETYPE', cmap='jet', ax=ax, legend=True)
        plot.axis([141, 150, -39, -34])

        fig = plot.get_figure()
        fig.suptitle("VIC Bushfire Season: {}".format(i), fontsize=30)
        fig.savefig("{}/{}.png".format(output_dir, i), bbox_inches='tight', pad_inches=0.1, metadata=None)
        print("Saved: {}".format(i))

    return output_dir


# Use generated images to create a visualisation in video form
def generate_video(images_dir):
    base_dir = os.path.realpath(".")
    images_dir = base_dir + '\\' + images_dir + '\\'
    images = sorted(os.listdir(images_dir))

    clips = []
    for filename in images:
        if filename.endswith(".png"):
            clips.append(ImageClip(images_dir + filename).set_duration(1))

    video = concatenate(clips, method="compose")
    video.write_videofile('VIC_bushfires.mp4', fps=3)


def main():
    images_dir = generate_images()
    generate_video(images_dir)


if __name__ == "__main__":
    main()
