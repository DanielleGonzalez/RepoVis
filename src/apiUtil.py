import requests
import sys
import os

'''
apiUtil
Author: Danielle Gonzalez dng2551@rit.edu

This file contains the actual code to retrieve the metadata from the API

'''

'''
getContributors 

This code also counts anonymous contributors, due to the following statement from the API documentation:
"This API attempts to group contribution counts by GitHub user, across all of their associated email addresses. 
For performance reasons, only the first 500 author email addresses in the repository will be linked to GitHub users. 
The rest will appear as anonymous contributors without associated GitHub user information."
'''

# contributors API doc: https://developer.github.com/v3/repos/#list-contributors
def getContributors(user, pw, repoURL):

	# API returns paginated results!
	pageNum = 1
	contributors = []

	while True:
		
		contribURL = repoURL + "/contributors"
		params = {'page': pageNum, 'per_page': 100, 'anon': 1}

		apiResponse = requests.get(contribURL, auth=(user,pw), params=params)
		statusCode = int(apiResponse.headers['Status'].split()[0])
		
		# 200 is OK
		if statusCode == 200:
			contribObject = apiResponse.json() #get the data
			
			#stops when no more pages 
			if len(contribObject) < 1:
				break

			# add each contributor to a new object
			for person in contribObject:
				contributors.append(person)

		# increment the page 
		pageNum += 1
		
			
	#reference information
	print("API Request Rate Limit Remaining: " + str(apiResponse.headers['X-RateLimit-Remaining']) + "/5000")
	print("There are " + str(len(contributors)) + " contributors")
	#return the object
	return contributors 

#pull requests API doc: https://developer.github.com/v3/pulls/
def getPullRequests(user, pw, repoURL):
	# API returns paginated results!
	pageNum = 1
	pullrequests = []

	while True:
		
		pullrequestURL = repoURL + "/pulls"
		params = {'page': pageNum, 'per_page': 100, 'state': 'all'}

		apiResponse = requests.get(pullrequestURL, auth=(user,pw), params=params)
		statusCode = int(apiResponse.headers['Status'].split()[0])
		
		# 200 is OK
		if statusCode == 200:
			pullRequestObject = apiResponse.json() #get the data
			
			#stops when no more pages 
			if len(pullRequestObject) < 1:
				break

			# add each pull request to a new object
			'''
			Pull Request objects have nested attributes so I am adding them to the final object manually
			Totally Excluded:  __links, head, base, milestone, & assignee nested attributes 
			Select Attributes Included: user (login & html_url)
			If you want the excluded information please modify this to your needs
			'''
			for pr in pullRequestObject:
				pr_dict = {}
				pr_dict['locked'] = pr['locked']
				pr_dict['merge_commit_sha'] = pr['merge_commit_sha']
				pr_dict['created_at'] = pr['created_at']
				pr_dict['review_comments_url'] = pr['review_comments_url']
				pr_dict['merged_at'] = pr['merged_at']
				pr_dict['commits_url'] = pr['commits_url']
				pr_dict['url'] = pr['url']
				pr_dict['state'] = pr['state']
				pr_dict['diff_url'] = pr['diff_url']
				pr_dict['html_url'] = pr['html_url']
				pr_dict['comments_url'] = pr['comments_url']
				pr_dict['number'] = pr['number']
				pr_dict['title'] = pr['title'].replace(",", "") #because I am using csv commas in titles cause issues
				pr_dict['statuses_url'] = pr['statuses_url']
				pr_dict['patch_url'] = pr['patch_url']
				pr_dict['issue_url'] = pr['issue_url']
				pr_dict['review_comment_url'] = pr['review_comment_url']
				pr_dict['closed_at'] = pr['closed_at']
				pr_dict['user_login'] = pr['user']['login']
				pr_dict['user_htmlURL'] = pr['user']['html_url']
				pullrequests.append(pr_dict)

		# increment the page 
		pageNum += 1	

	#reference information
	print("API Request Rate Limit Remaining: " + str(apiResponse.headers['X-RateLimit-Remaining']) + "/5000")
	print("There are " + str(len(pullrequests)) + " pull requests")
	#return the object
	return pullrequests 

# issues API doc: https://developer.github.com/v3/issues/
def getIssues(user, pw, repoURL):
	print("temp")

# releases API doc: https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository	
def getReleases(user, pw, repoURL):
	print("temp")
	