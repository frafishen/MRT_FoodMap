<template>
 <div class="parentContainer">
   <header>
     <h3>TAIPEI MRT FOOD MAP SYSTEM</h3>
   </header>

   <button @click='backTofirst' type="button" name="backToFirstPage" class="backToFirst">
     <img src="../assets/home.png" width="100" height="100"/>
   </button>

   <h1>Find Tasy Food</h1>
   <img alt="MRT route map" class="mapImage" src="https://web.metro.taipei/pages/assets/images/routemap2023n.png" width="576" height="768" />
   <div class="info">

   </div>

   <h5 >food kind</h5>
   <div class="form-row">
     <label for="types">Types</label>
     <select name="types" id="types" v-model="type">
       <option v-for="type in types" :key="type.value">
         {{ type.text }}
       </option>
     </select>
   </div>

   <button @click='showOtherData' type="button" name="BR11Button" class="StationButton" >
     <img src="../assets/BR11G16.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="BR10Button" class="StationButton" >
     <img src="../assets/BR10BL15.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="BR09Button" class="StationButton" >
     <img src="../assets/BR09R05.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="O8Button" class="StationButton" >
     <img src="../assets/O08G15.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="O7Button" class="StationButton" >
     <img src="../assets/O07BL14.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="O6Button" class="StationButton" >
     <img src="../assets/O06R07.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="R11Button" class="StationButton" >
     <img src="../assets/R11G14.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="R10Button" class="StationButton" >
     <img src="../assets/R10BL12.png" width="22" height="12"/>
   </button>
   <button @click='showOtherData' type="button" name="R08Button" class="StationButton" >
     <img src="../assets/R08G10.png" width="22" height="12"/>
   </button>
 </div>

</template>

<script>
export default {
  name: 'findTastyFood',
  data () {
    return {
      date: '',
      time: '',
      station: '',
      type: 'BBQ',
      types: [
        { text: 'BBQ', value: 'BBQ' },
        { text: 'Hot Pot', value: 'hotpot' },
        { text: 'Ramen', value: 'ramen' }
      ],
      showData: false
    }
  },
  methods: {
    backTofirst () {
      this.$router.push('/')
    },
    showOtherData () {
      // 在這裡處理顯示其他資料的邏輯
      this.showData = true // 設置showData為true以顯示其他資料
    }
  }
}
</script>
<style scoped>
 /* .parentContainer {
 position: absolute;
 } */
.mapImage {
 position: absolute;
 left: 70px;
 top: 300px;
 /* display: flex; 將圖片容器設定為彈性盒子
 justify-content: flex-start; 將圖片容器內的內容靠左對齊 */
}

.info{
  position: absolute;
 left: 700px;
 top: 300px;
 width:576px;
 height:768px;
 border:2px solid black;
 background-color: #F5F5F5;
 border-radius: 20px;
}

.backToFirst{
 position: absolute;
 right: 0;
 top: 0px;
}
.foodKindinp{
 position: absolute;
 left: 1000px; /* 調整圖片與左側的距離，您可以根據需要調整此值 */
 top: 300px;
}
.StationButton{
 background-color:white;
 border: none; /* 移除邊框 */
}

header {
 line-height: 1.5;
}
 .logo {
 display: block;
 margin: 0 auto 2rem;
}
 @media (min-width: 1024px) {
 header {
   display: flex;
   place-items: center;
   padding-right: calc(var(--section-gap) / 2);
 }
    .logo {
     margin: 0 2rem 0 0;
   }
    header .wrapper {
     display: flex;
     place-items: flex-start;
     flex-wrap: wrap;
   }
 }
</style>
