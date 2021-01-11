
$(document).ready(function()
{



$('#search-Tags').submit(function(e){

  e.preventDefault();
  const TagSearch = $('#TagSearch').val();
  let data = {Tag:TagSearch}
  

  $.ajax({
    url:"/searchTags",
    type:'post',
    data:data
  })
    .done(function( data )
     {
      if ( data.success )
      {

        console.log(data.countByext);


        // pie chart
        var chart = new CanvasJS.Chart("chartContainer", {
          theme: "dark2", // "light1", "light2", "dark1", "dark2"
          exportEnabled: true,
          animationEnabled: true,
          title: {
            text: "Count File By FileType"
          },
          data: [{
            type: "pie",
            startAngle: 25,
            toolTipContent: "<b>{label}</b>: {y}%",
            showInLegend: "true",
            legendText: "{label}",
            indexLabelFontSize: 16,
            indexLabel: "{label} - {y}%",
            dataPoints: data.countByext
          }]
        });
        chart.render();

        // waterfall chart
          var chart = new CanvasJS.Chart("chartContainer1", {
            theme: "dark1", // "light1", "ligh2", "dark1", "dark2"
            animationEnabled: true,
            title: {
              text: "File Count by Extention"
            },
            axisY: {
              title: "total File count",
              lineThickness: 0,
              includeZero: true
            },
            data: [{
              type: "waterfall",
              indexLabel: "{y}",
              indexLabelFontColor: "#EEEEEE",
              indexLabelPlacement: "inside",
              // yValueFormatString: "#,##0k",
              dataPoints: data.countByext
            }]
          });
          chart.render();


          // end of waterfall chart

      }
      else
      {

        alert("false")
      }
    });
});
});