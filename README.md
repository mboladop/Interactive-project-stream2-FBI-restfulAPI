# DISCLAIMER: This Project was created for educational purposes ONLY.

RESTful/wrapper APIs. Used the FBI Crime Data Explorer API. 

![Desktop Demo](https://raw.githubusercontent.com/mboladop/Interactive-project-stream2-FBI-restfulAPI/master/stream2.gif "Desktop Demo")

# Crime Data Explorer FBI Website Back-End
 
## Overview
 
### What is this website for?
 
This is a back-end restful-wrapper API created to meet the new CORS requirements of the FBI API.
It specifically designed to access real time Data provided by the public FBI API.
 
### What does it do?
 
This website makes a call from the Back-End to the public FBI API. Also its has its own CORS which are in this case deleted to be able to call it as a mid way step from the Front-End part of this project that you can find [HERE](https://mboladop.github.io/Interactive-project-stream2/).

### How does it work
 
This website uses **Python** and **Flask** to route viewers through the site. The data was originally being called from the front-end using **Javascript** and **JQuery** code. Mid-way through the project the FBI API changed not only creating a unic API key for each user (provided at request) but also restructuring the data provided, including more and better parameters for the searchs. This changes also included the use of CORS, (Cross-Origin Resource Sharing) that avoided the calls from the front end. This made necessary the creation of a specific back end (restful-wrapper API) to meet the new requirements.

## Features
 
### Existing Features
- Eye catching graphs.
- Easy UX search form approach.
- Minimal simple Landing.
- Scrollable acces to navigate through the data the charts and graphs are based on.
- Links page to FBI API site which simplifies the access to the source.

## Tech Used

### Some the tech used includes:
- **Python3**
  - Base language used to create Back-End.
- Used **Flask** as the framework for Python.

## Testing
- All code used on the site has been tested to ensure everything is working as expected.
- Used several URL extensions 


## Contributing
 
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. The project will now run on [localhost](http://127.0.0.1:8080)
3. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

### Media
- The FBI logo used in this site was obtained from: [](https:#)
- The chart display design inspiration was taken from: [Code Institute](https://www.codeinstitute.net/student-projects/)

### Information
- The information used to create this site was from a number of sources
    - The FBI API used to extract the data charted was obtained from: [Crime Data Explorer](https://crime-data-explorer.fr.cloud.gov/api)
    
## Demo Gifs and Link to project:

[Link to project](https://mboladop.github.io/Interactive-project-stream2/)

gifs