import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    cartItems: [],
  },
  mutations: {
    addToCart(state, product) {
      const existingProduct = state.cartItems.find(item => item.id === product.id);
      if (existingProduct) {
        existingProduct.quantity += product.quantity;
      } else {
        state.cartItems.push(product);
      }
    },
    setSearchResults(state, results) {
      state.searchResults = results;
    },

    addToPurchaseHistory(state, purchase) {
      state.purchaseHistory.push(purchase);
    },
    removeFromCart(state, productId) {
      const productIndex = state.cartItems.findIndex(item => item.id === productId);
      if (productIndex !== -1) {
        state.cartItems.splice(productIndex, 1);
      }
    }, 

    clearCart(state) {
      state.cartItems = [];
    },
    
    updateQuantity(state, { productId, quantity }) {
      const product = state.cartItems.find(item => item.id === productId);
      if (product) {
        product.quantity = quantity;
      }
    }
  },
  actions: {
    async fetchProducts({ commit }) {
      try {
        const response = await axios.get('http://localhost:8000/api/products');
        commit('setProducts', response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
    addToCart({ commit }, product) {
      commit('addToCart', product);
    },
    removeFromCart({ commit }, productId) {
      commit('removeFromCart', productId);
    },
    updateQuantity({ commit }, { productId, quantity }) {
      commit('updateQuantity', { productId, quantity });
    },
    clearCart({ commit }) {
      commit('clearCart');
    },
    updateSearchResults({ commit }, results) {
      commit('setSearchResults', results);
    },
  },
  getters: {
    cartItems(state) {
      return state.cartItems;
    },
    subtotal(state) {
      return state.cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
    },
    getSearchResults(state) {
      return state.searchResults;
    },
  },
});