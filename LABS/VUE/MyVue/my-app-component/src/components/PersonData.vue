<template>
    <!--li>
        <h1>ชื่อ : {{name}}</h1>
        <button @click="showDescription(id)">ดูรายละเอียด</button> &nbsp;
        <button @click="deleteEmployee(id)">ลบข้อมูลพนักงาน</button>
        <transition name="fade">
            <div v-show="isVisible">
                <p>เงินเดือน : {{salary}} บาท, ตำแน่งงาน : {{department}}</p>
            </div>
        </transition>
    </li --> 

    <CardShow>
        <template v-slot:card-header>
            <h1>ชื่อ : {{name}}</h1>
        </template>
        <template v-slot:card-content>
           <p>เงินเดือน : {{salary}} บาท , เพศ : {{gender}}</p>
           <p>ตำแน่งงาน : {{department}}</p>
           <p>ทักษะด้านภาษา : {{skill}}</p>
        </template>
        <!--template v-slot:card-button>
            <button @click="showDescription(id)">ดูรายละเอียด</button> &nbsp;
            <button @click="deleteEmployee(id)">ลบข้อมูลพนักงาน</button>
         </template-->
         <!--template v-slot:card-content>
            <transition name="fade">
                <div v-show="isVisible">
                    <p>เงินเดือน : {{salary}} บาท, ตำแน่งงาน : {{department}}</p>
                </div>
            </transition>
        </template-->
    </CardShow> 
</template>
<!-- ******************************************************************* -->
<script>
import CardShow  from './CardShow.vue'
 
export default {
    name:"PersonData",
    components:{
      CardShow 
    },
    /*data(){
        return{
            message:"ข้อมูลพนักงาน"
        }       
    },*/
    //props:["name","salary"],
    /*methods:{
        showDescription(id){
            //console.log("Emp id = ",id)
            this.$emit("show",id) 
        },
        deleteEmployee(id){
            //console.log("Emp id = ",id)
            this.$emit("delete",id) 
        }        
    },*/
    props:{
        /*id:{
            type:Number,
            required:true
        },*/
        name:{
            type:String,
            required:true
        },
        salary:{
            type:Number,            
            default:0,
            required:true
        }, 
        department:{
            type:String,  
            required:true
        },
        gender:{
            type:String,    
        }, 
        skill:{
            type:Array,  
            required:true
        },        
        /*isVisible:{
            type:Boolean,              
            default:false,
            required:true,
        },*/            
    },
}
</script>
<!-- ******************************************************************* -->
<style scoped> 
    /*li{
        margin: 1rem 0;
        font-size: 1.25rem;
        font-weight: bold;
        background: #8ddba4;
        padding: 0.5rem;
        color: #1f1f1f;
        border-radius: 25px;
        
        
    }*/
    button{
        font: inherit;
        cursor: pointer;
        border: 1px solid #ff0077;
        background: #ff0077;
        color: white;
        padding: 0.05rem 1rem;
        box-shadow: 1px 1px 2px rgba(0,0,0,0.25);
        border-radius: 5px;
    }
    .fade-enter-from{
        opacity: 0;
    }
    .fade-enter-active{
        transition: all 1s linear;
    }
</style>
<!-- ******************************************************************* -->