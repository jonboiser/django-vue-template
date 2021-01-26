<template>

  <div v-if="currentQuestion">
    <h1>{{ currentQuestion.prompt }}</h1>

    <form ref="questions">
      <!-- QUESTION: How can we trap focus to the buttons when using the keyboard? -->
      <!-- QUESTION: Why do we have to provide a "type=button" attribute? -->
      <!-- TODO implement keyboard shortcuts for pressing A-D instead of using mouse -->
      <div class="choices">
        <button
          v-for="(choice, idx) in currentQuestion.choices"
          :key="idx"
          @click="handleClickChoice(idx + 1)"
          class="choice"
          type="button"
        >
          ({{['A', 'B', 'C', 'D'][idx] }}) {{ choice }}
        </button>
      </div>
    </form>

    <!-- TODO: Fix this section, since it always says the response is wrong -->
    <template v-if="response">
      <div v-if="responseIsCorrect">
        That's right!
      </div>

      <div v-else>
        The correct answer is: {{ correctChoice }}
      </div>

      <div>
        <button @click="handleClickNext">Next Question</button>
      </div>
    </template>
  </div>

</template>


<script>
import quizService from '@/services/quizService';

export default {
  name: 'QuizMain',
  data() {
    // If a ?numQuestions query is provided in the URL, use that value instead
    // of the default of 4 questions
    const numQuestions = this.$route.query.numQuestions || 4;
    return {
      questions: [],
      currentIdx: 0,
      finished: false,
      response: null,
      numQuestions,
      numCorrect: 0,
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentIdx];
    },
    responseIsCorrect() {
      // TODO: Implement this
      return false;
    },
    correctChoice() {
      // TODO: Show the label of the correct choice
      return 'Something else 😉';
    },
  },
  methods: {
    handleClickChoice(idx) {
      this.response = idx;
    },
    handleClickNext() {
      this.response = null;
      if (this.currentIdx < this.numQuestions - 1) {
        this.currentIdx = this.currentIdx + 1;
      } else {
        this.$router.replace({
          name: 'summary',
          params: {
            results: {
              numCorrect: this.numCorrect,
              numQuestions: this.numQuestions,
            },
          },
        });
      }
    },
    initializeQuestions(questions) {
      // TODO: Randomize the order of the questions
      const selectedQuestions = questions.slice(0, this.numQuestions);

      this.questions = selectedQuestions.map(question => {
        // TODO: Randomize the choices for each question
        // Make sure correctIdx still points to the correct choice after shuffling
        const choices = [
          question.choice_a,
          question.choice_b,
          question.choice_c,
          question.choice_d,
        ];
        return {
          prompt: question.prompt,
          choices,
          correctIdx: question.answer - 1, // subtract one since arrays are zero-based
        };
      });
    },
  },
  mounted() {
    quizService.fetchQuestions().then(questions => {
      this.initializeQuestions(questions);
      this.$nextTick().then(() => {
        // Focus on the first button after the choices mount
        this.$refs.questions.elements[0].focus();
      });
    });
  },
};
</script>


<style lang="css" scoped>

  .choices {
    display: flex;
    flex-direction: column;
    width: 50%;
    margin: auto;
  }

  .choice {
    margin: 16px 0;
    font-size: 24px;
    font-weight: bold;
    text-align: left;
  }

</style>
