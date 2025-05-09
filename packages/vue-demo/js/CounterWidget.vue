<script setup lang="ts">
import { useModelState } from "@anywidget/vue";
import Text from "./Text.vue";

const value = useModelState<number>("value");
</script>

<template>
<Text></Text>
<button :onClick="() => value++">count is {{value}}</button>
</template>

<style scoped>
button {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	gap: 0.5rem;
	padding: .5rem 1.5rem;
	margin: 8px;
	font-size: 1.05rem;
	border: 1px solid ButtonBorder;
	border-radius: 99999px;
	box-shadow: 0 1px 2px 0 #0000000d;
}
</style>
