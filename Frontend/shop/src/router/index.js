import { createRouter, createWebHistory } from 'vue-router'
import ProductsView from '@/views/ProductsView.vue'
import CategoriesView from '@/views/CategoriesView.vue'
import BooksView from '@/views/BooksView.vue'
import SchoolSuppliesView from '@/views/SchoolSuppliesView.vue'
import CartView from '@/views/CartView.vue'
import PaymentView from '@/views/PaymentView.vue'
import SearchItemView from '@/views/SearchItemView.vue'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
      },
    ],
  },
  {
    path: '/products',
    name: 'products',
    component: ProductsView
  },
  {
    path: '/categories',
    name: 'categories',
    component: CategoriesView
  },
  {
    path: '/books',
    name: 'books',
    component: BooksView
  },
  {
    path: '/school-supplies',
    name: 'school-supplies',
    component: SchoolSuppliesView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/payment',
    name: 'payment',
    component: PaymentView
  },
  {
    path: '/search-results',
    name: 'search-results',
    component: SearchItemView,
    props: true,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router