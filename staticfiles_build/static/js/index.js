AOS.init();
      // When the user scrolls down 20px from the top of the document, show the button
      //window.onscroll = function () { scrollFunction() };

      const counters = document.querySelectorAll('.counter')
      counters.forEach(counter => {
         counter.innerText = '0'
         const updateCounter = () => {
            const target = +counter.getAttribute('data-target')
            const c = +counter.innerText
            const increment = target / 2000
            if (c < target) {
               counter.innerText = `${Math.ceil(c + increment)}`
               setTimeout(updateCounter, 1)
            } else {
               counter.innerText = target
            }

         }
         updateCounter()


      })


      


      window.addEventListener('load', function () {
         new Glider(document.querySelector('.glider'), {
             slidesToShow: 1.5,
             dots: '.dots',
             arrows: {
                 prev: '.glider-prev',
                 next: '.glider-next'
             },
             responsive: [
                 {
                     // screens greater than >= 775px
                     breakpoint: 1400,
                     settings: {
                         // Set to `auto` and provide item width to adjust to viewport
                         slidesToShow: 6,
                         slidesToScroll: 'auto',
                         itemWidth: 250,
                         duration: 0.25
                     }
                 }, {
                     // screens greater than >= 1024px
                     breakpoint: 768,
                     settings: {
                         slidesToShow: 5,
                         slidesToScroll: 1,
                         itemWidth: 200,
                         duration: 0.25
                     }
                 }
             ]
         });
     });

      const open_accordion = (v) => {
         const accordion = document.querySelectorAll(".accordion")
         const child = document.querySelectorAll(".child")
         const group = document.querySelectorAll(".group ")
         var i
         //for (i = 0; i <= accordion.length; i++) {
            /*child[i].classList.add("hidden")
            group[i].classList.remove("[&:not([data-te-collapse-collapsed])]:bg-secondary-color")
            group[i].classList.remove("[&:not([data-te-collapse-collapsed])]:bg-white")*/


            
               child[v].classList.remove("hidden")
               //group[i].classList.remove("[&:not([data-te-collapse-collapsed])]:bg-white")
               //group[v].classList.add("bg-secondary-color")


           

         


      }

      const nav__menu__open = document.querySelector("#nav__menu__open")
      const btn__menu__open = document.querySelector("#btn__menu__open")
      const btn__menu__fermer = document.querySelector("#btn__menu__fermer")

      btn__menu__open.addEventListener("click",()=>{
         nav__menu__open.classList.remove("hidden")
         btn__menu__open.classList.add("hidden")
         btn__menu__fermer.classList.remove("hidden")
      })
      btn__menu__fermer.addEventListener("click",()=>{
         nav__menu__open.classList.add("hidden")
         btn__menu__fermer.classList.add("hidden")
         btn__menu__open.classList.remove("hidden")
      })