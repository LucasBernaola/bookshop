<template>
    <v-card class="cart-item" elevation="2">
      <v-row align="center" justify="start">
        <v-col cols="3">
          <v-img :src="product.image" alt="Product Image" class="cart-item-image"></v-img>
        </v-col>
        <v-col cols="9">
          <div class="cart-item-details">
            <h3>{{ product.name }}</h3>
            <p>Price: ${{ product.price }}</p>
            <div class="quantity-controls">
              <v-btn icon @click="decrementQuantity" :disabled="product.quantity <= 1">
                <v-icon>mdi-minus</v-icon>
              </v-btn>
              <span>{{ product.quantity }}</span>
              <v-btn icon @click="incrementQuantity">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </div>
            <p>Subtotal: ${{ product.price * product.quantity }}</p>
            <v-btn color="error" @click="removeFromCart(product.id)">Remove</v-btn>
          </div>
        </v-col>
      </v-row>
    </v-card>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useStore } from 'vuex';
  import axios from 'axios';
  
  const props = defineProps({
    product: Object
  });
  
  const store = useStore();
  const product = ref(props.product);
  
  const updateQuantity = (quantity) => {
    if (quantity >= 1) {
      store.dispatch('updateQuantity', { productId: product.value.id, quantity });
    }
  };
  
  const decrementQuantity = () => {
    if (product.value.quantity > 1) {
      updateQuantity(product.value.quantity - 1);
    }
  };
  
  const incrementQuantity = () => {
    updateQuantity(product.value.quantity + 1);
  };
  
  const removeFromCart = (productId) => {
    store.dispatch('removeFromCart', productId);
  };
  
  onMounted(async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/products/${product.value.id}/`);
      Object.assign(product.value, response.data);
    } catch (error) {
      console.error('Error fetching product details:', error);
    }
  });
  </script>
  
  <style scoped>
  .cart-item {
    margin-bottom: 20px;
    padding: 10px;
  }
  
  .cart-item-image {
    width: 100%;
    height: auto;
  }
  
  .quantity-controls {
    display: flex;
    align-items: center;
  }
  
  .quantity-controls v-btn {
    min-width: 0;
  }
  
  .cart-item-details {
    margin-left: 20px;
  }
  </style>
  