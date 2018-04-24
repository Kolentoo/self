<template>
    <div class="movies">
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
        <div class="anime-section">
            <h2>北美票房</h2>
            <showpart :movietype="america"></showpart>
        </div>
    </div>
</template>
    
<script>
    import showpart from '../components/show'
    export default{
        data(){
            return{
                now:{
                    images:{
                        large:'',
                        small:''
                    },
                    rating:{
                        average:''
                    }
                },
                coming:{
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
                }
            }
        },
        created(){
            let now = localStorage.getItem('now');
            if(now){
                let nowJson = JSON.parse(now)
                console.log(nowJson)
                this.now = nowJson
            }else{
                this.$axios.get(`http://xkolento.cn/v2/movie/in_theaters`,{
                    params:{}
                }).then(res=>{
                    this.now=res.data.subjects;
                    let nowstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('now', nowstr);
                })
            }

            let comeing = localStorage.getItem('comeing');
            if(comeing){
                let comeingJson = JSON.parse(comeing)
                console.log(comeingJson)
                this.comeing = comeingJson
            }else{
                this.$axios.get(`http://xkolento.cn/v2/movie/coming_soon`,{
                    params:{}
                }).then(res=>{
                    this.comeing=res.data.subjects;
                    let comeingstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('comeing', comeingstr);
                })
            }

            let ranking = localStorage.getItem('ranking');
            if(ranking){
                let rankingJson = JSON.parse(ranking)
                console.log(rankingJson)
                this.ranking = rankingJson
            }else{
                this.$axios.get(`http://xkolento.cn/v2/movie/top250`,{
                    params:{}
                }).then(res=>{
                    this.ranking=res.data.subjects;
                    let rankingstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('ranking', rankingstr);
                })
            }

            let america = localStorage.getItem('america');
            if(america){
                let americaJson = JSON.parse(america)
                console.log(americaJson)
                this.america = americaJson
            }else{
                this.$axios.get(`http://xkolento.cn/v2/movie/us_box`,{
                    params:{}
                }).then(res=>{
                    this.america=res.data.subjects;
                    let americastr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('america', americastr);
                })
            }
        },
        components:{
            showpart
        }
    }
</script>

<style scoped>
    .movies {padding:2rem 3%;}
    .movies h2{font-size: 3rem;}
</style>