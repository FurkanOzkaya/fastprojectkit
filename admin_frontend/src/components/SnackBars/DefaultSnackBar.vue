<template>
    <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="blue"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
</template>

<script>
export default {
    data(){
        return {
            snackbar: true,
            timeout: 3000,
        }
    },
    method:{
        display(text)
        {
            this.text = text
            this.snackbar = true
        }
    }
}
</script>

<style>

</style>