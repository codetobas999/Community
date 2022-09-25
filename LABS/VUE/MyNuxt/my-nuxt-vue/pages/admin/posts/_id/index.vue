<template>
    <!--
    <AdminForm @sendData="onSubmitted" @delData="deletePost" :post="singlePost" />
    -->
    <AdminForm @sendData="onSubmitted" :post="singlePost" />
</template> 

<script>
import AdminForm from '@/components/admin/AdminForm.vue'
import axios from 'axios'
axios 
export default { 
    layout:"coreLayout",
    components:{
        AdminForm 
    },
    asyncData(context){
        return axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts/"+ context.params.id +".json")
                       .then(res=>{
                       return {
                        singlePost:{
                            ...res.data,id:context.params.id
                        }
                       }
                }).catch(e=>context.error(e)) 
    },
    methods:{
        onSubmitted(postData,actionType){ 
            console.log("Result",postData);
            //Call Store --> addPost
            //this.$store.dispatch("addPost",postData).
            if(actionType === "Update"){
                this.$store.dispatch("editPost",postData).
                then(()=>{
                    this.$router.push('/admin/posts')
                })
            }else if(actionType === "Delete"){
                this.$store.dispatch("deletePost",postData).
                then(()=>{
                    this.$router.push('/admin/posts')
                })                
            }else{
                console.log("Error actionType Found :",actionType);
            }   
        } 
    }
}
</script>