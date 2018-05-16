document.addEventListener('DOMContentLoaded', function () {
  particleground(document.getElementById('particles'), {
    dotColor: '000000',
    lineColor: '#C4EBFE',
    directionX: 'right',
    directionY: 'up',
    density: '6000',
    particleRadius: 7,
    proximity: 140,
    parallax: false
  });
})
