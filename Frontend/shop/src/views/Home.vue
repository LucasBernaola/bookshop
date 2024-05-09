<template>
  <v-app>
    <NavBar />
    <v-main>
      <v-container>
        <v-row v-if="isLoading">
          <v-col cols="12" class="text-center">
            <v-progress-circular indeterminate color="primary"></v-progress-circular>
          </v-col>
        </v-row>
        <v-row v-else>
          <v-col cols="12">
            <v-carousel class="background" :visible="3">
              <v-carousel-item v-for="product in products" :key="product.id">
                <v-row class="align-center">
                  <v-col cols="12" md="4" class="d-flex justify-center">
                    <img :src="product.image" alt="Product Image" style="max-width: 100%" />
                  </v-col>
                  <v-col class="text-color" cols="12" md="8">
                    <h2>{{ product.name }}</h2>
                    <p>{{ product.description }}</p>
                  </v-col>
                </v-row>
              </v-carousel-item>
            </v-carousel>
          </v-col>
          <v-toolbar color="transparent">
              <v-toolbar-title>Popular Products</v-toolbar-title>
              <v-spacer></v-spacer>
          </v-toolbar>
          <v-col cols="12" sm="12" class="mt-10">
            <Popular />
          </v-col>
          <v-toolbar color="transparent">
              <v-toolbar-title>Featured Products</v-toolbar-title>
              <v-spacer></v-spacer>
          </v-toolbar>
          <v-col cols="12" sm="12" class="mt-10">
            <Featured />
          </v-col>
          <v-col cols="12" sm="12" class="mt-n10">
            <Client />
          </v-col>
        </v-row>
      </v-container>
    <Footer />
    </v-main>
  </v-app>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import Popular from '@/components/Popular.vue';
import Client from '@/components/Client.vue';
import Footer from '@/components/Footer.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';

const products = ref([]);
const isLoading = ref(true);
const isError = ref(false);

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/carousel/');
    products.value = response.data;
    isLoading.value = false;
  } catch (error) {
    console.error('Error fetching products:', error);
    isError.value = true;
    isLoading.value = false;
  }
});
</script>

<style scoped>
.background {
  background-color: rgb(8, 10, 23);
}

.text-color {
  color: #f5f5f5;
}

@media screen and (max-width: 768px) {
  .v-carousel-item {
    max-width: 80%;
    margin: auto;
  }
}
</style>
