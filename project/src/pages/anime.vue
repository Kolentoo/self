<template>
    <div class="anime">
        
    </div>
</template>

<script>
    export default{
        data(){
            return{
                anime1:''
            }
        },
        created(){
            this.$.ajax({
                type: "GET",
                url: "https://api.bilibili.com/x/web-interface/ranking/region?jsonp=jsonp&day=3&rid=32",
                data: {},
                dataType: "json",
                success: (data)=>{
                    console.log(data)
                }
            })
        }
    }
</script>

<style>
    
</style>
