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
  name: 'HistoryList',
  data () {
    return {
      // todo: get data from db
      tableRows: [
        {
          storeName: 'Store 1',
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
        },
        {
          storeName: 'Store 4',
          address: 'Address 4',
          isClicked: false
        }
      ]
    }
  },
  components: {
    StoreTable
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
      } catch (error) {
        console.error(error)
        this.historyList = null
      }
    }
  },
  async mounted () {
    await this.fetchHistoryList()
  }
  // setup () {
  //   const store = useStore()
  //   const histories = computed(() => store.getters.histories)

  //   return {
  //     histories
  //   }
  // },
  // methods: {
  // }
}
</script>
<style>
</style>
