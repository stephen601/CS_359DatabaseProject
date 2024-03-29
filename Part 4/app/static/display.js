function displayData() {
    var new_database = "{{ database }}";
    var url = "/api/display?new_database=" + new_database;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            
            // Define a dictionary with old and new column names
            var colNames = {
                "modelNo": "Model Number",
                "schedulerSystem": "Scheduler System",
                "serialNo": "Serial Number"
            };
            
            var table = "<table>";
            table += "<tr>";
            
            // Iterate through the old column names and dynamically create the column headers
            for (var i = 0; i < Object.keys(colNames).length; i++) {
                table += "<th>" + colNames[Object.keys(colNames)[i]] + "</th>";
            }
            
            // Add a new column header for the links
            table += "<th>Details</th>";
            table += "</tr>";
                    
            for (var i = 0; i < data.length; i++) {
                table += "<tr>";
                
                // Iterate through the old column names and dynamically create the table rows
                for (var j = 0; j < Object.keys(colNames).length; j++) {
                    table += "<td>" + data[i][Object.keys(colNames)[j]] + "</td>";
                }
                
                // Add a new column for links in each row
                table += "<td><a href='/details?modelNo=" + data[i]['modelNo'] + "'>Model Details</a></td>";
                table += "</tr>";
            }
            
            table += "</table>";
            
            document.getElementById("data").innerHTML = table;
        });
}

displayData();