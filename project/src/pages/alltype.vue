<template>
    <div class="alltype">
        <div class="anime-section anime-new">
            <h2>动漫榜单</h2>
            <showpart :animenew="animenew"></showpart>
        </div>

    </div>
</template>

<script>
    import showpart from '../components/show'
    export default{
        data(){
            return{
                animenew:''
            }
        },
        created(){

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
