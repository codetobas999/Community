import { request,HOSTNAME } from './api'

export async function showMenu() { 
  const url = `${HOSTNAME}/api/v1/permission_user` 
  const response = await request('get', url, {}, true) 
  return response.data
 
}
 