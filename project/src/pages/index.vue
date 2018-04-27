<template>
    <div class="kolento">
        <div :class="['banner',bannerclass,{banneroff:banneroff}]" ref="banner">
            <div class="mask">
                <div class="title">
                    <div class="title1">
                        <h1 >{{weekday}} {{dateday}}</h1>
                    </div>
                    <div class="title2">
                        <h2 >{{tips}}</h2>
                    </div>
                </div>
            </div>
        </div>
        <div class="content">
            <swiper class="part" ref="part"></swiper>
        </div>
        <navigation class="menu-box"></navigation>
    </div>
</template>

<script>
    import navigation from '../components/menu'
    import swiper from '../components/swiper'
    export default{
        data(){
            return{
                bannerclass:'',
                banneroff:false,
                weekday:'',
                dateday:'',
                tips:'KOLENTO'
            }
        },
        created(){
            let week = new Date().getDay();  
            if (week == 0) {  
                this.weekday = "星期日";  
            } else if (week == 1) {  
                this.weekday = "星期一";  
            } else if (week == 2) {  
                this.weekday = "星期二";  
            } else if (week == 3) {  
                this.weekday = "星期三";  
            } else if (week == 4) {  
                this.weekday = "星期四";  
            } else if (week == 5) {  
                this.weekday = "星期五";  
            } else if (week == 6) {  
                this.weekday = "星期六";  
            }  

            setTimeout(()=> {
                this.enter=true; 
            }, 500);


            let myDate = new Date();
            let month = myDate.getMonth(); //获取当前月份(0-11,0代表1月)
            let day = myDate.getDate(); //获取当前日(1-31)
            this.dateday=month + '月'+ day+'日'
            
            let firstday = localStorage.getItem('today')
            if(firstday==day){
                this.hon1=true
                this.hon2=true
                this.banneroff=true
            }else{
                let hours = myDate.getHours();
                if(hours>=6&&hours<11){
                    this.tips='早安，加油'
                }else if(hours <16&&hours>=12){
                    this.tips='喝杯咖啡，休息一下'
                }else if(hours <20&&hours>=16){
                    this.tips='今天不加班!'
                }else{
                    this.tips='夜深了，早点休息'
                }
                let random = Math.random();
                let number = Math.floor(random*10)
                this.bannerclass=`banner${number}`
                setTimeout(()=> {
                    this.banneroff=true
                }, 4000);
                localStorage.setItem('today',day)
            }

            this.$nextTick(()=>{
                let bHeight = document.documentElement.clientHeight;
                this.$refs.banner.style.height=bHeight+'px';
            });

        },
        components:{
            swiper,navigation
        }
    }
</script>

<style scoped>
    .menu-box {position: fixed;top: 0;left: 0;width: 100%;z-index:300;}
    .menu-box a{color:#fff;}
    .banner {color:#fff;transition:all ease 1.6s;opacity: 1;z-index:600;position: relative;transform:scale(1,1);}
    .banner1 {background: url('../public/images/bj1.jpg') no-repeat center center;background-size: cover;}
    .banner2 {background: url('../public/images/bj2.jpg') no-repeat center center;background-size: cover;}
    .banner3 {background: url('../public/images/bj3.jpg') no-repeat center center;background-size: cover;}
    .banner4 {background: url('../public/images/bj4.jpg') no-repeat center center;background-size: cover;}
    .banner5 {background: url('../public/images/bj5.jpg') no-repeat center center;background-size: cover;}
    .banner6 {background: url('../public/images/bj6.jpg') no-repeat center center;background-size: cover;}
    .banner7 {background: url('../public/images/bj7.jpg') no-repeat center center;background-size: cover;}
    .banner8 {background: url('../public/images/bj8.jpg') no-repeat center center;background-size: cover;}
    .banner9 {background: url('../public/images/bj9.jpg') no-repeat center center;background-size: cover;}
    .banneroff {opacity: 0;z-index:-1;transform:scale(1.3,1.3);}
    .mask {background:rgba(0,0,0,0.1);position: fixed;top: 0;left: 0;width: 100%;height: 100%;display: flex;align-items: center;
    text-align: center;}
    .content {position: fixed;width: 100%;height: 100%;top: 0;left: 0;z-index:100;}
    .title {width: 100%;height: 16rem;overflow: hidden;}
    .title1,.title2 {height: 8rem;overflow: hidden;}
    h1{font-size: 4rem;letter-spacing: 1.4rem;width: 100%;transition:all ease 1s;position: relative;top: 8rem;opacity: 1;animation: title1 3.8s 0.5s forwards;}
    h2{font-family: 'druk_pierre_testregular';font-size: 3.6rem;text-transform: uppercase;
    letter-spacing: 1rem;font-weight: 100;width: 100%;transition:all ease 1s;position: relative;top: 8rem;opacity: 1;animation: title2 3.8s 0.7s forwards;}
    @keyframes title1{
        0%{top:8rem;opacity: 1}
        30%{top:0;opacity: 1;}
        70%{top:0;opacity: 1;}
        100%{top: -7rem;opacity: 0.5;}
    }
    @keyframes title2{
        0%{top:8rem;opacity: 1}
        30%{top:0;opacity: 1;}
        70%{top:0;opacity: 1;}
        100%{top: -7rem;opacity: 0.5;}
    }
</style>