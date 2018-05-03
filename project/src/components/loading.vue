<template>
    <div class="loading">
        <img class="loading-gif" src="../public/images/loading.gif" alt="">
    </div>
</template>

<script>
    export default{
        data(){
            return{

            }
        }
    }
</script>

<style>
    .loading {position: fixed;z-index:600;background: #fff;top: 0;left: 0;transition:all ease 0.7s;width: 100%;height: 100%;
    display: flex;justify-content: center;align-items: center;transition:all ease 0.5s;}
    .loading img{width: 30rem;}
</style>