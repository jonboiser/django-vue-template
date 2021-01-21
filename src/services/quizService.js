import api from '@/services/api';

export default {
  async fetchQuestions() {
    const response = await api.get('questions/');
    return response.data;
  },
  async saveResults(data) {
    console.log(data);
    // TODO implement this
  },
};
