<template>
  <div>
    <!-- <h2 class="head">Find Mealpal</h2> -->
    <div class="text">
      <p>New Event</p>
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
        <div class="form-row">
          <label for="gender">Gender </label>
          <select name="gender" id="gender" v-model="gender">
            <option v-for="gender in genders" :key="gender.value">
              {{ gender.text }}
            </option>
          </select>
        </div>
        <div class="form-row">
          <label for="other">Other</label>
          <input type="text" placeholder="Type something..." name="other" v-model="other">
        </div>
      </form>
      <button class="button-container1" @click="cancel">Cancel</button>
      <button class="button-container2" @click="submit">Confirm</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NewEvent',
  data () {
    return {
      date: '',
      time: '',
      station: '',
      type: 'BBQ',
      gender: 'Male',
      other: '',
      types: [
        { text: 'BBQ', value: 'BBQ' },
        { text: 'Hot Pot', value: 'hotpot' },
        { text: 'Ramen', value: 'ramen' }
      ],
      genders: [
        { text: 'Male', value: 'Male' },
        { text: 'Female', value: 'Female' },
        { text: 'Other', value: 'Other' }
      ]
    }
  },
  mounted () {
    this.getDate()
  },
  methods: {
    cancel: function () {
      this.$router.push('/findMealPal')
    },
    submit: function () {
      this.addEvent()
      this.$router.push('/findMealPal')
    },
    addEvent: async function () {
      const P1_ID = this.$store.state.P1_ID
      console.log(this.$store)
      console.log(P1_ID, this.time, this.date, this.station, this.type)
      try {
        const config = { headers: { 'Content-Type': 'application/json' } }
        const timeDate = this.date + ' ' + this.time + ':00'
        const response = await axios.post('http://127.0.0.1:5000/api/addEvent', { EventID: '10002', P1_ID: P1_ID, P2_ID: '00000000', Time: timeDate, FoodType: this.type, StationID: this.station }, config)
        console.log(response.data)
      } catch (error) {
        console.error('An error occurred:', error)
      }
    },
    getDate: function () {
      try {
        const currentDate = new Date()
        // 設定日期格式選項
        const options = { year: 'numeric', month: '2-digit', day: '2-digit' }
        this.date = currentDate.toLocaleDateString(undefined, options)
        this.date = this.date.replaceAll('/', '-')
        console.log(this.date)
      } catch (error) {
        console.error('An error occurred:', error)
      }
    }
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

  .form-row{
    font-size: 32px;
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
</style>
