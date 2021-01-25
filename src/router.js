import Vue from 'vue';
import Router from 'vue-router';
// import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages';
import QuizMain from '@/components/QuizMain';
import Summary from '@/components/Summary';
import QuizHome from '@/components/QuizHome';
import Scores from '@/components/Scores';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: QuizHome,
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuizMain,
    },
    {
      name: 'summary',
      path: '/summary',
      component: Summary,
      props(route) {
        return {
          results: route.params.results,
        };
      },
      beforeEnter(to, from, next) {
        // Redirect to home page if arriving directly to the /summary URL
        if (to.params.results) {
          next();
        } else {
          next({ name: 'home' });
        }
      },
    },
    {
      path: '/scores',
      name: 'scores',
      component: Scores,
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages,
    },
  ],
});
