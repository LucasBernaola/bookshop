describe('Home Page', () => {
  it('should load the home page and verify components', () => {
    // Visita la página principal
    cy.visit('/');

    // Verifica que exista un encabezado con el texto 'Welcome to My Website'
    cy.get('h1').should('contain.text', 'Welcome to My Website');

    // Verifica que la barra de navegación sea visible
    cy.get('.navbar').should('be.visible');

    // Verifica que la imagen de héroe sea visible
    cy.get('.hero-image').should('be.visible');

    // Agrega más comandos de Cypress para verificar otros componentes importantes de tu página
  });
});