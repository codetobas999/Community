<template>
         <ul >              
            <person-data 
                v-for="(item,index) in employees" 
                :key="index"  
                :name="item.name"
                :salary="item.salary"
                :department="item.department"    
                :gender="item.gender"
                :skill="item.skill"            
            />           
        </ul>
        <!--ul >  
            <person-data 
                v-for="(item) in employees" 
                :key="item.id" 
                :id="item.id"
                :name="item.name"
                :salary="item.salary"
                :department="item.department"
                :isVisible="item.isVisible"
                @show="toggleVisible"
                @delete="removeEmployee"
                
            />
            
        <ul-->  
   
        <!--
        <h1>{{message}}</h1>    
        <person-data name="บาส#1" salary=30000 />
        <person-data name="บาส#2" salary=20000 />
        <person-data name="บาส#3" salary=15000 />
        <person-data name="บาส#4" salary=18000 />
        -->
</template>
<!-- ******************************************************************* -->

<script>  
import PersonData from './PersonData.vue' 
 
export default {
    name:"ListData",
    components:{
      PersonData 
    },
    props:["employees"],
    data(){
        /*return{
            employees:[
              {id:1 ,name:"บาส#1",salary:50000,department:"โปรแกรมเมอร์1",isVisible:false },
              {id:2 ,name:"บาส#2",salary:40000,department:"โปรแกรมเมอร์2",isVisible:false },
              {id:3 ,name:"บาส#3",salary:30000,department:"โปรแกรมเมอร์3",isVisible:false },
              {id:4 ,name:"บาส#4",salary:20000,department:"โปรแกรมเมอร์4",isVisible:false }, 
            ]
        }        */
    },
    /*methods:{
        toggleVisible(emp_id){
            console.log("Emp id = ",emp_id)
            this.employees = this.employees.map((item)=>{
                if(item.id === emp_id){
                    return {...item,isVisible:!item.isVisible}                
                }
                return item
            })
        },
        removeEmployee(emp_id){
            console.log("Emp id = ",emp_id)
            this.employees = this.employees.filter(item=>{
                return item.id != emp_id
            })
        }
    },*/
    /*data(){
        return{
            message:"แสดงรายชื่อพนักงานทุกคน"
        }        
    },*/
}
</script>
<!-- ******************************************************************* -->
<style scoped>
    ul{
        list-style: none;
        margin: 1rem 0;
        padding: 0;
    }

</style>
<!-- ******************************************************************* -->