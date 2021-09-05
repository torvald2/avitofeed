<template lang="pug">
  div(id="app")
    
    b-navbar(type="dark" variant="info")
      b-navbar-brand(href="#")
        img(src="https://placekitten.com/g/30/30" alt="Kitten")
        span.ml-2 Feed
      div
        b-navbar-nav.ml-auto
          b-container.right
            b-row
              b-col
                b-button(variant="info" ).mr-5
                  b-icon(icon="gear-fill" font-scale="1.5" )
              b-col
                b-nav-text Администратор 
              b-col
                b-button(variant="info").ml-5
                  b-icon(icon="box-arrow-right" font-scale="1.5" )
    router-view

</template>

<style>

</style>
