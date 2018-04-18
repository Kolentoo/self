<template>
    <div class="kolento">
        <div class="banner" ref="banner">
            <div class="title">
                <h1>让美好触手可及！</h1>
                <h2>BY KOLENTO</h2>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        data(){
            return{

            }
        },
        created(){
            this.$nextTick(function(){
                let bHeight = document.documentElement.clientHeight;
                this.$refs.banner.style.height=bHeight+'px';
            });
        }
    }
</script>

<style scoped>
    .banner {background: url('../public/images/bj3.jpg') no-repeat center center;
    background-size: 100%;color:#fff;display: flex;align-items: center;text-align: center;}
    .title {width: 100%;height: 100%;}
    h1{font-size: 5.4rem;letter-spacing: 1.4rem;width: 100%;}
    h2{font-family: 'druk_pierre_testregular';font-size: 4.8rem;text-transform: uppercase;
    letter-spacing: 1rem;font-weight: 100;width: 100%;}
    /*.banner {background: url('../assets/images/banner.jpg') no-repeat;background-size: 100%;height: 70rem;}*/
</style>