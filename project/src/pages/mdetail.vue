<template>
    <div class="moviedetail">
        <div class="mbox">
            <div class="mtop">
                <img class="back" src="../public/images/back.png" alt="" @click="goback()">
                <p class="mtitle">{{detail.title}}</p>
                <img class="share" src="../public/images/share.png" alt="">
            </div>
            <div class="mbanner">
                <img class="mpic vm" :src="detail.images.large-0!=0?'https://images.weserv.nl/?url='+detail.images.large.substring(7):'../public/images/K.jpg'" alt="">
            </div>
        </div>
        <div class="mcontent">
            <div class="minfo">
                <p class="name">{{detail.title}}</p>
                <p class="originname normal">{{detail.original_title}}</p>
                <p class="year normal">年份：{{detail.year}}</p>
                <p class="country normal">国家：<em v-for="(list,idx) in detail.countries" :key="idx">{{list}} </em></p>
                <p class="type normal">
                    类型：
                    <em v-for="(item,idx) in detail.genres" :key="idx">{{item}} </em>
                </p>
                <p class="othername normal">别名：<em v-for="(item,idx) in detail.aka" :key="idx">{{item}}</em></p>
            </div>
            <div class="evaluate">
                <p class="p1">评分</p>
                <p class="score b">{{detail.rating.average}}</p>
                <div v-if="detail.rating.average >= 9">
                    <div class="star10"></div>
                </div>
                <div v-else-if="detail.rating.average >= 8 && detail.rating.average <9">
                    <div class="star9"></div>
                </div>
                <div v-else-if="detail.rating.average >= 7 && detail.rating.average <8">
                    <div class="star8"></div>
                </div>
                <div v-else-if="detail.rating.average >= 6 && detail.rating.average <7">
                    <div class="star7"></div>
                </div>
                <div v-else-if="detail.rating.average >= 5 && detail.rating.average <6">
                    <div class="star6"></div>
                </div>
                <div v-else-if="detail.rating.average >= 4 && detail.rating.average <5">
                    <div class="star5"></div>
                </div>
                <div v-else-if="detail.rating.average >= 3 && detail.rating.average <4">
                    <div class="star4"></div>
                </div>
                <div v-else-if="detail.rating.average >= 2 && detail.rating.average <3">
                    <div class="star3"></div>
                </div>
                <div v-else-if="detail.rating.average >= 1 && detail.rating.average <0">
                    <div class="star2"></div>
                </div>
                <div v-else>
                    <div class="star1"></div>
                </div>
                <p class="member"><i class="b">{{detail.collect_count}}</i> 评价</p>
            </div>
        </div>
        <div class="mstory">
            <h2>剧情简介</h2>
            <p class="p1">
                {{detail.summary}}
            </p>
        </div>
        <div class="actor" v-if="detail.casts.length!=0">
            <h2>演员</h2>
            <div class="wrapper">
                <swiper :options="swiperOption" ref="mySwiper" v-if="detail.casts">
                    <!-- slides -->
                    <swiper-slide ref="slides" class="swiper-slide actor-con clearfix" v-for="(item,idx) in detail.casts" :key="idx">
                        <div class="actor-list fl"  @click="persondetail(item.id)">
                            <img class="actor-pic vm" v-if="item.avatars-0!=0" :src="'https://images.weserv.nl/?url='+item.avatars.small.substring(7)" alt="">
                            <img class="actor-pic vm" v-if="item.avatars-0===0" src="../public/images/K.jpg" alt="">
                            <p class="actor-name">{{item.name}}</p>
                        </div>
                    </swiper-slide>
                    <!-- Optional controls -->
                    <div class="swiper-pagination"  slot="pagination"></div>
                    <div class="swiper-button-prev hide" slot="button-prev"></div>
                    <div class="swiper-button-next hide" slot="button-next"></div>
                    <div class="swiper-scrollbar hide" slot="scrollbar"></div>
                </swiper>
            </div>
        </div>
        <div class="actor" v-if="detail.directors.length!=0">
            <h2>导演</h2>
            <div class="wrapper">
                <swiper :options="swiperOption" ref="mySwiper" v-if="detail.directors">
                    <swiper-slide ref="slides" class="swiper-slide actor-con clearfix" v-for="(item,idx) in detail.directors" :key="idx">
                        <div class="actor-list fl"  @click="persondetail(item.id)">
                            <img class="actor-pic vm" v-if="item.avatars-0!=0" :src="'https://images.weserv.nl/?url='+item.avatars.small.substring(7)" alt="">
                            <img class="actor-pic vm" v-if="item.avatars-0===0" src="../public/images/K.jpg" alt="">
                            <p class="actor-name">{{item.name}}</p>
                        </div>
                    </swiper-slide>
                </swiper>
            </div>
        </div>
        <loading v-if="load"></loading>
        <pop :popmsg="popmsg" :popshow="popshow"></pop>
    </div>
</template>

<script>
    import loading from '../components/loading'
    import BScroll from 'better-scroll'
    import pop from '../components/pop'
    export default{
        data(){
            return{
                detail:{
                    images:{
                        large:''
                    },
                    rating:{
                        average:''
                    },
                    casts:[
                        {
                            avatars:{
                                small:''
                            }
                        }
                    ],
                    directors:[

                    ]
                },
                load:true,
                popmsg:'',
                popshow:false,
                swiperOption: {
                    freeMode:true,
                    slidesPerView: 3,
                    slidesPerGroup: 3,
                    spaceBetween: 20
                }
            }
        },
        created(){
            let curl = window.location.href;
            let midgroup = curl.split('?')[1];
            let mid = midgroup.split('=')[1];
            let detailgroup = localStorage.getItem(mid);
            
            this.$nextTick(()=>{
                this.$axios.get(`http://xkolento.cn/v2/movie/subject/${mid}`,{

                }).then(res=>{
                    this.detail=res.data;
                    let mdetail = JSON.stringify(res)
                    localStorage.setItem(mid, mdetail);
                    this.load=false
                }).then(()=>{
                    let clength = this.detail.casts.length;
                    if(this.detail.casts.length!=0){
                        
                    }

                    if(this.detail.directors.length!=0){


                    }
                })
            })

        },
        methods:{
            goback(){
                window.history.go(-1);
            },
            persondetail(pid){
                if(pid-0!=0){
                    this.$router.push(`person?${pid}`)
                }else{
                    this.popshow=true
                    this.popmsg='信息不足'
                    setTimeout(()=> {
                        this.popshow=false
                    }, 2500);
                }
                
            }
        },
        components:{
            loading,pop
        }
    }
</script>

<style scoped>
    body,html {width: 100%;overflow-x:hidden;}
    .mbox {background:rgba(30,29,35,0.75);}
    .mbanner {display:flex;justify-content: center;align-items: center;}
    .mbanner .mpic {width: 75%;max-height:70rem;margin:2rem 0 5rem 0;box-shadow:0 0 1rem rgba(0,0,0,0.08);border-radius:1rem;}
    .mtop {display: flex;justify-content: space-between;color:#fff;font-size: 3rem;padding: 2rem;}
    .mtop img{width: 3.6rem;height: 3.6rem;}
    .mcontent {padding:2rem;display:flex;justify-content: space-between;margin-top: 2rem;}
    .minfo {width: 65%;}
    .minfo .name {font-size: 4rem;font-weight:bold;}
    .minfo .normal {font-size: 2.8rem;}
    .evaluate {width: 16rem;height: 16rem;padding:1.5rem;box-shadow:0 0 1rem rgba(0,0,0,0.08);text-align: center;margin:2rem 0 0 0;
    border-radius:1rem;}
    .evaluate .p1 {color:#666;font-size: 2.4rem;}
    .evaluate .score {font-size: 3.8rem;}
    .evaluate .member {font-size: 2.4rem;margin-top: 0.7rem;}
    .evaluate .member i{color:#e09015;}
    .mcontent .star10 {background: url('../public/images/stars.png') no-repeat 0 0;
    background-size: 100%;width: 15rem;height: 3.1rem;position: relative;top: 0.3rem;}
    .mcontent .star9 {background: url('../public/images/stars.png') no-repeat 0 -3rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star8 {background: url('../public/images/stars.png') no-repeat 0 -6rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star7 {background: url('../public/images/stars.png') no-repeat 0 -9rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star6 {background: url('../public/images/stars.png') no-repeat 0 -12rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star5 {background: url('../public/images/stars.png') no-repeat 0 -15rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star4 {background: url('../public/images/stars.png') no-repeat 0 -18rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star3 {background: url('../public/images/stars.png') no-repeat 0 -21rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star2 {background: url('../public/images/stars.png') no-repeat 0 -24rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star1 {background: url('../public/images/stars.png') no-repeat 0 -27rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mcontent .star0 {background: url('../public/images/stars.png') no-repeat 0 -30rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .mstory {padding:2rem;}
    .mstory h2{color:#aaa;font-size: 3.2rem;}
    .mstory .p1 {font-size: 2.8rem;margin-top: 1.5rem;}
    ::-webkit-scrollbar{width:0px;height:0px;}
    .actor {margin: 2rem;overflow: hidden;}
    .actor h2{color:#aaa;font-size: 3.2rem;}
    .actor .actor-con {width: 150%;overflow: scroll;margin-top: 1.5rem;white-space: nowrap;}
    .actor .actor-list {text-align: center;width: 22rem;margin-right: 3rem;white-space: nowrap;}
    .actor .actor-list img{width: 100%;border-radius:1rem;}
    .actor .actor-name {color:#333;font-size: 2.8rem;margin-top: 0.5rem;}
    .director {margin: 4rem 2rem 2rem;}
    .director h2{color:#aaa;font-size: 3.2rem;}
    .director .director-con {margin-top: 1.5rem;}
    .director .d-list {text-align: center;width: 22rem;margin-right: 3rem;}
    .director .d-list img{width: 100%;border-radius:1rem;}
    .director .director-name {color:#333;font-size: 2.8rem;margin-top: 0.5rem;}
</style>