import requests
import sys
import codecs
import os

def main():
	if(len(sys.argv) < 4):
		print("Please include the following arguments, in this order:")
		print("API URL of Gihub Repository, Github Username, Github Password")
	else:

		'''
		API documentation for metadata 
		releases: https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository
		contributors: https://developer.github.com/v3/repos/#list-contributors
		pull requests: https://developer.github.com/v3/pulls/
		issues: https://developer.github.com/v3/issues/
		'''

		# collect input arguments 
		username = sys.argv[1]
		pw = sys.argv[2]
		project = sys.argv[3]

		'''
		Create output .csv files in the \data folder of the project.
		Each metadata has its own file, and each row is an entry. 
		For example, each row of issueOutput is data for one issue in the repository
		'''

	    contributorOutput = "../data/contributors.csv"
	    pullRequestOutput = "../data/pullrequests.csv"
	    issueOutput = "../data/issues.csv"
	    releasesOutput = "../data/releases.csv"

	    # contributorOutput = codecs.open(output, "w", "utf-8")
	    # contributorOutput.write("Pattern,Project,File\n")
	    # contributorOutput.close()
main()