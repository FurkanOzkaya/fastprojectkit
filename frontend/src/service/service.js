import axios from 'axios'

const host =  process.env.VUE_APP_BACKEND_HOST || "127.0.0.1"
const port =  process.env.VUE_APP_BACKEND_PORT || "9000"
const url_prefix =  process.env.VUE_APP_BACKEND_URL_PREFIX || "/api/v1"

export default axios.create({
    baseURL: `http://${host}:${port}${url_prefix}`
})
