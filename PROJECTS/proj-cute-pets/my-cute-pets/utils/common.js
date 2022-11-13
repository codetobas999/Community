//import { request } from './api'

//const HOSTNAME = 'https://sakko-demo-api.herokuapp.com'
//import { showMenu } from './authorize'

export function writelog(message,level = 0) {
  console.log("writelog[" + level + "] : " + message )
  return true
}

export function getMenus() { 
  //console.log("getMenusXXXXX : " + JSON.stringify(showMenu()) )        
  return [  
    // { icon: 'mdi-apps', title: 'Welcome', to: '/' },
    // { icon: 'mdi-chart-bubble', title: 'Inspire', to: '/inspire' },
              {id:1000, name:"หน้าแรก", title: 'หน้าแรก',icon: 'mdi-apps', to: '/sss',isAuthen:true,
              pages: []  
              },
              {id:2000, name:"บทความ", title: 'บทความ',icon: 'mdi-chart-bubble',to: '/',isAuthen:true, 
              pages: [ {id:2001, title: 'บทความ1', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                     {id:2002, title: 'บทความ2', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                     ]  
              },    
              {id:3000, name:"ผู้เขียน", title: 'ผู้เขียน',icon: 'mdi-database',to: '/',isAuthen:true, 
              pages: [ {id:3001, title: 'ผู้เขียน1', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                     {id:3002, title: 'ผู้เขียน2', icon: 'mdi-format-list-checks', to: '/',isAuthen:true},
                     ]  
              },
              {id:4000, name:"ข้อมูลลูกค้า", title: 'ข้อมูลลูกค้า',icon: 'mdi-database',to: '/',isAuthen:true, 
              pages: [ {id:4001, title: 'เพิ่มประวัติ', icon: 'mdi-format-list-checks', to: '/registers',isAuthen:true},
                     {id:4002, title: 'แก้ไขประวัติ2', icon: 'mdi-format-list-checks', to: '/registers/customer_info',isAuthen:true},
                     {id:4003, title: 'แก้ไขประวัติ3', icon: 'mdi-format-list-checks', to: '/registers/customer_info2',isAuthen:true},
                     {id:4004, title: 'แก้ไขประวัติ4', icon: 'mdi-format-list-checks', to: '/registers/customer_info3',isAuthen:true},
                     {id:4005, title: 'แก้ไขประวัติ5', icon: 'mdi-format-list-checks', to: '/registers/customer_info4',isAuthen:true},
                     {id:4006, title: 'แก้ไขประวัติ6', icon: 'mdi-format-list-checks', to: '/registers/customer_info5',isAuthen:true},
                     {id:4007, title: 'แก้ไขประวัติ7', icon: 'mdi-format-list-checks', to: '/registers/customer_info6',isAuthen:true},
                     {id:4008, title: 'แก้ไขประวัติ8', icon: 'mdi-format-list-checks', to: '/registers/customer_info7',isAuthen:true},
                     {id:4009, title: 'แก้ไขประวัติ9', icon: 'mdi-format-list-checks', to: '/registers/customer_info8',isAuthen:true},
                     ]  
              }, 
              {id:5000, name:"ตารางนัดหมาย", title: 'ตารางนัดหมาย',icon: 'mdi-database',to: '/',isAuthen:true, 
              pages: [ {id:5001, title: 'ดูนัดหมาย', icon: 'mdi-format-list-checks', to: '/appointments',isAuthen:true},
                       {id:5002, title: 'ดูนัดหมาย2', icon: 'mdi-format-list-checks', to: 'appointments/apppintment_2',isAuthen:true},       
                     ]  
              },     
              {id:6000, name:"กิจกรรม", title: 'กิจกรรม',icon: 'mdi-database',to: '/',isAuthen:true, 
              pages: [ {id:6001, title: 'ดูกิจกรรม', icon: 'mdi-format-list-checks', to: '/activitys',isAuthen:true}, 
                     ]  
              },  
              {id:7000, name:"Demo", title: 'Demo',icon: 'mdi-database',to: '/',isAuthen:true, 
              pages: [ {id:7001, title: 'Demo', icon: 'mdi-format-list-checks', to: '/demo',isAuthen:true}, 
                     ]  
              }, 
              {id:8000, name:"คลังยา", title: 'คลังยา',icon: 'mdi-database',to: '/',isAuthen:true, 
              pages: [ {id:8001, title: 'Store', icon: 'mdi-format-list-checks', to: '/stores',isAuthen:true}, 
                     ]  
              }, 
        ] 
}

