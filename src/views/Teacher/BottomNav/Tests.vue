<template>
  <div>
    <v-toolbar>
      <v-toolbar-side-icon>
        <v-icon>arrow_back_ios</v-icon>
      </v-toolbar-side-icon>
      <v-toolbar-title>Tests</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>search</v-icon>
      </v-btn>
    </v-toolbar>

    <v-container>
      <v-layout row wrap>
        <v-flex xs12 v-for="i in 10" :key="i">
          <v-card flat class="ourCard" height="250px">
            <!-- <v-img class="cardImage" :src="require(`@/assets/card_bg.png`)" ></v-img> -->

            <v-card-title primary-title>
              <h3 class="ourCardHeading display-1" style="font-family: Dosis, sans-serif">Test {{i}}</h3>
            </v-card-title>

            <v-layout column>
              <v-flex
                xs6
                style=" margin-left: 10px; font-size: 20px; margin-bottom: 10px"
              >Date: 23/2/42</v-flex>
              <v-flex
                xs6
                style="margin-left: 10px; font-size: 20px; margin-bottom: 10px;  "
              >Time: 10:00pm</v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-btn
          @click="dialog = !dialog"
          color="secondary"
          dark
          fixed
          style="margin: auto 16px 60px auto"
          bottom
          right
          fab
        >
          <v-icon>add</v-icon>
        </v-btn>

        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
          <template v-slot:activator="{ on }"></template>
          <v-card>
            <v-toolbar dark color="primary">
              <v-btn icon dark @click="dialog = false">
                <v-icon>close</v-icon>
              </v-btn>
              <v-toolbar-title>Add test</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                <v-btn dark flat @click="dialog = false">Save</v-btn>
              </v-toolbar-items>
            </v-toolbar>
            <v-list three-line subheader>
              <v-subheader>Information</v-subheader>
              <v-list-tile style="margin-top: 8rem">
                <v-layout column>
                  <v-flex>
                    <v-text-field v-model="test.testname" label="Test Name"></v-text-field>
                  </v-flex>
                  <v-flex>
                    <v-text-field v-model="test.organiser" label="Organised by"></v-text-field>
                  </v-flex>
                  <v-flex>
                    <v-text-field v-model="test.venue" label="Venue"></v-text-field>
                  </v-flex>
                  <v-flex>
                    <v-menu
                      v-model="menu1"
                      :close-on-content-click="false"
                      full-width
                      max-width="290"
                    >
                      <template v-slot:activator="{ on }">
                        <v-text-field
                          :value="computedDateFormattedMomentjs"
                          clearable
                          prepend-icon="calendar_today"
                          label="Pick date"
                          readonly
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker v-model="date" @change="menu1 = false"></v-date-picker>
                    </v-menu>
                  </v-flex>
                  <v-flex>
                    <v-menu
                      ref="menu"
                      v-model="menu2"
                      :close-on-content-click="false"
                      :nudge-right="40"
                      :return-value.sync="time"
                      lazy
                      transition="scale-transition"
                      offset-y
                      full-width
                      max-width="290px"
                      min-width="290px"
                    >
                      <template v-slot:activator="{ on }">
                        <v-text-field
                          v-model="time"
                          label="Picker in menu"
                          prepend-icon="access_time"
                          readonly
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-time-picker
                        v-if="menu2"
                        v-model="time"
                        full-width
                        @click:minute="$refs.menu.save(time)"
                      ></v-time-picker>
                    </v-menu>
                  </v-flex>
                </v-layout>
              </v-list-tile>
            </v-list>
            <v-divider style="margin-top: 8.5rem"></v-divider>
            <v-btn @click="postTestData">Post</v-btn>
            <v-list three-line subheader>
              <v-subheader>Questions</v-subheader>
            </v-list>
            <v-container>
              <v-card v-for="q in questions" :key="q"></v-card>
            </v-container>
          </v-card>
          <v-btn
            @click="questions = questions + 1"
            color="secondary"
            dark
            fixed
            style="margin: auto 16px 16px auto"
            bottom
            right
            fab
          >
            <v-icon>add</v-icon>
          </v-btn>
        </v-dialog>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";

export default {
  data() {
    return {
      test: {
        testname: "",
        organiser: "",
        venue: ""
      },
      time: null,
      menu2: false,
      modal2: false,
      questions: 1,
      date: new Date().toISOString().substr(0, 10),
      menu1: false,
      card_text:
        " adipisci. Ignota salutandi accusamus in sed, et per malis fuisset, qui id ludus appareat.",
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false
    };
  },
  computed: {
    computedDateFormattedMomentjs() {
      return this.date ? moment(this.date).format("dddd, MMMM Do YYYY") : "";
    },
    getRandomImage() {
      return "https://gradientjoy.com/400x300";
    }
  },
  methods: {
    postTestData() {
      var bodyFormData = new FormData();
      bodyFormData.set("testid", Math.floor(Math.random() * 90000) + 10000);
      bodyFormData.set("testname", this.test.testname);
      bodyFormData.set("organized", this.test.organiser);
      bodyFormData.set("testdate", this.computedDateFormattedMomentjs);
      bodyFormData.set("venue", this.test.venue);
      bodyFormData.set("time", this.time);

      axios({
        method: "post",
        url: "http://b6019fce.ngrok.io/api/test",
        data: bodyFormData,
        config: { headers: { "Content-Type": "multipart/form-data" } }
      })
        .then(function(response) {
          //handle success
          console.log(response);
        })
        .catch(function(response) {
          //handle error
          console.log(response);
        });
    }
  }
};
</script>

<style scoped>
.cardImage {
  margin-left: 150px;
  background-color: black;
  height: 80px;
  width: 300px;
}

.ourCard {
  background-image: url("../../../assets/card_bg.png");
  background-size: 220px 150px;
  background-position: right top;
}

.ourCardHeading {
  /* transform: translate(0px, -70px); */
}
</style>
