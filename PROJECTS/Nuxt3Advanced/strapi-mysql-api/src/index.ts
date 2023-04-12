const { faker } = require('@faker-js/faker')

export default {
  /**
   * An asynchronous register function that runs before
   * your application is initialized.
   *
   * This gives you an opportunity to extend code.
   */
  register(/*{ strapi }*/) {},

  /**
   * An asynchronous bootstrap function that runs before
   * your application gets started.
   *
   * This gives you an opportunity to set up your data model,
   * run jobs, or perform some special logic.
   */
  async bootstrap({ strapi }) {
    /*
    for (let i = 0; i < 100; i++) {
      await strapi.entityService.create("api::product.product",{
        data: {
          title: faker.word.adjective() + " " + faker.word.noun(),
          slug: faker.lorem.slug(),
          description: faker.lorem.paragraph(),
          price: faker.commerce.price(),
          qty: 5,
          is_featured: 1,
          category: 2,
          publishedAt: '2023-02-11 21:33:38.928000',
          created_by_id: 1,
          updated_by_id: 1
        },
      });
    }
    */
  },
};
