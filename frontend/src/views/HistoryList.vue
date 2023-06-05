<template>
  <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class=" w-5/6 hero-content flex-col lg:flex-row">
        <div class="px-6 w-4/5 lg:w-1/2">
          <h1 class="text-5xl font-bold py-6 h-1/3 text-center"><span class="text-primary">H.i.story </span> List </h1>
          <p class="py-4 md-6 text-natural h-2/3 text-center">People who love to eat are always the best people :></p>
        </div>
        <div class="px-6 w-4/5 lg:w-1/2">
          <!-- left component -->
          <div class="max-w-full">
            <!-- ========== table component ========== -->
            <table class="table w-full">
            <!-- head -->
            <tbody>
                <!-- row 1 -->
                <tr v-for="(history, index) in historyList" :key="index">
                    <td>
                        <div class="flex items-center space-x-3">
                            <div>
                                <div class="font-bold">{{ history.Name }}</div>
                                <div>Loc. {{ history.Location }}</div>
                            </div>
                        </div>
                    </td>
                    <th>
                        <a role="button" class="btn btn-ghost btn-xs" @click="toggleMap(index)">Go to Map</a>
                    </th>
                </tr>
                <!-- row end -->
            </tbody>
          </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'HistoryList',
  data () {
    return {
      historyList: null,
      buttonStatus: null
    }
  },
  components: {
  },
  methods: {
    fetchHistoryList: async function () {
      const P1_ID = this.$store.state.P1_ID
      // console.log(P1_ID)
      try {
        console.log('start fetching', P1_ID)
        const response = await axios.get(`http://127.0.0.1:5000/api/history/${P1_ID}`)
        console.log('get response')
        this.historyList = response.data
        console.log(this.historyList)
      } catch (error) {
        console.error(error)
        this.historyList = null
      }
    },
    toggleMap (index) {
      // console.log(this.historyList[index])
      window.open(this.historyList[index].URL)
    }
  },
  async mounted () {
    await this.fetchHistoryList()
  }
}
</script>
<style>
</style>
