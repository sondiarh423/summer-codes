<!DOCTYPE html>
<html>
<head>
<style>
.container {
    overflow: hidden;
    background-color: #333;
    font-family: Arial;
}

.container a {
    float: left;
    font-size: 16px;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.dropdown {
    float: left;
    overflow: hidden;
}

.dropdown .dropbtn {
    font-size: 16px;
    border: none;
    outline: none;
    color: white;
    padding: 14px 16px;
    background-color: inherit;
}

.container a:hover, .dropdown:hover .dropbtn {
    background-color: red;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    float: none;
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

.dropdown-content a:hover {
    background-color: #ddd;
}

.dropdown:hover .dropdown-content {
    display: block;
}
</style>
</head>
<body>

<div class="container">
  <div class="dropdown">
  <button class="dropbtn">Lips</button>
  <div class="dropdown-content">
    <a href="#">Lipstick</a>
    <a href="#">Lipliner</a>
    <a href="#">Lipgloss</a>
   </div>
 </div>

  <div class="dropdown">
  <button class="dropbtn">Face</button>
  <div class="dropdown-content">
    <a href="https://www.google.com">Foundation</a>
    <a href="#">Concelear</a>
    <a href="#">Eyebrows</a>
   </div>
 </div>

<div class="dropdown">
  <button class="dropbtn">Eyes</button>
  <div class="dropdown-content">
    <a href="#">Eyeshadow Palettes</a>
    <a href="#">Eyeliner</a>
    <a href="#">Mascara</a>
   </div>
 </div>

  <div class="dropdown">
    <button class="dropbtn">Skincare</button>
    <div class="dropdown-content">
      <a href="#">Dry Skin</a>
      <a href="#">Oily Skin</a>
      <a href="#">Acne Products</a>
      <a href="#">Spot Treatment</a>
      <a href="#">Body Wash</a>
    </div>
  </div>

  <div class="dropdown">
    <button class="dropbtn">Other</button>
    <div class="dropdown-content">
      <a href="#">Makeup Brushes</a>
      <a href="#">Sponges</a>
      <a href="#">Setting Sprays and Primers</a>
     </div>
  </div>

</body>
</html>
