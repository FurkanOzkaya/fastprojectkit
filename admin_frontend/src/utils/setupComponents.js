// Core Components
import Toolbar from '../components/core/Toolbar.vue';
import Navigation from '../components/core/NavigationDrawer.vue';
import Widget from '../components/widget/Widget.vue';
import About from '../components/views/About.vue';
import DataTable from '../components/Table/DataTable.vue';
import LineChart from '../components/Chart/LineChart.vue';
import RadialBar from '../components/Chart/RadialBar.vue';
import PieChart from '../components/Chart/PieChart.vue';
import DefaultSnackBar from '../components/SnackBars/DefaultSnackBar';

function setupComponents(Vue){

  Vue.component('toolbar', Toolbar);
  Vue.component('navigation', Navigation);
  Vue.component('widget', Widget);
  Vue.component('about', About);
  Vue.component('data-table', DataTable);
  Vue.component('line-chart', LineChart);
  Vue.component('radial-bar', RadialBar);
  Vue.component('pie-chart', PieChart);
  Vue.component('default-snackbar', DefaultSnackBar);
}


export {
  setupComponents
}
