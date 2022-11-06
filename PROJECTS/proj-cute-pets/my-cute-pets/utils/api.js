import axios from 'axios'
const getToken = function() {
  if (process.server) {
    // server side
    return
  }
  if (window.$nuxt) {
    return window.$nuxt.$auth.getToken('local')
  }
}

export async function request(method_in, url_in, data_in, auth_in = false) {
  const headers = {}
  if (auth_in) {
    headers['auth-token'] = getToken()
  }
  try {
    // call api
    const response = await axios({
      method : method_in,
      url: url_in,
      data: data_in,
      headers: headers_in
    })
    return response
  } catch (e) {
    return e
  }
}