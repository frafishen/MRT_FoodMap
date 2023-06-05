<template>
    <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class="w-5/6 hero-content flex-col lg:flex-row-reverse">
        <div class="px-6 w-4/5 lg:w-1/2">
          <h1 class="text-5xl font-bold py-6 h-1/3 text-center"><span class="text-primary">Favor.i.te </span> List </h1>
          <p class="py-4 md-6 text-natural h-2/3 text-center">Food tastes even better <br> when shared with whose u love :></p>
        </div>
        <div class="px-6 w-4/5 lg:w-1/2">
          <!-- left component -->
          <div class="max-w-full">
            <!-- ========== table component ========== -->
            <StoreTable />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StoreTable from '@/components/StoreTable.vue'
import axios from 'axios'
// import { computed } from 'vue'
// import { useStore } from 'vuex'

export default {
  name: 'FavoriteList',
  data () {
    return {
      favoriteList: null,
      buttonStatus: null
    }
  },
  components: {
    StoreTable
  },
  methods: {
    fetchFavoriteList: async function () {
      const P1_ID = this.$store.state.P1_ID
      // console.log(P1_ID)
      try {
        console.log('start fetching', P1_ID)
        const response = await axios.get(`http://127.0.0.1:5000/api/favorite/${P1_ID}`)
        console.log('get response')
        this.favoriteList = response.data
        const len = this.favoriteList.length
        this.buttonStatus = new Array(len)
        for (let i = 0; i < len; i++) {
          this.buttonStatus[i] = true
        }
        console.log(this.buttonStatus)
      } catch (error) {
        console.error(error)
        this.favoriteList = null
      }
    },
    toggleColor (index) {
      this.buttonStatus[index] = !this.tableRows[index]
      if (this.tableRows[index]) { // 被按喜歡
        this.addFavorite(this.tableRows[index].storeName)
      } else {
        this.deleteFavorite(this.tableRows[index].storeName)
      }
    },
    addFavorite: async function (storeName) {
      const config = { headers: { 'Content-Type': 'application/json' } }
      const P1_ID = this.$store.state.P1_ID
      const StoreID = await axios.get(`http://127.0.0.1:5000/api/storeID/${storeName}`)
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/addFavorite', { StoreID: StoreID, P1_ID: P1_ID }, config)
        console.log(response.data)
      } catch (error) {
        console.error('An error occurred:', error)
      }
    },
    deleteFavorite: async function (storeName) {
      const config = { headers: { 'Content-Type': 'application/json' } }
      const P1_ID = this.$store.state.P1_ID
      const StoreID = await axios.get(`http://127.0.0.1:5000/api/storeID/${storeName}`)
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/deleteFavorite', { StoreID: StoreID, P1_ID: P1_ID }, config)
        console.log(response.data)
      } catch (error) {
        console.error('An error occurred:', error)
      }
    }
  },
  async mounted () {
    await this.fetchFavoriteList()
  }
  // setup () {
  //   const store = useStore()
  //   const favorites = computed(() => store.getters.favorites)
  //   console.log(store.Name)
  //   const toggleFavorite = (favorite) => {
  //     favorite.isFavorite = !favorite.isFavorite
  //     store.dispatch('removeFavorite', favorite.id)
  //   }

  //   return {
  //     favorites,
  //     toggleFavorite
  //   }
  // }
}
</script>

<style>
.favorite {
    font-style: normal;
    font-weight: 400;
    font-size: 48px;
    line-height: 77px;
    align-items: center;
    text-align: center;
    color: #363636;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.homeButton{
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
.home{
  background-color:#ffffff;
  height:65px;
  width:65px;
}

.user1{
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
.favorite-list {
  margin: 0 auto;
  width: 800px;
  height: 500px;
  padding:10px;
  background: #FFFFFF;
  border: 1px solid #000000;
  border-radius: 30px;
  overflow-y: auto; /* 啟用垂直滾動條 */
  margin-top: 10px;
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

.listItem {
  width: 700px;
  text-align: left;
  padding-left: 20px;
  font-size: 24px;
  font-weight: bold;
  border-radius: 30px;
  /* background-color: rgb(255, 239, 186); */
  margin: 0px;
}

</style>
