<template>
    <div class="alltype">
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
            <h2>恐怖榜单</h2>
            <showpart :movietype="disaster"></showpart>
        </div>

    </div>
</template>

<script>
    import showpart from '../components/show'
    export default{
        data(){
            return{
                anime:'',
                story:'',
                happy:'',
                act:'',
                love:'',
                scientist:'',
                scare:'',
                horror:'',
                disaster:''
            }
        },
        created(){
            let anime = localStorage.getItem('anime');
            if(anime){
                let animeJson = JSON.parse(anime)
                this.anime = animeJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_list`,{
                    params:{}
                }).then(res=>{
                    this.anime=res.data;
                    let animestr = JSON.stringify(res.data)
                    localStorage.setItem('anime', animestr);
                })
            }

            let story = localStorage.getItem('stories');
            if(story){
                let storyJson = JSON.parse(story)
                this.story = storyJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_story`,{
                    params:{}
                }).then(res=>{
                    this.story=res.data;
                    let storystr = JSON.stringify(res.data)
                    localStorage.setItem('stories', storystr);
                })
            }

            let happy = localStorage.getItem('happy');
            if(happy){
                let happyJson = JSON.parse(happy)
                this.happy = happyJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_happy`,{
                    params:{}
                }).then(res=>{
                    this.happy=res.data;
                    let happystr = JSON.stringify(res.data)
                    localStorage.setItem('happy', happystr);
                })
            }

            let act = localStorage.getItem('act');
            if(act){
                let actJson = JSON.parse(act)
                this.act = actJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_act`,{
                    params:{}
                }).then(res=>{
                    this.act=res.data;
                    let actstr = JSON.stringify(res.data)
                    localStorage.setItem('act', actstr);
                })
            }

            let love = localStorage.getItem('love');
            if(love){
                let loveJson = JSON.parse(love)
                this.love = loveJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_love`,{
                    params:{}
                }).then(res=>{
                    this.love=res.data;
                    let lovestr = JSON.stringify(res.data)
                    localStorage.setItem('love', lovestr);
                })
            }

            let scientist = localStorage.getItem('scientist');
            if(scientist){
                let scientistJson = JSON.parse(scientist)
                this.scientist = scientistJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_scientist`,{
                    params:{}
                }).then(res=>{
                    this.scientist=res.data;
                    let scientiststr = JSON.stringify(res.data)
                    localStorage.setItem('scientist', scientiststr);
                })
            }

            let scare = localStorage.getItem('scare');
            if(scare){
                let scareJson = JSON.parse(scare)
                this.scare = scareJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_scare`,{
                    params:{}
                }).then(res=>{
                    this.scare=res.data;
                    let scarestr = JSON.stringify(res.data)
                    localStorage.setItem('scare', scarestr);
                })
            }

            let horror = localStorage.getItem('horror');
            if(horror){
                let horrorJson = JSON.parse(horror)
                this.horror = horrorJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_horror`,{
                    params:{}
                }).then(res=>{
                    this.horror=res.data;
                    let horrorstr = JSON.stringify(res.data)
                    localStorage.setItem('horror', horrorstr);
                })
            }

            let disaster = localStorage.getItem('disaster');
            if(disaster){
                let disasterJson = JSON.parse(disaster)
                this.disaster = disasterJson
            }else{
                this.$axios.get(`http://xkolento.cn/chart/top_disaster`,{
                    params:{}
                }).then(res=>{
                    this.disaster=res.data;
                    let disasterstr = JSON.stringify(res.data)
                    localStorage.setItem('disaster', disasterstr);
                })
            }
        },
        components:{
            showpart
        }
    }
</script>

<style>
    .alltype {padding:2rem 3%;}
    .alltype h2{font-size: 3rem;}
</style>
