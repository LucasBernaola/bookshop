<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <NavBar />
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <div class="cart-container">
          <h2>Shopping Cart</h2>
          <v-divider class="divider"></v-divider>
          <v-container v-if="cartItems.length === 0" class="empty-cart">
            <p>Your cart is empty</p>
          </v-container>
          <v-container v-else>
            <CartItem v-for="item in cartItems" :key="item.id" :product="item" />
            <v-divider class="divider"></v-divider>
            <div class="cart-total">
              <p>Total: ${{ total }}</p>
            </div>
            <v-btn color="primary" @click="openPaymentModal" class="paybtn">Pay</v-btn>
          </v-container>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
  
<script setup>
import NavBar from '../components/NavBar.vue';
import CartItem from '../components/CartItem.vue';
import Swal from 'sweetalert2';
import { useStore } from 'vuex';
import { computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useStore();
const { cartItems } = store.state;
const subtotal = computed(() => {
  return cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
});
const total = computed(() => {
  return subtotal.value;
});
  

const openPaymentModal = () => {
  const totalToPay = computed(() => {
    return store.getters.subtotal;
  });
  
  Swal.fire({
    title: 'Enter payment details',
    html: `
      <p>Total to pay: $${totalToPay.value}</p>
      <input id="cardNumber" type="text" placeholder="Card number">
      <input id="cardName" type="text" placeholder="Name/Lastname">
    `,
    showCancelButton: true,
    confirmButtonText: 'Confirm',
    cancelButtonText: 'Cancel',
    showLoaderOnConfirm: true,
    preConfirm: () => {
      const cardNumber = document.getElementById('cardNumber').value;
      const cardName = document.getElementById('cardName').value;
  
      if (!cardNumber || !cardName) {
        Swal.showValidationMessage('Por favor, complete todos los campos');
      } else {
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve();
          }, 2000);
        });
      }
    },
    allowOutsideClick: false
  }).then((result) => {
    if (result.isConfirmed) {
      router.push({ name: 'payment' });
      Swal.fire({
        title: 'Successful payment',
        icon: 'success',
        showConfirmButton: false,
        timer: 1500
      });
    }
  });
};
</script>
  
<style scoped>
.cart-container {
  margin: 20px;
}
  
.divider {
  margin-top: 20px;
  margin-bottom: 20px;
}
  
.empty-cart {
  text-align: center;
}
  
.cart-total {
  margin-top: 20px;
  font-weight: bold;
  font-size: 70px;
}

.paybtn {
  width: 100%;
}
</style>
  