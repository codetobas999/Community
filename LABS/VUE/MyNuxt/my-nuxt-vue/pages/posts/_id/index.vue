<template>
    <SinglePost :post="singlePost" />
</template> 

<script> 
import SinglePost from '@/components/posts/SinglePost.vue'
import axios from 'axios'

axios 
export default { 
    layout:"coreLayout",
    components:{
        SinglePost 
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
    }
}
</script>