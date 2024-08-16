// Function to get a random happiness message
function getRandomHappinessMessage() {
    const messages = [
        "Football is a game of mistakes. Whoever makes the fewest mistakes wins.” - Johan Cruyff1",
        "You have to fight to reach your dream. You have to sacrifice and work hard for it.” - Lionel Messi",
        "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing.” - Pelé1",
        "Football is played with your head. Your feet are just the tools.” - Andrea Pirlo",
        "“The more difficult the victory, the greater the happiness in winning.” - Pelé",
        "In football, the greatest satisfaction is winning when they say you can’t.” - Xavi",
        "Play for the badge on the front of the shirt and they’ll remember the name on the back. - Tony Adams",
        "Football is not just a game, it’s an art form.” - Arsene Wenger",
        "“The secret is to believe in your dreams; in your potential that you can be like your star.” - Neymar Jr.",
        "“Football, like life, is filled with ups and downs, and the most important thing is to keep moving forward and never give up.” - Diego Maradona",
        "“Football is a simple game; 22 men chase a ball for 90 minutes and at the end, the Germans always win,” - Gary Lineker.",
        "“The ball is round, the game lasts 90 minutes, and everything else is just theory,” - Sepp Herberger.",
        "“In football, the worst blindness is only seeing the ball,” - Nelson Falcão Rodrigues.",
        "Football is the ballet of the masses,” - Dmitri Shostakovich.",
        "“The more difficult the victory, the greater the happiness in winning,” - Pelé.",
    ];
    return messages[Math.floor(Math.random() * messages.length)];
  }
  
  // Function to update the footer date and message
  function updateFooter() {
    const currentDate = new Date().toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    document.getElementById("footer-date").textContent =
      "Today is " + currentDate;
    document.getElementById("footer-message").textContent =
      getRandomHappinessMessage();
  }
  
  // Call updateFooter function when the page loads
  window.onload = updateFooter;