<template>
    <b-container fluid="md" class="py-2">
        <h2 align="center">เขียนบทความ</h2>
        
        <b-form > 
       
        <!--
        <b-form @submit.prevent="onSubmit" @reset="onReset">    
         -->
            <b-form-group label="ชื่อบทความ">
                <b-form-input type="text" placeholder="ชื่อบทความ" v-model="form.title" ></b-form-input>
            </b-form-group>

            <b-form-group label="รายละเอียดบทความ">
                <b-form-textarea type="text" placeholder="รายละเอียดบทความ" rows=8 v-model="form.content"></b-form-textarea>
            </b-form-group>    

            <b-form-group label="รูปภาพ(URL)">
                <b-form-input type="text" placeholder="ระบุรูปถาพ" v-model="form.image"></b-form-input>
            </b-form-group>    

            <b-form-group label="ผู้เขียน">
                <b-form-input type="text" placeholder="นามปากกา" v-model="form.author" ></b-form-input>
            </b-form-group>  

            <!--
            <b-button type="submit" variant="primary">บันทึก</b-button>
            <b-button type="reset" variant="warning">ล้าง</b-button> 
            -->
            
            <b-button @click="addPost" variant="primary" v-show="! form.id">เพิ่ม</b-button>
            <b-button @click="savePost" variant="primary" v-show="form.id">บันทึก</b-button>
            <b-button @click="claerPost" variant="warning" >ล้าง</b-button>             
            <b-button @click="deletePost" variant="danger" v-show="form.id">ลบ</b-button>
            

        </b-form> 
        <b-card header="result" class="mt-3">
            {{form}}
        </b-card>
    </b-container>
</template>

<script>
export default {
    data(){
        return{
            form:this.post?{...this.post}:
            { 
                title:"",
                content:"",
                image:"",
                author:"",
            }
        }
    },
    methods:{
        /*onSubmit(evt){            
            this.$emit('sendData',this.form) //ส่งค่า form ไปให้ Page แม่
            this.$router.push('/admin/')
        },
        onReset(evt){
            this.$emit('sendData',this.form) //ส่งค่า form ไปให้ Page แม่
            this.$router.push('/admin/')
        }, */
        
        addPost(evt){            
            this.$emit('sendData',this.form,"Insert") //ส่งค่า form ไปให้ Page แม่
            this.$router.push('/admin/')
        },
        savePost(evt){
            this.$emit('sendData',this.form,"Update") //ส่งค่า form ไปให้ Page แม่
            this.$router.push('/admin/')
        },        
        claerPost(evt){
            //evt.preventDefault(); 
            this.form.title='';
            this.form.content='';
            this.form.image='';
            this.form.author='';

        },
        deletePost(evt){
            this.$emit('sendData',this.form,"Delete") //ส่งค่า form ไปให้ Page แม่
            this.$router.push('/admin/')
        },
    },
    props:{
        post:{
            type:Object,
            required:false
        }
    }
}
</script>
