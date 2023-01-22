import axios from 'axios' 
 
export const HOSTNAME = 'http://127.0.0.1:8000'
const getToken = function() {
  if (process.server) {
    // server side
    return
  }
  if (window.$nuxt) {
    return window.$nuxt.$auth.getToken('local')
  }
}

const getAPIHostName = function() {
  return this.$nuxt.context.env.config.BASE_API_URL
}




export async function request(method_in, url_in, data_in,headers_in, auth_in = false) {
  //console.log("request["+ method_in + "(Authen Flag: "+ auth_in +")] : " + url_in + ", data-in: "+ JSON.stringify(data_in) )   
  const headers = {}
  //if (auth_in) { 
    //console.log(" getToken : " + getToken() ) 
    //headers['Authorization'] = getToken()
    //console.log(" headers : " + headers.Authorization)
    
  //} 
  axios.defaults.headers.common['Authorization'] = getToken() ;
  try {
    // call api 
    const response = await axios({
      method : method_in,
      url: url_in,
      data: data_in,
      //headers: headers_in
      /*headers: {
        Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Njg3ODc3MjksInN1YiI6IjkwNmMwNDYzLTc1M2ItNDJiNS1hZDFjLTM2YzJkZDU0Y2RhZSJ9.m9P_mkVUs6LWgp9j_4A_l5keNCXOzCuw_rYuEt2YAx8'
      }*/
   })    
    //console.log("response : ",response);
    /*if(response.status == 200){
        //do something
    }
    else if(response.status == 202){
        //do something
    }
    else if(response.status == 301){
        //do something
    }*/

    return response
  } catch (e) {
      console.log("err : ",e);
    return e
  }
}