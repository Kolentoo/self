<template>
    <div class="kolento">
        <div :class="['banner',bannerclass,{banneroff:banneroff}]" ref="banner">
            <div class="mask">
                <div class="title">
                    <h1 :class="{'hon1':hon1}">让美好触手可及!</h1>
                    <h2 :class="{'hon2':hon2}">KOLENTO</h2>
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
                hon1:false,
                hon2:false
            }
        },
        created(){
            let random = Math.random();
            let number = Math.floor(random*10)
            this.bannerclass=`banner${number}`
            setTimeout(()=> {
                this.hon1=true
            }, 1000);
            setTimeout(()=> {
                this.hon2=true
            }, 1200);
            setTimeout(()=> {
                this.banneroff=true
            }, 1700);

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
    .banner {color:#fff;transition:all ease 1.6s;opacity: 1;z-index:200;position: relative;transform:scale(1,1);}
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
    h1{font-size: 5.4rem;letter-spacing: 1.4rem;width: 100%;transition:all ease 0.6s;position: relative;top: 0;}
    h2{font-family: 'druk_pierre_testregular';font-size: 4.2rem;text-transform: uppercase;
    letter-spacing: 1rem;font-weight: 100;width: 100%;transition:all ease 0.6s;position: relative;top: 0;}
    .hon1 {top: -7rem;}
    .hon2 {top: -13rem;}
</style>