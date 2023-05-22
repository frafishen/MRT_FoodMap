<template>
  <div class="hello">
    <div class="query">
      <input type="text" name="test_pereson" id="id_test_person" cols="30" rows="1" v-model="person_input">
      <button @click="fetchPerson(person_input)">Fetch Person</button>
      <div v-if="person" class="result">
        ID: {{ person.PersonID }}<br>
        Name: {{ person.Name }}<br>
        Password: {{ person.Password }}<br>
        Location: {{ person.Location }}<br>
      </div>
      <div v-else class="result">
        Person (ID: {{ person_input }}) not found.
      </div>
    </div>

    <div class="query">
      <input type="text" name="test_station" id="id_test_station" col="30" row="1" v-model="station_input">
      <button @click="fetchStation(station_input)">Fetch Station</button>
      <div v-if="station" class="result">
        ID: {{ station.StationID }}<br>
        Name: {{ station.Name }}<br>
      </div>
      <div v-else class="result">
        Station(ID: {{ station_input }}) not found.
      </div>
    </div>

    <div class="query">
      <input type="text" name="test_event" id="id_test_event" col="30" row="1" v-model="event_input">
      <button @click="fetchEvent(event_input)">Fetch Event</button>
      <div v-if="event" class="result">
        ID: {{ event.EventID }}<br>
        P1ID: {{ event.P1_ID }}<br>
        P2ID: {{ event.P2_ID }}<br>
        Time: {{ event.Time }}<br>
        FoodType: {{ event.FoodType }}<br>
        Station: {{ event.StationID }}<br>
      </div>
      <div v-else class="result">
        Event(ID: {{ event_input }}) not found.
      </div>
    </div>
  </div>

  <div class="hello">
    <div class="query">
      <button @click="getPersons()">Get Persons</button>
      <div v-for="(person, index) in persons" :key="index" class="result">
        ID: {{ person.PersonID }}<br>
        Name: {{ person.Name }}<br>
        Password: {{ person.Password }}<br>
        Location: {{ person.Location }}<br>
      </div>
    </div>
    <div class="query">
      <button @click="getStations()">Get Stations</button>
      <div v-for="(station, index) in stations" :key="index" class="result">
        ID: {{ station.StationID }}<br>
        Name: {{ station.Name }}<br>
      </div>
    </div>
    <div class="query">
      <button @click="getEvents()">Get Events</button>
      <div v-for="(event, index) in events" :key="index" class="result">
        ID: {{ event.EventID }}<br>
        P1ID: {{ event.P1_ID }}<br>
        P2ID: {{ event.P2_ID }}<br>
        Time: {{ event.Time }}<br>
        FoodType: {{ event.FoodType }}<br>
        Station: {{ event.StationID }}<br>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

async function fetchPerson (personInput) {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/person/${personInput}`)
    this.person = response.data
  } catch (error) {
    console.error(error)
    this.person = null
  }
}
async function getPersons () {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/person')
    this.persons = response.data
  } catch (error) {
    console.error(error)
    this.persons = []
  }
}

async function fetchStation (stationInput) {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/station/${stationInput}`)
    this.station = response.data
  } catch (error) {
    console.error(error)
    this.station = null
  }
}
async function getStations () {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/station')
    this.stations = response.data
  } catch (error) {
    console.error(error)
    this.stations = []
  }
}

async function fetchEvent (eventInput) {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/event/${eventInput}`)
    this.event = response.data
  } catch (error) {
    console.error(error)
    this.event = null
  }
}
async function getEvents () {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/event')
    this.events = response.data
  } catch (error) {
    console.error(error)
    this.events = []
  }
}

export default {
  name: 'HelloWorld',
  data () {
    return {
      person_input: '00001002',
      person: null,
      persons: [],
      station_input: 'R10',
      station: null,
      stations: [],
      event_input: '3',
      event: null,
      events: []
    }
  },
  methods: {
    fetchPerson: fetchPerson,
    getPersons: getPersons,
    fetchStation: fetchStation,
    getStations: getStations,
    fetchEvent: fetchEvent,
    getEvents: getEvents
  }
}
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}

.hello {
  display: flex;
  justify-content: space-between;
  margin-right: 5%;
  margin-left: 5%;
}

.query {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 10px;
}

.result {
  text-align: left;
  margin-top: 10px;
  flex: 1;
}
</style>
