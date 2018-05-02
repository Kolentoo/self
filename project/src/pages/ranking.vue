<template>
    <div class="ranking" ref="ranking">
        <swiper :options="swiperOption" ref="mySwiper" :class="['sbox']">
            <!-- slides -->
            <swiper-slide ref="slides" :class="['swiper-slide','slide'+idx]" v-for="(item,idx) in subjectbox" :key="idx">
                <div class="rankbox">
                    <div class="slidestart" v-if="idx===0">
                        <img class="rankingbj" src="../public/images/ranking.gif" alt="">
                        <img class="rankingtitle1" src="../public/images/rankingtitle1.png" alt="">
                        <img class="rankinglight" src="../public/images/rankinglight.png" alt="">
                        <img class="downpic" src="../public/images/down.png" alt="">
                    </div>
                    <div class="slidecon" v-if="idx>0">
                        <img class="imgbj" :src="'https://images.weserv.nl/?url='+item.payload.mobile_background_img.substring(7)" alt="">
                        <div class="titlebox">
                            <p class="p1">{{item.payload.title}}</p>
                            <p class="p2"><em>TOP1</em>{{item.subject.title}}</p>
                            <div class="scorebox">
                                <div v-if="item.subject.rating >= 9">
                                    <div class="star10"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 8 && item.subject.rating <9">
                                    <div class="star9"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 7 && item.subject.rating <8">
                                    <div class="star8"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 6 && item.subject.rating <7">
                                    <div class="star7"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 5 && item.subject.rating <6">
                                    <div class="star6"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 4 && item.subject.rating <5">
                                    <div class="star5"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 3 && item.subject.rating <4">
                                    <div class="star4"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 2 && item.subject.rating <3">
                                    <div class="star3"></div>
                                </div>
                                <div v-else-if="item.subject.rating >= 1 && item.subject.rating <0">
                                    <div class="star2"></div>
                                </div>
                                <div v-else>
                                    <div class="star1"></div>
                                </div>
                                <p class="score b">{{item.subject.rating}}</p>
                                <p class="comments">{{item.subject.rating_count}}人 评价</p>
                            </div>
                            <p class="desc">{{item.payload.description}}</p>
                        </div>
                        <moviesubject :item="item.subjects"></moviesubject>
                    </div>
                    
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
    import moviesubject from '../components/subject'
    export default{
        data() {
            return {
                subjectbox:[
                    {
                        payload:{
                            mobile_background_img:'',
                            title:'',
                            description:''
                        },
                        subject:{
                            orig_title:'',
                            rating:'',
                            id:''
                        },
                        subjects:[
                            {
                                cover:'',
                                rating:'',
                                title:'',
                                id:''
                            }
                        ]
                    }
                ],
                swiperon:true,
                swiperOption: {
                    direction: 'vertical',
                    mousewheel: true,
                    height: window.innerHeight
                },
                page:1
            }
        },
        created(){
            this.newmsg();
        },
        computed: {
            swiper() {
                return this.$refs.mySwiper.swiper
            }
        },
        methods:{
            newmsg(){
                this.$axios.get(`http://xkolento.cn/2017/${this.page}`,{

                }).then((res)=>{
                    this.subjectbox.push(res.data.res)
                })
            }
        },
        components:{
            moviesubject
        }
    }
</script>

<style scoped>
    .swiper-container {height: 100%;}
    .swiper-slide {width: 100%;}
    .rankbox {height: 100%;width: 100%;}
    .slidestart {height: 100%;}
    .rankingbj {width: 100%;height: 100%;}
    .rankingtitle1 {position: absolute;width: 90%;top: 25%;left: 5%;z-index:80;}
    .rankinglight {position: absolute;width: 100%;top: 0;left: 0;height: 100%;}
    .downpic {position: absolute;width: 4rem;left: 50%;bottom: 2rem;margin-left: -2rem;}
    .slidecon {width: 100%;height: 100%;}
    .slidecon .imgbj {height: 100%;position: relative;left: -30%;}
    .titlebox {color:#fff;width: 80%;margin:0 auto;background: rgba(0,0,0,0.5);position: absolute;top: 20%;left: 50%;margin-left: -40%;
    text-align: center;}
    .titlebox .p1 {font-size: 4rem;font-weight:bold;background: rgba(165, 118, 53, 0.7);padding:1rem 0;}
    .titlebox .p2 {font-size: 3rem;font-weight:bold;padding:1.5rem 0;}
    .titlebox .p2 em{background: #e58b00;border-radius:2rem;display: inline-block;padding:0 1rem;margin-right: 2rem;}
    .scorebox {display:flex;justify-content: center;}
    .titlebox .desc {font-size: 2.8rem;color:#fff;padding:1rem;}
    .scorebox .score {font-size: 2.8rem;margin-left: 2rem;}
    .scorebox .comments {font-size: 2.8rem;color:#fff;margin-left: 2rem;}
    .ranking .star10 {background: url('../public/images/stars.png') no-repeat 0 0;
    background-size: 100%;width: 15rem;height: 3.1rem;position: relative;top: 0.3rem;}
    .ranking .star9 {background: url('../public/images/stars.png') no-repeat 0 -3rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star8 {background: url('../public/images/stars.png') no-repeat 0 -6rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star7 {background: url('../public/images/stars.png') no-repeat 0 -9rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star6 {background: url('../public/images/stars.png') no-repeat 0 -12rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star5 {background: url('../public/images/stars.png') no-repeat 0 -15rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star4 {background: url('../public/images/stars.png') no-repeat 0 -18rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star3 {background: url('../public/images/stars.png') no-repeat 0 -21rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star2 {background: url('../public/images/stars.png') no-repeat 0 -24rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star1 {background: url('../public/images/stars.png') no-repeat 0 -27rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .ranking .star0 {background: url('../public/images/stars.png') no-repeat 0 -30rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .subject {position: absolute;width: 100%;bottom: 1.5rem;left: 0;z-index:500;}
</style>