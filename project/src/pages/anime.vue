<template>
    <div class="anime">
        <div class="anime-section anime-new">
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
    .anime {padding:0 3%;}
</style>
