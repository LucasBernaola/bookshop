<template>
  <div>
    <NavBar />
    <v-container>
      <h2 class="text-center">¡Successful payment!</h2>
      <p class="subtext-center">Thanks for buy. Here are the details:</p>
      <v-list>
        <v-list-item v-for="item in cartItems" :key="item.id">
          <v-list-item-content>
            <v-list-item-title>{{ item.name }}</v-list-item-title>
            <v-list-item-subtitle>$ {{ item.price }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <p class="text-center">Total: ${{ total }}</p>
      <v-row justify="center" class="mt-6">
        <v-btn color="primary" @click="backToMenu">Back to Home</v-btn>
      </v-row>
    </v-container>
  </div>
</template>
  
<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import NavBar from '../components/NavBar.vue';
  
const store = useStore();
const router = useRouter();
  
const cartItems = store.getters.cartItems;
const total = store.getters.subtotal;
  
const backToMenu = () => {
  store.dispatch('clearCart');
  router.push({ name: 'Home' });
};
</script>
  
<style scoped>
.text-center {
  text-align: center;
  font-size: 50px;
}

.subtext-center {
  text-align: center;
  font-size: 40px;
}
</style>
  