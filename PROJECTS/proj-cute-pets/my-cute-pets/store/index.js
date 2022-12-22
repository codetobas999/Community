  export const state = () => ({
    setting_app:{
                  language:"",
                  theme:"default",
                  show_page:0,
                  token_age:15
                },
    //myState: 'Hello',
    //toggle_menu: false,
    //menus: [],            //Authorize Main Menu 
    //authorizes: [],       //Authorize Page & Component By User Login

    //Layout : main-default  
    drawer: false,
    fixed: false

  })
  
  export const mutations = {
    /*set_toggle_menu(state, newVal) {
      state.toggle_menu = newVal
    },
    set_authorizes(state, newVal) {
      state.authorizes = newVal
    },
    set_menus(state, newVal) {
      console.log('SETTING MENU TO', newVal)
      state.menus = newVal
    },  */

    //Layout : main-default 
    set_drawer(state, newDrawerState) {
      //console.log('STORE (SETTING DRAWER TO) :', newDrawerState)
      state.drawer = newDrawerState
    },
    set_fixed(state, newFixedState) {
      //console.log('STORE (SETTING FIXED TO)', newFixedState)
      state.fixed = newFixedState
    },
    set_settingApp(state, newsettingApp) {
      console.log('STORE (SETTING APP)', newsettingApp)
      state.setting_app = newsettingApp
    }
  }