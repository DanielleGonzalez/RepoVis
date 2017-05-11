google.charts.load("current", {'packages':['corechart','line','timeline']});
google.charts.setOnLoadCallback(drawPRData);
google.charts.setOnLoadCallback(drawIssueData);
google.charts.setOnLoadCallback(drawContribData);

function drawPRData():
	var prChart = new google.visualization.LineChart(document.getElementById('prdata'));

function drawIssueData():
	var issueChart = new google.visualization.LineChart(document.getElementById('issuedata'));

function drawContribData():
	var contribChart = new google.visualization.LineChart(document.getElementById('contribdata'));


