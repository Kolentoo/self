<template>
  <swiper :options="swiperOption" ref="mySwiper" :class="['sbox',{swiperon:swiperon}]">
    <!-- slides -->
    <swiper-slide ref="slides" :class="['swiper-slide','slide'+idx]" v-for="(item,idx) in nums" :key="idx">
        <div class="mask" @click="go(item.title)">
            <div class="stitle">
                <p class="p1">{{item.title}}</p>
                <p class="p2">{{item.num}}</p>
            </div>
        </div>
        <input v-model="searchwords" placeholder="KEYWORDS" v-if="item.num===''" class="words" type="text" @keyup.enter="search(searchwords)">
        
    </swiper-slide>
    <!-- Optional controls -->
    <div class="swiper-pagination"  slot="pagination"></div>
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
        nums:[
            {title:'MOVIES',num:'01'},
            {title:'TVPLAY',num:'02'},
            {title:'ANIME',num:'03'},
            {title:'RANKING',num:'04'},
            {title:'SEARCH',num:''}
            // {title:'ABOUT ME',num:'04'}
        ],
        swiperon:false,
        swiperOption: {
          // some swiper options/callbacks
          // 所有的参数同 swiper 官方 api 参数
          // ...
        },
        searchwords:''
      }
    },
    computed: {
      swiper() {
        return this.$refs.mySwiper.swiper
      }
    },
    created(){
      let myDate = new Date();
      let day = myDate.getDate();
      let firstday = localStorage.getItem('today')
      if(firstday==day){
        this.swiperon=true
      }else{
        setTimeout(()=> {
            this.swiperon=true
        }, 4000);
      }
    },
    mounted() {
        this.$nextTick(()=>{
            let bHeight = document.documentElement.clientHeight;
        })
        // this.swiper.slideTo(3, 1000, false)
    },
    methods:{
      go(target){
        if(target!='SEARCH'){
          this.$router.push(target);
        }
      },
      search(swords){
        if(this.searchwords!=''){
          this.$router.push(`search?${swords}`);
        }
      }
    }
  }
</script>

<style scoped>
    .sbox {transition: all ease 0.6s;opacity: 0;}
    .swiperon {opacity: 1;}
    .swiper-container {height: 100%;}
    .swiper-slide {width: 100%;}
    .mask {background: rgba(0,0,0,0.1);position: absolute;width: 100%;height: 100%;left: 0;top: 0;display: flex;align-items: center;}
    .masksearch {align-items:}
    .stitle {color:#fff;text-align: center;width: 100%;font-family: 'druk_pierre_testregular';text-transform: uppercase;
    letter-spacing: 0.8rem;}
    .stitle .p1 {font-size: 5rem;}
    .stitle .p2 {font-size: 3.8rem;}
    .slide0 {background: url('../public/images/bj16.jpg') no-repeat center center;background-size: cover;}
    .slide1 {background: url('../public/images/bj17.jpg') no-repeat center center;background-size: cover;}
    .slide2 {background: url('../public/images/bj14.jpg') no-repeat center center;background-size: cover;}
    .slide3 {background: url('../public/images/bj20.jpg') no-repeat center center;background-size: cover;}
    .slide4 {background: url('../public/images/bj13.jpg') no-repeat center center;background-size: cover;}
    .videobox {width: 100%;position: fixed;top: 0;left: 0;height: 100%;}
    .videobox:-webkit-full-screen {width: 100%;height: 100%;}
    .words {width: 50rem;height: 6rem;line-height: 6rem;border-radius:3rem;font-size: 3.2rem;text-align: center;
    position: absolute;top: 50%;left: 50%;margin:4rem 0 0 -25rem;z-index:300;color:#333;}
</style>