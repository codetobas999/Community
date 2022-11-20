import { request } from './api'

const HOSTNAME = 'http://127.0.0.1:7000'

export async function showMenu() {
  const url = `${HOSTNAME}/menus` 
  const response = await request('get', url, {}, true) 
  return response.data
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