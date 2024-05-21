var menu =document.querySelector("#nav i")
var cross =document.querySelector("#full i")


var  tl =gsap.timeline()

tl.to("#full",{
    right:0,
    duration:0.5
})
tl.from("#full a",{
    x:150,
    duration:0.6,
    stagger:0.28,
    opacity:0
})
tl.from("#full i",{
    opacity:0,
})
tl.pause()

menu.addEventListener("click",function(){
    tl.play()
})
cross.addEventListener("click",function(){
    tl.reverse()
})

var body = document.querySelector("body")
// var cursor =document.querySelector("#cursor")
var imageDiv = document.querySelector("#full a")

body.addEventListener("mousemove",function(dets){
    gsap.to("#cursor",{
        x:dets.x,
        y:dets.y,
        duration:0.6,
        // easing:"back.out",
       
    })
})


// wrapper.addEventListener("mousemove",function(dets){
//     gsap.to("#cursor",{
//         x:dets.x,
//         y:dets.y,
//         duration:0.6,
//         easing:"back.out",
       
//     })
// })

    
imageDiv.addEventListener("mouseenter",function(){
    // cursor.innerHTML ="view more"
    gsap.to("#cursor",{
        scale:3,
        backgroundColor:"#ffffff8a",

    })
})

imageDiv.addEventListener("mouseleave",function(){
    cursor.innerHTML=""
    gsap.to("#cursor",{
        scale:1,
        backgroundColor:"#fff"

    })
})