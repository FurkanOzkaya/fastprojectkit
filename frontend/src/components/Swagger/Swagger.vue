<template>
   <div>
    <div id="swagger-ui"></div>
  </div>
</template>

<script>
import SwaggerUIBundle from 'swagger-ui'
import 'swagger-ui/dist/swagger-ui.css'

export default {
  name: 'console',
  data () {
    return {
      error: false,
      baseHttp: process.env.VUE_BASE_HTTP_ADDRESS || "http://",
      host:  process.env.VUE_APP_BACKEND_HOST || "127.0.0.1",
      port:  process.env.VUE_APP_BACKEND_PORT || "9000",
      prefix:  process.env.VUE_APP_BACKEND_SWAGGER_PREFIX || "openapi.json",
      url: ""
    }
  },
  created () {
  },
  mounted () {
    this.url = `${this.baseHttp}${this.host}:${this.port}/${this.prefix}`
    this.dispatchSwagger()
  },
  methods: {
    dispatchSwagger () {
      SwaggerUIBundle({
        url: this.url ,
        dom_id: '#swagger-ui',
        deepLinking: false,
        options:this.options,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        plugins: [
          SwaggerUIBundle.plugins.DownloadUrl,
        ]
      })
    }
  }
}
</script>

<style>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#swagger-ui {
  text-align: left;
}


</style>