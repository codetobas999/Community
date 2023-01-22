const configs = {
    development:{
        BASE_URL: 'http://localhost:3000',
        BASE_API_URL: 'http://127.0.0.1:8000'
        
    },
    staging:{
        BASE_URL: 'http://localhost:4000',
        BASE_API_URL: 'http://127.0.0.1:8000'
    },
    production:{
        BASE_URL: 'http://localhost:5000',
        BASE_API_URL: 'http://127.0.0.1:8000'
    },    
}

const nodeEnv = process.env.NODE_ENV
module.exports = configs[nodeEnv]