<template>
  <swiper :options="swiperOption" ref="mySwiper" :class="['showbox']" v-if="seen">
    <!-- slides -->
    <swiper-slide ref="slides" :class="['swiper-slide']" v-for="(item,idx) in animenew" :key="idx">
        <div class="chart" @click="godetail(item.id)">
          <img class="show-pic vm g10" :src="item.cover_url" alt="">
        </div>
        <p class="name">{{item.title}}</p>
        <div class="score">

            <div v-if="item.score >= 9">
              <div class="star10"></div>
            </div>
            <div v-else-if="item.score >= 8 && item.score <9">
              <div class="star9"></div>
            </div>
            <div v-else-if="item.score >= 7 && item.score <8">
              <div class="star8"></div>
            </div>
            <div v-else-if="item.score >= 6 && item.score <7">
              <div class="star7"></div>
            </div>
            <div v-else-if="item.score >= 5 && item.score <6">
              <div class="star6"></div>
            </div>
            <div v-else-if="item.score >= 4 && item.score <5">
              <div class="star5"></div>
            </div>
            <div v-else-if="item.score >= 3 && item.score <4">
              <div class="star4"></div>
            </div>
            <div v-else-if="item.score >= 2 && item.score <3">
              <div class="star3"></div>
            </div>
            <div v-else-if="item.score >= 1 && item.score <0">
              <div class="star2"></div>
            </div>
            <div v-else>
              <div class="star1"></div>
            </div>
          
          <p class="score-num">{{item.score}}</p>
        </div>
    </swiper-slide> 
    <!-- Optional controls -->
    <div class="swiper-pagination hide"  slot="pagination"></div>
    <div class="swiper-button-prev hide" slot="button-prev"></div>
    <div class="swiper-button-next hide" slot="button-next"></div>
    <div class="swiper-scrollbar hide" slot="scrollbar"></div>
  </swiper>
</template>

<script>
  export default {
    name: 'carrousel',
    data() {
      return {
        animenew:[],
        starnum:'',
        seen:false,
        swiperOption: {
            slidesPerView: 2,
            slidesPerGroup: 2,
            spaceBetween: 30
        }
      } 
    },
    created(){
        let anime1 = localStorage.getItem('anime1');
        if(anime1){
          let animeJson = JSON.parse(anime1)
          this.animenew = animeJson
          setTimeout(()=> {
              this.seen=true
          }, 200);
          console.log(animeJson)
        }else{
          this.$axios.get(`http://localhost:3000/chart/top_list`,{
              params:{}
          }).then(res=>{
              this.animenew=res.data;
              let anime1 = JSON.stringify(res.data)
              localStorage.setItem('anime1', anime1);
              setTimeout(()=> {
                  this.seen=true
              }, 200);
          })
        }

    },
    methods:{
      godetail(mid){
        console.log(1)
        this.$router.push(`mdetail?mid=${mid}`);
      }
    },
    computed: {
      swiper() {
        return this.$refs.mySwiper.swiper
      }
    }
  }
</script>

<style scoped>
    .showbox {padding:1rem 0;}
    .swiper-wrapper {padding:0 2%;}
    .showbox .swiper-slide {text-align: center;}
    .showbox .show-pic {border-radius:0.8rem;margin-bottom: 0.8rem;}
    .showbox .chart {height: 45rem;overflow: hidden;}
    .showbox .chart img{height: 100%;}
    .showbox .name {font-size: 2.8rem;max-height:9.5rem;overflow: hidden;margin: 0.8rem 0 0.5rem 0;}
    .showbox .type {font-size: 2.6rem;}
    .showbox .score {font-size: 2.6rem;display: flex;justify-content: center;}
    .showbox .star10 {background: url('../public/images/stars.png') no-repeat 0 0;
    background-size: 100%;width: 15rem;height: 3.1rem;position: relative;top: 0.3rem;}
    .showbox .star9 {background: url('../public/images/stars.png') no-repeat 0 -3rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star8 {background: url('../public/images/stars.png') no-repeat 0 -6rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star7 {background: url('../public/images/stars.png') no-repeat 0 -9rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star6 {background: url('../public/images/stars.png') no-repeat 0 -12rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star5 {background: url('../public/images/stars.png') no-repeat 0 -15rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star4 {background: url('../public/images/stars.png') no-repeat 0 -18rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star3 {background: url('../public/images/stars.png') no-repeat 0 -21rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star2 {background: url('../public/images/stars.png') no-repeat 0 -24rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star1 {background: url('../public/images/stars.png') no-repeat 0 -27rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .star0 {background: url('../public/images/stars.png') no-repeat 0 -30rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .showbox .score-num {margin-left: 1.5rem;color:#e09015;}
</style>