<template>
  <div>
    <v-container fluid grid-list-xl>
     <v-layout row wrap>
       <v-flex d-flex lg3 sm6 xs12>
        <widget icon="mdi-server" :title="userCount" subTitle="User Database" supTitle="Total User Count" color="#00b297"/>
      </v-flex>
      <v-flex d-flex lg3 sm6 xs12>
        <widget icon="mdi-google-earth" title="$141,291" subTitle="$117,212" supTitle="widgetTodaysSale" color="#dc3545"/>
      </v-flex>
      <v-flex d-flex lg3 sm6 xs12>
        <widget icon="mdi-emoticon-happy" title="33.45%" subTitle="13%"  supTitle="widgetUniqueVisits" color="#0866C6"/>
      </v-flex>
      <v-flex d-flex lg3 sm6 xs12>
        <widget icon="mdi-heart" title="13.00%" subTitle="17.25%" supTitle="'widgetBounceRate" color="#1D2939"/>
      </v-flex>
     
      <v-flex d-flex lg4 sm6 xs12>
       <v-card  class="line_chart_card pa-3">
          <line-chart title="User Per Month" :categories="monthlyUserCategories" :series="monthlyUserSeries"/>
       </v-card>
      </v-flex>
      <v-flex d-flex lg4 sm6 xs12>
         <v-card class="pie_chart">
          <pie-chart title="User Access Level Chart"  :labels="accessLevelLabels" :series="accessLevelSeries"/>
         </v-card>
      </v-flex>
      <v-flex d-flex lg4 sm6 xs12>
        <v-card class=radial_bar_chart>
          <radial-bar :series="monthlyUserRatioSeries"  :labels="monthlyUserRatioLabels"/>
        </v-card>
      </v-flex>
      
       <v-flex d-flex lg8 sm6 xs12>
        <data-table :users="users"/>
      </v-flex>
    </v-layout>
    
  </v-container>
  </div>
</template>

<script>
import userService from '../../service/services/UserService'
export default {

  data() {
    return{
      users: [],
      userCount: 0,
      token: undefined,
      accessLevelSeries: [],
      accessLevelLabels: [],
      monthlyUserSeries: [],
      monthlyUserCategories: [],
      monthlyUserRatioSeries: [],
      monthlyUserRatioLabels: []

    }
  },
  created() {
    this.token = this.$store.getters.token
      userService.getUsers(this.token).then((response) => {
        if(response.status == 200) 
        {
          this.users = response.data
          this.userCount= this.users.length
          this.getUserAccesInformation()
          this.getUserMonthlyRatioInformation()
        }
        else
        {
          //give some alert with snackbar or alert
        }
        
      }).catch((error) => {
        if(error.response.status == 401)
        {
          this.$store.dispatch("updateToken", null)
          this.$router.push("Login")
        }
        else {
          // her give alert box
        }
        
      })
  },
 methods: {
   getUserAccesInformation(){
     userService.getUserAccessLevelRatio(this.token).then((response) => {
       if(response.status == 200) 
        {
          this.prepareAccessData(response.data)
        }
        else{
           this.prepareAccessData([])
        }
     }).catch(() => {
       this.prepareAccessData("error")
     })
   },
   getUserMonthlyRatioInformation(){
     userService.getUserMontlyRatio(this.token).then((response) => {
       if(response.status == 200) 
        {
          this.prepareUserMonthlysData(response.data)
          this.prepareIncreaseRatio(response.data)
        }
        else{
           this.prepareUserMonthlysData([])
        }
     }).catch(() => {
       this.prepareUserMonthlysData("error")
     })
   },
   prepareAccessData(data){
     if (data === "error")
     {
        this.accessLevelSeries = ["error"]
        this.accessLevelLabels = ["error"]
     }
     else if(data === [])
     {
        this.accessLevelSeries = []
        this.accessLevelLabels = []
     }
     else{
        let series = [] 
        let labels= [];
        data.forEach(element => {
          series.push(element.count)
          labels.push(element._id)
        });

        this.accessLevelSeries = series
        this.accessLevelLabels = labels
     }
     
   },
   prepareUserMonthlysData(data){
     // TODO MAKE NO DATA AND ERROR CASES
     let categories = Object.keys(data)
     let series = Object.values(data)
     
     this.monthlyUserCategories = categories
     this.monthlyUserSeries.push( {
       "name": "Monthly Registered Users",
       data: series
     })
   },
   prepareIncreaseRatio(data){
     // TODO MAKE NO DATA AND ERROR CASES
     const monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"];
    let thismonth = ""
    let nextmonth = ""
    let thisMonthData = ""
    let nextMonthData = ""
    let ratio = 0
    let seriesData = []
    let labelsData = []
    let d = new Date();
    let cm = d.getMonth();
    cm = parseInt(cm, 10)
      console.log(cm)
    for(let i=cm-3; i<cm; i++){
        thismonth = monthNames[i]
        nextmonth = monthNames[i+1]
        thisMonthData = data[thismonth]
        nextMonthData = data[nextmonth]
        if (thisMonthData === 0 || nextMonthData === 0)
        {
          ratio = 0
        }
        else{
          ratio = (nextMonthData * 100) / thisMonthData
        }
        seriesData.push(ratio)
        labelsData.push(thismonth + "-" + nextmonth)
    }
    this.monthlyUserRatioLabels = labelsData.reverse()
    this.monthlyUserRatioSeries = seriesData.reverse()
    
   }
 }


}
</script>

<style>
.line_chart_card{
  width: 100%;
}
.radial_bar_chart{
  width: 100%;
  display: grid;
  place-items: center;
}
.pie_chart{
   width: 100%;
  display: grid;
  place-items: center;
}

</style>