<template>
    <b-container fluid>
        <Header/>
        <PostList :posts="loadData" /> 
    </b-container>  
</template> 

<script>
import Header from '@/components/posts/Header.vue'
import PostList from '@/components/posts/PostList.vue'

export default { 
    layout:"coreLayout",
    components:{
        Header,
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
            loadData:[
               {id:"1",
                title:"เที่ยวกะบี่", 
                content:"long boat and rocks on railay beach in Krabi, Thailand",
                image:"https://media.istockphoto.com/photos/long-boat-docked-on-beach-in-krabi-thailand-summers-picture-id469733898",
                },
               {id:"2",
                title:"เที่ยวตลาดน้ำ", 
                content:"floating boats at floating market",
                image:"https://media.istockphoto.com/photos/floating-market-thailand-picture-id944871842",
                },
               {id:"3",
                title:"เที่ยวเชียงใหม่", 
                content:"The best of landscape in Chiang mai. Pagodas Noppamethanedol & Noppapol Phumsiri at sunset in Inthanon mountain, Thailand",
                image:"https://media.istockphoto.com/photos/the-best-of-landscape-in-chiang-mai-inthanon-mountain-picture-id622780072?s=612x612",
                },
               {id:"4",
                title:"เที่ยวสุราษธานี", 
                content:"Lady hold red umbrellas with arch at Khao Na Nai Luang Dharma Park in Surat Thani Thailand",
                image:"https://media.istockphoto.com/photos/lady-hold-red-umbrellas-with-arch-at-khao-na-nai-luang-dharma-park-in-picture-id1034702598",
                } 
            ]
        }
    }*/
}
</script>