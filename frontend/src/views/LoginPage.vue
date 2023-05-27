<template>
  <div class="hero min-h-[80vh] bg-base-200">
    <div class="hero-content flex-col lg:flex-row-reverse w-2/3">
      <div class="text-center p-8 lg:text-left">
        <div class="flex justify-center lg:justify-start">
          <img class="h-40 w-auto md-4" src="../assets/login_logo.png" alt="logo" />
        </div>
        <h1 class="text-5xl font-bold">Log in now!</h1>
        <p class="py-6">Sign in to your account and start your food trip!</p>
        <div class="mt-2 text-center text-sm text-gray-500 lg:text-left">
          Don't have an account?
          {{ '   ' }}
          <router-link to="/regist" class="font-semibold leading-6 text-primary hover:text-secondary">
                            Sign up
          </router-link>
        </div>
      </div>
      <form class="w-1/2" action="#" method="POST" @submit.prevent="submitLogin">
        <div class="card flex-shrink-0 w-full shadow-2xl bg-base-100">
          <div class="card-body">
            <div class="form-control">
              <label class="label">
                <span class="label-text">Account</span>
              </label>
              <input id="text" name="text" type="text" autocomplete="your account" class="input input-bordered" required=""/>
            </div>
            <div class="form-control">
              <label class="label">
                <span class="label-text">Password</span>
              </label>
              <input id="password" name="password" type="password" autocomplete="cyourpassword" class="input input-bordered" required=""/>
              <label class="label">
                <a href="#" class="label-text-alt link link-hover text-primary hover:text-secondary">Forgot password?</a>
              </label>
              <div class="form-control">
                <label class="label cursor-pointer">
                  <span class="label-text">Remember me</span>
                  <input type="checkbox" checked="checked" class="checkbox" />
                </label>
              </div>
            </div>
            <div class="form-control mt-6">
              <button class="btn btn-primary">Log in</button>
            </div>
          </div>
        </div>
      </form>
    </div>
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
    submitLogin () {
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

<style></style>
