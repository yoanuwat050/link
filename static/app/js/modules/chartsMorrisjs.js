export const morrisjs_demo = () =>{
      if ($('#morris_area_chart').length) {
  var data = [{
          y: '2016',
          a: 35,
          b: 90
      }, {
          y: '2017',
          a: 45,
          b: 75
      }, {
          y: '2018',
          a: 55,
          b: 50
      }, {
          y: '2019',
          a: 65,
          b: 60
      }, {
          y: '2020',
          a: 75,
          b: 65
      }, {
          y: '2021',
          a: 90,
          b: 70
      }, {
          y: '2022',
          a: 95,
          b: 75
      }, {
          y: '2023',
          a: 105,
          b: 75
      }, {
          y: '2024',
          a: 115,
          b: 85
      }, {
          y: '2025',
          a: 125,
          b: 85
      }, {
          y: '2026',
          a: 145,
          b: 95
      }],
      config = {
          data: data,
          xkey: 'y',
          ykeys: ['a', 'b'],
          labels: ['Total Income', 'Total Outcome'],
          fillOpacity: 0.6,
          hideHover: 'auto',
          behaveLikeLine: true,
          resize: true,
          pointFillColors: ['#ffffff'],
          pointStrokeColors: ['black'],
          lineColors: [ MaterialLab.APP_COLORS.mw_purple,MaterialLab.APP_COLORS.success ],
          barColors: [MaterialLab.APP_COLORS.mw_purple, MaterialLab.APP_COLORS.success ]
      };
  config.element = 'morris_area_chart';
  Morris.Area(config);
  config.element = 'morris_line_chart';
  Morris.Line(config);
  config.element = 'morris_bar_chart';
  Morris.Bar(config);
  config.element = 'morris_stacked';
  config.stacked = true;
  Morris.Bar(config);
  Morris.Donut({
      element: 'morris_pie_chart',
      data: [{
          label: "Study",
          value: 30
      }, {
          label: "Sleep",
          value: 15
      }, {
          label: "Work",
          value: 45
      }, {
          label: "Eat",
          value: 10
      }],
    colors: [MaterialLab.APP_COLORS.success , MaterialLab.APP_COLORS.mw_grayBlue, MaterialLab.APP_COLORS.mw_purple,MaterialLab.APP_COLORS.mw_gray ]
  });
  }
}
