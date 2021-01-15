# Australian Bushfire History Visualisation

Visualises Australian Bushfire History by state. Produces both images for each year and a video.
Currently still in development.

Demo of NSW Bushfire History video:

[![NSW Bushfire History Visualisation](https://j.gifs.com/oV3PQz.gif)](https://www.youtube.com/watch?v=cyI8xhLx5VE)

## Getting Started

These instructions will allow you to reproduce the generated images and video.


### Prerequisites

The required Python modules and versions have been listed in requirements.txt. You can install
all the required modules using the following command:

```
pip install -r requirements.txt
```

### Obtaining the datasets

The datasets used were obtained from the Victorian and NSW Government websites.
I haven't included the raw data files due to their size, however you may obtain the data using the links below:

* [VIC Ward Boundaries 2020](https://discover.data.vic.gov.au/dataset/ward-boundaries-2020-polygon-vicmap-admin)
	* Area Type: Whole of State
	* Area: VIC
	* Buffer Distance: +1km
	* Format: ESRI Shape File
	* Projection: Geographicals on GDA-94
* [VIC Fire History](https://discover.data.vic.gov.au/dataset/fire-history-overlay-of-most-recent-fires)
	* Area Type: Whole of State
	* Area: VIC
	* Buffer Distance: +1km
	* Format: ESRI Shape File
	* Projection: Geographicals on GDA-94
* [NSW Local Government Areas](https://data.gov.au/dataset/ds-dga-f6a00643-1842-48cd-9c2f-df23a3a1dc1e/details)
	* Download "NSW LGA POLYGON shp GDA2020.zip(SHP)"
* [NSW Fire History](https://data.nsw.gov.au/data/dataset/fire-history-wildfires-and-prescribed-burns-1e8b6)
	* Select "Download package"
	* Select "Go to resource"

Once all datasets have been downloaded, navigate to the directories containing the shapefile data (i.e. .shp, .shx files).

Place all VIC data (ward boundaries and fire history) files within `/data/VIC/`, and all NSW data files within `/data/NSW/`.


## Producing Visualisations

After obtaining the datasets and placing them in the specified directories, simply execute the script for the desired state.
E.g. Run `gen_visualisation_VIC.py` to produce a visualisation of VIC Bushfire History in a video format, as well as the
utilised images within `/images/VIC_bushfire_images`.


## Authors

* **Aveesha Seneviratne** - *Developer* - [GitHub](https://github.com/avees)
* **Aaron Westbury** - *Co-Developer and Project Idea Originator* - [LinkedIn](https://www.linkedin.com/in/aaron-westbury-709889189/)


## License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.


## Acknowledgments

* VIC Government - Providing VIC Ward Boundaries and Fire History data
* NSW Government - Providing NSW Fire History data
* Australian Government - Providing NSW Local Government Areas data
