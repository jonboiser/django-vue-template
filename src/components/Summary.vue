<template>

  <div>
    <h1>Summary</h1>
    <div>You got {{ results.numCorrect }} of {{ results.numQuestions }} correct</div>

    <!-- TODO save the results to the backend -->
    <div v-if="true">
      <h2>Save your score!</h2>
      <form @submit.prevent="handleFormSubmit">
        <label for="name">Your Name
          &nbsp;
          <input v-model="name" type="text" id="name" name="name">
        </label>
        &nbsp;
        <button type="submit">Submit</button>
      </form>
    </div>
  </div>

</template>


<script>
import quizService from '@/services/quizService';

export default {
  name: 'Summary',
  components: {},
  mixins: [],
  props: {
    // Passed in from the router with numQuestions and numTotal values
    results: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      name: '',
    };
  },
  computed: {},
  methods: {
    // QUESTION: What else should/could we do before and after we submit the results?
    async handleFormSubmit() {
      // TODO implement this
      await quizService.saveResults()
    },
  },
  $trs: {},
};
</script>


<style lang="css" scoped>
</style>
