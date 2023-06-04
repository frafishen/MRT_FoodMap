<template>
  <div class="invite">
    <div class="text1">
      Invitation
    </div>
    <div v-if="submittedData !== null">
      <div class="text2">
        Date: 2023/06/05<br>
        Time: 12:10<br>
        Station: Taipei Main Station<br>
        Type: Ramen<br>
        <!-- Date: {{ submittedData.date }}<br>
        Time: {{ submittedData.time }}<br>
        Station: {{ submittedData.station }}<br>
        Type: {{ submittedData.type }}<br> -->
      </div>
    </div>
    <div>
      <button @click='confirm' name="yes" class="button-container1">
        <p class="yes">Yes</p>
      </button>
      <button @click='reject' name="No" class="button-container2">
        <p class="yes">No</p>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InvitationPage',
  data () {
    return {
      submittedData: null
    }
  },
  methods: {
    confirm () {
      // this.$router.push({
      //   path: '/intersection',
      //   query: {
      //     date: this.$route.query.date || '',
      //     time: this.$route.query.time || '',
      //     station: this.$route.query.station || '',
      //     type: this.$route.query.type || ''
      //   }
      // })
    },
    reject () {
      this.$router.push('/findMealPal')
    }
  },
  mounted () {
    this.submittedData = {
      date: this.$route.query.date || '',
      time: this.$route.query.time || '',
      station: this.$route.query.station || '',
      type: this.$route.query.type || ''
    }
  }
}
</script>

<style scoped>
.invite{
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.text1{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 64px;
  line-height: 77px;
  background-color: #FFEDED;
  border-radius: 50px;
  align-items: center;
  text-align: center;
  margin-bottom: 15px;
}
.text2{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-size: 30px;
  line-height: 60px;
  /* text-align: center; */
  padding: 5px;
}

.button-container1 {
    margin-left: 70px;
    margin-top: 15px;
    font-size: 26px;
    background-color: #FFEDED;
    border-radius: 20px;
    padding: 10px;
  }
  .button-container2 {
    margin-left: 100px;
    margin-top: 15px;
    font-size: 26px;
    background-color: #FFEDED;
    border-radius: 20px;
    padding: 10px;
  }
</style>
