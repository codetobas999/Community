export default defineNuxtRouteMiddleware((to, from) => {
    
    // check local storage for token
    /*const token = localStorage.getItem('token')
    if (!token) {
        return navigateTo('/')
    }
    */
    //get token from cookie
    const token = useCookie('token')
    console.log("token : " + token) 
    // if no token, redirect to login page
    if (!token.value) {
        return navigateTo('/')
    }
 
})