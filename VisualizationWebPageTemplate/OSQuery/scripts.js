google.charts.load("current", {'packages':['corechart','line','timeline','table','bar']});
google.charts.setOnLoadCallback(drawContribData);
google.charts.setOnLoadCallback(drawPRData);
google.charts.setOnLoadCallback(drawIssueData);


function drawPRData(){
	
	 $.get("osquery-prByRelease.csv", function(csvString) {
      // transform the CSV string into a 2-dimensional array
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      
      // // this new DataTable object holds all the data
      var data = new google.visualization.arrayToDataTable(arrayData);

      // the ReleaseName column is assumed to be numbers, but it needs to be strings due to formatting
      // assumes you want to convert column 0 of DataTable "data" to type "number"
      // insert a new column at the desired index; this bumps all columns at or after the chosen index up by 1 (so column 0 becomes column 1, 1 becomes 2, etc)
      data.insertColumn(0, 'string', data.getColumnLabel(0));
      // copy values from column 1 (old column 0) to column 0, converted to numbers
      for (var i = 0; i < data.getNumberOfRows(); i++) {
          var val = data.getValue(i, 1);
          if (val != '' && val != null) {
              data.setValue(i, 0, new String(val).valueOf());
          }
      }
      // remove column 1 (the old column 0)
      data.removeColumn(1);
      // data.addColumn('string', 'ReleaseName')
      // data.addColumn('number', 'PRsOpened')
      // data.addColumn('number', 'PRsClosed')
      var view = new google.visualization.DataView(data);
      view.setColumns([0,2,3])
      var options = {
            title: 'Number of Pull Requests Opened And Closed Per Release',
            // hAxis: {title: 'Release Name'},
            // vAxis: {title: 'Number of Pull Requests'}
      };
      var prLineChart = new google.visualization.LineChart(document.getElementById('prLineData'));
      prLineChart.draw(view, options)
   });
}



function drawIssueData(){
	$.get("osquery-issueByRelease.csv", function(csvString) {
      // transform the CSV string into a 2-dimensional array
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      
      // // this new DataTable object holds all the data
      var data = new google.visualization.arrayToDataTable(arrayData);

      // the ReleaseName column is assumed to be numbers, but it needs to be strings due to formatting
      // assumes you want to convert column 0 of DataTable "data" to type "number"
      // insert a new column at the desired index; this bumps all columns at or after the chosen index up by 1 (so column 0 becomes column 1, 1 becomes 2, etc)
      data.insertColumn(0, 'string', data.getColumnLabel(0));
      // copy values from column 1 (old column 0) to column 0, converted to numbers
      for (var i = 0; i < data.getNumberOfRows(); i++) {
          var val = data.getValue(i, 1);
          if (val != '' && val != null) {
              data.setValue(i, 0, new String(val).valueOf());
          }
      }
      // remove column 1 (the old column 0)
      data.removeColumn(1);
      // data.addColumn('string', 'ReleaseName')
      // data.addColumn('number', 'PRsOpened')
      // data.addColumn('number', 'PRsClosed')
      var view = new google.visualization.DataView(data);
      view.setColumns([0,2,3])
      var options = {
            title: 'Number of Issues Opened And Closed Per Release',
            // hAxis: {title: 'Release Name'},
            // vAxis: {title: 'Number of Issues'}
      };
      var issueLineChart = new google.visualization.LineChart(document.getElementById('issueLineData'));
      issueLineChart.draw(view, options)
   });
}

function drawContribData(){
	$.get("osquery-contribByRelease.csv", function(csvString) {
      // transform the CSV string into a 2-dimensional array
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
      
      // // this new DataTable object holds all the data
      var data = new google.visualization.arrayToDataTable(arrayData);

      // the ReleaseName column is assumed to be numbers, but it needs to be strings due to formatting
      // assumes you want to convert column 0 of DataTable "data" to type "number"
      // insert a new column at the desired index; this bumps all columns at or after the chosen index up by 1 (so column 0 becomes column 1, 1 becomes 2, etc)
      data.insertColumn(0, 'string', data.getColumnLabel(0));
      // copy values from column 1 (old column 0) to column 0, converted to numbers
      for (var i = 0; i < data.getNumberOfRows(); i++) {
          var val = data.getValue(i, 1);
          if (val != '' && val != null) {
              data.setValue(i, 0, new String(val).valueOf());
          }
      }
      // remove column 1 (the old column 0)
      data.removeColumn(1);
      // data.addColumn('string', 'ReleaseName')
      // data.addColumn('number', 'PRsOpened')
      // data.addColumn('number', 'PRsClosed')
      var view = new google.visualization.DataView(data);
      view.setColumns([0,2])
      var options = {
          title: 'Number of Contributors To A Release',
          hAxis: {title: 'Number of Contributors'},
          vAxis: {title: 'Number of Releases'},
          legend: 'none',
          trendlines: { 0: {} }    // Draw a trendline for data series 0.
      };

      var contribChart = new google.visualization.Histogram(document.getElementById('contribdata'));
      contribChart.draw(view, options);
  });
}


