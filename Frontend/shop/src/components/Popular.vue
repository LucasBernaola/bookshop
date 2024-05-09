<template>
  <v-row>
    <v-col cols="12" sm="6" md="4" lg="3" v-for="(popular, i) in populars" :key="i">
      <router-link :to="{ name: 'books' }">
        <v-card class="mx-auto my-12 pb-4 product-card" max-width="374">
          <v-img height="250" class="mx-4" :src="popular.img"></v-img>
          <v-card-item class="mt-n4">
            <v-card-title class="text-center">{{ popular.title }}</v-card-title>
          </v-card-item>
          <v-card-text>
            <div class="text-center">
              {{ popular.bio }}
            </div>
            <v-row align="center" class="mx-0 mt-2">
              <v-rating
                :model-value="4.5"
                color="amber"
                density="compact"
                half-increments
                readonly
                size="small"
              ></v-rating>
              <v-spacer></v-spacer>
              <div class="text-grey ms-4">$ {{ popular.price }}</div>
            </v-row>
          </v-card-text>
        </v-card>
      </router-link>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    populars: [
      {
        "img": "image/twilight.jpg",
        "title": "Twilight",
        "price": "25.000",
      },
      {
        "img": "image/new-moon.jpg",
        "title": "New Moon",
        "price": "25.000",
      },
      {
        "img": "image/eclipse.jpg",
        "title": "Eclipse",
        "price": "25.000",
      },
      {
        "img": "image/breaking-dawn.jpg",
        "title": "Breaking Dawn",
        "price": "25.000",
      },
    ]
  })
}
</script>

<style scoped>
.product-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

@media screen and (max-width: 768px) {
  .product-card {
    max-width: 100%;
  }
  .product-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 14px rgba(0, 0, 0, 0.1);
  }
}
</style>
