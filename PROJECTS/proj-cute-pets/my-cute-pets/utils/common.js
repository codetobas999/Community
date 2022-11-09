//import { request } from './api'

//const HOSTNAME = 'https://sakko-demo-api.herokuapp.com'

export function writelog(message,level = 0) {
  console.log("writelog[" + level + "] : " + message )
  return true
}
