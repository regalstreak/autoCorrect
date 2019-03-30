<template>
  <v-card height="100vh" flat>
    <component :is="bottomNav"></component>
    <v-bottom-nav :active.sync="bottomNav" :value="true" fixed>
      <v-btn color="primary" flat value="Tests">
        <span>Tests</span>
        <v-icon>texture</v-icon>
      </v-btn>

      <v-btn color="primary" flat value="Student">
        <span>Students</span>
        <v-icon>people</v-icon>
      </v-btn>

      <v-btn color="primary" flat value="Profile">
        <span>Profile</span>
        <v-icon>person_outline</v-icon>
      </v-btn>
    </v-bottom-nav>
  </v-card>
</template>

<script>
import Profile from "./BottomNav/Profile";
import Tests from "./BottomNav/Tests";
import Student from "./BottomNav/Student";
export default {
  data() {
    return {
      bottomNav: "Tests"
    };
  },
  components: {
    Profile,
    Tests,
    Student
  }
};
</script>