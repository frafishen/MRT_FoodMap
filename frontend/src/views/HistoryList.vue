<template>
  <div class="history">
    History List

    <button @click="goHome" class="homeButton" type="button" name="home"><img class="home" src="../assets/home.png"></button>

    <button class="userButton" type="button" name="user" @click="goPersonal">
      <img class="user1" src="../assets/user.png"/>
    </button>

    <div class="history-list">
      <div v-for="history in histories" :key="history.id">
        <span>{{ history.name }}</span>
      </div>
    </div>

  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'HistoryList',

  setup () {
    const store = useStore()
    const histories = computed(() => store.getters.histories)

    return {
      histories
    }
  },
  methods: {

    goHome () {
      this.$router.push('/')
    },
    goPersonal () {
      this.$router.push('/person')
    }
  }
}
</script>

<style>
.history {

    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 64px;
    line-height: 77px;
    align-items: center;
    text-align: center;
    color: #363636;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.homeButton
{
background-color: transparent;
border-color: lightgray;
height:76px;
width:76px;
padding:0px;
left:1180px;
top:34px;
position:absolute;

}

.userButton{
  background-color: transparent;
  border-color: lightgray;
  width: 76px;
  height: 76px;
  left: 1072px;
  top: 34px;
  position: absolute;
}
.home
{
background-color:#ffffff;
height:65px;
width:65px;

}

.user1
{
height:65px;
width:65px;
}
.border{
  margin: 0 auto;
   width: 800px;
   height: 600px;
    padding:50px;
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 50px;
}
.history-list {
 margin: 0 auto;
  width: 800px;
 height: 500px;
    padding:50px;
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 50px;
  overflow-y: auto; /* 啟用垂直滾動條 */
}
.heart-button {
  width: 40px;
  height: 40px;
  background-image: url('../assets/redHeart.png'); /* 白色愛心圖片的路徑 */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border: none;
  outline: none;
  cursor: pointer;
}

.active {
  background-image: url('../assets/whiteHeart.png'); /* 紅色愛心圖片的路徑 */
}

</style>
