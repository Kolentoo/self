<template>
  <swiper :options="swiperOption" ref="mySwiper" :class="['showbox']" v-if="seen">
    <!-- slides -->
    <swiper-slide ref="slides" :class="['swiper-slide']" v-for="(item,idx) in animenew" :key="idx">
        <div class="chart">
          <img class="show-pic vm g10" :src="item.cover_url" alt="">
        </div>
        <p class="name">{{item.title}}</p>
        <p class="type">{{item.types}}</p>
        <p class="score">评分:{{item.score}}</p>
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
        seen:false,
        swiperOption: {
            slidesPerView: 2,
            slidesPerGroup: 2,
            spaceBetween: 30
        }
      } 
    },
    created(){
        let snimeTop = localStorage.getItem('animeTop');
        this.$axios.get(`http://localhost:3000/chart/top_list`,{
            params:{}
        }).then(res=>{
            this.animenew=res.data;
            localStorage.setItem('animeTop', this.animenew);
            setTimeout(()=> {
                this.seen=true
            }, 200);
            console.log(this.animenew)
        })

    },
    mounted(){      
    },
    computed: {
      swiper() {
        return this.$refs.mySwiper.swiper
      }
    }
  }
</script>

<style scoped>
    .showbox {padding:3rem 0;}
    .swiper-wrapper {padding:0 2%;}
    .showbox .swiper-slide {text-align: center;}
    .showbox .show-pic {border-radius:0.8rem;margin-bottom: 0.8rem;}
    .showbox .chart {height: 45rem;overflow: hidden;}
    .showbox .chart img{height: 100%;}
    .showbox .name {font-size: 3rem;max-height:9.5rem;overflow: hidden;margin-top: 0.5rem;}
    .showbox .type {font-size: 2.6rem;}
    .showbox .score {font-size: 2.6rem;}
</style>