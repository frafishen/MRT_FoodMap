<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="getHelloWorld">Get Hello World</button>
    <p>{{ helloWorldText }}</p>
    <div>
      <textarea name="test_pereson" id="id_test_person" cols="30" rows="3" v-model="person_input"></textarea>
      <button @click="fetchPerson(person_input)">Fetch Person</button>
      <div v-if="person">
        ID: {{ person.PersonID }}<br>
        Name: {{ person.Name }}<br>
        Password: {{ person.Password }}<br>
        Location: {{ person.Location }}<br>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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

async function fetchPerson (personInput) {
  try {
    // const personId = Number(personInput)
    const response = await axios.get(`http://localhost:5000/api/person/${personInput}`)
    this.person = response.data
  } catch (error) {
    console.error(error)
  }
}

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      helloWorldText: '',
      person: null,
      person_input: ''
    }
  },
  methods: {
    getHelloWorld: getHelloWorld,
    fetchPerson: fetchPerson
  }
}
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}
</style>
