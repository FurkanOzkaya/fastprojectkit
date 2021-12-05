import service from '../service'

export default {
    login(email, password){
        let data = {
            "email": email,
            "password": password
          }
        return service.post("/user/login/", data)
    },
    getUsers(token, date=null){
        let url = "/user/all/"
        if(date)
        {
            url = "/user/all/?date=" + date
        }
        return service.get(url, {headers: {"token": token }})
       
    },
    getUser(token)
    {
        let url = "/user/get/"
        return service.get(url, {headers: {"token": token }})
    },
    getUserMontlyRatio(token)
    {
        let url = "/user/statistic/monthly_user_ratio/"
        return service.get(url, {headers: {"token": token }})
    },
    getUserAccessLevelRatio(token)
    {
        let url = "/user/statistic/access_level_ratio/"
        return service.get(url, {headers: {"token": token }})
    }
}