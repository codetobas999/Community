  export const state = () => ({
    //myState: 'Hello',
    toggle_menu: false,
    menus: [],            //Authorize Main Menu 
    authorizes: [],       //Authorize Page & Component By User Login
    

  })
  
  export const mutations = {
    set_toggle_menu(state, newVal) {
      state.toggle_menu = newVal
    },
    set_authorizes(state, newVal) {
      state.authorizes = newVal
    },
    set_menus(state, newVal) {
      state.menus = newVal
    },  
  }