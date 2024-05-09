<template>
  <v-footer >
    <v-card flat tile class="white--text py-12 px-5" width="100%" color="rgb(212, 214, 225)">
      <v-row>
        <v-col cols="12" xs="12" sm="6" md="4" class="pa-16">
          <div class="text-center">
            <span>P</span><strong>hoenix Bookshop</strong>
          </div>
          <v-card-text class="mt-2">
            <div class="text-center">
              The place where you will find all you need.
            </div>
            <div class="text-center">
              &copy; 2024 All Rights Reserved
            </div>
          </v-card-text>
        </v-col>
        <v-col cols="12" xs="12" sm="6" md="2" class="about-col">
          <v-card-text class="white--text pt-0">
            <h3>About</h3>
          </v-card-text>
          <v-card-text class="grey--text">How we Work</v-card-text>
          <v-card-text class="grey--text mt-n4">Our locals</v-card-text>
          <v-card-text class="grey--text mt-n4">Suppliers</v-card-text>
        </v-col>
        <v-col cols="12" xs="12" sm="6" md="2" class="delivery-col">
          <v-card-text class="white--text pt-0">
            <h3>Delivery</h3>
          </v-card-text>
          <v-card-text class="grey--text">Cost on Delivery</v-card-text>
          <v-card-text class="grey--text mt-n4">Payment Method</v-card-text>
          <v-card-text class="grey--text mt-n4">Returns</v-card-text>
        </v-col>
        <v-col cols="12" xs="12" sm="6" md="4" class="contact-col">
          <v-card-text class="white--text pt-0">
            <h3>Contact</h3>
          </v-card-text>
          <v-card-text class="grey--text mt-n4">phoenixbookshop@contact.com</v-card-text>
          <v-card-text class="grey--text mt-n4">+54212315644888</v-card-text>
        </v-col>
      </v-row>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data: () => ({

  }),
};
</script>

<style scoped>
.v-footer {
  background-color: rgb(212, 214, 225);
}

.about-col,
.delivery-col,
.contact-col {
  margin-top: 20px;
}

@media screen and (max-width: 768px) {
  .about-col,
  .delivery-col,
  .contact-col {
    margin-top: 0;
    margin-bottom: 20px;
  }
}
</style>

