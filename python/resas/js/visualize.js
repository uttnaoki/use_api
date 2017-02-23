var margin = {
    top: 30,
    right: 50,
    bottom: 230,
    left: 50
};
var w = 1300;
// var w = window.parent.screen.width;
// var h = window.parent.screen.height;
var h = 1000;
var width = w - margin.left - margin.right;
var height = h - margin.top - margin.bottom;
var color = d3.scale.category10();
//var rightpadding = 600;
var once_duration_controle = 0;
// var speed_power=8;
var svg = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var mercator = d3.geo.mercator()
    .center([133.837613, 34.94759]) // [編集する行] 地図の中心の[経度，緯度]を入力
    .translate([width / 2, height / 2 - 100])
    .scale(30000);

// geojsonからpath要素を作るための設定。
var geopath = d3.geo.path()
    .projection(mercator);



var rscale = d3.scale.linear()
    .domain([0, 400])
    .range([5, 100])

//後で各地点のデータをプロットするための座標処理
var positions = [];
var city = [];
d3.csv("map/zahyo.csv", type, function(error, data) {
    if (error) throw error;
    data.forEach(function(d) {
        positions.push(mercator([d.y, d.x]));
    });
    data.forEach(function(d) {
        city.push(d.city);
    });
});

// map で色を変える市町村を読み込む
var area = [];
d3.csv("map/change_color.csv", function(error, data) {
    if (error) throw error;
    data.forEach(function(d) {
        area.push(d.city);
    })
})

d3.json("map/map.geojson", function(error, okayama) {
    makegeo(okayama.features);
    var employ_value = [];
    var max;
    d3.csv("data", function(error, data) {
      if (error) throw error;
      employ_value = data.map(function(d) {
        return d.value;
      });
      max = d3.max(employ_value);
    });
});


function makegeo(geodata) {
    var sflag = [];
    for (var i = 0; i < geodata.length; i++) {
        sflag.push({
            flag: 0
        });
    };
    var map = svg
        .selectAll("puth")
        .data(geodata)
        .enter().append("path")
        .attr({
            "id": function(d, i) {
                return "city" + i;
            },
            "d": geopath,
            "fill": function(d) {
                if (is_valid_area(d)) return "red";
                return "lightgray";
            },
            opacity: function(d) {
              tmp = is_valid_area(d,1);
              if(tmp)return tmp;
              return 1;
            },
            "stroke": "white",
            "stroke-width": 1
        })
}

function is_valid_area(d,flag) {
    var ret = 0;
    var len = area.length;
    for (var i = 0; i < len; i++) {
        if (d.properties["N03_004"].indexOf(area[i]) != -1) {
            ret = 1;
            break;
        }
    }
    if (flag == 1 && i < len){
      return employ_value[i]/max;
    }
    return ret;
}

function type(d) {
    var dkeys = d3.map(d).keys();
    dkeys.shift();
    var dlen = dkeys.length;
    for (var i = 0; i < dlen; i++) d[dkeys[i]] = +d[dkeys[i]];
    return d;
}
