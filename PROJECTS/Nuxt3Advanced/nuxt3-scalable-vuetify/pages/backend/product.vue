<script setup lang="ts">

  import EditData from "@/components/tables/EditData"
  import useStrapiApi from "@/composables/useStrapiApi"

  definePageMeta({
    layout: "backend",
  })

  useHead({
    title: 'Product',
    meta: [
      { 
        name: 'keywords', 
        content: 'Product, Nuxt 3, Backend'
      },
      {
        name: 'Description',
        content: 'Product Nuxt 3,  IT Genius Engineering'
      }
    ]
  })

  const dialog = ref(false);
  const search = ref("");
  const desserts = ref(EditData);
  const editedIndex = ref(-1);

  // Call Product API useStrapiApi
  const { data: products, error } = await useStrapiApi().getProducts()
  console.log(products.value?.data)


  function close() {
    dialog.value = false;
    setTimeout(() => {
    }, 300);
  }

  //Methods
  const filteredList = computed(() => {
    return desserts.value.filter((user: any) => {
      return user.userinfo.toLowerCase().includes(search.value.toLowerCase());
    });
  });

  //Computed Property
  const formTitle = computed(() => {
    return editedIndex.value === -1 ? "New Product" : "Edit Product";
  });

</script>

<template>
  <v-row>
    <v-col cols="12" sm="12">
      <v-card>
        <v-card-text class="pa-5">
          
          <v-row>
            <v-col cols="12" lg="4" md="6">
              <v-text-field
                density="compact"
                v-model="search"
                label="Search Products"
                hide-details
                variant="outlined"
              ></v-text-field>
            </v-col>
            <v-col cols="12" lg="8" md="6" class="text-right">

              <!-- Add Product Diaglog -->
              <v-dialog v-model="dialog">
                <template v-slot:activator="{ props }">
                  <v-btn color="primary" v-bind="props" class="ml-auto">
                    <MIcon name="ph:plus" /> Add Product
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title class="pa-4 bg-secondary">
                    <span class="title text-white">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-form ref="form">
                        <v-row>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              variant="outlined"
                              hide-details
                              label="Id"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              variant="outlined"
                              hide-details
                              label="User info"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              variant="outlined"
                              hide-details
                              label="User email"
                              type="email"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              variant="outlined"
                              hide-details
                              label="Phone"
                              type="phone"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              variant="outlined"
                              hide-details
                              label="Joining Date"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              variant="outlined"
                              hide-details
                              label="Role"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-form>
                    </v-container>
                  </v-card-text>

                  <v-card-actions class="pa-4">
                    <v-spacer></v-spacer>
                    <v-btn color="error" @click="close">Cancel</v-btn>
                    <v-btn
                      color="secondary"
                      variant="elevated"
                      >Save</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </v-dialog>

            </v-col>
          </v-row>

          <v-table class="mt-5">

            <thead>
              <tr>
                <th>Id</th>
                <th>ProductInfo</th>
                <th>Price</th>
                <th>Qty</th>
                <th>Category</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="product in products?.data" :key="product.id">
                <td>{{ product.id }}</td>
                <td>
                  <div class="d-flex align-center py-4">

                    <div v-if="product.attributes.image.data">
                      <v-img
                        :src="`http://localhost:1337${product.attributes.image.data[0].attributes.formats.thumbnail.url}`"
                        class="rounded-circle img-fluid"
                        width="100px"
                      ></v-img>
                    </div>
                    <div v-else>
                      <v-img
                        src="/images/products/4.jpg"
                        width="100px"
                        class="rounded-circle img-fluid"
                      ></v-img>
                    </div>

                    <div class="ml-5">
                      <h2>{{ product.attributes.title }}</h2>
                      <span class="subtitle-2 d-block font-weight-regular">{{
                        product.attributes.description.slice(0, 150)
                      }}...</span>
                    </div>
                  </div>
                </td>
                <td>{{ product.attributes.price }}</td>
                <td>{{ product.attributes.qty }}</td>
                <td>{{ product.attributes.category.data.attributes.title }}</td>
                <td>
                  <v-icon
                    small
                    class="mr-2 text-info cursor-pointer"
                    title="Edit"
                    >mdi-pencil</v-icon
                  >
                  <v-icon
                    small
                    class="text-error cursor-pointer"
                    title="Delete"
                    >mdi-delete</v-icon
                  >
                </td>
              </tr>
            </tbody>
            
          </v-table>

        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<style scoped></style>