import requests
import sys
import codecs
import os
import apiUtil

'''
getRepoMetadata
Author: Danielle Gonzalez dng2551@rit.edu

This program collects metadata for a project by calling the Github API

PROGRAM INPUT:
	your Github USERNAME
	your Gihub PASSWORD (Please note, there is no persistent storage of credentials!)
	the OWNER of the github repository
	the NAME of the github repository
	Example: python getRepoMetadata userName passWord golang go

The program is designed to work with any project, as well as to be extensible to include
other desired metadata

Current Metadata Collected (On Repository-Level):
1. Releases
2. Issues
3. Pull Requests
4. Contributors


PROGRAM OUTPUT:
	One CSV file for each type of metadata
	Each row is one entry returned by the API
	For example, each row of issueOutput is data for one issue in the repository
'''


def writeDataToFile(data, outputPath):
	outFile = open(outputPath, "a", encoding="utf-8")
	firstItem = data[0]
	try:
		#create the header with the attribute names
		for attrib in firstItem:
			print((str(attrib)))
			outFile.write(str(attrib) + ",")
		outFile.write('\n')
		# # Add data to the CSV
		for result in data:
			for attribute in result:
				outFile.write(str(result[attribute]) + ",")
			outFile.write("\n")
	except Exception as exc:
	        print('Generated an exception during output: ' + str(exc))
	outFile.close()

	print("Data has been added to " + str(outputPath))


def main():
	if(len(sys.argv) < 5):
		print("Please include the following arguments, in this order:")
		print("Github Username, Github Password, Repository Owner, Repository Name")
	else:
		# collect input arguments 
		userName = sys.argv[1]
		pw = sys.argv[2]
		repoOwner = sys.argv[3]
		repoName = sys.argv[4]
		repoURL = "https://api.github.com/repos/" + repoOwner + "/" + repoName
		
		'''
		Create output .csv files in the \data folder of the project.
		Each metadata has its own file. 
		'''

		#contributorOutput = "../data/" + str(repoName) + "-contributors.csv"
		#pullRequestOutput = "../data/" + str(repoName) + "-pullrequests.csv"
		#issueOutput = "../data/" + str(repoName) + "-issues.csv"
		#releasesOutput = "../data/" + str(repoName) + "-releases.csv"

		# get the requested data from the Github API and then write it to the data file

		# contributorData = apiUtil.getContributors(userName, pw, repoURL)
		# writeDataToFile(contributorData, contributorOutput)
		
		#pullRequestData = apiUtil.getPullRequests(userName, pw, repoURL)
		#writeDataToFile(pullRequestData, pullRequestOutput)
		
		issueData = apiUtil.getIssues(userName, pw, repoURL)
		writeDataToFile(issueData, issueOutput)
		
		# releasesData = apiUtil.getReleases(userName, pw, repoURL)
		# writeDataToFile(releasesData, releasesOutput)
main()