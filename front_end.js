function obtain(){
  let year1=document.getElementById("year_1");
  let valueofyear1=get_value_and_clear(year1);
  let year2=document.getElementById("year_2");
  let valueofyear2=get_value_and_clear(year2);
  let year_dic={"year_start":valueofyear1,"year_end":valueofyear2};
  let dictionaryofJSON=JSON.stringify(year_dic);
  console.log('Post Request');
  ajaxPostRequest("/donut",dictionaryofJSON, showchart);
  ajaxPostRequest("/donut2",dictionaryofJSON, showchart2);
  
}

function showchart(response){
  console.log('Show chat');
  let myresponse_data=JSON.parse(response);
  let outputdiv=document.getElementById("output");
  let getname=myresponse_data[0]["name"];
  let getdataname=myresponse_data[myresponse_data.length-1]["name"];
  let html_page={
    title:'Nike Sales Report<br>'+getname+" - "+getdataname,
    showlegend:true,
    grid:{rows:1,columns:myresponse_data.length}
  };
  Plotly.newPlot(outputdiv,myresponse_data,html_page);
}
function showchart2(response){
  console.log('Show chat');
  let myresponse_data=JSON.parse(response);
  let outputdiv=document.getElementById("output2");
  let getname="";
  let getdataname="";
  let html_page={
    title:'Nike Availability Report<br>'+getname+" - "+getdataname,
    showlegend:true,
    
  };
  Plotly.newPlot(outputdiv,myresponse_data,html_page);
}

function get_value_and_clear(input_obj) {
  let retVal = input_obj.value;
  input_obj.value = "";
  return retVal;
}



function ajaxGetRequest(path, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
        callback(this.response);
    }
  };
  request.open("GET", path);
  request.send();
}

function ajaxPostRequest(path, data, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
      callback(this.response);
    }
  };
  request.open("POST", path);
  request.send(data);
}