#!/usr/bin/env python
# coding: utf-8

styles = """<style>
.hover-effect-container {
    position: relative;
    display: inline-block;
  }

  .hover-effect-text {
    display: inline-block;
    position: relative;
    z-index: 1;
    font-size: 20px;
    transition: color 0.3s ease;
    padding: 15px;
    color: #fffafa;
  }

  .hover-effect-background {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 100%;
    background: linear-gradient(to right, #6495ed, #6495ed));
    transition: right 0.3s ease, height 0.3s ease;
    border-radius: 15px;
  }

  .hover-effect-container:hover .hover-effect-background {
    right: 0;
    border-radius: 10px;
  }

  .hover-effect-container:hover .hover-effect-text {
    color: rgb(255, 198, 196);
  }
  .card-container {
    display: flex;
    justify-content: space-between;
    margin: 0px 0;
}

.card {
    width: 320px;  /* Adjust the width as needed */
    height: 250px;  /* Half of the original height */
    background-color: rgb(139, 48, 88);
    border: 1px solid ccc;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    transition: background-color 0.5s ease;
}

.card:hover {
    background-color: rgb(103, 32, 68);
}

.card-content {
    padding: 20px;
    color: rgb(255, 198, 196);
}

.title {
    color: rgb(227, 129, 145);
}

.text-gradient-hover {
    font-size: 18px;
    padding: 0px;  
    background: linear-gradient(to right, rgb(173, 70, 108), rgb(227, 129, 145));
    color: rgb(255, 198, 196);
    transition: background-position 0.3s ease-in-out, color 0.5s ease;  /* Specify the transition duration for color */
    background-size: 200% 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%; /* Ensure the element takes the full height of its container */
}

.text-gradient-hover:hover {
    background-position: right center;
    color: rgb(103, 32, 68);
}

.text-gradient-hover h2 {
    padding: 0px;  /* Adjust the outer padding as needed */
    margin: 10;  /* Remove default margin to ensure the padding is consistent */
}

.hover-effect {
    background-color: rgb(255, 220, 196);
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
  }

  .hover-effect:hover {
    background-color: #ffd2ae;
  }

  .text {
  padding: 20px;
    font-size: 22px;
    font-family: 'Arial', Times, serif;
    line-height: 1.6em;
    text-align: center;
    color: #333;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  }

  .hover-effect {
    padding: 15px;
    background-color: #45b1e8;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    border-radius:45px 100px;
  }

  .hover-effect .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, #f0f8ff, #f0f8ff);
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .hover-effect:hover .overlay {
    opacity: 1;
  }

  .hover-effect:hover .text {
    color: #45b1e8;
  }

  .text {
    padding: 5px;
    position: relative;
    z-index: 1;
    transition: color 0.3s ease; 
    color: #f0f8ff;
    text-align:center;
    font-family:cursive;
    font-size: 28px;
    font-family:calibri;
  }

  <style>
  .hover-steps {
    margin: 20px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background-color: #45b1e8; /* Set the custom background color here */
    border-radius:10px
  }

  .hover-steps .overlay-steps {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, #45b1e8, #45b1e8));
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .hover-steps:hover .overlay-steps {
    opacity: 1;
  }

  .hover-steps:hover .text-steps {
    color: #45b1e8;
  }

  .text-steps {
    padding: 15px;
    position: relative;
    z-index: 1;
    font-size: 24px;
    transition: color 0.3s ease; 
    color: #45b1e8;
    text-align: center;
    
  }

  .three-d-shape {
        position: relative;
        width: 250px;
        height: 30px;
        background: linear-gradient(to right, rgb(103, 32, 68), rgb(173, 70, 108));
        border-radius: 10px;
        box-shadow: 1px 1px 1px #0000ff;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        overflow: hidden;
        float: right; /* Add this property to move it to the right */
    }
    .three-d-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 12px;
        font-weight: bold;
    }
    .three-d-shape:hover {
        transform: translate(5px, 5px);
        box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.3);
    }

    <style>
  .visual-steps {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background: linear-gradient(to right, #0000ff, black);
    border-radius: 10px;
    transition: background 0.7s ease;
  }

  .visual-steps:hover {
    background: linear-gradient(to right, rgb(255, 198, 196), rgb(255, 198, 196));
  }

  .visual-steps .overlay-visual-steps {
    position: absolute;
    top: 0;
    left: -100%; /* Initial position off-screen to the left */
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgb(173, 70, 108), rgb(173, 70, 108));
    opacity: 0;
    transition: left 0.7s ease, opacity 0.7s ease;
  }

  .visual-steps:hover .overlay-visual-steps {
    left: 0; /* Move to the original position on hover */
    opacity: 1;
  }

  .visual-steps:hover .text-visual-steps {
    color: rgb(255, 198, 196);
  }

  .text-visual-steps {
    padding: 5px;
    position: relative;
    z-index: 1;
    font-size: 18px;
    transition: color 0.3s ease; 
    color: rgb(139, 48, 88);
    text-align: center;
  }

  .button3d {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
    outline: none;
    color: #D6F3FF;
    background-color: #45b1e8;
    border: none;
    border-radius: 5px;
    box-shadow: 0 5px #D6F3FF;
    position: relative;
    transition: background-color 0.3s, color 0.3s;  /* Added color transition */
    margin: 5px 0;  /* Added margin of 5px from top and bottom */
}

.button3d:active {
    top: 5px;
    box-shadow: 0 0 #D6F3FF;
}

.button3d:hover {
    background-color: #D6F3FF;
    color: #45b1e8;  /* Text color changes to #45b1e8 on hover */
    box-shadow: 0 5px #45b1e8;  /* Change the box shadow on hover */
}
  .box-row {
    display: flex;
    justify-content: space-around;
  }

  .moving-box-container {
    width: 250px;
    height: 400px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 1px;
  }

  .moving-box {
    width: 300px;
    height: 330px;
    background-color: #D6F3FF;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.5s ease, background-color 0.5s ease;
    cursor: pointer;
    border-radius: 20px; /* Added more border-radius for curved corners */
  }

  .animated-face {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: #D6F3FF;
    opacity: 0.7;
    transform: translateZ(10px);
    transition: background-color 0.5s ease; /* Added transition for background-color */
    border-radius: 20px; /* Added more border-radius for curved corners */
  }

  .box-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: blue;
    text-align: center;
    font-size: 30px; /* Adjusted font size */
    line-height: 1.2; /* Added line-height for spacing between lines */
    z-index: 2;
    padding: 10px; /* Added padding for space around the text */
    transition: color 0.5s ease, font-size 0.5s ease, padding 0.5s ease; /* Added transition for text color, font size, and padding */
  }

  .moving-box:hover {
    transform: translateY(-30px) scale(1.1); /* Adjust the distance and size change on hover */
    background-color: #fffafa; /* Change the color on hover */
  }

  .moving-box:hover .animated-face {
    background-color: #45b1e8; /* Change the color of the face on hover */
  }

  .moving-box:hover .box-content {
    color: black; /* Change the text color on hover */
  }

  /* Remove the outline for focused elements within the .box-row */
  .box-row :focus {
    outline: none;
  }
</style>
"""



get_ipython().run_line_magic('store', 'styles')
