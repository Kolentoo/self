<template>
    <div class="moviebox">
        <div class="commonbox">
            <div class="top">
                <img class="back" src="../public/images/back.png" alt="" @click="goback()">
                <p class="mtitle">电影</p>
                <img class="share opacity" src="../public/images/share.png" alt="">
            </div>
            <ul class="nav">
                <li :class="['nav-list',{liston:self.liston}]" @click="tab(idx)" v-for="(self,idx) in types" :key="idx">{{self.name}}</li>
            </ul>
        </div>
        <div class="moviecon">
            <div class="movies" v-if="tabstatus===0">
                <div class="section">
                    <div class="anime-section">
                        <h2>正在热映</h2>
                        <showpart :movietype="now"></showpart>
                    </div>
                    <div class="anime-section">
                        <h2>即将上映</h2>
                        <showpart :movietype="comeing"></showpart>
                    </div>
                    <div class="anime-section">
                        <h2>口碑排行</h2>
                        <showpart :movietype="ranking"></showpart>
                    </div>
                </div>
            </div>
            <div class="alltype" v-if="tabstatus===1">
                <div class="anime-section">
                    <h2>动漫榜单</h2>
                    <showpart :movietype="anime" ></showpart>
                </div>
                <div class="anime-section">
                    <h2>剧情榜单</h2>
                    <showpart :movietype="story"></showpart>
                </div>
                <div class="anime-section">
                    <h2>喜剧榜单</h2>
                    <showpart :movietype="happy"></showpart>
                </div>
                <div class="anime-section">
                    <h2>动作榜单</h2>
                    <showpart :movietype="act"></showpart>
                </div>
                <div class="anime-section">
                    <h2>爱情榜单</h2>
                    <showpart :movietype="love"></showpart>
                </div>
                <div class="anime-section">
                    <h2>科幻榜单</h2>
                    <showpart :movietype="scientist"></showpart>
                </div>
                <div class="anime-section">
                    <h2>惊悚榜单</h2>
                    <showpart :movietype="scare"></showpart>
                </div>
                <div class="anime-section">
                    <h2>恐怖榜单</h2>
                    <showpart :movietype="horror"></showpart>
                </div>
                <div class="anime-section">
                    <h2>灾难榜单</h2>
                    <showpart :movietype="disaster"></showpart>
                </div>

            </div>
        </div>
        <loading v-if="load"></loading>
    </div>
</template>
    
<script>
    import loading from '../components/loading'
    import showpart from '../components/show'
    export default{
        data(){
            return{
                tabstatus:0,
                types:[
                    {name:'推荐',liston:true},
                    {name:'分类',liston:false}
                ],
                now:{
                    images:{
                        large:'',
                        small:''
                    },
                    rating:{
                        average:''
                    }
                },
                comeing:{
                    images:{
                        large:'',
                        small:''
                    },
                    rating:{
                        average:''
                    }
                },
                ranking:{
                    images:{
                        large:'',
                        small:''
                    },
                    rating:{
                        average:''
                    }
                },
                america:{
                    images:{
                        large:'',
                        small:''
                    },
                    rating:{
                        average:''
                    }
                },
                anime:'',
                story:'',
                happy:'',
                act:'',
                love:'',
                scientist:'',
                scare:'',
                horror:'',
                disaster:'',
                load:true
            }
        },
        created(){
            let myDate = new Date();
            let day = myDate.getDate();
            let firstday = localStorage.getItem('today')

            if(firstday!=day){
                this.nowapi();
                this.comingapi();
                this.topapi();
                this.toplistapi();
                this.topstoryapi();
                this.tophappyapi();
                this.topactapi();
                this.toploveapi();
                this.topscientistapi();
                this.topscareapi();
                this.tophorrorapi();
                this.topdisasterapi();
            }else{
                let now = localStorage.getItem('now');
                if(now){
                    let nowJson = JSON.parse(now)
                    console.log(nowJson)
                    this.now = nowJson
                }else{
                    this.nowapi();
                }

                let comeing = localStorage.getItem('comeing');
                if(comeing){
                    let comeingJson = JSON.parse(comeing)
                    console.log(comeingJson)
                    this.comeing = comeingJson
                }else{
                    this.comingapi();
                }

                let ranking = localStorage.getItem('ranking');
                if(ranking){
                    let rankingJson = JSON.parse(ranking)
                    console.log(rankingJson)
                    this.ranking = rankingJson
                    this.load=false
                }else{
                    this.topapi();
                }
                
                let anime = localStorage.getItem('anime');
                if(anime){
                    let animeJson = JSON.parse(anime)
                    this.anime = animeJson
                }else{
                    this.toplistapi();
                }

                let story = localStorage.getItem('stories');
                if(story){
                    let storyJson = JSON.parse(story)
                    this.story = storyJson
                }else{
                    this.topstoryapi();
                }

                let happy = localStorage.getItem('happy');
                if(happy){
                    let happyJson = JSON.parse(happy)
                    this.happy = happyJson
                }else{
                    this.tophappyapi();
                }

                let act = localStorage.getItem('act');
                if(act){
                    let actJson = JSON.parse(act)
                    this.act = actJson
                }else{
                    this.topactapi();
                }

                let love = localStorage.getItem('love');
                if(love){
                    let loveJson = JSON.parse(love)
                    this.love = loveJson
                }else{
                    this.toploveapi();
                }

                let scientist = localStorage.getItem('scientist');
                if(scientist){
                    let scientistJson = JSON.parse(scientist)
                    this.scientist = scientistJson
                }else{
                    this.topscientistapi();
                }

                let scare = localStorage.getItem('scare');
                if(scare){
                    let scareJson = JSON.parse(scare)
                    this.scare = scareJson
                }else{
                    this.topscareapi();
                }

                let horror = localStorage.getItem('horror');
                if(horror){
                    let horrorJson = JSON.parse(horror)
                    this.horror = horrorJson
                }else{
                    this.tophorrorapi();
                }

                let disaster = localStorage.getItem('disaster');
                if(disaster){
                    let disasterJson = JSON.parse(disaster)
                    this.disaster = disasterJson
                }else{
                    this.topdisasterapi();
                }
            }

        },
        methods:{
            tab(idx){
                this.tabstatus=idx
                for(let key in this.types){
                    if(key==idx){
                        this.types[key].liston=true
                    }else{
                        this.types[key].liston=false
                    }
                }
            },
            goback(){
                window.history.go(-1);
            },
            nowapi(){
                this.$axios.get(`https://xkolento.cn/v2/movie/in_theaters`,{
                    params:{}
                }).then(res=>{
                    this.now=res.data.subjects;
                    let nowstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('now', nowstr);
                })
            },
            comingapi(){
                this.$axios.get(`https://xkolento.cn/v2/movie/coming_soon`,{
                    params:{}
                }).then(res=>{
                    this.comeing=res.data.subjects;
                    let comeingstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('comeing', comeingstr);
                })
            },
            topapi(){
                this.$axios.get(`https://xkolento.cn/v2/movie/top250`,{
                    params:{}
                }).then(res=>{
                    this.ranking=res.data.subjects;
                    let rankingstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('ranking', rankingstr);
                    this.load=false
                })
            },
            toplistapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_list`,{
                    params:{}
                }).then(res=>{
                    this.anime=res.data;
                    let animestr = JSON.stringify(res.data)
                    localStorage.setItem('anime', animestr);
                })
            },
            topstoryapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_story`,{
                    params:{}
                }).then(res=>{
                    this.story=res.data;
                    let storystr = JSON.stringify(res.data)
                    localStorage.setItem('stories', storystr);
                })
            },
            tophappyapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_happy`,{
                    params:{}
                }).then(res=>{
                    this.happy=res.data;
                    let happystr = JSON.stringify(res.data)
                    localStorage.setItem('happy', happystr);
                })
            },
            topactapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_act`,{
                    params:{}
                }).then(res=>{
                    this.act=res.data;
                    let actstr = JSON.stringify(res.data)
                    localStorage.setItem('act', actstr);
                })
            },
            toploveapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_love`,{
                    params:{}
                }).then(res=>{
                    this.love=res.data;
                    let lovestr = JSON.stringify(res.data)
                    localStorage.setItem('love', lovestr);
                })
            },
            topscientistapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_scientist`,{
                    params:{}
                }).then(res=>{
                    this.scientist=res.data;
                    let scientiststr = JSON.stringify(res.data)
                    localStorage.setItem('scientist', scientiststr);
                })
            },
            topscareapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_scare`,{
                    params:{}
                }).then(res=>{
                    this.scare=res.data;
                    let scarestr = JSON.stringify(res.data)
                    localStorage.setItem('scare', scarestr);
                })
            },
            tophorrorapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_horror`,{
                    params:{}
                }).then(res=>{
                    this.horror=res.data;
                    let horrorstr = JSON.stringify(res.data)
                    localStorage.setItem('horror', horrorstr);
                })
            },
            topdisasterapi(){
                this.$axios.get(`https://xkolento.cn/chart/top_disaster`,{
                    params:{}
                }).then(res=>{
                    this.disaster=res.data;
                    let disasterstr = JSON.stringify(res.data)
                    localStorage.setItem('disaster', disasterstr);
                })
            }
        },
        components:{
            showpart,loading
        }
    }
</script>

<style scoped>
    .movies {padding:2rem 3%;padding-top: 15rem;}
    .movies h2{font-size: 3rem;}
    .alltype {padding:2rem 3%;padding-top: 15rem;}
    .alltype h2{font-size: 3rem;}
</style>