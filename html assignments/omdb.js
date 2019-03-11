
let btnMovieInfo = document.getElementById("btnMovieInfo")
let movieTitleHeading = document.getElementById("movieTitleHeading")
let episodesUL = document.getElementById("episodesUL")

let Title= document.getElementById("Title")
let Year= document.getElementById("Year")
let Type= document.getElementById("Type")
let Poster= document.getElementById("Poster")

btnMovieInfo.addEventListener('click',function(){
  let url=
  "http://www.omdbapi.com/?s=batman&apikey=a55cc47b"
  let request = new XMLHttpRequest()
  request.open("GET",url)
  request.send()

  request.onload = function() {

    if(request.status != 200) {
      console.log("Server not found.")
    } else {
      console.log("Response Recieved")
      // responseText is the response received as a string
      console.log(request.responseText)
      // JSON.parse is a function to convert text to object
      console.log(JSON.parse(request.responseText))
      let moviesResponse = JSON.parse(request.responseText)
      movieDetails(moviesResponse)
    }
  }
})

function movieDetails(movie) {

  movieTitleHeading.innerHTML = movie.Title

let movieItemsLi = movies.map(function(movie){
  return '<li> <a href = "#" onclick = movieDetails("${movie.imdbID}")'> ${movie.Title}</a></li>'})

movieListUl.innerHTML = movieItemsLi.join('')}
