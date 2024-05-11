app.component('review-list', {
    props: {
      reviews: {
        type: Array,
        required: true
      }
    },
    template:
    /*html*/
    `
    <div class="review-container">
    <h3>Reviews:</h3>
      <ul>
        <li v-for="(review, index) in reviews" :key="index">
          <b>{{ review.name }}</b> gave this <b>{{ review.rating }}</b> stars 
          <br/>
          "<i> {{ review.review }} </i>"
          <br/>
          Would you recommend this product? <b>{{ review.recommend }}</b>
        </li>
      </ul>
    </div>
  `
  })