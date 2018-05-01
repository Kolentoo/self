<template>
    <div :class="['pop',{popon:popshow}]">
        <p class="p1">{{popmsg}}</p>
    </div>
</template>

<script>
    export default{
        props:['popmsg','popshow'],
        data(){
            return{
                
            }
        }
    }
</script>

<style scoped>
    .pop {position: fixed;top: 0;left: 0;width: 100%;height: 100%;display: flex;justify-content: center;align-items: center;
    transition:all ease 0.5s;z-index:-1;opacity: 0;}
    .popon {z-index:1000;opacity: 1;}
    .pop .p1 {font-size: 2.8rem;color:#fff;background: rgba(0,0,0,0.5);padding:1rem 3rem;border-radius:1rem;}
</style>