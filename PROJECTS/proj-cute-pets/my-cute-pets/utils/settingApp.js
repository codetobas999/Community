import { request,HOSTNAME } from './api'
 
export async function queryByUser() {
  const url = `${HOSTNAME}/api/v1/setting_app_by_user/user`
  const response = await request('get', url, {}, true)  
  return response.data
}

export async function queryAll() {
  const url = `${HOSTNAME}/api/v1/setting_app_by_user`
  const response = await request('get', url, {}, true) 
  return response.data
}

export function create(item) {  
  const url = `${HOSTNAME}/api/v1/auth_user_group/create`
  console.log("create : " + JSON.stringify(item))
  //item.selectFlag = JSON.parse(item.select.toLowerCase())
  return request(
    'post',
    url, 
    { 
      user_code: item.user_code ,
      group_code: item.group_code ,  
      status: item.status
    },
    true
  )
}

export function update(item) {  
  const url = `${HOSTNAME}/api/v1/auth_user_group/${item.auth_user_id}`
  console.log("update : " + JSON.stringify(item))
  //const selectFlag = JSON.parse(item.select.toLowerCase())
  return request(
    'put',
    url, 
    { 
      user_code: item.user_code ,
      group_code: item.group_code ,  
      status: item.status
    },
    true
  )
}

export function destroy(id) {
  const url = `${HOSTNAME}/api/v1/auth_user_group/${id}`
  return request('delete', url, {}, true)
}

/*
export function show(id) {
  const url = `${HOSTNAME}/api/v1/user/blogs/${id}`
  return request('get', url, {}, true)
}

export function create(title, body) {
  const url = `${HOSTNAME}/api/v1/user/blogs`
  return request(
    'post',
    url,
    {
      blog: { title, body }
    },
    true
  )
}

export function update(id, title, body) {
  const url = `${HOSTNAME}/api/v1/user/blogs/${id}`
  return request(
    'put',
    url,
    {
      blog: { title, body }
    },
    true
  )
}

export function destroy(id) {
  const url = `${HOSTNAME}/api/v1/user/blogs/${id}`
  return request('delete', url, {}, true)
}*/