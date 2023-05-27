<template>
  <div>
    <div class="hello">
      <div class="query">
        <div class="form-control">
          <div class="input-group">
            <input type="text" placeholder="00001002" class="input input-bordered" v-model="person_input"/>
            <button class="btn btn-square"  @click="fetchPerson(person_input)">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </div>
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
        <div class="form-control">
          <div class="input-group">
            <input type="text" placeholder="R10" class="input input-bordered" v-model="station_input"/>
            <button class="btn btn-square"  @click="fetchStation(station_input)">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </div>
        <div v-if="station" class="result">
          ID: {{ station.StationID }}<br>
          Name: {{ station.Name }}<br>
        </div>
        <div v-else class="result">
          Station(ID: {{ station_input }}) not found.
        </div>
      </div>

      <div class="query">
        <div class="form-control">
          <div class="input-group">
            <input type="text" placeholder="3" class="input input-bordered" v-model="event_input"/>
            <button class="btn btn-square"  @click="fetchEvent(event_input)">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </div>
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
        <button class="btn btn-outline" @click="getPersons()">Get PersonList</button>
        <div v-for="(person, index) in persons" :key="index" class="result">
          ID: {{ person.PersonID }}<br>
          Name: {{ person.Name }}<br>
          Password: {{ person.Password }}<br>
          Location: {{ person.Location }}<br>
        </div>
      </div>
      <div class="query">
        <button class="btn btn-outline" @click="getStations()">Get Stations</button>
        <div v-for="(station, index) in stations" :key="index" class="result">
          ID: {{ station.StationID }}<br>
          Name: {{ station.Name }}<br>
        </div>
      </div>
      <div class="query">
        <button class="btn btn-outline" @click="getEvents()">Get Events</button>
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
    <div>
      <form @submit.prevent="addStation">
        <input type="text" placeholder="R10" v-model="stationID" class="input input-bordered" />
        <input type="text" v-model="stationName" placeholder="Station Name" class="input input-bordered" />
        <button class=" btn btn-outline" type="submit">Add Station</button>
      </form>
      <div>
        <div v-if="addStationStatus" :key="index" class="result">
          msg: {{ addStationStatus.message }}<br>
        </div>
      </div>
    </div>
    <div>
      <form @submit.prevent="deleteStation">
        <input type="text" placeholder="R10" v-model="dstationID" class="input input-bordered" />
        <button class=" btn btn-outline" type="submit">Delete Station</button>
      </form>
      <div>
        <div v-if="deleteStationStatus" :key="index" class="result">
          msg: {{ deleteStationStatus.message }}<br>
        </div>
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

// create an addStation function with inputStationID and stationName
async function addStation () {
  console.log(this.stationID, this.stationName)
  try {
    var config = { headers: { 'Content-Type': 'application/json' } }
    const response = await axios.post('http://127.0.0.1:5000/api/addStation', { StationID: this.stationID, Name: this.stationName }, config)
    this.addStationStatus = response.data
  } catch (error) {
    console.error('An error occurred:', error)
  }
}

// create an deleteStation function with inputStationID
async function deleteStation () {
  console.log(this.stationID)
  try {
    var config = { headers: { 'Content-Type': 'application/json' } }
    const response = await axios.post('http://127.0.0.1:5000/api/deleteStation', { StationID: this.dstationID }, config)
    this.addStationStatus = response.data
  } catch (error) {
    console.error('An error occurred:', error)
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
      events: [],
      stationID: '2345',
      stationName: 'zz',
      dstationID: '2345',
      addStationStatus: null,
      deleteStationStatus: null
    }
  },
  methods: {
    fetchPerson: fetchPerson,
    getPersons: getPersons,
    fetchStation: fetchStation,
    getStations: getStations,
    fetchEvent: fetchEvent,
    getEvents: getEvents,
    addStation: addStation,
    deleteStation: deleteStation
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
}</style>
