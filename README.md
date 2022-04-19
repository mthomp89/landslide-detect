![Banner](https://github.com/mthomp89/landslide-detect/blob/main/banner.png)

# Mapping Landslide Activity in SAR Imagery
> Purpose of this project is to evaluate the effectiveness of Synthetic Aperture Radar in mapping surface damage caused by landslides in reported locations. 


## Table of Contents
* [General Info](#general-information)
* [Data Sources](#data-sources)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#project-contacts)
* [License](#license)


## General Information
- This project is built upon a previously developed low-accuracy large spatial scale landslide database. Space-based SAR imagery will be utilized in order to improve the accuracy of landslide detection. This is a capstone project in the University of Colorado-Boulder Earth Analytics certifcation program. 
- Predicting  landslides is challenging  due to the many variables that should be considered when trying to identify what triggered a landslide. There is a need to better identify landslide locations across a large spatial scale. Can combining a low-accuracy large spatial scale landslide database with SAR imagery  improve the accuracy of landslide detection across a global scale?
- utilize human-assisted, programmatic, and possibly machine learning methods to identify landslides from satellite imagery. We hope that this will bridge the gap with landslide event detection and future event prediction. 


## Data Sources
- [NASA Global Landslide Catalog (GLC)](https://data.nasa.gov/Earth-Science/Global-Landslide-Catalog/h9d8-neg4)
- [Sentinel-1 SAR](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar)
- [Capella Space Open Data Program](https://www.capellaspace.com/)
- [ICEYE Open Data Program](https://www.iceye.com/)


## Screenshots
![Nasa Global Landslide Catalog (NGLC) - North America](https://github.com/mthomp89/landslide-detect/blob/main/doc/nglc_n_america.png)
![Detecting changes in Sentinel-1 imagery](https://github.com/mthomp89/landslide-detect/blob/main/doc/change_detect.png)
![Here are 4 out of our 230 Verified Landslide Locations](https://github.com/mthomp89/landslide-detect/blob/main/doc/4_locations.png)


## Setup
- Project requirements/dependencies: <!-- insert environment.yml -->
- QGIS software
- Google Earth Engine account access
- NGLC database access

## Project Status and workflow
Project is: _in progress_  

- Each week we meet on Tuesday to discuss progress on the project.
- We have currently worked on a Google Colab Document but are moving our code to Jupyter notebook to have access Version Control on Git Hub.
- We will be continuing a weekly-meeting setup throughout the sememster and into the summer.  

## Room for improvement
- We can be better about communicating where we are at with our project with eachother, but version control will help with this. 

## To Do:
- Get our code to work for major verified landslide sites.
- Continue to clean our code up to make it as reproducible as possible. 
- Discuss summer session plans

## Acknowledgements
- This project was inspired by Dr. Elsa Culler, CU Boulder Earth Lab
- This project was based on:
    - [A multi-sensor evaluation of precipitation uncertainty for landslide-triggering storm events](https://onlinelibrary.wiley.com/doi/full/10.1002/hyp.14260)
    - [Assessment of Sentinel-1 and Sentinel-2 Data for Landslides Identification using Google Earth Engine](https://ieeexplore.ieee.org/abstract/document/9688356)
    - [Sentinel-1 SAR Amplitude Imagery for Rapid Landslide Detection](https://www.mdpi.com/2072-4292/11/7/760)
    - [Alaska Satellite Facility SAR Basics Tutorial](https://step.esa.int/docs/tutorials/S1TBX%20SAR%20Basics%20Tutorial.pdf) 
    - [This tutorial on detecting changes in Sentinel-1 imagery](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-1)


## Project Contacts
- [@Leah Manak](mailto:leah.manak@gmail.com)
- [@Mitch Thompson](mailto:mitchell.thompson-1@colorado.edu)
- [@Elsa Culler](mailto:eculler@gmail.com)


## License
This project is open source and available under the [Apache License 2.0](https://github.com/mthomp89/landslide-detect/blob/main/LICENSE).
