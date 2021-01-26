<template>

  <div>

    <h1>Summary</h1>
    <div>You got {{ results.numCorrect }} of {{ results.numQuestions }} correct</div>

    <div v-if="!resultsSaved">
      <h2>Save your score!</h2>

      <form @submit.prevent="handleFormSubmit">
        <label for="name">Your Name
          &nbsp;
          <input v-model="name" type="text" id="name" name="name" autocomplete="off">
        </label>
        &nbsp;
        <button type="submit">Submit</button>
      </form>
    </div>

    <div v-else>
      <p>Your results have been saved!</p>

      <router-link to="/scores">View all scores</router-link>
    </div>

  </div>

</template>


<script>
import quizService from '@/services/quizService';

export default {
  name: 'Summary',
  props: {
    // `results` is pass from the router with `numQuestions` and `numTotal` values
    results: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      name: '',
      resultsSaved: false,
    };
  },
  methods: {
    // QUESTION: What else should/could we do before and after we submit the results?
    async handleFormSubmit() {
      // TODO implement this
      await quizService.saveScore();
      this.resultsSaved = true;
    },
  },
};
</script>


<style lang="css" scoped>
</style>
