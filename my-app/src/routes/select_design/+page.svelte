<script>
	import Carousel from './Carousel.svelte'
	
	let colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
</script>

<style>
	div {
		height: 8rem;
		width: 8rem;
	}
	
	span {
		display: inline-block;
		margin-top: 6rem;
	}

	html, body, main{
		box-sizing: border-box;
		width: 100%;
		height: 100%;
	}
</style>

<main>
	<Carousel />
</main>