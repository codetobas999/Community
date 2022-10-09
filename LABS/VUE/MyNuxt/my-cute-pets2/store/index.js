  export const state = () => ({
    //myState: 'Hello',
    drawer: false,
    authorize: []
  })
  
  export const mutations = {
    set_drawer(state, newVal) {
      state.drawer = newVal
    },
    set_authorize(state, newVal) {
      state.authorize = newVal
    },  
  }