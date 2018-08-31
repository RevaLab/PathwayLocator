<template>
<div class="gene-input">
    <div class="navigation-from-input">
            <button id="try-example"
                    class="button is-info"
                    v-on:click="addExampleList"
            >
                Try Example
            </button>
    </div>
    <textarea
        v-model="geneList"
        placeholder="Enter Query Gene List"
    >
    </textarea>
    <button class="button is-primary"
       v-on:click="submitGeneList"
   >
            Analyze
   </button>
</div>
</template>

<script>
    export default {
        name: "gene-input",
        data() {
            return {
                geneList: ''
            }
        },
        computed: {
        },
        methods: {
            addExampleList() {
                this.geneList =['FLT3', 'SMO', 'GLA', 'SGCB', 'OAT', 'CAPN3', 'ASS1', 'AGXT', 'AKT1', 'PTPN1',
                    'PIAS1', 'CDKN1B', 'THEM4', 'CCNE1', 'MAP2K4', 'ATG7','ATG12','BAD','BCL2L1'].join("\n")
            },
            submitGeneList() {
                if (!this.geneList.length) {
                    alert("Please enter genes.");
                    return;
                }

                let geneListArr = [];
                const trimmedGeneList = this.geneList.trim();
                if (trimmedGeneList.includes("\t") && trimmedGeneList.includes(" ")) {
                    alert("Enter genes separated by a newline, tab, or space. Your list seems to include multiple separators.")
                }

                if (trimmedGeneList.includes("\t")) {
                    geneListArr = trimmedGeneList.split("\t");
                } else if (trimmedGeneList.includes(" ")) {
                    geneListArr = trimmedGeneList.split(" ");
                } else {
                    geneListArr = trimmedGeneList.split("\n")
                }

                this.$store.dispatch('updateQueryList', geneListArr);
                this.$router.push('/results');
            }
        }
    }
</script>

<style scoped>

.gene-input {
    display: flex;
    flex-direction: column;
    margin: auto;
    max-width: 45%;
    min-width: 450px;
}

.gene-input textarea {
    width: 100%;
    margin: 20px auto;
    border: 1px solid;
    height: 30vh;
}

.navigation-from-input {
    display: flex;
    flex-direction: row;
}


.gene-input #try-example {
    margin-left:auto;
    margin-right:0;
    margin-bottom: -10px;
    max-width: 20%;
    min-width: 150px;
}

</style>
