<template>
  <div class="calendar">
    <app-header></app-header>
    <div class="month">
      <ul>
        <li class="prev"><ion-icon name="arrow-dropleft" @click="subtractMonth"></ion-icon></li>
        <li class="next"><ion-icon name="arrow-dropright" @click="addMonth"></ion-icon></li>
        <li>{{ month }}<br><span style="font-size:18px">{{year}}</span></li>
      </ul>
    </div>

    <ul class="weekdays">
      <li v-for="day in days" :key="day">{{ day }}</li> 
    </ul>

    <ul class="days">
      <li v-for="blank in firstDayOfMonth" :key="blank"></li>
      <li v-for="date in daysInMonth" :key="date">{{date}}</li> 
    </ul>
  </div>
</template>

<script>
import AppHeader from '../AppHeader.vue';
export default {
  name: "Calendar",
  components: {AppHeader},
  data() {
    return {
      today: moment(),
      dateContext: moment(),
      days: ['S', 'M', 'T', 'W', 'T', 'F', 'S']
    }
  },
  computed: {
    year: function () {
      var t = this;
      return t.dateContext.format('Y');
    },
    month: function () {
      var t = this;
      return t.dateContext.format('MMMM');
    },
    daysInMonth: function () {
      var t = this;
      return t.dateContext.daysInMonth();
    },
    currentDate: function () {
        var t = this;
        return t.dateContext.get('date');
    },
    firstDayOfMonth: function () {
        var t = this;
        var firstDay = moment(t.dateContext).subtract((t.currentDate - 1), 'days');
        return firstDay.weekday();
    },
    initialDate: function () {
      var t = this;
      return t.today.get('date');
    },
    initialMonth: function () {
        var t = this;
        return t.today.format('MMMM');
    },
    initialYear: function () {
        var t = this;
        return t.today.format('Y');
    }
  },
  methods: {
    addMonth: function () {
      var t = this;
      t.dateContext = moment(t.dateContext).add(1, 'month');
    },
    subtractMonth: function () {
        var t = this;
        t.dateContext = moment(t.dateContext).subtract(1, 'month');
    }
  }
}
</script>
