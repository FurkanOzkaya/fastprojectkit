import service from "../../service/services/UserService";

export default {
    state: {
        token: undefined
    },
    mutations: {
        updateToken(state, value) {
            state.token = value
        }
    },
    actions: {
        login(state, {email, password}) {
            return service.login(email, password)
                .then((response) => {
                    if (response.status == 200) {
                        state.commit("updateToken", response.data["access_token"]);
                        // TODO check user access level
                    }
                    else{
                        state.commit("updateToken", null);
                    }
                }).catch(()=> {
                    state.commit("updateToken", null);
                })
        },
        updateToken(state, value=null)
        {
            state.commit("updateToken", value);
        }
    },
    getters: {
        token: state => {
            return state.token
        }
    }
}