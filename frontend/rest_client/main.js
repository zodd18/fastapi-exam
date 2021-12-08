new Vue({
  el: "#app",
  data: {
    geocaches: null,
    geocaches_hint_inside: null,
    logbooks: null,
    logbooks_by_email: null,
    geocaches_not_found: null,
  },
  methods: {
    async getGeocaches() {
      axios
        .get("http://localhost:8000/geocaches")
        .then((response) => {
          this.geocaches = response.data;
          console.log(this.geocaches);
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    async getGeocachesWithHintInside() {
        axios
          .get("http://localhost:8000/geocaches/hint/inside")
          .then((response) => {
            this.geocaches_hint_inside = response.data;
            console.log(this.geocaches_hint_inside);
          })
          .catch(function (error) {
            console.log(error);
          });
    },

    async getLogbooks() {
        axios
          .get("http://localhost:8000/logbooks")
          .then((response) => {
            this.logbooks = response.data;
            console.log(this.logbooks);
          })
          .catch(function (error) {
            console.log(error);
          });
    },

    async getLogbooksByEmail() {
        inputEmail = document.getElementById("input_email").value;

        if (inputEmail != null || inputEmail != "") {
            axios
            .get("http://localhost:8000/geocaches/email/" + inputEmail)
            .then((response) => {
              this.logbooks_by_email = response.data;
              console.log(this.logbooks_by_email);
            })
            .catch(function (error) {
              console.log(error);
            });

        }
    },
    
    async getNotFoundGeocaches() {
        axios
          .get("http://localhost:8000/geocaches-not-found")
          .then((response) => {
            this.geocaches_not_found = response.data;
            console.log(this.geocaches_not_found);
          })
          .catch(function (error) {
            console.log(error);
          });
    },
    
  },
  mounted() {
    this.getGeocaches();
    this.getGeocachesWithHintInside();
    this.getLogbooks();
    this.getNotFoundGeocaches();
  },
});
