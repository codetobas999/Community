<template>
    <b-container fluid class="mt-3"> 
        <nuxt-link to="/admin/posts" class="btn btn-primary">ดูบทความ</nuxt-link>
        <nuxt-link to="/admin/posts/create" class="btn btn-success">เขียนบทความ</nuxt-link>
    </b-container>  
</template> 
 


<script> 
import PostList from '@/components/posts/PostList.vue'
export default { 
    layout:"coreLayout",
    components:{ 
        PostList
    }
}
</script>