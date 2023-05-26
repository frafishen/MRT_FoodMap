<template>
  <div>
    <header>
      <h3>TAIPEI MRT FOOD MAP SYSTEM</h3>
    </header>

    <button @click="backToFirst" type="button" name="backToFirstPage" class="backToFirst">
      <img src="../assets/home.png" width="100" height="100" alt="home-icon" />
    </button>

    <button @click="goToHistory" type="button" name="goToHistoryList" class="goToHistoryList">
      <img src="../assets/clock.png" width="100" height="100" alt="clock-icon" />
    </button>

    <button @click="goToFavorite" type="button" name="goToFavoriteList" class="goToFavoriteList">
      <img src="../assets/redHeart_2.png" width="100" height="100" alt="heart-icon" />
    </button>

    <p>XXX's Personal Page</p>

    <img alt="randomPhoto" class="photo" src="public/qoopio大研創意形象照.jpg" width="150" height="160" />

    <p class="personalInfo">
      Name:<br>
      Usually appears at:<br>
      Meal time:<br>
    </p>

    <img alt="randomPhoto" class="photo" src="public/png-transparent-princess-ariel-ariel-rapunzel-king-triton-the-little-mermaid-ariel-disney-princess-fictional-character-flower.png" width="120" height="150" />
    <img alt="randomPhoto" class="photo" src="public/routemap2023n.png" width="120" height="150" />
  </div>
</template>

<script>
export default {
  name: 'PersonalPage',
  methods: {
    backToFirst () {
      this.$router.push('/')
    },
    goToHistory () {
      this.$router.push('/history')
    },
    goToFavorite () {
      this.$router.push('/favorite')
    }
  }
}
</script>

<style>
.backToFirst {
  position: absolute;
  right: 0;
  top: 0px;
}
.goToHistory {
  position: absolute;
  right: 150px;
  top: 0px;
}
.goToFavorite {
  position: absolute;
  right: 300px;
  top: 0px;
}
</style>
