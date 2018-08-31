<template>
    <div class="results">
        <h1>{{ enrichedPathways }}</h1>
    </div>
</template>

<script>
    export default {
        name: "results",
        computed: {
            enrichedPathways() {
                return this.$store.state.enrichedPathways
            }
        }
    }
</script>

<style scoped>

</style>
