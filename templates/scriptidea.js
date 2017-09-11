<script>

    {% autoescape off %}
        let selectedmodels = {{ selectedmodels }};
    {% endautoescape %}

    function getPlant () {
        let randommodel = Math.floor(Math.random() * selectedmodels.length);
        let plant = selectedmodels[randommodel];
        return plant;
    }

    function updateEntities () {
        $("#cursor").attr('intersection-spawn', `event: click; mixin: ${getPlant()}`);
    }



</script>