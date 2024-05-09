<template>
  <v-toolbar flat class="navbar">
    <template v-slot:prepend>
    <v-app-bar-nav-icon @click="toggleMenu"></v-app-bar-nav-icon>
    <v-menu v-model="menuOpen" offset-y>
      <v-list>
        <router-link class="nav-link" to="/" @click.native="handleItemClick('Home')">
          <v-list-item link>Home</v-list-item>
        </router-link>
        <router-link class="nav-link" to="/categories" @click.native="handleItemClick('Categories')">
          <v-list-item link>Categories</v-list-item>
        </router-link>
        <router-link class="nav-link" to="/products" @click.native="handleItemClick('Products')">
          <v-list-item link>Products</v-list-item>
        </router-link>
        <router-link class="nav-link" to="/cart" @click.native="handleItemClick('Cart')">
          <v-list-item link><svg-icon type="mdi" :path="path" class="carticon"></svg-icon></v-list-item>
        </router-link>
      </v-list>
    </v-menu>
</template>  
    <router-link aria-current="page" to="/" class="nav-link">
      <v-app-bar-title>Phoenix BookShop</v-app-bar-title>
    </router-link>
    <v-spacer></v-spacer>
    <v-text-field
      v-model="searchQuery"
      @keyup.enter="performSearch"
      density="compact"
      variant="solo"
      label="Search products"
      append-inner-icon="mdi-magnify"
      single-line
      hide-details
      flat
    ></v-text-field>
    <v-spacer></v-spacer>  
    <router-link aria-current="page" to="/categories" class="nav-link">
      <v-btn class="nav-button">Categories</v-btn>
    </router-link> 
    <router-link aria-current="page" to="/products" class="nav-link">
      <v-btn class="nav-button">Products</v-btn>
    </router-link>
    <router-link to="/cart" class="cart-link">
      <svg-icon type="mdi" :path="path" class="carticon"></svg-icon>
      <span class="cart-indicator">{{ cartIndicator }}</span>
    </router-link>
    <a href="http://127.0.0.1:8000/admin/login/?next=/admin/" target="_blank" class="nav-link admin-link">
        Admin Access
    </a>
  </v-toolbar>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { ref } from 'vue';


import SvgIcon from '@jamescoyle/vue-icon';
import { mdiCartOutline } from '@mdi/js';

const router = useRouter();
const store = useStore();

const path = mdiCartOutline;

let searchQuery = '';

const cartIndicator = computed(() => store.state.cartItems.length);

const performSearch = async () => {
  try {
    if (!searchQuery.trim()) {
      return;
    }

    const response = await axios.get(`http://127.0.0.1:8000/api/products/search/?q=${searchQuery}`);
    console.log('API Response:', response.data);
    const searchResults = response.data;
    
    store.dispatch('updateSearchResults', searchResults);

    router.push({ name: 'search-results' });
  } catch (error) {
    console.log('Error performing search:', error);
  }
}

const menuOpen = ref(false);

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};

const handleItemClick = (option) => {
  console.log('Clicked on:', option);
  menuOpen.value = false;
};
</script>

<style scoped>
.nav-link {
  text-decoration: none;
  color: #333;
}

.nav-button,
.cart-link {
  margin-right: 10px;
}

.carticon {
  color: #333;
  margin-right: 10px;
}

.cart-indicator {
  background-color: #333;
  color: white;
  border-radius: 30%;
  padding: 8px 8px;
  font-size: 12px;
  position: absolute;
  top: 5px;
  right: 120px;
}

.admin-link {
  margin-right: 10px;
  margin-left: 10px;
}

.v-menu {
 margin-top: 60px;
}

@media screen and (max-width: 768px) {
  .nav-button,
  .cart-link,
  .admin-link {
    display: none;
  }

  .cart-indicator {
    right: 10px;
  }

  .v-menu {
    margin-top: 40px;
  }

  .nav-title {
    display: inline-block;
  }
}
</style>

