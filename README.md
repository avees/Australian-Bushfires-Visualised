# Australian Bushfire History Visualisation

Visualises Australian Bushfire History by state. Produces both images for each year and a video.
Currently still in development.

Demo of VIC Bushfire History video:

***************TODO: INSERT PREVIEW OF VIC BUSHFIRE VIDEO HERE************************

## Getting Started

These instructions will allow you to reproduce the generated images and video.

### Prerequisites

The required Python modules and versions have been listed in requirements.txt. You can install
all of the required modules using the following command:

```
pip install -r requirements.txt
```

### Obtaining the datasets

The datasets used were obtained from the Victorian and NSW Government websites.
I haven't included the raw data files due to their size, however you may obtain the data using the links below:

* [VIC Ward Boundaries 2020](https://discover.data.vic.gov.au/dataset/ward-boundaries-2020-polygon-vicmap-admin)
	* Area Type: Whole of State
	* Area: VIC
	* Format: ESRI Shape File
	* Projection: _VICGRID on GDA-2020
* [VIC Fire History](https://discover.data.vic.gov.au/dataset/fire-history-overlay-of-most-recent-fires)
	* Area Type: Whole of State
	* Area: VIC
	* Format: ESRI Shape File
	* Projection: _VICGRID on GDA-2020
* [NSW Local Government Areas](https://data.gov.au/dataset/ds-dga-f6a00643-1842-48cd-9c2f-df23a3a1dc1e/details)
	* Download "NSW LGA POLYGON shp GDA2020.zip(SHP)"
* [NSW Fire History](https://data.nsw.gov.au/data/dataset/fire-history-wildfires-and-prescribed-burns-1e8b6)
	* Select "Download package"
	* Select "Go to resource"

Once all datasets have been downloaded, navigate to the directories containing the shapefile data (i.e. .shp, .shx files).

Place all VIC data (ward boundaries and fire history) files within `/data/VIC/`, and all NSW data files within `/data/NSW/`.




## Authors

* **Aveesha Seneviratne** - *Developer* - [GitHub](https://github.com/avees)
* **Aaron Westbury** - *Co-Developer and provided project idea* - [LinkedIn](https://www.linkedin.com/in/aaron-westbury-709889189/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* VIC Government - Providing VIC Ward Boundaries and Fire History data
* NSW Government - Providing NSW Local Government Areas and Fire History data
