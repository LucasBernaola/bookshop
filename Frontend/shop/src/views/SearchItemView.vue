<template>
  <div>
    <NavBar />
    <div class="search-results">
      <v-container>
        <v-row>
          <v-col
            v-for="product in products"
            :key="product.id"
            cols="12"
            sm="6"
            md="4"
            lg="4"
          >
          <ProductCard :product="product" :quantity="product.quantity" />
          </v-col>
        </v-row>
      </v-container>
      <div v-if="products && products.length === 0" class="no-results">
        No results found.
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import ProductCard from '@/components/ProductCard.vue';
import { useStore } from 'vuex';
import { computed } from 'vue';

const store = useStore();
const productsResponse = computed(() => store.getters.getSearchResults);

const products = computed(() => {
  return productsResponse.value.map(product => {
    return { ...product, quantity: 1 };
  });
});
</script>


<style scoped>
.search-results {
  margin-top: 20px;
}

/* Estilos para separar los elementos y darles espacio */
.search-results .v-col {
  margin-bottom: 20px; /* Espacio entre las filas */
}

.no-results {
  text-align: center;
  margin-top: 20px;
  font-size: 18px;
  color: gray;
}
</style>
