# RepoVis
This project provides python scripts to automatically collect and process metadata for a project using the Github API. Additionally, templates for developing visualizations using Google Charts are provided. The aim of this project is to develop a set of visualizations which can show changes in the project-level metadata of a large-scale open source project cross all releases. 
Four metadata are collected. Each one provides an important insight into the state of the project:
1. Contributors
2. Pull Requests
3. Issues
4. Releases

# Usage - Data Collection

**Step 1: Collect the Data from Github**
The first step is to scrape the repository metadata (listed above) using the Github API
To use the script, call 
`python getRepoMetadata (github username) (github password) (repo owner) (repo name)`
example:
 `python getRepoMetadata DanielleGonzalez myPass atom atom`
 
 ! Note: no persistent storage of credentials, don't worry :-)

The code is designed to be extensible, meaning other endpoints (such as commits) from the API could be added to include more data.

Please refer to the API documents for the schemas (or existing data - the headers are the attributes). For my purposes I excluded some data that was returned from the final output, so see what I've included and the adjust to your needs. 

**Step 2: Process the Data for Visualization by Release**
Next, the data is processed to be counted and categorized by release
To use the script, call

`python makeReleasesCSVs (repo name) (path to data)`

The "path to data" parameter specifies where the originally crawled data is located on your machine. By default, all data from getRepoMetadata goes to a /data directory, but you still have to specify this for this script. Use the path *relative* to this script.

# Data Collection Output
Data is set to output to a /data folder outside the /src folder.  
Data I've already collected I manually added to subfolders. If you run it with a new project, it will appear in /data but not in a subfolder.

The data format is csv (comma separated values)

the getRepoMetadata script releases one CSV per metadata, and the makeReleaseCSVs creates 1 csv file for each metadata, plus one "master" file with all metadata counts. 

# Usage - Visualization

:sparkles:Coming Soon!:sparkles:
