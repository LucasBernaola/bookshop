<template>
  <v-row>
    <v-col cols="12" sm="6" md="4" lg="3" v-for="(feature, i) in featured" :key="i">
      <router-link :to="{ name: 'products' }">
        <v-card class="mx-auto my-12 pb-4 product-card" max-width="374">
          <v-img height="250" class="mx-4" :src="feature.img"></v-img>

          <v-card-item class="mt-n4">
            <v-card-title class="text-center">{{ feature.title }}</v-card-title>
          </v-card-item>

          <v-card-text>
            <div class="text-center">
              {{ feature.bio }}
            </div>
            <v-row align="center" class="mx-0 mt-2">
              <v-spacer></v-spacer>
              <div class="text-grey ms-4">{{ feature.price }}</div>
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
    featured: [
      {
        img: "image/pelikan_marker_x4.png",
        title: "Pelikan Marker",
        price: "$ 25.000",
        bio: "Permanent marker 711 ",
      },
      {
        img: "image/pelikan_pen_black.png",
        title: "Pelikan Black Pen",
        price: "$ 25.000",
        bio: "Ballpoint pen with grip",
      },
      {
        img: "image/spiral_homework_notebook.png",
        title: "Potosí Spiral Notebook",
        price: "$ 25.000",
        bio: "Striped leaves",
      },
      {
        img: "image/mapped_black_pencil.png",
        title: "Mapped black pencil",
        price: "$ 25.000",
        bio: "12 pencil black HB=2",
      },
    ],
  }),
};
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
    transform: none;
  }

  .product-card:hover {
    transform: translateY(-8px);
  }
}
</style>

