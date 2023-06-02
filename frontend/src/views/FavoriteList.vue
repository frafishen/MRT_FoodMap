<template>
  <div class="favorite">
    Favorite List
    <div class="favorite-list">
      <table>
        <tbody>
          <tr v-for="favorite in this.favoriteList" :key="favorite.FListID">
            <td>{{ favorite.Name }}</td>
          </tr>
        </tbody>
      </table>
      <!-- <div v-for="favorite in favorites" :key="favorite.id">
        <span class="favorite-name">{{ favorite.name }}</span>
        <button
          class="heart-button"
          :class="{ 'active': favorite.isFavorite }"
          @click="toggleFavorite(favorite)"
        ></button>
      </div> -->
    </div>
    <!-- <button @click="goTo">添加最愛</button> -->
  </div>
</template>

<script>
import axios from 'axios'
// import { computed } from 'vue'
// import { useStore } from 'vuex'

export default {
  name: 'FavoriteList',
  data () {
    return {
      favoriteList: null
    }
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
      } catch (error) {
        console.error(error)
        this.favoriteList = null
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
.favorite-list {
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
