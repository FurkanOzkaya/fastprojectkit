import axios from 'axios'

const baseHttp =  process.env.VUE_BASE_HTTP_ADDRESS || "http://"
const host =  process.env.VUE_APP_BACKEND_HOST || "127.0.0.1"
const port =  process.env.VUE_APP_BACKEND_PORT || "9000"
const url_prefix =  process.env.VUE_APP_BACKEND_URL_PREFIX || "/api/v1"

export default axios.create({
    baseURL: `${baseHttp}${host}:${port}${url_prefix}`
})
