<template>
  <v-card height="100vh" flat>
    <div class="headline text-xs-center pa-5">
      <component :is="bottomNav"></component>
    </div>
    <v-bottom-nav
      :active.sync="bottomNav"
      :value="true"
      fixed
      color="transparent"
    >
      <v-btn
        color="teal"
        flat
        value="Student"
      >
        <span>Students</span>
        <v-icon>people</v-icon>
      </v-btn>

      <v-btn
        color="teal"
        flat
        value="Tests"
      >
        <span>Tests</span>
        <v-icon>texture</v-icon>
      </v-btn>

      <v-btn
        color="teal"
        flat
        value="Profile"
      >
        <span>Profile</span>
        <v-icon>person_outline</v-icon>
      </v-btn>
    </v-bottom-nav>
  </v-card>
</template>

<script>
import  Profile  from "./BottomNav/Profile";
import  Tests  from "./BottomNav/Tests";
import  Student  from "./BottomNav/Student";
  export default {
    data () {
      return {
        bottomNav: 'Student'
      }
    },
    components: {
        Profile,
        Tests,
        Student
    }
  }
</script>