<template>
  <div>
    <nav class =" mx-auto max-w-7xl justify-between p-2 lg:px-8">
      <router-link to="/homepage" class="p-6">MRT Food Map System</router-link>|
      <router-link to="/testpage" class="p-6">Test Page</router-link> |
      <router-link to="/findTastyFood" class="p-6">Find Tasty Food</router-link> |
      <router-link to="/findMealPal" class="p-6">Find MealPal</router-link>
      <!-- vendor NavBar component -->
      <NavBar />
    </nav>
    <router-view></router-view>

    <!-- vendor Footer component -->
    <AppFooter />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import AppFooter from '@/components/AppFooter.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    AppFooter
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@500;800&display=swap');
body {
  font-family: 'Source Code Pro', monospace;
}
</style>
