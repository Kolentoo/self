<template>
    <div class="person">
        <div class="mbox">
            <div class="mtop">
                <img class="back" src="../public/images/back.png" alt="" @click="goback()">
                <p class="mtitle">{{info.name}}</p>
                <img class="share" src="../public/images/share.png" alt="">
            </div>
        </div>
        <div class="content">
            <div class="infobox clearfix">
                <img class="actor-pic fl" :src="'https://images.weserv.nl/?url='+info.avatars.large.substring(7)" alt="">
                <div class="infotext">
                    <p class="name b">{{info.name}}</p>
                    <p class="enname"><b>英文名：</b>{{info.name_en}}</p>
                    <p class="bornplace"><b>出生地：</b>{{info.born_place}}</p>
                    <p class="nickname"><b>别名：</b><em v-for="(name,idx) in info.aka" :key="idx">{{name}} </em> </p>
                </div>
            </div>
            <div class="works">
                <h2 class="b">代表作品</h2>
                <ul class="work-con">
                    <li class="work-list clearfix" v-for="(work,idx) in info.works" :key="idx" @click="moredetail(work.subject.id)">
                        <img class="work-pic fl" :src="'https://images.weserv.nl/?url='+work.subject.images.large.substring(7)" alt="">
                        <div class="work-detail">
                            <p class="workname b">{{work.subject.title}}</p>
                            <p class="originname">{{work.subject.original_title}}</p>
                            <p class="other">
                                年份：{{work.subject.year}}
                                <em class="types" v-for="(item,idx) in work.subject.genres" :key="idx">{{item}} </em>
                            </p>
                            <p class="comment-num">{{work.subject.collect_count}} 人评价</p>
                            <div class="score-box clearfix">
                                <div class="score fl">
                                    <div v-if="work.subject.rating.average >= 9">
                                        <div class="star10"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 8 && work.subject.rating.average <9">
                                        <div class="star9"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 7 && work.subject.rating.average <8">
                                        <div class="star8"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 6 && work.subject.rating.average <7">
                                        <div class="star7"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 5 && work.subject.rating.average <6">
                                        <div class="star6"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 4 && work.subject.rating.average <5">
                                        <div class="star5"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 3 && work.subject.rating.average <4">
                                        <div class="star4"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 2 && work.subject.rating.average <3">
                                        <div class="star3"></div>
                                    </div>
                                    <div v-else-if="work.subject.rating.average >= 1 && work.subject.rating.average <0">
                                        <div class="star2"></div>
                                    </div>
                                    <div v-else>
                                        <div class="star1"></div>
                                    </div>
                                </div>
                                <div class="scorenum fl">{{work.subject.rating.average}}</div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        <loading v-if="load"></loading>
    </div>
</template>

<script>
    import loading from '../components/loading'
    export default{
        data(){
            return{
                load:true,
                info:{
                    avatars:{
                        large:''
                    },
                    works:[
                        {
                            subject:{
                                rating:{
                                    average:''
                                },
                                genres:'',
                                title:'',
                                casts:{
                                    avatars:{
                                        large:''
                                    },
                                    name:'',
                                    id:''
                                },
                                collect_count:'',
                                original_title:'',
                                directors:'',
                                year:'',
                                images:{
                                    large:''
                                },
                                id:''
                            }
                        }
                    ]
                }
            }
        },
        created(){
            let curl = window.location.href;
            let pid = curl.split('?')[1];
            this.$axios.get(`https://xkolento.cn/movie/person/${pid}`,{

            }).then(res=>{
                this.info=res.data;
                this.load=false
                console.log(this.info.works)
            })
        },
        components:{
            loading
        },
        methods:{
            goback(){
                window.history.go(-1);
            },
            moredetail(mid){
                this.$router.push(`mdetail?mid=${mid}`);
            }
        }
    }
</script>

<style scoped>
    .mbox {background:rgba(30,29,35,0.75);}
    .mtop {display: flex;justify-content: space-between;color:#fff;font-size: 3rem;padding: 2rem;}
    .mtop img{width: 3.6rem;height: 3.6rem;}
    .content {padding: 2rem;margin-top: 2rem;}
    .content .actor-pic {width: 30rem;border-radius:1rem;box-shadow:0 0 2rem rgba(0,0,0,0.2);}
    .content .infotext {margin:0 2rem 0 33rem;}
    .infotext .name {font-size: 4rem;margin-top: 2rem;}
    .infotext .enname {font-size: 2.8rem;margin-top: 5rem;}
    .infotext .bornplace {font-size: 2.8rem;margin-bottom: 1rem;}
    .infotext .nickname {font-size: 2.8rem;}
    .works {margin-top: 8rem;}
    .works h2{font-size: 3rem;margin-bottom: 2.5rem;}
    .works .work-list {padding-bottom: 2rem;margin-bottom: 2rem;}
    .work-detail {margin:2.5rem 0 0 23rem;}
    .work-pic {width: 20rem;border-radius:1rem;box-shadow:0 0 2rem rgba(0,0,0,0.2);}
    .workname {font-size: 3.2rem;margin-bottom: 1rem;}
    .originname {color:#aaa;font-size: 2.8rem;}
    .other {color:#aaa;font-size: 2.8rem;}
    .types {margin-left: 1rem;}
    .comment-num {font-size: 2.8rem;color:#aaa;margin-top: 0.5rem;}
    .score-box {margin-top: 0.5rem;}
    .scorenum {color:#e09015;font-size: 2.8rem;margin-left: 1rem;}
    .star10 {background: url('../public/images/stars.png') no-repeat 0 0;
    background-size: 100%;width: 15rem;height: 3.1rem;position: relative;top: 0.3rem;}
    .star9 {background: url('../public/images/stars.png') no-repeat 0 -3rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star8 {background: url('../public/images/stars.png') no-repeat 0 -6rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star7 {background: url('../public/images/stars.png') no-repeat 0 -9rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star6 {background: url('../public/images/stars.png') no-repeat 0 -12rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star5 {background: url('../public/images/stars.png') no-repeat 0 -15rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star4 {background: url('../public/images/stars.png') no-repeat 0 -18rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star3 {background: url('../public/images/stars.png') no-repeat 0 -21rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star2 {background: url('../public/images/stars.png') no-repeat 0 -24rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star1 {background: url('../public/images/stars.png') no-repeat 0 -27rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
    .star0 {background: url('../public/images/stars.png') no-repeat 0 -30rem;
    background-size: 100%;width: 15rem;height: 3.1rem;}
</style>