<template>
    <div class=" hero-overlay relative">
        <img src="../assets/concentric_taipei_mrt_metro_map_60186.jpg"
            class="object-cover w-full h-auto shadow-2xl lg:h-4/5 lg:w-auto" alt="mrt metro map" />
        <button class="rounded-full bg-opacity-90 hover:bg-opacity-50 btn-error absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 h-4 w-4" type="submit"></button>
        <button class="rounded-full bg-opacity-90 hover:bg-opacity-50 btn-info absolute pos-G13 transform -translate-x-1/2 -translate-y-1/2 h-4 w-4" type="submit"></button>
        <button class="rounded-full bg-opacity-90 hover:bg-opacity-50 btn-info absolute pos-G15 transform -translate-x-1/2 -translate-y-1/2 h-4 w-4" type="submit"></button>
        <button class="rounded-full bg-opacity-90 hover:bg-opacity-50 btn-warning absolute pos-G12 transform -translate-x-1/2 -translate-y-1/2 h-4 w-4" type="submit"></button>
        <button class="rounded-full bg-opacity-90 hover:bg-opacity-50 btn-error absolute pos-G16 transform -translate-x-1/2 -translate-y-1/2 h-4 w-4" type="submit"></button>
        <button class="rounded-full bg-opacity-90 hover:bg-opacity-50 btn-error absolute pos-R05 transform -translate-x-1/2 -translate-y-1/2 h-4 w-4" type="submit"></button>
    </div>
</template>
<script>
export default {
  name: 'MealPalMap',
  methods: {}
}
</script>
<style>
.pos-G13 {
    top: 46.88%;
    left: 44.59%;
}
.pos-R05 {
    top: 57.05%;
    left: 62.25%;
}
.pos-G15 {
    top: 43.75%;
    left: 60.78%;
}
.pos-G12 {
    top: 53.14%;
    left: 44.59%;
}
.pos-G16 {
    top: 40.59%;
    left: 66.19%;
}
</style>
