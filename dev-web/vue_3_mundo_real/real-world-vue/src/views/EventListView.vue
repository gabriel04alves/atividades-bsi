<script setup>
  import EventCard from '@/components/EventCard.vue';
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import EventService from '@/services/EventService.js'

  const events = ref(null)

  onMounted(() => {
    EventService.getEvents()
      .then((res) => {
        events.value = res.data
      }) .catch((error) => {
        console.log(error)
      })
  })
</script>

<template>
  <h1>Events For Good</h1>
  <div class="events">
    <EventCard v-for="event in events" :key="event.id" :event="event" />
  </div>
</template>

<style scoped>
.events {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>