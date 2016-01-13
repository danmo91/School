$(function() {

  // chart
  var overdueData = [
      {
        value: 300,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "90 Days"
      },
      {
          value: 100,
          color: "#FDB45C",
          highlight: "#FFC870",
          label: "60 Days"
      },
      {
          value: 50,
          color: "#46BFBD",
          highlight: "#5AD3D1",
          label: "30 Days"
      },

  ]; // overdueData

  var inventoryData = [
      {
        value: 300,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "In"
      },
      {
          value: 100,
          color: "#46BFBD",
          highlight: "#5AD3D1",
          label: "Out"
      },


  ]; // salesData

  var salesData = [
      {
        value: 300,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "Actual Sales"
      },
      {
          value: 100,
          color: "#FDB45C",
          highlight: "#FFC870",
          label: "Left to reach goal"
      },


  ]; // salesData


  window.onload = function(){
      var ctx = document.getElementById("overdue-chart").getContext("2d");
      window.overdueDonut = new Chart(ctx).Doughnut(overdueData, {responsive : true});

      ctx = document.getElementById("inventory-chart").getContext("2d");
      window.inventoryDonut = new Chart(ctx).Doughnut(inventoryData, {responsive : true});

      ctx = document.getElementById("sales-chart").getContext("2d");
      window.salesDonut = new Chart(ctx).Doughnut(salesData, {responsive : true});
  };


}); // Ready
