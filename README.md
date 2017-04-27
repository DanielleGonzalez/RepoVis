# RepoVis
The aim of this project is to develop a set of visualizations which can show changes in the project-level metadata of a large-scale open source project cross all releases. 
Three metadata were selected for to visualize. Each one provides an important insight into the state of the project:
1. Contributors: measuring how many people are adding to the project. This value can indicate popularity and development capabilities of the project. Sub-metadata can alson be retrieved such as how many commits, issues or pull requests were made by a specific contributor.
2. Pull Requests: pull requests are used to submit potential changes to the code base. These can be either accepted and merged or rejected. This metric can show how much “work” is being done on the project. In open source, when a contributor wishes to add their changes or completed tasks to the main codebase, they submit a pull-request, which is then peer-reviewed.
3. Issues: Issues are submitted by both developers and users and contain labels that can distinguish between bug reports, feature requests, and tasks that contributors request help with. This can indicate productivity (feature request/task issues being opened and closed) as well as providing a measure of how many bugs the project has.
# Methodology
The steps towards achieving these goals are as follows:
1. Develop a script using Python that leverages the Github API to extract the above metadata for each release of the selected project.
2. Python scripts will also be developed to process the data for each release into a suitable format for using visualization tools, such as a csv file.
3. The visualization tool Google Charts will be used to construct visualizations of the changes in the selected metrics. Visual representations will be divided into two categories: Over Time and Individual Releases.
  a.   Over Time visualizations will track the metrics across all 181 releases of the project.
  b. Individual Release visualizations will provide a ‘snapshot’ or quick report of the metrics for each release.

The current plan is to incorporate trend lines, scatter plots, and bar charts. However, once the data is collected, experimentation with other visualizations may lead to more interesting findings and also be included.

# Case Study
The Go Programming Language (<https://github.com/golang/go>) will be used as a case study for this approach. This project was chosen because it is a well-known, highly used project with 778 contributors, 32,012 commits, and 181 releases.

