<template>
  <v-container grid-list-lg>
    <v-card :v-for="job in jobs" :key="job" class="mb-2">
      <v-card-title>
        <div class="headline">{{ job.jobTitle }}</div>
      </v-card-title>

      <v-card-text>
        <v-layout column>
          <v-layout class="px-2">
            <v-flex xs6>
              <strong>{{ job.jobPaymentMode }}</strong>
            </v-flex>
            <v-flex xs6 class="text-xs-right">{{ job.jobPostDate }}</v-flex>
          </v-layout>

          <v-flex xs12 justify-center align-center>Skill level - {{ job.jobSkillLevel }}</v-flex>

          <v-layout class="px-1">
            <v-flex xs6>
              <v-icon color="orange darken-2">star</v-icon>
              {{job.jobRating}}
            </v-flex>

            <v-flex xs6 class="text-xs-right">Proposals - {{ job.jobProposals }}</v-flex>
          </v-layout>
        </v-layout>
      </v-card-text>
    </v-card>

    <v-btn fab @click="changeAddProposal(true)" fixed right bottom class="my-5" dark color="secondary">
      <div>
        <v-icon dark medium>add</v-icon>
      </div>
    </v-btn>

    <v-dialog
      v-model="addProposal"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
      scrollable
    >
      <v-card tile>
        <v-toolbar card dark color="teal">
          <v-btn dark @click="changeAddProposal(false)">
            <v-icon>close</v-icon>
          </v-btn>
          <v-toolbar-title>Proposal</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark flat @click="changeAddProposal(false)">Submit</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-card-text>
          <v-stepper v-model="e1">
            <v-stepper-header>
              <v-stepper-step :complete="e1 > 1" step="1" color="teal">Introduction</v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="e1 > 2" step="2" color="teal">Project</v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="e1 > 3" step="3" color="teal">Skills</v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="e1 > 4" step="4" color="teal">Budget</v-stepper-step>
              <v-divider></v-divider>
            </v-stepper-header>

            <v-stepper-items>
              <v-stepper-content step="1">
                <v-text-field v-model="newJob.jobTitle" label="Job title"></v-text-field>

                <v-textarea
                  v-model="newJob.jobDetail"
                  name="input-7-4"
                  label="Job details"
                  placeholder="Please enter a descriptive job description for the job that the freelancers will look at."
                ></v-textarea>

                <v-btn color="teal white--text" @click="e1 = 2">Next</v-btn>

                <v-btn flat @click="changeAddProposal(false)">Back</v-btn>
              </v-stepper-content>

              <v-stepper-content step="2">
                <v-menu>
                  <v-btn slot="activator" color="teal" dark>Project status</v-btn>

                  <v-list>
                    <v-list-tile
                      v-for="(item, i) in items"
                      :key="i"
                      @click="newJob.jobType = item.title"
                    >
                      <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>

                <div>
                  <v-btn color="teal white--text" @click="e1 = 3">Next</v-btn>

                  <v-btn flat @click="e1 = 1">Back</v-btn>
                </div>
              </v-stepper-content>

              <v-stepper-content step="3">
                <v-select
                  v-model="newJob.jobSkills"
                  :items="skills"
                  label="Skills required"
                  multiple
                >
                  <v-list-tile slot="prepend-item" ripple>
                    <v-list-tile-action>
                      <v-icon :color="selectedSkills.length > 0 ? 'indigo darken-4' : ''"></v-icon>
                    </v-list-tile-action>
                  </v-list-tile>
                  <v-divider slot="prepend-item" class="mt-2"></v-divider>
                  <v-divider slot="append-item" class="mb-2"></v-divider>
                </v-select>

                <div>
                  <v-menu>
                    <v-btn slot="activator" color="teal" dark>Skill level required</v-btn>

                    <v-list>
                      <v-list-tile
                        v-for="(item, i) in skillLevel"
                        :key="i"
                        @click="newJob.jobSkillLevel = item.title"
                      >
                        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                      </v-list-tile>
                    </v-list>
                  </v-menu>
                </div>

                <v-btn color="teal white--text" @click="e1 = 4">Next</v-btn>

                <v-btn flat @click="e1 = 2">Back</v-btn>
              </v-stepper-content>

              <v-stepper-content step="4">
                <v-layout align-center justify-center>
                  <v-flex xs6 class="text-xs-center">
                    <font class="headline">Your budget for this job is</font>
                    <v-text-field v-model="newJob.jobBudget" prefix="ETH"></v-text-field>
                  </v-flex>
                </v-layout>

                <div class="text-xs-center">
                  <v-menu>
                    <v-btn slot="activator" color="teal" dark>Payment Mode</v-btn>

                    <v-list>
                      <v-list-tile
                        v-for="(item, i) in paymentModes"
                        :key="i"
                        @click="newJob.jobPaymentMode = item.title"
                      >
                        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                      </v-list-tile>
                    </v-list>
                  </v-menu>
                </div>

                <v-btn color="teal white--text" @click="addJob()">Submit</v-btn>

                <v-btn flat @click="e1 = 3">Back</v-btn>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-card-text>

        <div style="flex: 1 1 auto;"></div>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      addProposal: false,
      e1: 0,
      tabs: null,
      job: {
        jobTitle: "VueJS Developer Needed",
        jobPaymentMode: "Hourly",
        jobPostDate: "5th January 2019",
        jobRating: 5.0,
        jobSkillLevel: "High",
        jobFavourited: false,
        jobPaid: false,
        jobDetail: "",
        jobEmployerId: "123",
        jobEmployer: "neil",
        jobEmployerAvatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        jobSkills: [],
        jobType: "OnGoing",
        jobProposals: 5,
        jobLookingToHire: 2,
        jobBudget: 0.003
      },
      ethBid: 0,
      items: [
        { title: "On-Going" },
        { title: "Not Started" },
        { title: "Completed" }
      ],
      skillLevel: [
        { title: "Expert" },
        { title: "High" },
        { title: "Medium" },
        { title: "Low" }
      ],
      paymentModes: [
        { title: "Monthly" },
        { title: "Hourly" },
        { title: "Fixed" }
      ],
      skills: [
        "JavaScript",
        "Java",
        "Python",
        "Ruby",
        "CSS",
        "PHP",
        "C++",
        "C",
        "Shell",
        "C#",
        "Objective-C",
        "R",
        "VimL",
        "Go",
        "Perl",
        "CoffeeScript",
        "TeX",
        "Scala",
        "Haskell",
        "Emacs Lisp"
      ],
      selectedSkills: [],
      newJob: {
        jobTitle: "",
        jobPaymentMode: "Hourly",
        jobPostDate: "5th January 2019",
        jobRating: 5.0,
        jobSkillLevel: "High",
        jobFavourited: false,
        jobPaid: false,
        jobDetail: "",
        jobEmployerId: "123",
        jobEmployer: "neil",
        jobEmployerAvatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        jobSkills: [],
        jobType: "OnGoing",
        jobProposals: 5,
        jobLookingToHire: 2,
        jobBudget: 0.003
      }
    };
  },

  computed: {
    ...mapState(["jobs"])
  },

  methods: {
    checkFavourite() {
      this.jobFavourited = !this.jobFavourited;
    },
    changeAddProposal(n) {
      this.addProposal = n;
    },
    async addJob() {
      this.addProposal = false;
      let accounts = await web3.eth.getAccounts();

      this.newJob.jobPostDate = new Date().getMonth.toString();

      this.newJob.jobEmployerId = accounts[0];

      db.collection("jobs")
        .add({
          jobTitle: this.newJob.jobTitle,
          jobPaymentMode: this.newJob.jobPaymentMode,
          jobPostDate: this.newJob.jobPostDate,
          jobRating: this.newJob.jobRating,
          jobSkillLevel: this.newJob.jobSkillLevel,
          jobFavourited: this.newJob.jobFavourited,
          jobPaid: this.newJob.jobPaid,
          jobDetail: this.newJob.jobDetail,
          jobEmployerId: this.newJob.jobEmployerId,
          jobEmployer: this.newJob.jobEmployer,
          jobEmployerAvatar: this.newJob.jobEmployerAvatar,
          jobSkills: this.newJob.jobSkills,
          jobType: this.newJob.jobType,
          jobProposals: this.newJob.jobProposals,
          jobLookingToHire: this.newJob.jobLookingToHire,
          jobBudget: this.newJob.jobBudget
        })
        .then(function() {
          console.log("Document successfully written!");
        })
        .catch(function(error) {
          console.error("Error writing document: ", error);
        });

      this.$store.commit("changeAccountInfo", accounts[0].toString());

      db.collection("employers")
        .doc(accounts[0].toString())
        .collection("jobs")
        .add({
          jobTitle: this.newJob.jobTitle,
          jobPaymentMode: this.newJob.jobPaymentMode,
          jobPostDate: this.newJob.jobPostDate,
          jobRating: this.newJob.jobRating,
          jobSkillLevel: this.newJob.jobSkillLevel,
          jobFavourited: this.newJob.jobFavourited,
          jobPaid: this.newJob.jobPaid,
          jobDetail: this.newJob.jobDetail,
          jobEmployerId: this.newJob.jobEmployerId,
          jobEmployer: this.newJob.jobEmployer,
          jobEmployerAvatar: this.newJob.jobEmployerAvatar,
          jobSkills: this.newJob.jobSkills,
          jobType: this.newJob.jobType,
          jobProposals: this.newJob.jobProposals,
          jobLookingToHire: this.newJob.jobLookingToHire,
          jobBudget: this.newJob.jobBudget
        })
        .then(function() {
          console.log("Document successfully written!");
        })
        .catch(function(error) {
          console.error("Error writing document: ", error);
        });
    }
  },
  async created() {
    this.$store.dispatch(
      "setAllEmployerJobsRef",
      db
        .collection("employers")
        .doc("0xc23f3136e6846f12A6a9A143EaE6DaF08f4F76b2")
        .collection("jobs")
    );
    console.log("askdjasdadjasdaskdjasndaskjnaskdjadksajdnasdkjn");
    console.log(this.jobs);
  }
};
</script>