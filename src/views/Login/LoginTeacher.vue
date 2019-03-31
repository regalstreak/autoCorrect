<template>
  <div id="ourContainer">
    <v-layout column class="layoutLoginBg" justify-center align-content-center>
      <v-flex xs4 style="padding-top: 100px" class="flexImage">
        <v-img  height="70" :src="require('../../assets/ourLogo.png')" contain></v-img>
      </v-flex>
      <v-flex xs1 class="flexLogin">
        <span class="display-1">Teacher Login</span>
      </v-flex> 
      <v-flex xs1 class="flexLogin">
        <v-text-field style="margin: 0rem 3.5rem" v-model="email" label="email"></v-text-field>
      </v-flex>

      <v-flex xs1 class="flexLogin">
        <v-text-field
          style="margin: 0rem 3.5rem"
          v-model="password"
          label="password"
          :append-icon="showPassword ? 'visibility' : 'visibility_off'"
          :type="showPassword ? 'text' : 'password'"
          @click:append="showPassword = !showPassword"
        ></v-text-field>
      </v-flex>
      <v-flex xs1>
        <v-layout column justify-center>
          <v-flex xs6 class="flexButton">
            <v-btn block round to="/teacher" class="white--text ma-2" color="secondary">
              <font style="text-transform: lowercase;">login</font>
            </v-btn>
          </v-flex>
          <v-flex xs6 class="flexButton flexButtonSignup">
            <v-btn block round to="/dashboard" class="ma-2">
              <div style="padding-right: 40px;padding-left: 40px;">
                <font style="text-transform: lowercase;">Signup</font>
              </div>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    <v-img height="300" style="margin-left: 100px" :src="require('../../assets/login_bg_2.png')"></v-img>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showPassword: false,
      password: "",
      email: "",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters"
        // emailMatch: () => "The email and password you entered don't match"
      }
    };
  }
};
</script>

<style scoped>
#ourContainer {
  /* background-color: blue; */
  /* clip-path: polygon(0 0, 100% 100%, 100% 20%, 0 0); */
  background-image: url("../../assets/teacher.png");
  background-size: contain;
  height: 100vh;
  transform: translateX(-1px);
  overflow: hidden;
}
.flexLogin {
  /* background-color: blue; */
  align-items: center;
  display: flex;
  justify-content: center;
  align-content: center;
  margin-bottom: 4px;
}
.flexImage {
  /* background-color: blue; */
  align-items: center;
  justify-content: center;
  align-content: center;
  display: flex;
}
.layoutLoginBg {
  height: 95vh;
}

.loginButton {
  background: #01ffd9;
  background: -webkit-linear-gradient(top left, #01ffd9, #01509e);
  background: -moz-linear-gradient(top left, #01ffd9, #01509e);
  background: linear-gradient(top left, #01ffd9, #01509e);
}

.flexButton {
  align-content: center;
  align-items: center;
  justify-content: center;
  display: flex;
  margin: 0 2rem;
}
</style>
