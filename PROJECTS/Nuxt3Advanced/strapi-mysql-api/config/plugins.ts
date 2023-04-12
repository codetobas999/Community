// path: ./config/plugins.ts

module.exports = (env) => ({
    'users-permissions': {
        enabled: true,
        config: {
        jwt: {
            expiresIn: '2d', // Default millisecond (60s)  1 minute
        },
    }
  },
})
  