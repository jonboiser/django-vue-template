<template>

  <div>
    <p><b>Are you ready for some trivia!?</b></p>
    <button
      class="start-button"
      @click="handleClickStart"
    >
      Let's do this!
    </button>
  </div>

</template>


<script>
export default {
  name: 'QuizHome',
  methods: {
    handleClickStart() {
      const questionsPageLink = {
        name: 'questions',
        query: { numQuestions: 4 },
      };
      this.$router.replace(questionsPageLink);
    },
  },
};
</script>


<style lang="css" scoped>

  .start-button {
    margin: 16px 0;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
  }

</style>
