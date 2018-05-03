<template>
    <div class="subject">
        <swiper :options="swiperOption" ref="mySwiper" :class="['sbox']" v-if="item">
            <!-- slides -->
            <swiper-slide ref="slides" :class="['swiper-slide','slide'+idx]" v-for="(list,idx) in item" :key="idx">
                <div class="sublist" @click="godetail(list.id)">
                    <div class="chart">
                        <img class="mpic vm" :src="list.cover?'https://images.weserv.nl/?url='+list.cover.substring(7):''" alt="">
                        <img class="corner" src="../public/images/corner.png" alt="">
                        <p class="number">{{idx+1}}</p>
                    </div>
                    <p class="mname tc" v-if="list.title">{{list.title}}</p>
                    <p class="score tc" v-if="list.rating">评分：{{list.rating}}</p>
                </div>
            </swiper-slide>
            <!-- Optional controls -->
            <div class="swiper-pagination"  slot="pagination"></div>
            <div class="swiper-button-prev hide" slot="button-prev"></div>
            <div class="swiper-button-next hide" slot="button-next"></div>
            <div class="swiper-scrollbar hide" slot="scrollbar"></div>
        </swiper>
        <swiper :options="swiperOption" ref="mySwiper" :class="['sbox']" v-if="people">
            <!-- slides -->
            <swiper-slide ref="slides" :class="['swiper-slide','slide'+idx]" v-for="(list,idx) in people" :key="idx">
                <div class="sublist">
                    <div class="chart">
                        <img class="mpic vm" :src="list.avatar?'https://images.weserv.nl/?url='+list.avatar.substring(7):''" alt="">
                        <img class="corner" src="../public/images/corner.png" alt="">
                        <p class="number">{{idx+1}}</p>
                    </div>
                    <p class="mname tc" v-if="list.name">{{list.name}}</p>
                </div>
            </swiper-slide>
            <!-- Optional controls -->
            <div class="swiper-pagination"  slot="pagination"></div>
            <div class="swiper-button-prev hide" slot="button-prev"></div>
            <div class="swiper-button-next hide" slot="button-next"></div>
            <div class="swiper-scrollbar hide" slot="scrollbar"></div>
        </swiper>
    </div>
</template>

<script>
    
    export default{
        props:['item','people'],
        data(){
            return{
                swiperOption: {
                    freeMode:true,
                    slidesPerView: 3,
                    slidesPerGroup: 3,
                    spaceBetween: 20
                }
            }
        },
        created(){

        },
        computed: {
            swiper() {
                return this.$refs.mySwiper.swiper
            }
        },
        methods:{
            godetail(mid){
                this.$router.push(`mdetail?mid=${mid}`);
            }
        }
    }
</script>

<style scoped>
    .sublist {width: 22rem;}
    .sublist .mname {color:#fff;font-size: 2.8rem;margin-top: 0.3rem;}
    .sublist .score {font-size: 2.4rem;color:#ea9a1e;}
    .chart {position: relative;height: 30rem;}
    .chart .mpic {width: 100%;height: 100%;}
    .chart .corner {position: absolute;top: 0;left: 0;width: 5rem;}
    .number {font-size: 2.8rem;position: absolute;top: -0.5rem;left: 0.8rem;color:#fff;}
</style>