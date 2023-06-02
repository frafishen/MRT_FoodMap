<template>
  <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class="hero-content flex-col lg:flex-row">
        <img src="../assets/personal_image_sample.jpg" class="max-w-sm rounded-lg shadow-2xl" />
        <div class="px-6">
          <h1 class="text-5xl font-bold py-6"><span class="text-primary" v-if="person">{{person.Name}}</span>'s Personal Page</h1>
          <div class="py-6">
            <span class="font-bold mr-2">User's id: </span><span v-if="person"> {{ person.PersonID }} </span><br>
            <span class="font-bold mr-2">Location: </span> <span v-if="person"> {{ person.Location }} </span><br>
          </div>
          <div class="flex justify-between py-6">
            <div class="flex">
              <router-link to="/history">
                <img src="../assets/clock.png" class="h-8 w-auto" />
              </router-link>
              <div class="px-4">History List</div>
            </div>
            <div class="flex">
              <router-link to="/favorite">
                <img src="../assets/red_heart.png" class="h-8 w-auto" />
              </router-link>
              <div class="px-4">Favorite List</div>
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
  name: 'PersonalPage',
  data () {
    return {
      person: null
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
    }
  },
  async mounted () {
    await this.fetchPerson()
  }
}
</script>

<style>
</style>
