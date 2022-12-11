import { request } from './api'

const HOSTNAME = 'http://127.0.0.1:8000'
/*
export async function showMenu() {
  const url = `${HOSTNAME}/menus` 
  const response = await request('get', url, {}, true) 
  return response
}*/
export async function queryAll() {
  const url = `${HOSTNAME}/api/v1/auth_page`
  const response = await request('get', url, {}, true) 
  return response.data
}


export function create(item) {  
  const url = `${HOSTNAME}/api/v1/auth_page/create`
  console.log("create : " + JSON.stringify(item))
  //item.selectFlag = JSON.parse(item.select.toLowerCase())
  return request(
    'post',
    url, 
    { 
      page_code: item.page_code ,
      menu_name_en: item.menu_name_en ,
      menu_name_th: item.menu_name_th ,
      icon: item.icon ,
      to: item.to ,   
      status: item.status
    },
    true
  )
}

export function update(item) {  
  const url = `${HOSTNAME}/api/v1/auth_page/${item.auth_page_id}`
  console.log("update : " + JSON.stringify(item))
  //const selectFlag = JSON.parse(item.select.toLowerCase())
  return request(
    'put',
    url, 
    { 
      page_code: item.page_code ,
      menu_name_en: item.menu_name_en ,
      menu_name_th: item.menu_name_th ,
      icon: item.icon ,
      to: item.to ,   
      status: item.status
    },
    true
  )
}

export function destroy(id) {
  const url = `${HOSTNAME}/api/v1/auth_page/${id}`
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