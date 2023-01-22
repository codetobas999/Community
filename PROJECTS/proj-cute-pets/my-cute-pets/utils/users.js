import { request,HOSTNAME } from './api' 
export async function queryAll() {
  const url = `${HOSTNAME}/api/v1/users`
  const response = await request('get', url, {}, true) 
  return response.data
}


export function create(item) {  
  const url = `${HOSTNAME}/api/v1/users/create`
  console.log("create : " + JSON.stringify(item))
  //item.selectFlag = JSON.parse(item.select.toLowerCase())
  return request(
    'post',
    url, 
    {  
      email: item.email ,
      username: item.username ,
      password: item.password ,
      first_name: item.first_name ,
      last_name: item.last_name ,
      disabled: item.disabled
    },
    true
  )
}

export function update(item) {  
  const url = `${HOSTNAME}/api/v1/users/update`
  console.log("update : " + JSON.stringify(item))
  //const selectFlag = JSON.parse(item.select.toLowerCase())
  return request(
    'post',
    url, 
    {  
      email: item.email , 
      first_name: item.first_name ,
      last_name: item.last_name 
    },
    true
  )
}

export function destroy(id) {
  const url = `${HOSTNAME}/api/v1/users/${id}`
  return request('delete', url, {}, true)
}
