<template>
<div>
  <div class="hero min-h-[80vh] bg-base-200">
    <div class="hero-content text-center lg: w-2/3">
      <div class="max-w-md my-8 ld: w-full">
        <div class="my-8">
          <h1 class="text-5xl font-bold mt-6">MRT <span class="text-primary"> F.o^o.d</span> Map</h1>
          <p class="py-4 md-6 text-natural">Enjoy your f.o^o.d trip with meal:pals in Taipei city!</p>
        </div>
        <div class="flex flex-col w-full my-8 lg:flex-row">
          <div class="grid flex-grow h-32 card bg-base-300 rounded-box place-items-center" @click="goFindFood">Find F.o^o.d</div>
          <div class="divider lg:divider-horizontal">OR</div>
          <div class="grid flex-grow h-32 card bg-base-300 rounded-box place-items-center" @click="goMealpal">Find Meal:Pal</div>
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
      this.$router.push('/findTastyFood')
    },
    goMealpal () {
      this.$router.push('/findMealPal')
    }
  }
}
</script>
<style>
</style>
