<template>
  <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class="w-5/6 hero-content flex-col lg:flex-row-reverse">
        <div class="px-6 w-full lg:w-1/2">
          <h1 class="text-center text-5xl font-bold py-6">Find Tasty <span class="text-primary">F.o^o.d </span></h1>
          <div class="w-full flex flex-row justify-between">
            <!-- button with a arror point to left -->
            <button class="flex justify-start btn btn-ghost hover:bg-primary hover:text-white" @click="showMap = true"><p>&larr;</p></button>
            <!-- selection bar -->
            <select class="flex justify-end select select-primary w-full max-w-xs">
              <option disabled selected class="text-primary">What do .u. want to eat today?</option>
              <option v-for="[key, value] in Object.entries(foodTypes)" :key="key">
                {{ value }}
              </option>
            </select>
          </div>
          <!-- ========== table component ========== -->
          <div class="overflow-x-auto w-full mt-4">
            <table class="table w-full">
              <!-- head -->
              <tbody>
                <!-- row 1 -->
                <tr v-for="(row, index) in tableRows" :key="index">
                  <td>
                    <div class="flex items-center space-x-3">
                      <div>
                        <div class="font-bold">{{ row.storeName }}</div>
                        <div class="rating rating-xs">
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" checked />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                        </div>
                      </div>
                    </div>
                  </td>
                  <td>
                    {{ row.address }}
                    <br />
                    <a role="button" class="badge badge-ghost badge-sm" href="https://www.google.com/">Go to Map</a>
                  </td>
                  <th>
                    <button class="btn btn-ghost btn-xs" @click="toggleMap">Details</button>
                  </th>
                  <th>
                    <button
                      name="add fav"
                      type="submit"
                      class="btn btn-sm mask mask-heart transition-colors duration-200"
                      :class="{ 'bg-red-400': row.isClicked, 'bg-gray-400': !row.isClicked }"
                      @click="toggleColor(index)"
                    ></button>
                  </th>
                </tr>
                <!-- row end -->
              </tbody>
            </table>
          </div>
          <!-- ========== table component end ========== -->
        </div>
        <div class="px-6 w-full py-4 lg:w-1/2">
          <!-- left conponent -->
          <div class="max-w-full" v-if="showMap">
            <FoodMap />
          </div>
          <div class="max-w-full" v-if="!showMap">
            <StoreDetailArea />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// import Store Table component
import FoodMap from '@/components/FoodMap.vue'
import StoreDetailArea from '@/components/StoreDetailArea.vue'
import axios from 'axios'

// async function modifyFavorite (id, isClicked) {
//   try {
//     var config = { headers: { 'Content-Type': 'application/json' } }
//     if(isClicked) { // already in fav list
//       // delete from fav list
//       const response = await axios.delete('http://localhost:5000/api/deleteFavorite', { PersonID: this.personID, StationID: this.stationName }, config)
//       console.log(response.data)
//       this.modifyFavoriteStatus = response.data
//     } else  {// not in fav list
//       // add to fav list
//       const response = await axios.post('http://localhost:5000/api/addFavorite', { PersonID: this.personID, StationID: this.stationName }, config)
//       console.log(response.data)
//       this.modifyFavoriteStatus = response.data
//     }
//   } catch (error) {
//     console.error('An error occurred:', error)
//   }
// }

// get store with food type

export default {
  name: 'findTastyFood',
  data () {
    return {
      foodTypes: {
        BBQ: 'BBQ',
        hotpot: 'Hot Pot',
        ramen: 'Ramen'
      },
      showMap: true,
      // todo: get data from db
      tableRows: [
        {
          storeName: '麵屋武藏',
          address: 'Address 1',
          isClicked: false
        },
        {
          storeName: 'Store 2',
          address: 'Address 2',
          isClicked: false
        },
        {
          storeName: 'Store 3',
          address: 'Address 3',
          isClicked: false
        }
      ],
      modifyFavoriteStatus: null
    }
  },
  components: {
    FoodMap,
    StoreDetailArea
  },
  methods: {
    toggleColor (index) {
      this.tableRows[index].isClicked = !this.tableRows[index].isClicked
      if (this.tableRows[index].isClicked) { // 被按喜歡
        this.addFavorite(this.tableRows[index].storeName)
      } else {
        this.deleteFavorite(this.tableRows[index].storeName)
      }
    },
    toggleMap () {
      this.showMap = false
      console.log(this.showMap)
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
  }
}
</script>
<style>
</style>
