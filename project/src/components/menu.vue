<template>
    <div class="menu">
        <ul class="menu-con">
            <li class="mlist opacity"><a href="https://m.weibo.cn/p/1005051921492471">Kolento</a></li>
            <li class="mlist">
                <img class="menu-pic vm" src="../public/images/menu.png" alt="">
            </li>
        </ul>
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

<style scoped>
    .menu-con {display: flex;justify-content: space-between;color:#fff;margin:3rem;font-size: 3.6rem;}
    .menu-con a{color:#fff;}
    .menu-pic {width: 4rem}
    .opacity {opacity: 0;}
</style>