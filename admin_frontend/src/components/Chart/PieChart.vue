<template>
<div>
  <div v-if="localSeries == []">
    There is No Data
  </div>
  <div v-else-if="localSeries == ['error']">
    Error Accoured
  </div>
  <apexchart  v-else type="pie"  :options="chartOptions" :series="localSeries"></apexchart>
</div>
</template>

<script>

export default {
  props: {
    series:{type: Array, default: () =>  []},
    labels:{type: Array, default: () =>  []},
    title: {type: String, default: () => "Pie Chart"}
  },
 data() {
    return {
          localSeries: undefined,
          chartOptions: {
            title: {
              text: this.title,
              align: 'center',
              margin: 5,
              offsetX: -20,
              offsetY: 0,
              floating: false,
              style: {
                fontSize:  '16px',
                fontWeight:  'bold',
                fontFamily:  undefined,
                color:  '#263238' // TODO CHANGE LATER
              },
            },
            chart: {
              width: '100%',
              type: 'pie',
            },
            labels: this.labels,
          },
        }
    },
    watch: {
      series(newval){
       this.$nextTick(() => {
         this.localSeries = this.$_.cloneDeep(newval)
       })
      },
      labels(newval){
        this.chartOptions = {...this.chartOptions,
          labels: newval
        }
      },
      title(newval){
        this.chartOptions = {...this.chartOptions,
          title:{
            text: newval,
            
          } 
        }
      },
      chartOptions(){
        this.localSeries = this.series
      }
    }
}
</script>

<style>
.message{
  display: grid;
  place-items: center;
}
</style>