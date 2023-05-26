<template>
  <div>
    <h2 class="head">Find Mealpal</h2>
    <div class="text">
      <p>
        Random Pair
      </p>
    </div>
    <div class="form">
      <form class="form-text" name="event">
        <div class="form-row">
          <label for="date">Date</label>
          <input type="date" name="date" v-model="date">
        </div>
        <div class="form-row">
          <label for="time">Time</label>
          <input type="time" name="time" v-model="time">
        </div>
        <div class="form-row">
          <label for="station">MRT Station</label>
          <input type="text" name="station" v-model="station">
        </div>
        <div class="form-row">
          <label for="types">Types</label>
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
    submitForm () {
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
      this.$router.push('/mealpal')
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
  border-radius: 100px;
}

.form {
  width: 800px;
  padding: 50px;
  background: #FFFFFF;
  border: 1px solid #000000;
  border-radius: 136px;
}

.form-text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 40px;
  line-height: 58px;
  color: #363636;
}

input, select {
  height: 40px;
  width: 300px;
  margin: 10px;
  font-size: 30px;
}

.button-container1 {
  margin-right: 50px;
  margin-top: 20px;
}

.button-container2 {
  margin-left: 50px;
  margin-top: 20px;
}

.form-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.form-row label {
  flex: 1;
  margin-right: 10px;
  text-align: left;
}

.form-row input,
.form-row select {
  flex: 1;
  width: 100%;
}
</style>
