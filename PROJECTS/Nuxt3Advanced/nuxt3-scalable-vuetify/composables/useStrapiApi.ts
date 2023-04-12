import { ProductResponse } from '@/types/product'

export default() => {

    // get token from cookie
    const token = useCookie('token')

    const config = useRuntimeConfig()
    const STRAPI_URL: string = config.strapi.url

    const get = async <T>(endpoint: string) => {
        return useFetch<T>(`${STRAPI_URL}/${endpoint}?populate=*`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token.value}`
            },
            cache: 'no-cache'
        })
    }

    // Get all products
    const getProducts = async () => {
        return await get<ProductResponse>('products')
    }


    return {
        get,
        getProducts
    }

}