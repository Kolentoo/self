<template>
    <swiper :options="swiperOption" ref="mySwiper" :class="['showbox']" v-if="seen">
      <!-- slides -->
      <swiper-slide ref="slides" :class="['swiper-slide']" v-for="(item,idx) in movietype" :key="idx">
          <div class="chart" @click="godetail(item.id)">
            <img class="show-pic vm g10" :src="'https://images.weserv.nl/?url='+item.cover.substring(7)" alt="">
          </div>
          <p class="name">{{item.title}}</p>
          <div class="score">
                <div class="score-box" v-if="item.rate">
                    <div v-if="item.rate >= 9">
                        <div class="star10"></div>
                    </div>
                    <div v-else-if="item.rate >= 8 && item.rate <9">
                        <div class="star9"></div>
                    </div>
                    <div v-else-if="item.rate >= 7 && item.rate <8">
                        <div class="star8"></div>
                    </div>
                    <div v-else-if="item.rate >= 6 && item.rate <7">
                        <div class="star7"></div>
                    </div>
                    <div v-else-if="item.rate >= 5 && item.rate <6">
                        <div class="star6"></div>
                    </div>
                    <div v-else-if="item.rate >= 4 && item.rate <5">
                        <div class="star5"></div>
                    </div>
                    <div v-else-if="item.rate >= 3 && item.rate <4">
                        <div class="star4"></div>
                    </div>
                    <div v-else-if="item.rate >= 2 && item.rate <3">
                        <div class="star3"></div>
                    </div>
                    <div v-else-if="item.rate >= 1 && item.rate <0">
                        <div class="star2"></div>
                    </div>
                    <div v-else>
                        <div class="star1"></div>
                    </div>
                
                </div>
                <p class="score-num" v-if="item.rate">{{item.rate}}</p>
            </div>

      </swiper-slide> 

      <div class="swiper-pagination hide"  slot="pagination"></div>
      <div class="swiper-button-prev hide" slot="button-prev"></div>
      <div class="swiper-button-next hide" slot="button-next"></div>
      <div class="swiper-scrollbar hide" slot="scrollbar"></div>
    </swiper>
</template>

<script>
    export default{
        name: 'carrousel',
        props:['movietype'],
        data(){
            return{
                starnum:'',
                seen:false,
                swiperOption: {
                    slidesPerView: 2,
                    slidesPerGroup: 2,
                    spaceBetween: 30
                }
            }
        },
        mounted(){
            this.seen=true
        },
        methods:{
            godetail(mid){
                this.$router.push(`mdetail?mid=${mid}`);
            }
        }
    }
</script>

<style scoped>
    .showbox {padding:1rem 0;}
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