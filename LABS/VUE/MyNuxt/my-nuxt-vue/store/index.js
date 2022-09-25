import VueX from "vuex"
import axios from 'axios'

const createStore=()=>{
    return new VueX.Store({
        state:{//ข้อมูล
            loadData : []
        },
        mutations:{//จัดการข้อมูลใน State
            setPostState(state,posts){
                console.log("setPostState");
                state.loadData = posts
            },
            addPostState(state,posts){
                console.log("addPostState");
                state.loadData.push(posts)
            },
            editPostState(state,editPost){
                console.log("editPostState : " + editPost.id);
                //find Index in loadData for  edit 
                const postIndex = state.loadData.findIndex((item) => item.id === editPost.id);
                //const postIndex = state.loadData.filter((item) => item.id !== editPost.id); 

                console.log("postIndex : " + postIndex);
                state.loadData[postIndex]=editPost; 
            },
            deletePostState(state,editPost){
                console.log("deletePostState : " + editPost.id);
                //find Index in loadData for  edit  
                state.loadData = state.loadData.filter((item) => item.id !== editPost.id);  
            }
        },
        actions:{//ทำงานร่วมกับ backend เรียกใช้ผ่าน component
            nuxtServerInit(vuexContext,context){
                console.log("เริ่มต้นโหลดข้อมูล");
                return axios.get("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json")
                       .then(res=>{
                       const data=[];
                       for(const key in res.data){
                            data.push({...res.data[key],id:key})
                       }
                       vuexContext.commit("setPostState",data) 
                }).catch(e=>context.error(e)) 
            },
            addPost(vuexContext,context){
                //รับค่าที่ส่งมาจากการใช้คำสั่ง dispatch 
                const createPost = {...context}
                //API POST
                return axios.post("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json",createPost)
                .then(res=>{
                    //console.log("Response",res.data);
                    vuexContext.commit("addPostState",{...createPost,id:res.data.name}) 
                })
            },
            editPost(vuexContext,context){
                //รับค่าที่ส่งมาจากการใช้คำสั่ง dispatch 
                //const editPost = {...context}
                //API PUT
                return axios.put("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts/"+ context.id +".json",context)
                .then(res=>{
                    //console.log("...editPost",res.data);
                    vuexContext.commit("editPostState",{...context}) 
                })
            },
            deletePost(vuexContext,context){
                //รับค่าที่ส่งมาจากการใช้คำสั่ง dispatch  
                //API PUT
                return axios.delete("https://nuxt-demo-9d201-default-rtdb.asia-southeast1.firebasedatabase.app/posts/"+ context.id +".json",context)
                .then(res=>{
                    //console.log("...deletePost",res.data);
                    vuexContext.commit("deletePostState",{...context}) 
                })
            }
        },
        getters:{//นำ state ไปใช้งาน
            getAllPosts(state){
                return state.loadData
            }
        }
    })
}
export default createStore