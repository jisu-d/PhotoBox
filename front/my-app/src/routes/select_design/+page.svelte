<script lang="ts">
	import Carousel from './Carousel.svelte'
	import Button from './Button.svelte';
</script>

<style>
	* {
		box-sizing: border-box;
	}
	main{
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		flex-direction: column;
		justify-content: center;
	}
</style>

<main class="">
	<Carousel />
	<Button />
</main>