<template>
  <apexchart type="line" :options="chartOptions" :series="localSeries"></apexchart>
</template>

<script>
export default {
 props:{
   title:{ String, default: () => ''}, 
   series: {Array, default: () => []},
   categories: {Array, default: () => []}
 },
  data() {
        return {  
          localSeries: this.series,
          chartOptions: {
            chart: {
              title:{
                text: this.title
              },
              height: 350,
              type: 'line',
              zoom: {
                enabled: false
              },
              toolbar: {
                show: false
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight'
            },
            title: {
              text: 'Product Trends by Month',
              align: 'left'
            },
            grid: {
              row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0.5
              },
            },
            xaxis: {
              categories: this.categories
            }
          },
        }
    },
    watch: {
      series(){
        this.localSeries = this.$_.cloneDeep(this.series)
      },
      title(){
        this.chartOptions = {
          ...this.chartOptions,
          title:{
            text: this.title
          }
        }
      },
      categories(){
        this.chartOptions = {
          ...this.chartOptions,
          xaxis: {
            categories: this.categories
          }
        }
      }
    }
}
</script>

<style>

</style>