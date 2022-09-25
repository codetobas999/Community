<template>
    <div>        
        <b-carousel id="slider" :interval="3000" controls indicators >
            <div v-for="(item,index) in items" :key="index">
                <b-carousel-slide  
                :caption=item.caption
                :text=item.text
                :img-src=item.image  
                ></b-carousel-slide>
            </div>
        </b-carousel>        
    </div>   
</template>

 <script> 
 export default {
  components: {  },
    data(){
        return{
            items:[
                {caption:"A", text:"Nulla vitae elit libero, a pharetra augue mollis interdum.",image:require("@/assets/images/p1.jpg")},
                {caption:"B", text:"Nulla vitae elit libero, a pharetra augue mollis interdum.",image:require("@/assets/images/p2.jpg")},
                {caption:"C", text:"Nulla vitae elit libero, a pharetra augue mollis interdum.",image:require("@/assets/images/p3.jpg")}
            ]
        }
    }
 }
 </script>