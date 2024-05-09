<template>
  <v-row style="background-color: #080A21;">
    <v-col cols="12" sm="6" md="4" lg="3">
      <v-card class="mx-auto my-12 pb-4" max-width="374" flat color="#080A21">
        <v-card-item class="top-day">
          <v-card-title class="text-center">Deals of the day</v-card-title>
        </v-card-item>
        <v-card-text>
          <div class="text-center">
            <h1>
              <span v-for="(digit, index) in countdownDigits" :key="index" class="countdown-digit" :class="{ 'rotate': index >= dynamicIndexStart && index <= dynamicIndexEnd }">
                {{ digit }}
              </span>
            </h1>
          </div>
        </v-card-text>
      </v-card>
    </v-col>

    <v-col cols="12" sm="6" md="4" lg="3" v-for="(client, i) in clients" :key="i">
      <router-link :to="{ name: 'books' }">
        <v-card class="mx-auto my-12 pb-4 product-card" max-width="374">
          <v-img height="250" class="mx-4" :src="client.img"></v-img>
          <v-card-item class="mt-n4">
            <v-card-title class="text-center">{{ client.title }}</v-card-title>
          </v-card-item>
          <v-card-text>
            <div class="text-center">{{ client.bio }}</div>
            <v-row align="center" class="mx-0 mt-2">
              <v-rating :model-value="4.5" color="amber" density="compact" half-increments readonly size="small"></v-rating>
              <v-spacer></v-spacer>
              <div class="text-grey ms-4">{{ client.price }}</div>
            </v-row>
          </v-card-text>
        </v-card>
      </router-link>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      clients: [
        {
          img: "image/the_fellowship_rings.png",
          title: "The Fellowship of the Ring",
          price: "$ 25.000",
          bio: "The beginning of the adventure, and where the future of Middle-earth will remain in small hands...",
        },
        {
          img: "image/the_two_towers.png",
          title: "The Two Towers",
          price: "$ 25.000",
          bio: "The journey continues, friendship is tested, and a great battle for survival...",
        },
        {
          img: "image/the_returns_king.png",
          title: "The Return of the King",
          price: "$ 25.000",
          bio: "The battle of good against evil breaks out in the Pelennor Fields, can Frodo complete his quest?",
        },
      ],
      countdown: "12:00:00",
      dynamicIndexStart: 0,
      dynamicIndexEnd: 2
    };
  },
  computed: {
    countdownDigits() {
      return this.countdown.split("");
    }
  },
  mounted() {
    const now = new Date();
    const startTimestamp = now.getTime();
    const totalTime = 12 * 60 * 60 * 1000;
    setInterval(() => {
      const currentTime = new Date().getTime();
      const elapsedTime = currentTime - startTimestamp;
      const remainingTime = totalTime - elapsedTime;
      const hours = Math.floor(remainingTime / (1000 * 60 * 60));
      const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);
      this.countdown = `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
      this.dynamicIndexStart = seconds === 0 ? 0 : 7;
      this.dynamicIndexEnd = seconds === 0 ? 0 : 7;
    }, 1000);
  },
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

.top-day {
  margin-top: 120px;
}

.countdown {
  font-size: 3rem;
  font-weight: bold;
}

.countdown-digit {
  display: inline-block;
}

.rotate {
  animation: spin 1.4s linear infinite;
}

@media screen and (max-width: 768px) {
  .product-card {
    max-width: 100%;
    margin-bottom: 20px;
    transform: none;
  }

  .product-card:hover {
    transform: translateY(-8px);
  }
}
</style>

