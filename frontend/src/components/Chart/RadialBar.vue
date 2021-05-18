<template>
  <apexchart class="chart" type="radialBar" :options="chartOptions" :series="localSeries"></apexchart>
</template>

<script>
export default {
  props:{
    series: {type: Array, default: () => []},
    labels: {type: Array, default: () => []},
  },
data() {
        return {
          localSeries: this.series,
          chartOptions: {
            chart: {
              height: "100%",
              width: "100%",
              type: 'radialBar',
              offsetY: -10
            },
            plotOptions: {
              radialBar: {
                startAngle: -135,
                endAngle: 135,
                dataLabels: {
                  name: {
                    fontSize: '16px',
                    color: undefined,
                    offsetY: 120
                  },
                  value: {
                    offsetY: 76,
                    fontSize: '22px',
                    color: undefined,
                    formatter: function (val) {
                      return val + "%";
                    }
                  }
                }
              }
            },
            fill: {
              type: 'gradient',
              gradient: {
                  shade: 'dark',
                  shadeIntensity: 0.15,
                  inverseColors: false,
                  opacityFrom: 1,
                  opacityTo: 1,
                  stops: [0, 50, 65, 91]
              },
            },
            stroke: {
              dashArray: 4
            },
            labels: this.labels,
          } 
        }
    },
    watch: {
      series(){
        this.localSeries = this.$_.cloneDeep(this.series)
      },
      // title(){
      //   this.chartOptions = {
      //     ...this.chartOptions,
      //     title:{
      //       text: this.title
      //     }
      //   }
      // },
      labels(){
        this.chartOptions = {
          ...this.chartOptions,
          labels: this.labels
        }
      }
    }
}
</script>

<style scoped>
.chart{
  width: 100%;
  height: 100%;
}
</style>
