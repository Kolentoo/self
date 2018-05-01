<template>
    <div class="tvplaybox">
        <div class="commonbox">
            <div class="top">
                <img class="back" src="../public/images/back.png" alt="" @click="goback()">
                <p class="mtitle">电视剧</p>
                <img class="share opacity" src="../public/images/share.png" alt="">
            </div>
            <div class="wrapper" ref="wrapper">
                <ul class="nav content" ref="content">
                    <li ref="navlist" :class="['nav-list',{liston:self.liston}]" @click="tab(idx)" v-for="(self,idx) in types" :key="idx">{{self.name}}</li>
                </ul>
            </div>
        </div>
        <div class="hot tvcon" v-if="tabstatus===0">
            <div class="anime-section">
                <h2>最新推送</h2>
                <tvshow :movietype="hotnew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>人气推荐</h2>
                <tvshow :movietype="hothot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>口碑榜单</h2>
                <tvshow :movietype="hotnice"></tvshow>
            </div>
        </div>
        <div class="america tvcon" v-if="tabstatus===1">
            <div class="anime-section">
                <h2>最新美剧</h2>
                <tvshow :movietype="americanew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热美剧</h2>
                <tvshow :movietype="americahot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>美剧榜单</h2>
                <tvshow :movietype="americanice"></tvshow>
            </div>
        </div>
        <div class="england tvcon" v-if="tabstatus===2">
            <div class="anime-section">
                <h2>最新英剧</h2>
                <tvshow :movietype="englandnew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热英剧</h2>
                <tvshow :movietype="englandhot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>英剧榜单</h2>
                <tvshow :movietype="englandnice"></tvshow>
            </div>
        </div>
        <div class="korea tvcon" v-if="tabstatus===3">
            <div class="anime-section">
                <h2>最新韩剧</h2>
                <tvshow :movietype="koreanew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热韩剧</h2>
                <tvshow :movietype="koreahot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>韩剧榜单</h2>
                <tvshow :movietype="koreanice"></tvshow>
            </div>
        </div>
        <div class="japan tvcon" v-if="tabstatus===4">
            <div class="anime-section">
                <h2>最新日剧</h2>
                <tvshow :movietype="japannew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热日剧</h2>
                <tvshow :movietype="japanhot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>日剧榜单</h2>
                <tvshow :movietype="japannice"></tvshow>
            </div>
        </div>
        <div class="china tvcon" v-if="tabstatus===5">
            <div class="anime-section">
                <h2>最新国剧</h2>
                <tvshow :movietype="chinanew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热国剧</h2>
                <tvshow :movietype="chinahot"></tvshow>
            </div>
            <div class="anime-section" v-if="chinanice">
                <h2>国剧榜单</h2>
                <tvshow :movietype="chinanice"></tvshow>
            </div>
        </div>
        <div class="hongkong tvcon" v-if="tabstatus===6">
            <div class="anime-section">
                <h2>最新港剧</h2>
                <tvshow :movietype="hongkongnew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热港剧</h2>
                <tvshow :movietype="hongkonghot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>港剧榜单</h2>
                <tvshow :movietype="hongkongnice"></tvshow>
            </div>
        </div>
        <div class="variety tvcon" v-if="tabstatus===7">
            <div class="anime-section">
                <h2>最新综艺</h2>
                <tvshow :movietype="varietynew"></tvshow>
            </div>
            <div class="anime-section">
                <h2>最热综艺</h2>
                <tvshow :movietype="varietyhot"></tvshow>
            </div>
            <div class="anime-section">
                <h2>综艺榜单</h2>
                <tvshow :movietype="varietynice"></tvshow>
            </div>
        </div>
        <loading v-if="load"></loading>
    </div>
</template>

<script>
    import BScroll from 'better-scroll'
    import loading from '../components/loading'
    import tvshow from '../components/tvshow'
    export default{
        data(){
            return{
                load:true,
                tabstatus:0,
                types:[
                    {name:'热门',liston:true},
                    {name:'美剧',liston:false},
                    {name:'英剧',liston:false},
                    {name:'韩剧',liston:false},
                    {name:'日剧',liston:false},
                    {name:'国剧',liston:false},
                    {name:'港剧',liston:false},
                    {name:'综艺',liston:false}
                ],
                hotnew:'',
                hothot:'',
                hotnice:'',
                americanew:'',
                americahot:'',
                americanice:'',
                englandnew:'',
                englandhot:'',
                englandnice:'',
                koreanew:'',
                koreahot:'',
                koreanice:'',
                japannew:'',
                japanhot:'',
                japannice:'',
                chinanew:'',
                chinahot:'',
                chinanice:'',
                hongkongnew:'',
                hongkonghot:'',
                hongkongnice:'',
                varietynew:'',
                varietyhot:'',
                varietynice:''
            }
        },
        created(){
            let myDate = new Date();
            let day = myDate.getDate();
            let firstday = localStorage.getItem('today')
            if(firstday!=day){
                this.hotnewapi();
                this.hothotapi();
                this.hotniceapi();
            }else{
                let hotnew = localStorage.getItem('hotnew');
                if(hotnew){
                    let hotnewJson = JSON.parse(hotnew)
                    console.log(hotnewJson)
                    this.hotnew = hotnewJson
                }else{
                    this.hotnewapi();
                }

                let hothot = localStorage.getItem('hothot');
                if(hothot){
                    let hothotJson = JSON.parse(hothot)
                    console.log(hothotJson)
                    this.hothot = hothotJson
                }else{
                    this.hothotapi();
                }

                let hotnice = localStorage.getItem('hotnice');
                if(hotnice){
                    let hotniceJson = JSON.parse(hotnice)
                    console.log(hotniceJson)
                    this.hotnice = hotniceJson
                    this.load=false
                }else{
                    this.hotniceapi();
                }
            }

        },
        mounted(){
            let content = this.$refs.content;
            let wrapper = this.$refs.wrapper;
            content.style.width=12*8+'rem'
            let scroll = new BScroll(wrapper,{
                startX:0,
                scrollX:true,
                scrollY:false,
                momentum:false,
                click:true
            })
        },
        methods:{
            tab(idx){
                this.load=true
                this.tabstatus=idx
                for(let key in this.types){
                    if(key==idx){
                        this.types[key].liston=true
                    }else{
                        this.types[key].liston=false
                    }
                }
                let myDate = new Date();
                let day = myDate.getDate();
                let firstday = localStorage.getItem('today')

                if(idx===1){
                    if(firstday!=day){
                        this.americanewapi();
                        this.americahotapi();
                        this.americaniceapi();
                    }else{
                        let americanew = localStorage.getItem('americanew');
                        if(americanew){
                            let americanewJson = JSON.parse(americanew)
                            console.log(americanewJson)
                            this.americanew = americanewJson
                        }else{
                            this.americanewapi();
                        }

                        let americahot = localStorage.getItem('americahot');
                        if(americahot){
                            let americahotJson = JSON.parse(americahot)
                            console.log(americahotJson)
                            this.americahot = americahotJson
                        }else{
                            this.americahotapi();
                        }

                        let americanice = localStorage.getItem('americanice');
                        if(americanice){
                            let americaniceJson = JSON.parse(americanice)
                            console.log(americaniceJson)
                            this.americanice = americaniceJson
                            this.load=false
                        }else{
                            this.americaniceapi();
                        }
                    }
                }else if(idx===2){
                    if(firstday!=day){
                        this.englandnewapi();
                        this.englandhotapi();
                        this.englandniceapi();
                    }else{
                        let englandnew = localStorage.getItem('englandnew');
                        if(englandnew){
                            let englandnewJson = JSON.parse(englandnew)
                            console.log(englandnewJson)
                            this.englandnew = englandnewJson
                        }else{
                            this.englandnewapi();
                        }

                        let englandhot = localStorage.getItem('englandhot');
                        if(englandhot){
                            let englandhotJson = JSON.parse(englandhot)
                            console.log(englandhotJson)
                            this.englandhot = englandhotJson
                        }else{
                            this.englandhotapi();
                        }

                        let englandnice = localStorage.getItem('englandnice');
                        if(englandnice){
                            let englandniceJson = JSON.parse(englandnice)
                            console.log(englandniceJson)
                            this.englandnice = englandniceJson
                            this.load=false
                        }else{
                            this.englandniceapi();
                        }
                    }
                }else if(idx===3){
                    if(firstday!=day){
                        this.koreanewapi();
                        this.koreahotapi();
                        this.koreaniceapi();
                    }else{
                        let koreanew = localStorage.getItem('koreanew');
                        if(koreanew){
                            let koreanewJson = JSON.parse(koreanew)
                            console.log(koreanewJson)
                            this.koreanew = koreanewJson
                        }else{
                            this.koreanewapi();
                        }

                        let koreahot = localStorage.getItem('koreahot');
                        if(koreahot){
                            let koreahotJson = JSON.parse(koreahot)
                            console.log(koreahotJson)
                            this.koreahot = koreahotJson
                        }else{
                            this.koreahotapi();
                        }

                        let koreanice = localStorage.getItem('koreanice');
                        if(koreanice){
                            let koreaniceJson = JSON.parse(koreanice)
                            console.log(koreaniceJson)
                            this.koreanice = koreaniceJson
                            this.load=false
                        }else{
                            this.koreaniceapi();
                        }
                    }

                }else if(idx===4){
                    if(firstday!=day){
                        this.japannewapi();
                        this.japanhotapi();
                        this.japanniceapi();
                    }else{
                        let japannew = localStorage.getItem('japannew');
                        if(japannew){
                            let japannewJson = JSON.parse(japannew)
                            console.log(japannewJson)
                            this.japannew = japannewJson
                        }else{
                            this.japannewapi();
                        }

                        let japanhot = localStorage.getItem('japanhot');
                        if(japanhot){
                            let japanhotJson = JSON.parse(japanhot)
                            console.log(japanhotJson)
                            this.japanhot = japanhotJson
                        }else{
                            this.japanhotapi();
                        }

                        let japannice = localStorage.getItem('japannice');
                        if(japannice){
                            let japanniceJson = JSON.parse(japannice)
                            console.log(japanniceJson)
                            this.japannice = japanniceJson
                            this.load=false
                        }else{
                            this.japanniceapi();
                        }
                    }

                }else if(idx===5){
                    if(firstday!=day){
                        this.chinanewapi();
                        this.chinahotapi();
                        this.chinaniceapi();
                    }else{
                        let chinanew = localStorage.getItem('chinanew');
                        if(chinanew){
                            let chinanewJson = JSON.parse(chinanew)
                            console.log(chinanewJson)
                            this.chinanew = chinanewJson
                        }else{
                            this.chinanewapi();
                        }

                        let chinahot = localStorage.getItem('chinahot');
                        if(chinahot){
                            let chinahotJson = JSON.parse(chinahot)
                            console.log(chinahotJson)
                            this.chinahot = chinahotJson
                        }else{
                            this.chinahotapi();
                        }

                        let chinanice = localStorage.getItem('chinanice');
                        if(chinanice){
                            let chinaniceJson = JSON.parse(chinanice)
                            console.log(chinaniceJson)
                            this.chinanice = chinaniceJson
                            this.load=false
                        }else{
                            this.chinaniceapi();
                        }
                    }

                }else if(idx===6){
                    if(firstday!=day){
                        this.hongkongnewapi();
                        this.hongkonghotapi();
                        this.hongkongniceapi();
                    }else{
                        let hongkongnew = localStorage.getItem('hongkongnew');
                        if(hongkongnew){
                            let hongkongnewJson = JSON.parse(hongkongnew)
                            console.log(hongkongnewJson)
                            this.hongkongnew = hongkongnewJson
                        }else{
                            this.hongkongnewapi();
                        }

                        let hongkonghot = localStorage.getItem('hongkonghot');
                        if(hongkonghot){
                            let hongkonghotJson = JSON.parse(hongkonghot)
                            console.log(hongkonghotJson)
                            this.hongkonghot = hongkonghotJson
                        }else{
                            this.hongkonghotapi();
                        }

                        let hongkongnice = localStorage.getItem('hongkongnice');
                        if(hongkongnice){
                            let hongkongniceJson = JSON.parse(hongkongnice)
                            console.log(hongkongniceJson)
                            this.hongkongnice = hongkongniceJson
                            this.load=false
                        }else{
                            this.hongkongniceapi();
                        }
                    }

                }else {
                    if(firstday!=day){
                        this.varietynewapi();
                        this.varietyhotapi();
                        this.varietyniceapi();
                    }else{
                        let varietynew = localStorage.getItem('varietynew');
                        if(varietynew){
                            let varietynewJson = JSON.parse(varietynew)
                            console.log(varietynewJson)
                            this.varietynew = varietynewJson
                        }else{
                            this.varietynewapi();
                        }

                        let varietyhot = localStorage.getItem('varietyhot');
                        if(varietyhot){
                            let varietyhotJson = JSON.parse(varietyhot)
                            console.log(varietyhotJson)
                            this.varietyhot = varietyhotJson
                        }else{
                            this.varietyhotapi();
                        }

                        let varietynice = localStorage.getItem('varietynice');
                        if(varietynice){
                            let varietyniceJson = JSON.parse(varietynice)
                            console.log(varietyniceJson)
                            this.varietynice = varietyniceJson
                            this.load=false
                        }else{
                            this.varietyniceapi();
                        }
                    }
                }

            },
            goback(){
                window.history.go(-1);
            },
            hotnewapi(){
                this.$axios.get(`http://xkolento.cn/hottv/new`,{
                    params:{}
                }).then(res=>{
                    this.hotnew=res.data.subjects;
                    let hotnewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('hotnew', hotnewstr);
                })
            },
            hothotapi(){
                this.$axios.get(`http://xkolento.cn/hottv/hot`,{
                    params:{}
                }).then(res=>{
                    this.hothot=res.data.subjects;
                    let hothotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('hothot', hothotstr);
                })
            },
            hotniceapi(){
                this.$axios.get(`http://xkolento.cn/hottv/nice`,{
                    params:{}
                }).then(res=>{
                    this.hotnice=res.data.subjects;
                    let hotnicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('hotnice', hotnicestr);
                    this.load=false
                })
            },
            americanewapi(){
                this.$axios.get(`http://xkolento.cn/america/new`,{
                    params:{}
                }).then(res=>{
                    this.americanew=res.data.subjects;
                    let americanewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('americanew', americanewstr);
                })
            },
            americahotapi(){
                this.$axios.get(`http://xkolento.cn/america/hot`,{
                    params:{}
                }).then(res=>{
                    this.americahot=res.data.subjects;
                    let americahotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('americahot', americahotstr);
                })
            },
            americaniceapi(){
                this.$axios.get(`http://xkolento.cn/america/nice`,{
                    params:{}
                }).then(res=>{
                    this.americanice=res.data.subjects;
                    let americanicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('americanice', americanicestr);
                    this.load=false
                })
            },
            englandnewapi(){
                this.$axios.get(`http://xkolento.cn/england/new`,{
                    params:{}
                }).then(res=>{
                    this.englandnew=res.data.subjects;
                    let englandnewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('englandnew', englandnewstr);
                })
            },
            englandhotapi(){
                this.$axios.get(`http://xkolento.cn/england/hot`,{
                    params:{}
                }).then(res=>{
                    this.englandhot=res.data.subjects;
                    let englandhotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('englandhot', englandhotstr);
                })
            },
            englandniceapi(){
                this.$axios.get(`http://xkolento.cn/england/nice`,{
                    params:{}
                }).then(res=>{
                    this.englandnice=res.data.subjects;
                    let englandnicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('englandnice', englandnicestr);
                    this.load=false
                })
            },
            koreanewapi(){
                this.$axios.get(`http://xkolento.cn/korea/new`,{
                    params:{}
                }).then(res=>{
                    this.koreanew=res.data.subjects;
                    let koreanewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('koreanew', koreanewstr);
                })
            },
            koreahotapi(){
                this.$axios.get(`http://xkolento.cn/korea/hot`,{
                    params:{}
                }).then(res=>{
                    this.koreahot=res.data.subjects;
                    let koreahotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('koreahot', koreahotstr);
                })
            },
            koreaniceapi(){
                this.$axios.get(`http://xkolento.cn/korea/nice`,{
                    params:{}
                }).then(res=>{
                    this.koreanice=res.data.subjects;
                    let koreanicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('koreanice', koreanicestr);
                    this.load=false
                })
            },
            japannewapi(){
                this.$axios.get(`http://xkolento.cn/japan/new`,{
                    params:{}
                }).then(res=>{
                    this.japannew=res.data.subjects;
                    let japannewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('japannew', japannewstr);
                })
            },
            japanhotapi(){
                this.$axios.get(`http://xkolento.cn/japan/hot`,{
                    params:{}
                }).then(res=>{
                    this.japanhot=res.data.subjects;
                    let japanhotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('japanhot', japanhotstr);
                })
            },
            japanniceapi(){
                this.$axios.get(`http://xkolento.cn/japan/nice`,{
                    params:{}
                }).then(res=>{
                    this.japannice=res.data.subjects;
                    let japannicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('japannice', japannicestr);
                    this.load=false
                })
            },
            chinanewapi(){
                this.$axios.get(`http://xkolento.cn/china/new`,{
                    params:{}
                }).then(res=>{
                    this.chinanew=res.data.subjects;
                    let chinanewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('chinanew', chinanewstr);
                })
            },
            chinahotapi(){
                this.$axios.get(`http://xkolento.cn/china/hot`,{
                    params:{}
                }).then(res=>{
                    this.chinahot=res.data.subjects;
                    let chinahotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('chinahot', chinahotstr);
                })
            },
            chinaniceapi(){
                this.$axios.get(`http://xkolento.cn/japan/nice`,{
                    params:{}
                }).then(res=>{
                    this.japannice=res.data.subjects;
                    let japannicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('japannice', japannicestr);
                    this.load=false
                })
            },
            hongkongnewapi(){
                this.$axios.get(`http://xkolento.cn/hongkong/new`,{
                    params:{}
                }).then(res=>{
                    this.hongkongnew=res.data.subjects;
                    let hongkongnewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('hongkongnew', hongkongnewstr);
                })
            },
            hongkonghotapi(){
                this.$axios.get(`http://xkolento.cn/hongkong/hot`,{
                    params:{}
                }).then(res=>{
                    this.hongkonghot=res.data.subjects;
                    let hongkonghotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('hongkonghot', hongkonghotstr);
                })
            },
            hongkongniceapi(){
                this.$axios.get(`http://xkolento.cn/hongkong/nice`,{
                    params:{}
                }).then(res=>{
                    this.hongkongnice=res.data.subjects;
                    let hongkongnicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('hongkongnice', hongkongnicestr);
                    this.load=false
                })
            },
            varietynewapi(){
                this.$axios.get(`http://xkolento.cn/variety/new`,{
                    params:{}
                }).then(res=>{
                    this.varietynew=res.data.subjects;
                    let varietynewstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('varietynew', varietynewstr);
                })
            },
            varietyhotapi(){
                this.$axios.get(`http://xkolento.cn/variety/hot`,{
                    params:{}
                }).then(res=>{
                    this.varietyhot=res.data.subjects;
                    let varietyhotstr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('varietyhot', varietyhotstr);
                })
            },
            varietyniceapi(){
                this.$axios.get(`http://xkolento.cn/variety/nice`,{
                    params:{}
                }).then(res=>{
                    this.varietynice=res.data.subjects;
                    let varietynicestr = JSON.stringify(res.data.subjects)
                    localStorage.setItem('varietynice', varietynicestr);
                    this.load=false
                })
            }
        },
        components:{
            tvshow,loading
        }
    }
</script>

<style scoped>
    .tvcon {padding:2rem 3%;margin-top: 15rem;}
    .tvcon h2{font-size: 3rem;}
    ::-webkit-scrollbar{width:0px;height:0px;}
</style>
