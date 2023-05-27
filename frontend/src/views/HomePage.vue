<template>
<div>
  <div class="hero min-h-[80vh] bg-base-200">
    <div class="hero-content text-center lg: w-2/3">
      <div class="max-w-md ld: w-full">
          <h1 class="text-5xl font-bold mt-6">MRT Food Map</h1>
          <p class="py-4 md-6">Enjoy your food trip with mealpals in Taipei city!</p>
        <div class="flex flex-col w-full lg:flex-row">
          <div class="grid flex-grow h-32 card bg-base-300 rounded-box place-items-center" @click="goFindFood">Find Food</div>
          <div class="divider lg:divider-horizontal">OR</div>
          <div class="grid flex-grow h-32 card bg-base-300 rounded-box place-items-center" @click="goMealpal">Find Mealpal</div>
        </div>
      </div>
    </div>

  </div>
</div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    goFindFood () {
      this.$router.push('/findFood')
    },
    goMealpal () {
      this.$router.push('/mealpal')
    }
  }
}
</script>
<style>
</style>
