function getRandomModel() {

    let models = ['http://127.0.0.1:8000/media/gardenbotvr/models/plant_qyA6PRn.dae',
        'http://127.0.0.1:8000/media/gardenbotvr/models/sunflower_0NQWYOe.dae',
        'http://127.0.0.1:8000/media/gardenbotvr/models/wildflower.dae'];
    let quotes = [];
    for (let i = 0; i < 6; i++) {
        quotes += models[Math.floor(Math.random() * 3)];
    }
    return quotes;
}

AFRAME.registerComponent('intersection-spawn', {
  schema: {
    default: '',
    parse: AFRAME.utils.styleParser.parse
  },

  init: function () {
    const data = this.data;
    const el = this.el;

    el.addEventListener(data.event, evt => {
      // Create element.
      const spawnEl = document.createElement('a-entity');

      // Snap intersection point to grid and offset from center.
      spawnEl.setAttribute('position', evt.detail.intersection.point);

      spawnEl.setAttribute('collada-model', `url(${getRandomModel()})`);

      // Set components and properties.
      Object.keys(data).forEach(name => {
        if (name === 'event') { return; }
        AFRAME.utils.entity.setComponentProperty(spawnEl, name, data[name]);
      });

      // Append to scene.
      el.sceneEl.appendChild(spawnEl);
    });
  }
});