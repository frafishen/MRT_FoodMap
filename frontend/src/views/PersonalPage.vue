<template>
  <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class="hero-content flex-col lg:flex-row">
        <img src="../assets/personal_image_sample.jpg" class="max-w-sm rounded-lg shadow-2xl" />
        <div class="px-6">
          <h1 class="text-5xl font-bold py-6"><span class="text-primary">{{'My '}}</span>Personal Page</h1>
          <div class="py-6">
            <span class="font-bold mr-2">Location: </span> {{ 'Taipei City' }} <br>
            <span class="font-bold mr-2">Usually at: </span> {{ 'Taipei Main Station' }} <br>
            <span class="font-bold mr-2">Meal time: </span> {{ '12:00 - 13:00' }} <br>
          </div>
          <div class="flex justify-between py-6">
            <div class="flex">
              <router-link to="/history">
                <img src="../assets/clock.png" class="h-8 w-auto" />
              </router-link>
              <div class="px-4">History List</div>
            </div>
            <div class="flex">
              <router-link to="/favorite">
                <img src="../assets/red_heart.png" class="h-8 w-auto" />
              </router-link>
              <div class="px-4">Favorite List</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'PersonalPage',
  methods: {
  }
}
</script>
<style>
</style>
