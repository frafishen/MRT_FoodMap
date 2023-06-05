<template>
  <div>
    <!-- <h2 class="head">Find Mealpal</h2> -->
    <div class="text">
      <p>Random Pair</p>
    </div>
    <div class="form">
      <form class="form-text" name="event">
        <div class="form-row">
          <label for="date">Date: </label><span>{{this.date}}</span>
        </div>
        <div class="form-row">
          <label for="time">Time </label>
          <input type="time" name="time" v-model="time">
        </div>
        <div class="form-row">
          <label for="station">MRT Station </label>
          <input type="text" name="station" v-model="station">
        </div>
        <div class="form-row">
          <label for="types">Types </label>
          <select name="types" id="types" v-model="type">
            <option v-for="type in types" :key="type.value">
              {{ type.text }}
            </option>
          </select>
        </div>
      </form>
      <button class="button-container1" @click="goMealpal">Cancel</button>
      <button class="button-container2" @click="submitForm">Confirm</button>
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
      type: 'BBQ',
      types: [
        { text: 'BBQ', value: 'BBQ' },
        { text: 'Hot Pot', value: 'hotpot' },
        { text: 'Ramen', value: 'ramen' }
      ]
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
      this.$router.push({
        path: '/invite',
        query: {
          date: this.date,
          time: this.time,
          station: this.station,
          type: this.type
        }
      })
    },
    goMealpal () {
      this.$router.push('/findMealPal')
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

<style scoped>
div {
  margin: 0 auto;
}
.head {
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

.text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 48px;
  line-height: 58px;
  align-items: center;
  text-align: center;
  background-color: #FFEDED;
  color: #363636;
  margin-left: 25%;
  margin-right: 25%;
  border-radius: 10px;
}

.form {
  width: 800px;
  padding: 50px;
  background: #FFFFFF;
  border: 1px solid #000000;
  border-radius: 100px;
}

.form-text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 58px;
  color: #363636;
}

input {
  height: 40px;
  width: 300px;
  margin: 10px;
  font-size: 24px;
}

.button-container1 {
    margin-left: 100px;
    margin-top: 30px;
    font-size: 26px;
    background-color: #FFEDED;
    border-radius: 20px;
    padding: 10px;
}

.button-container2 {
    margin-left: 100px;
    margin-top: 30px;
    font-size: 26px;
    background-color: #FFEDED;
    border-radius: 20px;
    padding: 10px;
}

.form-row {
  font-size: 32px;
}

</style>
