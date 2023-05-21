<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="getHelloWorld">Get Hello World</button>
    <p>{{ helloWorldText }}</p>
  </div>
</template>

<script>

async function getHelloWorld () {
  try {
    const response = await fetch('http://localhost:5000/')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    this.helloWorldText = await response.text()
  } catch (error) {
    console.log(error)
  }
}

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      helloWorldText: ''
    }
  },
  methods: {
    getHelloWorld: getHelloWorld
  }
}
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}
</style>
