# DISCLAIMER: This Project was created for educational purposes ONLY.

RESTful/wrapper APIs. Used the FBI Crime Data Explorer API. 

# Crime Data Explorer FBI Website Back-End

![Desktop Demo](https://raw.githubusercontent.com/mboladop/Interactive-project-stream2-FBI-restfulAPI/master/stream2.gif "Desktop Demo")

## Overview
 
### What is this website for?
 
This is a back-end restful-wrapper API created to meet the new CORS requirements of the FBI API.
It specifically designed to access real time Data provided by the public FBI API.
 
### What does it do?
 
This website makes a call from the Back-End to the public FBI API. Also its has its own CORS which are in this case deleted to be able to call it as a mid way step from the Front-End part of this project that you can find [HERE](https://mboladop.github.io/Interactive-project-stream2/).

### How does it work
 
This website uses **Python** and **Flask** to route viewers through the site. The data was originally being called from the front-end using **Javascript** and **JQuery** code. Mid-way through the project the FBI API changed not only creating a unic API key for each user (provided at request) but also restructuring the data provided, including more and better parameters for the searchs. This changes also included the use of CORS, (Cross-Origin Resource Sharing) that avoided the calls from the front end. This made necessary the creation of a specific back end (restful-wrapper API) to meet the new requirements.

## Technologies Used
- **Python3**
  - Base language used to create Back-End.
- Used **Flask** as the framework for Python.

## Testing
- All code used on the site has been tested to ensure everything is working as expected.
- Used several URL extensions to make sure the data for the different crimes (offenders and victims) displayed correctly and in a JSON format.

## Deployment
1. Navigate to the repository where you're setting up your deployments.
2. Under your repository name, click Settings.
3. Go to GitHub Pages section.
4. Click and choose master branch.
5. Click save.

## Contributing
 
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command.
2. After you've done that you'll need to make sure that you have **npm** installed. Link [npm package serve](https://www.npmjs.com/package/serve)
3. The project will now run locally.
4. Make changes to the code and if you think it belongs in here then just submit a pull request.

## Credits

### Information
- The information used to create this site was from a number of sources
    - The FBI API used to extract the data charted was obtained from: [Crime Data Explorer](https://crime-data-explorer.fr.cloud.gov)
    
## Demo Gifs and Link to project complete with FE:

[Link to project](https://mboladop.github.io/Interactive-project-stream2/)
