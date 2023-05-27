<template>
  <div>
    <nav class =" mx-auto max-w-7xl justify-between p-2 lg:px-8">
      <router-link to="/homepage" class="p-6">Taipei MRT Food Map System</router-link>|
      <router-link to="/" class="p-6">TestPage</router-link>
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
</style>
