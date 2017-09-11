AFRAME.registerComponent('random-model', {
  dependencies: ['id'],

  init: function () {
    this.el.setAttribute('material', 'color', getRandomModel());
  }
});

function getRandomModel() {
  const letters = '0123456789ABCDEF';
  var url = '#';
  for (var i = 0; i < 6; i++ ) {
    url += letters[Math.floor(Math.random() * 16)];
  }
  return url;
}