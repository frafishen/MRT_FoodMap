<template>
<div>
    <div class="desktop-1">
      <div class="taipeimrtfoodmapsystem">
          <p class="taipeimrtfoodmapsystem2">TAIPEI MRT FOOD MAP SYSTEM</p>
      </div>
      <button @click='goMealpal' class="primarybutton" type="button" name="mealpal">
          <p class="findmealpal">MealPal</p>
      </button>
      <button @click="goFindFood" class="primarybutton3" type="button" name="map">
          <p class="map3">Map</p>
      </button>

      <button @click='goToLogin' type="button" name="goToLoginPage" class="login">
        <p>Login/<br>
        Register</p>
      </button>
      <button class="homeButton" type="button" name="home" @click="goToLogin">
        <img class="home" src="../assets/home.png">
      </button>
      <button class="userButton" type="button" name="user" @click="goPersonal">
        <img class="user1" src="../assets/user.png">
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',

  methods: {
    goToLogin () {
      this.$router.push('/login')
    },
    goFindFood () {
      this.$router.push('/findFood')
    },
    goPersonal () {
      this.$router.push('/person')
    },
    goMealpal () {
      this.$router.push('/mealpal')
    }
  }
}
</script>
<style scoped>
.desktop-1
{
background-color:#ffffff;
padding:0px;
}
.taipeimrtfoodmapsystem
{
position: absolute;
width: 996px;
height: 100px;
left: 222px;
top: 100px;

filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));

}
.taipeimrtfoodmapsystem2
{
position: absolute;
left: 0%;
right: 0%;
top: 0%;
bottom: 0%;

font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 64px;
line-height: 77px;

color: #000000;

border: 1px solid #000000;
text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);

}
.primarybutton
{
display: flex;
  /* 水平置中 */
  justify-content: center;
  /* 垂直置中 */
  align-content: center;
  flex-wrap: wrap;

position: absolute;
border-radius:50px;
width: 429px;
height: 326px;
left: 799px;
top: 435px;
background: #FFF4CD;

}

.findmealpal
{

color:#363636;
font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 48px;
text-align: center;
line-height: center;

}
.primarybutton3
{
display: flex;
  /* 水平置中 */
  justify-content: center;
  /* 垂直置中 */
  align-content: center;
  flex-wrap: wrap;

height:326px;
width:429px;
border-radius:50px;
padding:0px;
top:435px;
left:212px;
position:absolute;

background-color:#fff4cd;
}

.map3
{
font-family: 'Inter';
font-style: normal;
font-weight: 400;
font-size: 48px;
text-align: center;
color: #363636;
}
.home
{
background-color:#ffffff;
height:65px;
width:65px;

}

.user1
{
height:65px;
width:65px;
}
.homeButton
{
background-color: transparent;
border-color: lightgray;
height:76px;
width:76px;
padding:0px;
left:1180px;
top:34px;
position:absolute;

}

.userButton{
background-color: transparent;
border-color: lightgray;
width: 76px;
height: 76px;
left: 1072px;
top: 34px;
position: absolute;
}
.login{
  width: 76px;
  height: 76px;
  left: 970px;
  top: 34px;
  position: absolute;
}

</style>
