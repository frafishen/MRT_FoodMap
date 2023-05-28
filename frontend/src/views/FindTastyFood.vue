<template>
  <div>
    <div class="hero min-h-[80vh] bg-base-200">
      <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="px-6">
          <h1 class="text-5xl font-bold py-6">Find Tasty <span class="text-primary">F.o^o.d </span></h1>
          <div class="w-full flex flex-row justify-between">
            <!-- construct a button with a arror point to left -->
            <button class="flex justify-start btn btn-ghost hover:bg-primary hover:text-white"><p>&larr;</p></button>
            <!-- selection bar -->
            <select class="flex justify-end select select-primary w-full max-w-xs">
              <option disabled selected class="text-primary">What .u. want to eat today?</option>
              <option v-for="[key, value] in Object.entries(foodTypes)" :key="key">
                {{ value }}
              </option>
            </select>
          </div>
          <!-- table component -->
          <div class="overflow-x-auto w-full mt-4">
            <table class="table w-full">
              <!-- head -->
              <tbody>
                <!-- row 1 -->
                <tr v-for="(row, index) in tableRows" :key="index">
                  <td>
                    <div class="flex items-center space-x-3">
                      <div>
                        <div class="font-bold">{{ row.storeName }}</div>
                        <div class="rating rating-xs">
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" checked />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                          <input type="radio" name="rating-5" class="mask mask-star-2 bg-secondary" />
                        </div>
                      </div>
                    </div>
                  </td>
                  <td>
                    {{ row.address }}
                    <br />
                    <button class="badge badge-ghost badge-sm" type="submit">{{ 'Details' }}</button>
                  </td>
                  <th>
                    <button class="btn btn-ghost btn-xs">comment</button>
                  </th>
                  <th>
                    <button
                      name="add fav"
                      type="submit"
                      class="btn btn-sm mask mask-heart transition-colors duration-200"
                      :class="{ 'bg-red-400': row.isClicked, 'bg-gray-400': !row.isClicked }"
                      @click="toggleColor(index)"
                    ></button>
                  </th>
                </tr>
                <!-- row end -->
              </tbody>
            </table>
          </div>
        </div>
        <div class="px-6 w-4/5 lg:w-1/2 p-4">
          <!-- left conponent -->
          <FoodMap />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// import Store Table component
import FoodMap from '@/components/FoodMap.vue'

export default {
  name: 'findTastyFood',
  data () {
    return {
      foodTypes: {
        BBQ: 'BBQ',
        hotpot: 'Hot Pot',
        ramen: 'Ramen'
      },
      // todo: get data from db
      tableRows: [
        {
          storeName: 'Store 1',
          address: 'Address 1',
          isClicked: false
        },
        {
          storeName: 'Store 2',
          address: 'Address 2',
          isClicked: false
        }
      ]
    }
  },
  components: {
    FoodMap
  },
  methods: {
    toggleColor (index) {
      this.tableRows[index].isClicked = !this.tableRows[index].isClicked
    }
  }
}
</script>
<style>
</style>
