<template>
    <AdminForm @sendData="onSubmitted" />
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
    methods:{
        onSubmitted(postData){ 
            console.log("Result",postData);
            //Call Store --> addPost
            this.$store.dispatch("addPost",postData).
            then(()=>{
                this.$router.push('/admin/posts')
            })
            
        } 
    }
}
</script>