<template>

  <div>
    <h1>Scores</h1>
    <table>
      <tr>
        <th>Name</th>
        <th># Correct</th>
        <th># Total</th>
      </tr>
      <template v-for="(score, idx) in scores">
        <tr :key="idx">
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </template>
    </table>

    <router-link to="/">Back to home</router-link>
  </div>

</template>


<script>
export default {
  name: 'Scores',
  data() {
    return {
      scores: [],
    };
  },
  beforeMount() {
    // load the scores from the backend and display them in the table
  },
};
</script>


<style lang="css" scoped></style>
