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
	print("Collecting Contributors for Project...")
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
	print("Collecting Pull Requests for Project...")
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
			Totally Excluded:  __links, head, base, & assignee nested attributes 
			Select Attributes Included: user (login & html_url), milestone (html_url, number)
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
				if pr['milestone'] != None:
					pr_dict['milestone_htmlURL'] = pr['milestone']['html_url']
					pr_dict['milestone_id'] = pr['milestone']['id']
				else:
					pr_dict['milestone_htmlURL'] = None
					pr_dict['milestone_id'] = None
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
	print("Collecting Issues for Project...")
	# API returns paginated results!
	pageNum = 1
	issues = []

	while True:
		
		issuesURL = repoURL + "/issues"
		params = {'page': pageNum, 'per_page': 100, 'milestone': '*', 'state':'all'}

		apiResponse = requests.get(issuesURL, auth=(user,pw), params=params)
		statusCode = int(apiResponse.headers['Status'].split()[0])
		
		# 200 is OK
		if statusCode == 200:
			issuesObject = apiResponse.json() #get the data
			
			#stops when no more pages 
			if len(issuesObject) < 1:
				break
			'''
			Issue objects have nested attributes so I am adding them to the final object manually
			Totally Excluded:  __links, head, base & assignee nested attributes 
			Select Attributes Included: user (login & html_url), milestone (html_url, number), labels(labelnames)
			If you want the excluded information please modify this to your needs
			'''

			for issue in issuesObject:
				issue_dict = {}
				issue_dict['id'] = issue['id']
				issue_dict['url'] = issue['url']
				issue_dict['repository_url'] = issue['repository_url']
				issue_dict['labels_url'] = issue['labels_url']
				issue_dict['comments_url'] = issue['comments_url']
				issue_dict['events_url'] = issue['events_url']
				issue_dict['html_url'] = issue['html_url']
				issue_dict['number'] = issue['number']
				issue_dict['state'] = issue['state']
				issue_dict['title'] = issue['title'].replace(",", "") #because I am using csv commas in titles cause issues
				issue_dict['user_login'] = issue['user']['login']
				issue_dict['user_htmlURL'] = issue['user']['html_url']
				
				if len(issue['labels']) != 0:
					labelList = issue['labels']
					issue_dict['labels'] = ""
					for label in labelList:
						issue_dict['labels'] += str(label['name'].replace(",", ""))+ " " #create a space-separated list of labels
				else:
					issue_dict['labels'] = ""

				if issue['milestone'] != None:
					issue_dict['milestone_htmlURL'] = issue['milestone']['html_url']
					issue_dict['milestone_id'] = issue['milestone']['id']
				else:
					issue_dict['milestone_htmlURL'] = None
					issue_dict['milestone_id'] = None
				
				issue_dict['locked'] = issue['locked']
				issue_dict['closed_at'] = issue['closed_at']
				issue_dict['created_at'] = issue['created_at']
				issue_dict['updated_at'] = issue['updated_at']

				issues.append(issue_dict)

		# increment the page 
		pageNum += 1
		
			
	#reference information
	print("API Request Rate Limit Remaining: " + str(apiResponse.headers['X-RateLimit-Remaining']) + "/5000")
	print("There are " + str(len(issues)) + " issues")
	#return the object
	return issues 


# releases API doc: https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository	
def getReleases(user, pw, repoURL):
	print("Collecting Releases for Project...")
	# API returns paginated results!
	pageNum = 1
	releases = []

	while True:
		
		releasesURL = repoURL + "/releases"
		params = {'page': pageNum, 'per_page': 100}

		apiResponse = requests.get(releasesURL, auth=(user,pw), params=params)
		statusCode = int(apiResponse.headers['Status'].split()[0])
		
		# 200 is OK
		if statusCode == 200:
			releasesObject = apiResponse.json() #get the data
			
			#stops when no more pages 
			if len(releasesObject) < 1:
				break
			'''
			Release objects have nested attributes so I am adding them to the final object manually
			Partially Included: assets -> uploader (login, html_url), author (login, html_url)
			Totally Excluded: author, assets
			'''

			for release in releasesObject:
				release_dict = {}
				release_dict['url'] = release['url']
				release_dict['html_url'] = release['html_url']
				release_dict['assets_url'] = release['assets_url']
				release_dict['upload_url'] = release['upload_url'].replace(",", "")
				release_dict['tarball_url'] = release['tarball_url']
				release_dict['zipball_url'] = release['zipball_url']
				release_dict['id'] = release['id']
				release_dict['tag_name'] = release['tag_name']
				release_dict['target_commitish'] = release['target_commitish']
				release_dict['name'] = release['name']
				release_dict['draft'] = release['draft']
				release_dict['prerelease'] = release['prerelease']
				release_dict['created_at'] = release['created_at']
				release_dict['published_at'] = release['published_at']
				releases.append(release_dict)

		# increment the page 
		pageNum += 1
		
	print("API Request Rate Limit Remaining: " + str(apiResponse.headers['X-RateLimit-Remaining']) + "/5000")
	#reference information
	print("There are " + str(len(releases)) + " releases")
	#return the object
	return releases 
