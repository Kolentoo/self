<template>
    <div class="result">
        <div class="search-box clearfix">
            <div class="input-box fl">
                <input v-model="swords" class="search block" type="text" placeholder="请输入关键字" @keyup.enter="searchwords(swords)">
            </div>
            <img class="search-icon" src="../public/images/search.png" alt="">
            <p class="cancel fr" @click="goindex()">取消</p>
        </div>
        <div class="result-con">
            <div class="wrapper" ref="wrapper">
                <div class="content" ref="content">
                    <h2 class="search-title"><i>{{searchtitle}}</i> <em>共 {{searchcounts}} 条</em></h2>
                    <ul class="search-con">
                        <li class="search-list" v-for="(slist,idx) in searchresult" :key="idx" @click="moredetail(slist.id)">
                            <img class="work-pic fl" :src="'https://images.weserv.nl/?url='+slist.images.large.substring(7)" alt="">
                            <div class="work-detail">
                                <p class="workname b">{{slist.title}}</p>
                                <p class="originname">{{slist.original_title}}</p>
                                <p class="other">
                                    年份：{{slist.year}}
                                    <em class="types" v-for="(item,idx) in slist.genres" :key="idx">{{item}} </em>
                                </p>
                                <p class="comment-num">{{slist.collect_count}} 人评价</p>
                                <div class="score-box clearfix" v-if="slist.rating">
                                    <div class="score fl">
                                        <div v-if="slist.rating.average >= 9">
                                            <div class="star10"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 8 && slist.rating.average <9">
                                            <div class="star9"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 7 && slist.rating.average <8">
                                            <div class="star8"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 6 && slist.rating.average <7">
                                            <div class="star7"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 5 && slist.rating.average <6">
                                            <div class="star6"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 4 && slist.rating.average <5">
                                            <div class="star5"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 3 && slist.rating.average <4">
                                            <div class="star4"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 2 && slist.rating.average <3">
                                            <div class="star3"></div>
                                        </div>
                                        <div v-else-if="slist.rating.average >= 1 && slist.rating.average <0">
                                            <div class="star2"></div>
                                        </div>
                                        <div v-else>
                                            <div class="star1"></div>
                                        </div>
                                    </div>
                                    <div class="scorenum fl">{{slist.rating.average}}</div>
                                </div>
                            </div>
                        </li>
                    </ul>
                    <div class="more-loading tc" v-show="moreload">
                        <img class="more-pic" src="../public/images/loading2.gif" alt="">
                    </div>
                </div>
            </div>
        </div>
        <loading v-if="load"></loading>
    </div>
</template>

<script>
    import loading from '../components/loading'
    import BScroll from 'better-scroll'
    export default{
        data(){
            return {
                searchresult:[
                    {
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
                ],
                searchcounts:'',
                searchtitle:'',
                load:true,
                swords:'',
                keywords:'',
                scroll:'',
                moreload:false,
                all:[],
                resultarray:[],
                length:0
            }
        },
        created(){
            this.$nextTick(()=>{
                this.searchapi();
            })
        },
        methods:{
            moredetail(mid){
                this.$router.push(`mdetail?mid=${mid}`);
            },
            searchwords(swords){
                if(swords!=''){
                    this.load=true
                    this.$axios.get(`http://xkolento.cn/search/${swords}`,{
                        params:{}
                    }).then(res=>{
                        this.searchresult=res.data.subjects
                        this.searchcounts=res.data.count
                        this.searchtitle=res.data.title
                        this.load=false
                        this.swords=''
                    })
                    
                }
            },
            goindex(){
                this.$router.push('/');
            },
            searchapi(){
                let curl = window.location.href;
                if(curl.indexOf('?')>-1){
                    this.keywords = curl.split('?')[1];
                }else{
                    this.keywords = '动漫'
                }

                this.$axios.get(`http://xkolento.cn/search/${this.keywords}`,{
                    params:{}
                }).then(res=>{
                    this.searchresult=res.data.subjects
                    this.searchcounts=res.data.count
                    this.searchtitle=res.data.title
                    this.load=false
                })
            }
        },
        components:{
            loading
        }
    }
</script>

<style scoped>
    .search-box {padding: 2rem 2.5%;border-bottom: 1px solid #F2F2F2;box-shadow:0 0 0.3rem rgba(0,0,0,0.2);position: fixed;
    top: 0;left: 0;width:95%;z-index:700;background: #fff;}
    .input-box {position: relative;width: 80%;}
    .search {width: 100%;height: 5rem;line-height: 5rem;border-radius:1rem;background: #f5f5f5;border:none;font-size: 2.8rem;color:#333;
    text-align: center;}
    .search-title {margin-top:7rem;}
    .result-con {margin-top: 10rem;}
    .cancel {font-size: 2.8rem;color:#e09015;line-height: 5rem;padding-right: 2rem;}
    .search-icon {position: absolute;left: 3.3rem;top: 3.3rem;width: 3rem;}
    .content {padding:2rem;margin-top: 2rem;}
    .content i{font-size: 3rem;font-weight:bold;}
    .content em {font-size: 2.6rem;margin-left: 3rem;color:#aaa;}
    .search-list {padding-bottom: 2rem;margin-bottom: 2rem;}
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
    .more-loading {height: 15rem;overflow: hidden;margin-top: -5rem;}
    .more-pic {width: 30rem;margin:-5rem auto 0;}
    /*.wrapper {position: absolute;left: 0;top: 0;width: 100%;height: 100%;}*/
</style>