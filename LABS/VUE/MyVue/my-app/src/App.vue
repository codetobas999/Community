<template>
  <!--img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/-->
    <section>
      <!--img v-bind:src="picture" v-bind:with="size" v-bind:height="size"/-->
      <img :src="picture" :with="size" :height="size"/>
      <h1>ชื่อ-นามสกุล : {{getFullName()}}</h1>
      <h1>อายุ : {{age}} ปี</h1>
      <p>ที่อยู่ : <span v-html="address"></span></p>
      <a href="social" target="_blank">Facebook</a>
      <p>งานอดิเรก :</p>
      <ul>
        <li>{{hobby[0]}}</li>
        <li>{{hobby[1]}}</li>
        <li>{{hobby[2]}}</li>
      </ul>   
      
    </section>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  //components: {
  //  HelloWorld
  //}
  data(){
    return{
      firstName:"Somsak",
      lastName:"Somboonpunpiput",
      age:41,
      address:"<i>กรุงเทพมหานคร</i>",
      picture:"https://cdn-icons-png.flaticon.com/512/1144/1144709.png",
      size:150,
      social:"https://www.facebook.com/",
      hobby:["ดูหนัง","ฟังเพลง","ขับรถ"]
    }
  },
  methods:{
    getFullName(){
      return this.firstName + ' ' + this.lastName
    }
  }
}
</script>

<style>
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
*/
</style>
