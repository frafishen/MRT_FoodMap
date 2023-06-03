<template>
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
                        <a role="button" class="badge badge-ghost badge-sm" href="https://www.google.com/">Go to Map</a>
                    </td>
                    <th>
                        <button class="btn btn-ghost btn-xs" @click="toggleMap">Details</button>
                    </th>
                    <th>
                        <button name="add fav" type="submit"
                            class="btn btn-sm mask mask-heart transition-colors duration-200"
                            :class="{ 'bg-red-400': row.isClicked, 'bg-gray-400': !row.isClicked }"
                            @click="toggleColor(index)"></button>
                    </th>
                </tr>
                <!-- row end -->
            </tbody>
        </table>
    </div>
</template>
<script>
export default {
  name: 'findTastyFood',
  data () {
    return {
      tableRows: [
        {
          storeName: 'Store 1',
          address: 'Address 1',
          isClicked: false
        },
        {
          storeName: 'Store 2',
          address: 'Address 2',
          isClicked: true
        },
        {
          storeName: 'Store 3',
          address: 'Address 3',
          isClicked: true
        },
        {
          storeName: 'Store 4',
          address: 'Address 4',
          isClicked: false
        }
      ]
    //   ],
    //   modifyFavoriteStatus: null
    }
  },
  components: {
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
