const $btnSignIn= document.querySelector('.sign-in-btn'),
      $btnSignUp = document.querySelector('.sign-up-btn'),  
      $signUp = document.querySelector('.sign-up'),
      $signIn  = document.querySelector('.sign-in');

document.addEventListener('click', e => {
    if (e.target === $btnSignIn || e.target === $btnSignUp) {
        $signIn.classList.toggle('active');
        $signUp.classList.toggle('active')
    }
});

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('formRegistro');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const datos = new FormData(form);
    const usuario = Object.fromEntries(datos.entries());

    try {
      const respuesta = await fetch('http://localhost:8000/registrar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(usuario)
      });

      const resultado = await respuesta.json();
      alert(resultado.massage || "Usuario creado exitosamente 🙌");
      form.reset();
    } catch (error) {
      alert("Ocurrió un error al registrar.");
    }
  });
});
