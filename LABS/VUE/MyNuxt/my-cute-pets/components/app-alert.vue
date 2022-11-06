<template>
  <v-flex>
    <template v-for="alert in alerts">
      <v-alert
        class="mb-2"
        :key="alert.id"
        outlined
        dense
        text
        :type="alert.type"
        transition="scale-transition"
      >
        <v-row align="center" no-gutters>
          <v-col class="pa-0">
            {{ alert.message }}
          </v-col>
          <v-col class="shrink">
            <v-btn icon :color="alert.type" @click="remove(alert)" small
              ><v-icon>mdi-close-circle</v-icon></v-btn
            >
          </v-col>
        </v-row>
      </v-alert>
    </template>
  </v-flex>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Alert',
  computed: {
    ...mapGetters({ alerts: 'alert/getAll' }),
  },
  methods: {
    ...mapActions({ remove: 'alert/remove' }),
    ...mapActions({ clear: 'alert/clear' }),
  },
}
</script>
