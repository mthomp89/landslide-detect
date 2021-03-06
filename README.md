![Banner](https://github.com/mthomp89/landslide-detect/blob/main/banner.png)

# Mapping Landslide Activity in SAR Imagery
> Purpose of this project is to evaluate the effectiveness of Synthetic Aperture Radar in mapping surface damage caused by landslides in reported locations. We also intend for this project to help enhance the understanding of detecting, measuring, and visualizing landslide locations on a large scale. 


## Table of Contents
* [General Info](#general-information)
* [Data Sources](#data-sources)
* [Example Data](#example-data)
* [Workflow](#workflow)
* [Installation](#installation)
* [Running the Workflow](#running-the-workflow)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#project-contacts)
* [Citations](#citations)
* [License](#license)


## General Information
- This project is built upon a previously developed low-accuracy large spatial scale landslide database. Space-based SAR imagery will be utilized in order to improve the accuracy of landslide detection. This is a capstone project in the University of Colorado-Boulder Earth Analytics certifcation program. 
- Predicting  landslides is challenging  due to the many variables that should be considered when trying to identify what triggered a landslide. There is a need to better identify landslide locations across a large spatial scale. Can combining a low-accuracy large spatial scale landslide database with SAR imagery  improve the accuracy of landslide detection across a global scale?
- Utilize human-assisted, programmatic, and possibly machine learning methods to identify landslides from satellite imagery. We hope that this will bridge the gap with landslide event detection and future event prediction. 


## Data Sources
- [NASA Global Landslide Catalog (GLC)]
      Link: https://data.nasa.gov/Earth-Science/Global-Landslide-Catalog/h9d8-neg4
      Info: The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources. 
      Type: Geospatial data can be downloaded as: KLM, KMZ, Shapefile or GeoJSON
- [Sentinel-1 SAR]
      Link: https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar
      Info: SENTINEL-1 is an imaging radar mission providing continuous all-weather, day-and-night imagery at C-band.
      Type: The SENTINEL-SAFE format wraps a folder containing image data in a binary data format and product metadata in XML. 


## Example Data
![Nasa Global Landslide Catalog (NGLC) - North America](https://github.com/mthomp89/landslide-detect/blob/main/doc/nglc_n_america.png)
![Detecting changes in Sentinel-1 imagery](https://github.com/mthomp89/landslide-detect/blob/main/doc/change_detect.png)
![Here are our 230 Verified Landslide Locations](https://github.com/mthomp89/landslide-detect/blob/main/doc/VerifiedLocations.png)


## Workflow
![Workflow](https://github.com/mthomp89/landslide-detect/blob/main/doc/workflow.png)

## Installation 
Installation and usage of this repository requires an account on Google Earth Engine in order to access the Sentinel-1 data. As of 25 April, area of interests (AOIs) are ingested into the workflow through a ```json.load()``` function. The json files are located within the ./inputs path. The virtual environment is best constructed within an Anaconda Powershell prompt. To initiate the envrionment after forking the repository, open an Anaconda Powershell prompt, change the local directory path to the ./env path, then execute the command: "conda env create -f environment.yml"
- Project requirements/dependencies: ![environment.yml](https://github.com/mthomp89/landslide-detect/blob/main/env/environment.yml)
- Google Earth Engine account access

## Running the Workflow
Begin by opening an Anaconda Powershell or similiar python command prompt on your computer. Activate the ![earth-analytics environment](https://github.com/mthomp89/landslide-detect/blob/main/env/environment.yml) by typing ```conda activate earth-analytics```. Once activated, open a Jupyter notebook in the IDE of your choice (e.g., VSCode, Spyder, or PyCharm). Conversely, you can type ```jupyter notebook``` at the Powershell prompt. This will open jupyter notebook in a browser tab. Navigate to the ![Mitchell_Manak_Landslide_Detecting_Changes.ipynb](https://github.com/mthomp89/landslide-detect/blob/main/Mitchell_Manak_Landslide_Detecting_Changes.ipynb) file located at the root directory of this repository. Run the notebook by selecting earth-analytics Kernel from the menu bar and then Restart & Run All. The notebook is formatted to inform the reader of processes within each code block as well as the overall current status of the project.

## Future Work
- Continue to investigate Google Earth Engine more and make sure we are leveraging all of their tools the best way that we can. 
- Iterate over a provided database or spreadsheet file.
- Look into cross referencing with higher resolution SAR imagery offerred by commercial imaging companies such as ICEYE, Airbus, or Capella Space.

## Acknowledgements
- This project was inspired by Dr. Elsa Culler, CU Boulder Earth Lab
- This project was based on:
    - [A multi-sensor evaluation of precipitation uncertainty for landslide-triggering storm events](https://onlinelibrary.wiley.com/doi/full/10.1002/hyp.14260)
    - [Assessment of Sentinel-1 and Sentinel-2 Data for Landslides Identification using Google Earth Engine](https://ieeexplore.ieee.org/abstract/document/9688356)
    - [Sentinel-1 SAR Amplitude Imagery for Rapid Landslide Detection](https://www.mdpi.com/2072-4292/11/7/760)
    - [Alaska Satellite Facility SAR Basics Tutorial](https://step.esa.int/docs/tutorials/S1TBX%20SAR%20Basics%20Tutorial.pdf) 
    - [This tutorial on detecting changes in Sentinel-1 imagery](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-1)
    - [A collection of 360+ Jupyter Python notebook examples for using Google Earth Engine with interactive mapping](https://github.com/giswqs/earthengine-py-notebooks)


## Project Contacts
- [@Leah Manak](mailto:leah.manak@gmail.com)
- [@Mitch Thompson](mailto:mitchell.thompson-1@colorado.edu)
- [@Elsa Culler](mailto:eculler@gmail.com)

## Citations
- Our Github is currently private and we intend to keep it private until the end of the summer course. We will be linking Zenodo with our Git Hub repository to ensure that our code is visible and citable! 

## License
This project is open source and available under the [Apache License 2.0](https://github.com/mthomp89/landslide-detect/blob/main/LICENSE).
