<template>
  <div class="login">
    <img alt="logo" src="../assets/login_logo.png" class="fork1">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input placeholder="Enter email here" type="text" id="username" v-model="username" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input placeholder="Enter password here" type="password" id="password" v-model="password" required>
      </div>
      <button class="loginbt" type="submit" @click="goMealpal">Login</button>
      <br>
       <button type="button" @click="goRegist">Regist</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'LoginPage',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      // 在這裡處理登入邏輯
      console.log('Username:', this.username)
      console.log('Password:', this.password)
      // 可以向後端發送登入請求或執行其他相關操作
    },
    goMealpal () {
      this.$router.push('/mealpal')
    },
    goRegist () {
      this.$router.push('/regist')
    }
  }
}

</script>

<style scoped>
.fork1
{
height:100px;
width:100px;
}

.login {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

h2 {
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 10px;
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.loginbt {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
