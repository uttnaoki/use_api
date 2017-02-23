const api_key = "key";
const getcitycode = "https://opendata.resas-portal.go.jp/api/v1/cities?prefCode=33";
const getsiccode = "https://opendata.resas-portal.go.jp/api/v1/industries/broad";
const getsimccode = "https://opendata.resas-portal.go.jp/api/v1/industries/middle";

const forIndustry = "https://opendata.resas-portal.go.jp/api/v1/industry/power/forIndustry"; //産業特化係数
const empnum = "https://opendata.resas-portal.go.jp/api/v1/municipality/employee/perYear"; //従業者数（事業所単位）

var year = "year=2012";
var prefCode = "prefCode=33";
var cityCode1 = "cityCode=33202";
var cityCode2 = "cityCode=33203";
var sicCode = "sicCode=-";
var sicCode1 = "sicCode=E";
var sicCode2 = "sicCode=-";
var param = "?" + year +
    "&" + prefCode +
    "&" + cityCode1 +
    "&" + sicCode;

var array = [];

var wrapper = document.getElementById("hoge")
// var tree = jsonTree.create([], wrapper)

if (1) //産業別特化係数
    d3.request(forIndustry + param)
    .header("X-API-KEY", api_key)
    .mimeType("application/json")
    .response(function(xhr) {
        return JSON.parse(xhr.responseText)
    })
    .get(function(dataset) {
        var list = dataset.result.data
        // tree.loadData(dataset)
        // console.log(dataset)
        var h = '<tr>' + '<th>' + '産業中分類' + '</th>' +
            '<th>' + '特化係数（付加価値額）' + '</th>' +
            '<th>' + '特化係数（従業者数）' + '</th>' +
            '<th>' + '特化係数（労働生産性）' + '</th>' +
            '</tr>'
        $("#hoge").append(h);
        for (var i in list) {
            array.push(list[i].simcName)
            var h = '<tr>' + '<td>' + list[i].simcName + '</td>' +
                '<td>' + list[i].value + '</td>' +
                '<td>' + list[i].employee + '</td>' +
                '<td>' + list[i].labor + '</td>' +
                '</tr>';
            $("#hoge").append(h);
        }
        console.log(array)
    });

if (0) //市町村別コード
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

if (0) //産業大分類コード
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

if (0) //産業中分類コード
    d3.request(getsimccode)
    .header("X-API-KEY", api_key)
    .mimeType("application/json")
    .response(function(xhr) {
        return JSON.parse(xhr.responseText)
    })
    .get(function(dataset) {
        for (var i in dataset.result) {
            var h = '<div>' + '(' + dataset.result[i].sicCode + ')' + dataset.result[i].simcCode + ' : ' +
                dataset.result[i].simcName + '</div>';
            $("#hoge").append(h);
        }
    });
