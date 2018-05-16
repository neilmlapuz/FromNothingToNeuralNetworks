var ctx = document.getElementById("line-chart");
var myChart;
var data = {
    datasets: [
                {
                label: "Loss",
                data: [0,0,0,0,0],
                backgroundColor:"red",
                borderColor: "lightred",
                fill: false,
                lineTension:0,
                pointRadius:5
                },
                {
                label: "Val_loss",
                data: [0,0,0,0,0],
                backgroundColor:"purple",
                borderColor: "purple",
                fill: false,
                lineTension:0,
                pointRadius:5
                },
                {
                label: "Acc",
                data: [0,0,0,0,0],
                backgroundColor:"blue",
                borderColor: "lightblue",
                fill: false,
                lineTension:0,
                pointRadius:5
                },
                {
                label: "Val_Acc",
                data: [0,0,0,0,0],
                backgroundColor:"green",
                borderColor: "lightgreen",
                fill: false,
                lineTension:0,
                pointRadius:5
                }
    ]
};
var options = {
    responsive:false,
    maintainAspectRatio: false,
};
//Builds chart
myChart = new Chart(ctx,{
    type: "line",
    data:data,
    options:options
});

//Updates chart once the info of the model has been determined
function updateChart(result_model){
    var data = {
        labels: result_model["epochs"],
        datasets: [
                {
                label: "Loss",
                data: result_model["loss"],
                backgroundColor:"red",
                borderColor: "red",
                fill: false,
                lineTension:0,
                pointRadius:5
                },
                {
                label: "Val_loss",
                data: result_model["val_loss"],
                backgroundColor:"purple",
                borderColor: "purple",
                fill: false,
                lineTension:0,
                pointRadius:5
                },
                {
                label: "Acc",
                data: result_model["acc"],
                backgroundColor:"blue",
                borderColor: "lightblue",
                fill: false,
                lineTension:0,
                pointRadius:5
                },
                {
                label: "Val_Acc",
                data: result_model["val_acc"],
                backgroundColor:"green",
                borderColor: "lightgreen",
                fill: false,
                lineTension:0,
                pointRadius:5
                }
    ]
    };
    var options = {
    responsive:false,
    maintainAspectRatio: false,
};
    myChart = new Chart(ctx,{
    type: "line",
    data:data
});
}