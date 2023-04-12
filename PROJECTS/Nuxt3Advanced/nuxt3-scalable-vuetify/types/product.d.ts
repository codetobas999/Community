// define types for product read data from strapi

interface ImageDataAttributes {
    name: string
    alternativeText: string | null
    caption: string | null
    width: number
    height: number
    formats: {
      thumbnail: {
        name: string
        hash: string
        ext: string
        mime: string
        path: string | null
        width: number
        height: number
        size: number
        url: string
      }
      small: {
        name: string
        hash: string
        ext: string
        mime: string
        path: string | null
        width: number
        height: number
        size: number
        url: string
      }
      medium: {
        name: string
        hash: string
        ext: string
        mime: string
        path: string | null
        width: number
        height: number
        size: number
        url: string
      }
    }
    hash: string
  }
  
  interface ProductAttributes {
    title: string
    slug: string
    description: string
    price: number
    qty: number
    is_featured: boolean
    createdAt: string
    updatedAt: string
    publishedAt: string
    image: {
      data: [
        {
          id: number
          attributes: ImageDataAttributes
        }
      ]
    }
    category: {
      data: {
        id: number
        attributes: {
          title: string
          status: boolean
          createdAt: string
          updatedAt: string
          publishedAt: string
        }
      }
    }
  }
  
  interface ProductData {
    id: number
    attributes: ProductAttributes
  }
  
  interface ProductResponse {
    data: ProductData[]
  }

  export { ProductResponse }