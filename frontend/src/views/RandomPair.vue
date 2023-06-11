<template>
  <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class=" w-5/6 hero-content flex-col lg:flex-row-reverse">
        <div class="px-6 w-4/5 lg:w-2/5">
          <h1 class="text-5xl font-bold py-6 h-1/3 text-center"> Random <span class="text-primary">:Pair</span></h1>
          <p class="py-4 md-6 text-natural h-2/3 text-center"> Start to make a new friend now!</p>
        </div>
        <div class="px-6 w-full lg:w-3/5">
          <!-- left component -->
          <div class="max-w-full">
            <!-- ========== right component ========== -->
            <div class="isolate bg-white px-12 py-4 rounded-3xl" v-if="showcontent">
              <form action="#" method="POST" class="mx-auto mt-16 max-w-xl sm:mt-20">
                <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
                  <div>
                    <label for="data" class="block text-sm font-semibold leading-6 text-gray-900">Date</label>
                    <div class="mt-2.5 text-primary">
                      <span>{{ this.date }}</span>
                    </div>
                  </div>
                  <div>
                    <label for="time" class="block text-sm font-semibold leading-6 text-gray-900">Time</label>
                    <div class="mt-2.5">
                      <input type="time" name="time" v-model="time" class="input input-bordered w-full" />
                    </div>
                  </div>
                  <!-- <div class="sm:col-span-2">
                    <label for="station" class="block text-sm font-semibold leading-6 text-gray-900">MRT Station</label>
                    <select name="types" id="types" class="flex justify-end select select-bordered w-full">
                      <option disabled selected class="text-primary">What do .u. want to go today?</option>
                      <option v-for="[key, value] in Object.entries(stationList)" :key="key">
                        {{ value }}
                      </option>
                    </select>
                  </div> -->
                  <div class="sm:col-span-2">
                    <label for="station" class="block text-sm font-semibold leading-6 text-gray-900">MRT Station</label>
                    <select id="station" v-model="station" class="flex justify-end select select-bordered w-full font-normal">
                      <option disabled value="">What do .u. want to go today?</option>
                      <option v-for="[key, value] in Object.entries(stationList)" :key="key" :value="key">
                        {{ value }}
                      </option>
                    </select>
                  </div>
                  <div class="sm:col-span-2">
                    <label for="foodtype" class="block text-sm font-semibold leading-6 text-gray-900">Food Type</label>
                    <div class="mt-2.5">
                      <select name="types" id="types" v-model="type" class="flex justify-end select select-bordered w-full font-normal">
                        <option disabled value="">What do .u. want to eat today?</option>
                        <option v-for="[key, value] in Object.entries(foodTypes)" :key="key" :value="key">
                          {{ value }}
                        </option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="my-12 py-6 flex flex-row justify-between">
                  <button class="flex btn btn-outline btn-error mx-12" @click="goMealpal">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>Cancel
                  </button>
                  <button type="submit" class="flex btn btn-outline btn-warning mx-12" @click="submitForm">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>Search
                  </button>
                </div>
              </form>
            </div>
            <!-- ========== invitation success! ========== -->
            <div class="isolate bg-white px-12 py-4 rounded-3xl" v-if="!showcontent">
              <div class="p-6">
                <div class="p-4">
                  <h3 class="text-3xl text-center font-semibold leading-7 text-primary"> Invitation Success! </h3>
                </div>
                <div class="mt-6 border-t border-gray-100 max-w-full">
                  <dl class="divide-y divide-gray-100">
                    <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                      <dt class="text-sm font-medium leading-6 text-gray-900">Date</dt>
                      <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ '2023/06/06' }}</dd>
                    </div>
                    <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                      <dt class="text-sm font-medium leading-6 text-gray-900">Time</dt>
                      <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ '06:00 PM' }}</dd>
                    </div>
                    <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                      <dt class="text-sm font-medium leading-6 text-gray-900">Food Type</dt>
                      <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ 'Ramen' }}</dd>
                    </div>
                    <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
                      <dt class="text-sm font-medium leading-6 text-gray-900">MRT Station</dt>
                      <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ 'Taipei Main Station' }}
                      </dd>
                    </div>
                    <div class="px-4 py-4 sm:grid sm:grid-cols-2 sm:gap-4 sm:px-0">
                      <dt class="text-sm font-medium leading-6 text-gray-900"> Restaurant .u. may like</dt>
                      <!-- <dd class="mt-1 leading-6 sm:col-span-2 sm:mt-0"> -->
                      <!-- <div>Add a comment</div> -->
                      <!-- </dd> -->
                    </div>
                    <!-- ========== carousel component - Comment ========== -->
                    <div class="max-w-full w-full">
                      <div class="carousel carousel-center p-2 space-x-4 bg-primary rounded-box">
                        <div class="carousel-item">
                          <div class="card w-96 bg-base-100 shadow-xl">
                            <div class="card-body">
                              <h2 class="card-title">{{ '麵屋武藏' }}</h2>
                              <p>{{ '台北市中正區忠孝西路一段36號B1' }}</p>
                            </div>
                          </div>
                        </div>
                        <div class="carousel-item">
                          <div class="card w-96 bg-base-100 shadow-xl">
                            <div class="card-body">
                              <h2 class="card-title">{{ '太陽蕃茄拉麵 站前本店' }}</h2>
                              <p>{{ '台北市中正區忠孝西路一段38號凱撤飯店B1F' }}</p>
                            </div>
                          </div>
                        </div>
                        <div class="carousel-item">
                          <div class="card w-96 bg-base-100 shadow-xl">
                            <div class="card-body">
                              <h2 class="card-title cursor-pointer" @click="goFindFood"> See More! </h2>
                              <p> Go to our f.o^o.d map <br> to find more tasty food! </p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'RandomPair',
  data () {
    return {
      date: '',
      time: '',
      station: '',
      type: '',
      foodTypes: {
        BBQ: 'BBQ',
        hotpot: 'Hot Pot',
        ramen: 'Ramen'
      },
      stationList: {
        R10: 'Taipei Main Station',
        R11: 'Zhongshan Station',
        G16: 'Nanjing Fuxing Station'
      },
      showcontent: true
    }
  },
  methods: {
    fetchPerson: async function () {
      const P1_ID = this.$store.state.P1_ID
      console.log(P1_ID)
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/person/${P1_ID}`)
        this.person = response.data
      } catch (error) {
        console.error(error)
        this.person = null
      }
    },
    submitForm () {
      this.randomPair()
      // this.$router.push({
      //   path: '/invite',
      //   query: {
      //     date: this.date,
      //     time: this.time,
      //     station: this.station,
      //     type: this.type
      //   }
      // })
      this.showcontent = false
    },
    goMealpal () {
      this.$router.push('/findMealPal')
    },
    goFindFood () {
      this.$router.push('/findTastyFood')
    },
    randomPair: async function () {
      const data = {
        P2_ID: this.person.PersonID,
        Time: this.date + ' ' + this.time + ':00',
        FoodType: this.type,
        StationID: this.station
      }
      console.log(data.Time)
      const response = await axios.post('http://localhost:5000/api/randomPair', data)
      if (response.data.status === 'success') {
        console.log(response.data.event)
      } else {
        console.error(response.data.message)
      }
    },
    getDate: function () {
      try {
        const currentDate = new Date()
        // 設定日期格式選項
        const options = { year: 'numeric', month: '2-digit', day: '2-digit' }
        this.date = currentDate.toLocaleDateString(undefined, options)
        this.date = this.date.replaceAll('/', '-')
      } catch (error) {
        console.error('An error occurred:', error)
      }
    }
  },
  async mounted () {
    this.getDate()
    await this.fetchPerson()
  }
}
</script>
<style></style>
