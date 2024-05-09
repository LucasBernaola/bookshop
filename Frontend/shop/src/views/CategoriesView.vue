<template>
  <div>
    <NavBar />
    <v-container>
      <v-row justify="center">
        <v-col v-for="category in categories" :key="category.id" cols="12" sm="6" md="4">
          <router-link :to="getCategoryRoute(category)" class="category-link">
            <v-card class="category-card" elevation="10">
              <v-img :src="'http://127.0.0.1:8000' + category.image_url" alt="Category Image" class="category-image"></v-img>
              <v-card-title class="category-name" style="font-size: 30px;">{{ category.name }}</v-card-title>
            </v-card>
          </router-link>
        </v-col>
      </v-row>
    </v-container>
    <Footer />
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import { ref, onMounted } from 'vue';

const categories = ref([]);

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/categories/');
    const data = await response.json();
    categories.value = data;
  } catch (error) {
    console.error('Error fetching categories:', error);
  }
});

const getCategoryRoute = (category) => {
  if (category.name === 'Books') {
    return '/books';
  } else if (category.name === 'School Supplies') {
    return '/school-supplies';
  } else {
    return `/categories/${category.name}`;
  }
};
</script>

<style scoped>
.category-card {
  margin: 20px;
  border-radius: 10px;
  overflow: hidden;
}

.category-link {
  text-decoration: none;
  color: inherit;
}

.category-image {
  height: 400px;
  object-fit: cover;
}

.category-name {
  text-align: center;
  padding: 20px 0;
  color: #000;
}
</style>
