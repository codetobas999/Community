// Select the database to use.
use('cutepet-demo-db');
 
db.auth_main_page.drop();
 
db.auth_main_page.insertMany([
  {'page_code':'10000', 'name':'หน้าแรก', 'title': 'หน้าแรก','icon': 'mdi-apps', 'to': '/sss','status':true},
  {'page_code':'20000', 'name':'บทความ', 'title': 'บทความ','icon': 'mdi-chart-bubble','to': '/','status':true},
  {'page_code':'30000', 'name':'ผู้เขียน', 'title': 'ผู้เขียน','icon': 'mdi-database','to': '/','status':true},
  {'page_code':'40000', 'name':'ข้อมูลลูกค้า', 'title': 'ข้อมูลลูกค้า','icon': 'mdi-database','to': '/','status':true},
  {'page_code':'50000', 'name':'ตารางนัดหมาย', 'title': 'ตารางนัดหมาย','icon': 'mdi-database','to': '/','status':true},
  {'page_code':'60000', 'name':'กิจกรรม', 'title': 'กิจกรรม','icon': 'mdi-database','to': '/','status':true},
  {'page_code':'70000', 'name':'Demo', 'title': 'Demo','icon': 'mdi-database','to': '/','status':true},
  {'page_code':'80000', 'name':'คลังยา', 'title': 'คลังยา','icon': 'mdi-database','to': '/','status':true},
  {'page_code':'90000', 'name':'หน้าแรก', 'title': 'หน้าแรก','icon': 'mdi-apps', 'to': '/sss','status':true},
  {'page_code':'100000', 'name':'สิ่งที่ต้องทำ', 'title': 'สิ่งที่ต้องทำ','icon': 'mdi-database','to': '/','status':true},
]);

db.auth_sub_page.drop();

db.auth_sub_page.insertMany([
  {'page_code':'20000', "sub_page_code":2001, "title": "บทความ1", "icon": "mdi-format-list-checks", "to": "/","status":true},
  {'page_code':'20000', "sub_page_code":2002, "title": "บทความ2", "icon": "mdi-format-list-checks", "to": "/","status":true},
  {'page_code':'30000', "sub_page_code":3001, "title": "ผู้เขียน1", "icon": "mdi-format-list-checks", "to": "/","status":true},
  {'page_code':'30000', "sub_page_code":3002, "title": "ผู้เขียน2", "icon": "mdi-format-list-checks", "to": "/","status":true},
  {'page_code':'40000', "sub_page_code":4001, "title": "แก้ไขประวัติ1", "icon": "mdi-format-list-checks", "to": "/registers/customer_info0","status":true},
  {'page_code':'40000', "sub_page_code":4002, "title": "แก้ไขประวัติ2", "icon": "mdi-format-list-checks", "to": "/registers/customer_info1","status":true},
  {'page_code':'40000', "sub_page_code":4003, "title": "แก้ไขประวัติ3", "icon": "mdi-format-list-checks", "to": "/registers/customer_info2","status":true},
  {'page_code':'40000', "sub_page_code":4004, "title": "แก้ไขประวัติ4", "icon": "mdi-format-list-checks", "to": "/registers/customer_info3","status":true},
  {'page_code':'40000', "sub_page_code":4005, "title": "แก้ไขประวัติ5", "icon": "mdi-format-list-checks", "to": "/registers/customer_info4","status":true},
  {'page_code':'40000', "sub_page_code":4006, "title": "แก้ไขประวัติ6", "icon": "mdi-format-list-checks", "to": "/registers/customer_info5","status":true},
  {'page_code':'40000', "sub_page_code":4007, "title": "แก้ไขประวัติ7", "icon": "mdi-format-list-checks", "to": "/registers/customer_info6","status":true},
  {'page_code':'40000', "sub_page_code":4008, "title": "แก้ไขประวัติ8", "icon": "mdi-format-list-checks", "to": "/registers/customer_info7","status":true},
  {'page_code':'40000', "sub_page_code":4009, "title": "แก้ไขประวัติ9", "icon": "mdi-format-list-checks", "to": "/registers/customer_info8","status":true},
  {'page_code':'40000', "sub_page_code":4010, "title": "แก้ไขประวัติ10", "icon": "mdi-format-list-checks", "to": "/registers/customer_info9","status":true},
  {'page_code':'50000', "sub_page_code":5001, "title": "ดูนัดหมาย", "icon": "mdi-format-list-checks", "to": "/appointments","status":true},
  {'page_code':'50000', "sub_page_code":5002, "title": "ดูนัดหมาย2", "icon": "mdi-format-list-checks", "to": "/appointments/apppintment_2","status":true}, 
  {'page_code':'60000', "sub_page_code":6001, "title": "ดูกิจกรรม", "icon": "mdi-format-list-checks", "to": "/activitys","status":true},
  {'page_code':'70000', "sub_page_code":7001, "title": "Demo", "icon": "mdi-format-list-checks", "to": "/demo","status":true},
  {'page_code':'80000', "sub_page_code":8001, "title": "Store", "icon": "mdi-format-list-checks", "to": "/stores","status":true},
  {'page_code':'90000', "sub_page_code":9001, "title": "สร้าง", "icon": "mdi-format-list-checks", "to": "/todo/create","status":true},
  {'page_code':'90000', "sub_page_code":9002, "title": "สร้าง2", "icon": "mdi-format-list-checks", "to": "/todo/todo1","status":true},
  {'page_code':'100000', "sub_page_code":10001, "title": "User", "icon": "mdi-format-list-checks", "to": "/admin/users","status":true},
  
]);

-------------------------------------
use('cutepet-demo-db');

db.auth_main_page.aggregate([{
  $lookup: {
    from: 'auth_sub_page',
    localField: 'page_code',
    foreignField: 'page_code',
    as: 'pages'
  }
}])