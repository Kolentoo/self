<template>
    <div class="animebox">
        <div class="commonbox">
            <div class="top">
                <img class="back" src="../public/images/back.png" alt="" @click="goback()">
                <p class="mtitle">动漫</p>
                <img class="share opacity" src="../public/images/share.png" alt="">
            </div>
        </div>
        <div class="anime">
            <div class="anime-section">
                <h2>最新动漫</h2>
                <tvshow :movietype="animenew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>人气动漫</h2>
                <tvshow :movietype="animehot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>动漫榜单</h2>
                <tvshow :movietype="animenice"></tvshow>
            </div>
        </div>
    </div>
</template>

<script>
    import loading from '../components/loading'
    import tvshow from '../components/tvshow'
    export default{
        data(){
            return{
                load:true,
                animenew:'',
                animehot:'',
                animenice:''
            }
        },
        created(){
            let myDate = new Date();
            let day = myDate.getDate();
            let firstday = localStorage.getItem('today')
            
            if(firstday!=day){
                this.animenewapi();
                this.animehotapi();
                this.animeniceapi();
            }else{
                let animenew = localStorage.getItem('animenew');
                if(animenew){
                    let animenewJson = JSON.parse(animenew)
                    console.log(animenewJson)
                    this.animenew = animenewJson
                }else{
                    this.animenewapi();
                }

                let animehot = localStorage.getItem('animehot');
                if(animehot){
                    let animehotJson = JSON.parse(animehot)
                    console.log(animehotJson)
                    this.animehot = animehotJson
                }else{
                    this.animehotapi();
                }

                let animenice = localStorage.getItem('animenice');
                if(animenice){
                    let animeniceJson = JSON.parse(animenice)
                    console.log(animeniceJson)
                    this.animenice = animeniceJson
                    this.load=false
                }else{
                    this.animeniceapi();
                }
            }

        },
        methods:{
            goback(){
                window.history.go(-1);
            },
            animenewapi(){
                this.$axios.get(`http://xkolento.cn/anime/new`,{
                    params:{}
                }).then(res=>{
                    this.animenew=res.data.subjects;
                    let animenewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('animenew', animenewstr);
                })
            },
            animehotapi(){
                this.$axios.get(`http://xkolento.cn/anime/hot`,{
                    params:{}
                }).then(res=>{
                    this.animehot=res.data.subjects;
                    let animehotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('animehot', animehotstr);
                })
            },
            animeniceapi(){
                this.$axios.get(`http://xkolento.cn/anime/nice`,{
                    params:{}
                }).then(res=>{
                    this.animenice=res.data.subjects;
                    let animenicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('animenice', animenicestr);
                    this.load=false
                })
            }
        },
        components:{
            tvshow,loading
        }
    }
</script>

<style scope>
    .share {z-index:-1;}
    .anime {padding:2rem 3%;margin-top: 10rem;}
    .anime h2{font-size: 3rem;}
</style>