var btn = document.getElementById("submit").addEventListener("click", displayData);

// var btn = document.getElementById("submit").onclick = displayData();
function loading() {
    // document.getElementById("result").innerHTML = "Loading...";
    document.getElementById("time_elapsed").innerHTML = "Loading...";
}

function populateDatabases(dbtype) {
    console.log(dbtype)
    var xmlHttp = new XMLHttpRequest();
    var url;
    if(dbtype == "mysql") {
        url = "/" + dbtype + "?query=" + "show databases;";
    }
    else if(dbtype == "redshift") {
        url = "/" + dbtype + "?query=" + "SELECT \* FROM pg_database;" + "&database=adni";
    }
    else {
        url = "/" + dbtype + "?query=" + "show databases;"+"&database=ADNI";
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.onreadystatechange = function () {
        console.log("working");
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            //console.log(xmlHttp);
            databasesResponse = xmlHttp.responseText;
            //console.log(databasesResponse)
            var jsonDatabases = JSON.parse(databasesResponse).result;
            //console.log(jsonDatabases)
            databases = []
            for (key in jsonDatabases) {
                databases.push(jsonDatabases[key][0])
            }
            //console.log(databases);
            inputDatabasesElement = document.getElementById("InputDatabases")
            inputDatabasesElement.innerHTML=""
            databases.forEach(function(database) {
                console.log(database)
                inputDatabasesElement.innerHTML += "<option label='" + database + "'value='"+ database +"'/>"
            })
        } else if (xmlHttp.readyState == 4) {
            console.log("failed")
        }
    };
    xmlHttp.send(null);

}

function clearCache() {
    var table = document.getElementById("rounded-corner");
    var child1 = document.getElementById("tbhead");
    var child2 = document.getElementById("tbmain");
    table.removeChild(child1);
    table.removeChild(child2);
    document.getElementById("time_elapsed").innerHTML = "";
}

function Reset() {
    
        
        clearCache();
        location.reload();
        location.href = "/";
    
}

function displayData() {
    var method = $("input[id='InputName']").val();
    var q = $("textarea[id='InputMessage']").val();
    var database = $("#InputDatabase").val();
    var xmlHttp = new XMLHttpRequest();
    var url = "/" + method + "?query=" + q + "&database=" + database;
    console.log(database);
    document.getElementById('whatis').scrollIntoView();
    loading();
    xmlHttp.open("GET", url, true);
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            var responseText = xmlHttp.responseText;
            var obj = JSON.parse(responseText);
            createDataTable(obj);
            // var data = "Res: " + "\n";
            // for (var o in obj['result']) {
            //     data += obj['result'][o] + "\n";
            // }
            var time = obj['query_time'];
            // document.getElementById("result").innerHTML = data;
            document.getElementById("time_elapsed").innerHTML = time;

        } else if (xmlHttp.readyState == 4) {
            // var error = "Wrong Input";
            var error=xmlHttp.responseText;
            // document.getElementById("result").innerHTML = error;
            // var responseText = xmlHttp.responseText;
            // var obj = JSON.parse(responseText);
            // console.log(obj);
            document.getElementById("time_elapsed").innerHTML = error;

        }
        console.log(xmlHttp.responseText);
    };
    xmlHttp.send(null);
}

function createDataTable(obj) {
    var table = document.getElementById("rounded-corner");
    var create1 = document.createElement("thead");
    create1.setAttribute("id", "tbhead");
    table.appendChild(create1);
    var thead = document.getElementById('tbhead');
    var row = document.createElement('tr');
    for (var j = 0; j < obj['col_name'].length; j++) {
        var idCell = document.createElement('th');
        idCell.setAttribute("scope", "col");
        if (j === 0) {
            idCell.setAttribute("class", "rounded-first");
            // alert("success")
        }
        if (j === obj['col_name'].length - 1) {
            idCell.setAttribute("class", "rounded-last");
        }
        idCell.innerHTML = obj['col_name'][j];
        row.appendChild(idCell);
    }
    thead.appendChild(row);

    var create2 = document.createElement("thead");
    create2.setAttribute("id", "tbmain");
    table.appendChild(create2);
    var tbody = document.getElementById('tbmain');
    if(obj['result'].length>1000){
        alert("Too many records")
    }
    for (var i = 0; i < obj['result'].length; i++) {
        var trow = fillTable(obj['result'][i]);
        tbody.appendChild(trow);
    }
}

function fillTable(data) {
    var row = document.createElement('tr');
    for (var i = 0; i < data.length; i++) {
        var idCell = document.createElement('td');
        idCell.innerHTML = data[i];
        row.appendChild(idCell);
    }
    return row;
}
