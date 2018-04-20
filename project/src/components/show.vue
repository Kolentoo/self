<template>
  <swiper :options="swiperOption" ref="mySwiper" :class="['showbox']" v-if="seen">
    <!-- slides -->
    <swiper-slide ref="slides" :class="['swiper-slide']" v-for="(item,idx) in animenew" :key="idx">
        <img class="show-pic vm" :src="item.cover" alt="">
        <p class="name">{{item.title}}</p>
        <p class="update">更新:{{item.lastupdate_at}}</p>
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
            slidesPerGroup: 2
        }
      }
    },
    created(){
        this.$axios.get(`http://xkolento.cn/api/timeline_v2_global`,{
            params:{}
        }).then(res=>{
            this.animenew=res.data.result.slice(0,9);
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
    .showbox .swiper-slide {width: 45%;text-align: center;}
    .showbox .show-pic {border-radius:0.8rem;margin-bottom: 0.8rem;}
    .showbox .name {font-size: 3.2rem;max-height:9.5rem;overflow: hidden;}
    .showbox .update {font-size: 2.8rem;}
</style>