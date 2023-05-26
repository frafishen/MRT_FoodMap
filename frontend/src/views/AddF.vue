<template>
  <div>
    <h2>添加最愛</h2>
    <input v-model="newFavorite" type="text" placeholder="輸入最愛項目">
    <button @click="addFavorite">添加</button>
    <button @click="back">返回</button>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'AddF',
  methods: {
    back () {
      this.$router.push('/favorite')
    }
  },
  setup () {
    const store = useStore()
    const newFavorite = ref('')

    const addFavorite = () => {
      if (newFavorite.value.trim() !== '') {
        const favorite = { id: Date.now(), name: newFavorite.value }
        store.dispatch('addFavorite', favorite)
        newFavorite.value = ''
      }
    }

    return {
      newFavorite,
      addFavorite
    }
  }
}
</script>
