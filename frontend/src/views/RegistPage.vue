<template>
  <div>
    <div class="login">
      <img alt="logo" src="../assets/login_logo.png" class="fork1">
      <h2>Regist</h2>
      <form @submit.prevent="regist">
        <div>
          <label for="username">Username:</label>
          <input placeholder="Enter email here" type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input placeholder="Enter password here" type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Regist</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegistPage',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    regist () {
      console.log('Username:', this.username)
      console.log('Password:', this.password)
      // 可以向後端發送登入請求或執行其他相關操作
    },
    goToLogin () {
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.fork1 {
  height: 100px;
  width: 100px;
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

button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
