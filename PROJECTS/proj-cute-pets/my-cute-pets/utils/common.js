import { showMenu } from './permission'

export function writelog(message,level = 0) {
  console.log("writelog[" + level + "] : " + message )
  return true
}

export async function getMenus() { 
  console.log("getMenus")    
  const data = []
  const json_data = await showMenu()  
  for (var i = 0; i < json_data.length; i++) { 
       data.push(json_data[i]); 
  } 

  //const xx = Object.keys(json_data).map((key) => [key, json_data[key]]);
  //console.log("xx : " + JSON.stringify(xx) )  
  //console.log(data) 
  /*//const yy = JSON.parse('{"id":1000, "name":"หน้าแรก", "title": "หน้าแรก","icon": "mdi-apps", "to": "/sss","isAuthen":"true"}')
  const yy = JSON.parse(xx)
  const z = '{"id":1000, "name":"หน้าแรก", "title": "หน้าแรก","icon": "mdi-apps", "to": "/sss","isAuthen":"true" ,"pages": [] }'
  console.log("z : " + z )  
  const zz = JSON.parse(z)
  console.log("yy : " + yy ) 
  console.log(typeof xx);
  console.log(typeof yy);
  console.log(typeof zz);
  console.log("getMenusXXXXX End")         
  //return JSON.stringify(await showMenu())*/
  return data

}

