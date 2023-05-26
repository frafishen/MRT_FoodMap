<template>
  <div>
      <div class="parentContainer">
      <header>
        <h3>TAIPEI MRT FOOD MAP SYSTEM</h3>
      </header>

      <button @click='backTofirst' type="button" name="backToFirstPage" class="backToFirst">
        <img src="../assets/home.png" width="100" height="100"/>
      </button>

      <h1>Find Mealpal</h1>

      <img alt="MRT route map" class="mapImage" src="https://web.metro.taipei/pages/assets/images/routemap2023n.png" width="576" height="768" />

      <h5>amount of people</h5>
      <h6>Many</h6>
      <h6>Medium</h6>
      <h6>Few</h6>

      <button @click='goToNewEvent' type="button" class="newEvent" name="New Event">
        <p >New Event</p>
      </button>

      <button @click='goToRandomPair' type="button" class="randomPair" name="Random Pair">
        <p>Random Pair</p>
      </button>
    </div>
    <router-view></router-view>
    <main>
      <TheWelcome />
    </main>
  </div>
</template>

<script>
export default {
  name: 'findMealpal',
  methods: {
    backTofirst () {
      this.$router.push('/')
    },
    goToNewEvent () {
      this.$router.push('/newEvent')
    },
    goToRandomPair () {
      this.$router.push('/randomPair')
    },
    goToInvatation () {
      this.$router.push('/invite')
    },
    goToIntersection () {
      this.$router.push('/intersection')
    }
  }
}
</script>

<style scoped>
 /* .parentContainer {
  position: absolute;
  } */
.mapImage {
  position: absolute;
  left: 70px;
  top: 300px;
  /* display: flex; 將圖片容器設定為彈性盒子
  justify-content: flex-start; 將圖片容器內的內容靠左對齊 */
}

.backToFirst{
  position: absolute;
  right: 0;
  top: 0px;
}

.newEvent{
  position: absolute;
  left: 1000px;
  top: 600px;
}
.randomPair{
  position: absolute;
  left: 1000px;
  top: 800px;
}
.inva{
  position: absolute;
  left: 1000px;
  top: 1000px;
}

.inter{
  position: absolute;
  left: 1200px;
  top: 1000px;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: left;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
