<template>
    <div class="moviedetail">
        <div class="mbox">
            <div class="mtop">
                <img class="back" src="../public/images/back.png" alt="">
                <p class="mtitle">电影</p>
                <img class="share" src="../public/images/share.png" alt="">
            </div>
            <div class="mbanner">
                <img class="mpic vm" :src="detail.images.large" alt="">
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
                <p class="p1">豆瓣评分</p>
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
        <div class="actor">
            <h2>演员</h2>
            <div class="wrapper" ref="wrapper">
                <ul class="actor-con clearfix content" ref="content">
                    <li class="actor-list fl" v-for="(item,idx) in detail.casts" :key="idx">
                        <img class="actor-pic vm" :src="'https://images.weserv.nl/?url='+item.avatars.small.substring(7)" alt="">
                        <p class="actor-name">{{item.name}}</p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    import BScroll from 'better-scroll'
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
                    casts:[]
                }
            }
        },
        created(){
            let curl = window.location.href;
            let midgroup = curl.split('?')[1];
            let mid = midgroup.split('=')[1];
            let detailgroup = localStorage.getItem(mid);
            
            if(detailgroup){
                let mdetail = JSON.parse(detailgroup);
                this.detail=mdetail
            }else{
                this.$.ajax({
                    url:`https://api.douban.com/v2/movie/subject/${mid}`,
                    dataType:'jsonp',
                    success:(res)=>{
                        this.detail=res;
                        let mdetail = JSON.stringify(res)
                        localStorage.setItem(mid, mdetail);
                    }
                })
            }
        },
        mounted(){
            let content = this.$refs.content;
            let wrapper = this.$refs.wrapper;
            let clength = this.detail.casts.length;
            content.style.width=25*clength+'rem'
            let scroll = new BScroll(wrapper,{
                startX:0,
                scrollX:true,
                scrollY:false,
                momentum:false
            })
        }
    }
</script>

<style scoped>
    body,html {width: 100%;overflow-x:hidden; }
    .mbox {background:rgb(30,29,35);}
    .mbanner {display:flex;justify-content: center;align-items: center;}
    .mbanner .mpic {width: 75%;max-height:70rem;padding:2rem 0 5rem 0;}
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
    .actor {margin: 2rem;overflow: hidden;}
    .actor h2{color:#aaa;font-size: 3.2rem;}
    .actor .actor-con {width: 150%;overflow: scroll;margin-top: 1.5rem;white-space: nowrap;}
    .actor .actor-list {text-align: center;width: 22rem;margin-right: 3rem;white-space: nowrap;}
    .actor .actor-list img{width: 100%;border-radius:1rem;}
    .actor .actor-name {color:#333;font-size: 2.8rem;margin-top: 0.5rem;}
</style>