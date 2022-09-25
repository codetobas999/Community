<template>
    <b-container fluid> 
        <PostList isAdmin :posts="loadData" /> 
       <!-- <b-button @click="postsAll" >Load..</b-button> -->
    </b-container>  
</template> 

<script> 
import PostList from '@/components/posts/PostList.vue'
import axios from 'axios'
export default { 
    layout:"coreLayout",
    components:{ 
        PostList
    },
    computed:{
        loadData(){
            return this.$store.getters.getAllPosts
        }
    }
    /*
    data(){
        return{
            loadData:[]
        }
    },*/
    /* asyncData(context){
        console.log("เริ่มต้นโหลดข้อมูล");
        return axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json")
               .then(res=>{
               const data=[];
               for(const key in res.data){
                    data.push({...res.data[key],id:key})
               }
               return {
                    loadData:data
               }
        }) 
    }*/
    /*asyncData(context){ //Promise
        return new Promise((resolve,reject)=>{
                setTimeout(()=>{
                    const data = axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json")
                    .then(res=>{
                        const data=[];
                         for(const key in res.data){
                             data.push({...res.data[key],id:key})
                         }
                        return {
                            loadData:data
                        }
                     })
                     resolve(data) //Get Data Success
                },4000)
        }) 
    }*/
    /*asyncData(context){
        console.log("เริ่มต้นโหลดข้อมูล");
        return axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json")
               .then(res=>{
               const data=[];
               for(const key in res.data){
                    data.push({...res.data[key],id:key})
               }
               return {
                    loadData:data
               }
        }) 
    }*/
    /*
    methods:{
        
        async postsAll(){ //await async
            //API GET
            console.log("เริ่มต้นโหลดข้อมูล");
            await axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json")
            .then(res=>{
                console.log("Response",res);
            })
            console.log("โหลดข้อมูลเสร็จเรียบร้อย");
        }
        
        async postsAll(){ //Promise
            console.log("เริ่มต้นโหลดข้อมูล");
            await this.getData().then((res)=>{
                 console.log("Response",res);
            })
            console.log("โหลดข้อมูลเสร็จเรียบร้อย");
        } ,
        getData(){ //Promise
            //API GET
            return new Promise((resolve,reject)=>{
                    setTimeout(()=>{
                    const data = axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json")
                    .then(res=>{
                        return res
                     })
                     resolve(data) //Get Data Success
                     },4000)
            })            
        }        
    }*/
}
</script>