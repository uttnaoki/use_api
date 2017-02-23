const api_key = "key";
const getcitycode = "https://opendata.resas-portal.go.jp/api/v1/cities?prefCode=33";
const getsiccode = "https://opendata.resas-portal.go.jp/api/v1/industries/broad";
const getsimccode = "https://opendata.resas-portal.go.jp/api/v1/industries/middle";

if(0)//市町村別コード
d3.request(getcitycode)
    .header("X-API-KEY", api_key)
    .mimeType("application/json")
    .response(function(xhr) {
        return JSON.parse(xhr.responseText)
    })
    .get(function(dataset) {
        for (var i in dataset.result) {
            var h = '<div>' + dataset.result[i].cityCode + ' : ' + dataset.result[i].cityName + '</div>';
            $("#hoge").append(h);
        }
    });

if(0)//産業大分類コード
d3.request(getsiccode)
    .header("X-API-KEY", api_key)
    .mimeType("application/json")
    .response(function(xhr) {
        return JSON.parse(xhr.responseText)
    })
    .get(function(dataset) {
        for (var i in dataset.result) {
            var h = '<div>' + dataset.result[i].sicCode + ' : ' + dataset.result[i].sicName + '</div>';
            $("#hoge").append(h);
        }
    });

if(0)//産業中分類コード
d3.request(getsimccode)
    .header("X-API-KEY", api_key)
    .mimeType("application/json")
    .response(function(xhr) {
        return JSON.parse(xhr.responseText)
    })
    .get(function(dataset) {
        for (var i in dataset.result) {
            var h = '<div>' + '(' + dataset.result[i].sicCode + ')' + dataset.result[i].simcCode + ' : '
             + dataset.result[i].simcName + '</div>';
            $("#hoge").append(h);
        }
    });
