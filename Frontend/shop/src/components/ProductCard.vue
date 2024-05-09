<template>
  <v-card class="product-card" elevation="10">
    <v-img class="product-image" :src="product.image" alt="Product Image"></v-img>
    <div class="product-details">
      <h3>{{ product.name }}</h3>
      <p v-if="!isExpanded">{{ truncatedDescription }}</p>
      <p v-else>{{ product.description }}</p>
      <span v-if="showToggle" class="toggle-button" @click="toggleDescription">
        {{ isExpanded ? 'See less' : 'See more' }}
      </span>
      <p class="currency-symbol"><span>$</span> {{ product.price }}</p>
    </div>
    <div class="quantity-controls">
      <v-card-actions class="quantity-actions">
        <v-btn icon @click="decrementQuantity">
          <v-icon>mdi-minus</v-icon>
        </v-btn>
        <span>{{ product.quantity }}</span>
        <v-btn icon @click="incrementQuantity">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-card-actions>
      <v-btn color="primary" class="add-to-cart-btn" @click="addToCart(product.id, product.quantity)">Add to Cart</v-btn>
    </div>
  </v-card>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import Swal from 'sweetalert2';

const store = useStore();
const props = defineProps({
  product: Object
});

const product = ref(props.product);
const isExpanded = ref(false);

const incrementQuantity = () => {
  product.value.quantity++;
};

const decrementQuantity = () => {
  if (product.value.quantity > 1) {
    product.value.quantity--;
  }
};

const addToCart = (productId, quantity) => {
  console.log('Adding to cart:', productId, quantity);
  store.dispatch('addToCart', { id: productId, quantity });
  Swal.fire({
    icon: 'success',
    title: 'Product added to cart',
    showConfirmButton: false,
    timer: 1500
  });
};

const showToggle = computed(() => props.product.description.length > 100);

const truncatedDescription = computed(() => {
  if (props.product.description.length <= 100) {
    return props.product.description;
  } else {
    return props.product.description.slice(0, 100) + '...';
  }
});

const toggleDescription = () => {
  isExpanded.value = !isExpanded.value;
};
</script>

<style scoped>
.product-card {
  width: 300px;
  height: auto;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.product-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-details {
  flex-grow: 1;
  text-align: center;
  padding: 10px;
}

.quantity-controls {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding: 10px;
}

.quantity-actions {
  display: flex;
  align-items: center;
}

.add-to-cart-btn {
  margin-top: 10px;
}

.currency-symbol{
  color: rgb(11, 11, 240);
}

.toggle-button {
  cursor: pointer;
  color: blue;
}
</style>
