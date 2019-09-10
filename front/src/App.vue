<template>
    <div id="app">
        <h1>{{messageFromGetMethod}}</h1>
        <h1>{{messageFromPostMethod}}</h1>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                messageFromGetMethod: "",
                messageFromPostMethod: ""
            }
        },
        created() {
            const that = this
            that.axios
                .get("/hello")
                .then((res) => {
                    that.messageFromGetMethod = res.data
                })
                .catch((error) => {
                    alert(error)
                })
            that.axios
                .post("/hello")
                .then((res) => {
                    that.messageFromPostMethod = res.data
                })
                .catch((error) => {
                    alert(error)
                })

        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
