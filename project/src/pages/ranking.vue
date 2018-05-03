<template>
    <div class="ranking" ref="ranking">
        <div class="commonbox">
            <div class="top">
                <img class="back" src="../public/images/back.png" alt="" @click="goback()">
                <img v-if="playstatus===true" class="mgif" src="../public/images/music.gif" alt="" @click="musicstop()">
                <img v-if="playstatus===false" class="mgif" src="../public/images/music.png" alt="" @click="musicplay()">
            </div>
        </div>
        <swiper :options="swiperOption" ref="mySwiper" :class="['sbox']">
            <!-- slides -->
            <swiper-slide ref="slides" :class="['swiper-slide','slide'+idx]" v-for="(item,idx) in subjectbox" :key="idx" v-if="item.kind_cn!='榜单电影在线观看'">
                <div class="rankbox">
                    <div class="slidestart" v-if="idx===0">
                        <img class="rankingbj" src="../public/images/ranking.gif" alt="">
                        <img class="rankingtitle1" src="../public/images/rankingtitle1.png" alt="">
                        <img class="rankinglight" src="../public/images/rankinglight.png" alt="">
                        <img class="downpic" src="../public/images/down.png" alt="">
                    </div>
                    <div class="slidecon" v-if="idx>0">
                        <img class="imgbj" :src="item.payload.mobile_background_img?'https://images.weserv.nl/?url='+item.payload.mobile_background_img.substring(7):'https://images.weserv.nl/?url='+item.subjects[0].cover.substring(7)" alt="">
                        <div class="titlebox" v-if="item.kind_cn==='Top 10'">
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
                        <div class="titlebox" v-if="item.kind_cn==='Top 5'">
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
                        <div class="titlebox" v-if="item.kind_cn==='人物'">
                            <p class="p1">{{item.payload.title}}</p>
                            <p class="p2"><em>TOP1</em>{{item.subject.name}}</p>
                        </div>
                        <div class="titlebox" v-if="item.kind_cn==='结束页'">
                            <div class="p3">SEE YOU</div>
                        </div>
                        <moviesubject :item="item.subjects" v-if="item.kind_cn==='Top 10'"></moviesubject>
                        <moviesubject :people="item.people" v-if="item.kind_cn==='人物'"></moviesubject>
                    </div>
                </div>
                <div class="lines" v-if="item.kind_cn==='台词'">
                    <p class="linetext tc">
                        {{item.payload.text}}
                        <em>——《{{item.subject.title}}》</em>
                    </p>
                </div>
                
                
            </swiper-slide>
            <!-- Optional controls -->
            <div class="swiper-pagination"  slot="pagination"></div>
            <div class="swiper-button-prev hide" slot="button-prev"></div>
            <div class="swiper-button-next hide" slot="button-next"></div>
            <div class="swiper-scrollbar hide" slot="scrollbar"></div>
        </swiper>
        <audio id="audio" autoplay="autoplay" loop="loop">
            <source src="../public/images/music.mp3" type="audio/ogg">
        </audio>
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
                    height: window.innerHeight,
                    on: {
                        slideChangeTransitionEnd: ()=>{
                            this.newmsg();
                        }
                    }
                },
                page:1,
                playstatus:true
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
                if(this.page<90){
                    this.$axios.get(`http://xkolento.cn/2017/${this.page}`,{

                    }).then((res)=>{
                        this.subjectbox.push(res.data.res)
                        if(this.page===6||this.page===53){
                            this.page+=2
                        }else if(this.page===81){
                            this.page+=3
                        }else if(this.page===90){
                            return false
                        }else{
                            this.page+=1
                        }
                    })
                }
            },
            goback(){
                window.history.go(-1);
            },
            musicstop(){
                this.playstatus=false
                document.getElementById('audio').pause();
            },
            musicplay(){
                this.playstatus=true
                document.getElementById('audio').play();
            }
        },
        components:{
            moviesubject
        }
    }
</script>

<style scoped>
    .ranking .commonbox {background:none;}
    .music .mgif {width: 3rem;}
    .swiper-container {height: 100%;}
    .swiper-slide {width: 100%;}
    .rankbox {height: 100%;width: 100%;}
    .slidestart {height: 100%;}
    .rankingbj {width: 100%;height: 100%;}
    .rankingtitle1 {position: absolute;width: 90%;top: 18%;left: 5%;z-index:80;}
    .rankinglight {position: absolute;width: 100%;top: 0;left: 0;height: 100%;}
    .downpic {position: absolute;width: 4rem;left: 50%;bottom: 2rem;margin-left: -2rem;}
    .slidecon {width: 100%;height: 100%;}
    .slidecon .imgbj {height: 100%;}
    .titlebox {color:#fff;width: 80%;margin:0 auto;background: rgba(0,0,0,0.5);position: absolute;top: 20%;left: 50%;margin-left: -40%;
    text-align: center;padding-bottom: 1.5rem;}
    .titlebox .p1 {font-size: 4rem;font-weight:bold;background: rgba(165, 118, 53, 0.7);padding:1rem 0;}
    .titlebox .p2 {font-size: 3rem;font-weight:bold;padding:1.5rem 0;}
    .titlebox .p2 em{background: #e58b00;border-radius:2rem;display: inline-block;padding:0 1rem;margin-right: 2rem;}
    .titlebox .p3 {font-size: 5rem;text-align: center;color:#fff;padding-top: 1.8rem;}
    .scorebox {display:flex;justify-content: center;}
    .titlebox .desc {font-size: 2.8rem;color:#fff;padding:1rem;height: 12rem;overflow: hidden;}
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
    .lines {background: rgba(0,0,0,0.7);height: 24rem;text-align: center;position: absolute;width: 100%;bottom: 0;left: 0;color:#fff;
    font-size: 3rem;z-index:200;display: flex;align-items: center;justify-content: center;}
    .lines em{margin-top: 1.5rem;display: inline-block;font-size: 2.6rem;}
    .audio {z-index:-1;opacity: 0;}
</style>