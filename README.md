# RepoVis
This project provides python scripts to automatically collect metadata for a project using the Github API. Additionally, templates for developing visualizations using Google Charts are provided. The aim of this project is to develop a set of visualizations which can show changes in the project-level metadata of a large-scale open source project cross all releases. 
Five metadata are collected. Each one provides an important insight into the state of the project:
1. Contributors
2. Pull Requests
3. Issues
4. Releases

# Usage - Data Collection
To use the script, call 
`python getRepoMetadata (github username) (github password) (repo owner) (repo name)`
example:
 `python getRepoMetadata DanielleGonzalez myPass atom atom`
 
 ! Note: no persistent storage of credentials, don't worry :-)

The code is designed to be extensible, meaning other endpoints (such as commits) from the API could be added to include more data.

Please refer to the API documents for the schemas (or existing data - the headers are the attributes). For my purposes I excluded some data that was returned from the final output, so see what I've included and the adjust to your needs. 

# Data Collection Output

Data is set to output to a data folder outside the src folder. If you download the project it will just work. 
Data I've already collected I manually added to subfolders. If you run it with a new project, it will appear in /data but not in a subfolder.

The data format is csv (comma separated values)

# Usage - Visualization

:sparkles:Coming Soon!:sparkles:
