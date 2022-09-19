<template>
  <!--img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/-->
  <section>
    <!--img v-bind:src="picture" v-bind:with="size" v-bind:height="size"/-->
    <img :src="picture" :with="size" :height="size" ref="imageEL" /><br />

    <form @submit.prevent="submitForm">
      <label>ป้อนชื่อเล่น :</label>
      <!--input type="text" v-on:input="setNickName" ref="nickNameEL"/-->
      <input type="text" ref="nickNameEL" />
      <button type="submit">บันทึก</button>
    </form>

    <!--ป้อนชื่อเล่น : <input type="text" v-on:input="setNickName" /-->
    <!--h2>ชื่อ-นามสกุล : {{ getFullName() }}</!--h2-->
    <h2>ชื่อ-นามสกุล : {{ getFullName }}</h2>
    <h2>ชื่อเล่น : {{ nickName }}</h2>
    <h2>อายุ : {{ age }} ปี</h2>
    <h2>เงินเดือน : {{ salary }} บาท</h2>
    <h2>รายได้ต่อปี : {{ getIncome }} บาท</h2>
    <h2>ตำแหน่งงาน : {{ getDepartment }} </h2>
    <button @click="addSalary(5000)">เพิ่มเงินเดือน</button>
    <button @click="delSalary(5000)">ลดเงินเดือน</button>
    <!--h2>Method1 : {{ getRandomByMethod() }} </h2>
    <h2>Method2 : {{ getRandomByMethod() }} </h2>
    <hr/>
    <h2>Computed1 : {{ getRandomByComputed }} </h2>
    <h2>Computed2 : {{ getRandomByComputed }} </h2> -->

    <button @click="toggleVisible()"> {{isVisible ? "ซ่อน" : "แสดง"}}รายละเอียด</button>

    <article v-show="isVisible">
      <p>ที่อยู่ : <span v-html="address"></span></p>
      <a href="social" target="_blank">Facebook</a>
      <p>งานอดิเรก :</p>
      <ul>
        <li>{{ hobby[0] }}</li>
        <li>{{ hobby[1] }}</li>
        <li>{{ hobby[2] }}</li>
      </ul>
      <p>ข้อมูลพื้นฐาน :</p>
      <ul>
        <li>เพศ :{{ general.gender }}</li>
        <li>น้ำหนัก :{{ general.weight }} kg</li>
        <li>ความสูง :{{ general.height }} cm</li>
        <li>โรคประจำตัว :{{ general.status }}</li>
      </ul>
      <p v-if="books.length === 0">หนังสือที่ชอบ : ไม่มี</p>
      <div v-else>
        <p>หนังสือที่ชอบ :</p>
        <ul>
          <li v-for="(item, index) in books" :key="index">
            {{ index + 1 }} : {{ item }}
          </li>
        </ul>
      </div>

      <p>กีฬาที่ชอบ :</p>
      <ul>
        <li v-for="(item, key, index) in sports" :key="key">
          {{ index + 1 }}.{{ key }} : {{ item }}
        </li>
      </ul>

      <!--button v-on:click="showData()">คลิกเพื่อดูข้อมูล</button-->
      <button @click="showData()">คลิกเพื่อดูข้อมูล</button>
      <button @click.ctrl="increment(10)">เพิ่มอายุ</button>
      <button @click.middle="decrement(10)">ลดอายุ</button>
    </article>
  </section>
</template>

<!-- **************************************************************************************** -->
<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: "App",
  //components: {
  //  HelloWorld
  //}
  data() {
    return {
      firstName: "Somsak",
      lastName: "Somboonpunpiput",
      nickName: "",
      age: 41,
      address: "<i>กรุงเทพมหานคร</i>",
      picture: "https://cdn-icons-png.flaticon.com/512/1144/1144709.png",
      size: 150,
      social: "https://www.facebook.com/",
      hobby: ["ดูหนัง", "ฟังเพลง", "ขับรถ"],
      general: { gender: "ชาย", weight: 107, height: 167, status: false },
      books: ["Python", "Go", "Vue", "Oracle"],
      sports: { sportName: "บาสเกตบอล", players: 5, time: 20, status: false },
      isVisible:false,
      salary:20000
    };
  },
  methods: {
    /*getFullName() {
      return this.firstName + " " + this.lastName;
    },*/
    showData() {
      alert(this.firstName);
    },
    increment(value) {
      this.age += value;
    },
    decrement(value) {
      this.age -= value;
    },
    /*setNickName(event){
      //console.log(event.target.value)
      this.nickName = event.target.value
    },*/
    submitForm() {
      //event.preventDefault();
      this.nickName = this.$refs.nickNameEL.value;
      //alert("บันทึกชือเล่นเรียบร้อย")
    },
    toggleVisible(){
      this.isVisible = !this.isVisible
    },
    addSalary(value){
      this.salary += value
    },
    delSalary(value){
      this.salary -= value
    },
    /*getRandomByMethod(){
      return Math.random()
    },*/
  },
computed:{
    getFullName() {
      return this.firstName + " " + this.lastName;
    },
    getIncome(){
      return this.salary *12
    },
    getDepartment(){
      return this.salary >= 35000 ? "Project Manager" : "Programmer"
    },
    /*getRandomByComputed(){
      return Math.random()
    },*/
  },
watch:{
    salary(value){
      if(value > 50000){
        alert("เงินเดือนไม่ควรเกิน 50,000 บาท")
        setTimeout(()=>{
          this.salary=50000
        },2000)
      }
    }
},  
};
</script>

<!-- **************************************************************************************** -->
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
<!-- **************************************************************************************** -->