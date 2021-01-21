<template>

  <div>
    <!-- TODO: fix TypeErrors that are seen when this component loads -->
    <h1>{{ currentQuestion.prompt }}</h1>
    <form>
      <!-- QUESTION: How can we trap focus to the buttons when using the keyboard? -->
      <!-- QUESTION: Why do we have to provide a "type=button" attribute? -->
      <div class="choices">
        <button
          v-for="(choice, idx) in currentQuestion.choices"
          :key="idx"
          @click="handleClickCheck(idx)"
          class="choice"
          type="button"
        >
          {{ choice }}
        </button>
      </div>
    </form>

    <!-- TODO: Show feedback and "next" button after user responds -->
    <!-- QUESTION: What else should/could the UI do after the user responds? -->
    <template v-if="true">
      <div v-if="responseIsCorrect">
        That's right!
      </div>
      <div v-else>
        The correct answer is: {{ correctChoice }}
      </div>
      <div>
        <button>Next Question</button>
      </div>
    </template>
  </div>

</template>


<script>
import quizService from '@/services/quizService';

// Basic shuffle function
// function shuffle(array) {
//   return array.sort(() => Math.random() - 0.5);
// }

export default {
  name: 'QuizMain',
  components: {},
  mixins: [],
  props: {},
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
    handleClickCheck() {
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
  },
  mounted() {
    quizService.fetchQuestions().then(allQuestions => {
      // TODO: Randomize the order of the questions
      const selectedQuestions = allQuestions.slice(0, this.numQuestions);

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
    });
  },
  $trs: {},
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
    cursor: pointer;
  }

</style>
