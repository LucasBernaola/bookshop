<template>
  <div>
    <NavBar />
    <v-container>
      <v-row>
        <v-col v-for="product in displayedProducts" :key="product.id" cols="12" sm="6" md="4">
          <ProductCard :product="product" />
        </v-col>
      </v-row>
    </v-container>
    <v-pagination v-model="currentPage" :length="totalPages" @input="fetchProducts" />
    <Footer />
  </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import ProductCard from '../components/ProductCard.vue';
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';

const products = ref([]);
const currentPage = ref(1);
const itemsPerPage = 6;

onMounted(fetchProducts);

async function fetchProducts() {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/products/?category=23&page=${currentPage.value}&limit=${itemsPerPage}`);
    response.data.forEach(product => {
      product.quantity = ref(1);
    });
    products.value = response.data;
  } catch (error) {
    console.error('Error fetching library items:', error);
  }
}

const totalPages = computed(() => Math.ceil(products.value.length / itemsPerPage));

const displayedProducts = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return products.value.slice(start, end);
});
</script>


  
  