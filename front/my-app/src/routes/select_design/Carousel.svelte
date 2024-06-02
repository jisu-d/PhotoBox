<script lang="ts">
	import { writable } from 'svelte/store';
	import type { FRAME_IMG } from '$lib/public/type';
	import { user_data } from '$lib/store';
	import { frameimg } from './frame_imgs';
    import { onMount } from 'svelte';

	// 선택된 이미지 인덱스를 저장할 상태
	const selectedImage = writable<string | null>(null);

	// 이미지 클릭 핸들러
	function handleImageClick(croppSize: string, title: string, cover:boolean) {
		user_data.set({ ...$user_data, design_num: title, cropp_size: croppSize, cover: cover});
		selectedImage.set(title); // 선택된 이미지를 업데이트
	}

	// let scrollWidth = 0;
    // let scrollPositionX = 0;
    // let scrollPositionY = 0;

    // onMount(() => {
    //     const container = document.getElementById('container') as HTMLElement
    //     scrollWidth = container.scrollWidth;

    //     // 스크롤 위치 업데이트
    //     container.addEventListener('scroll', () => {
    //         scrollPositionX = container.scrollLeft;
	// 		console.log(scrollPositionX, scrollWidth);
			
    //     });
    // });
	
</script>

<style>
	#container {
		width: 100%;
		overflow: auto;
		scroll-snap-type: x mandatory;
		white-space: nowrap;
	}
	#container::-webkit-scrollbar {
		display: none;
	}
	.item {
		display: inline-flex;
		width: 100%;
		height: 100%;
		align-items: center;
		justify-content: center;
		scroll-snap-align: start;
	}
	.selected {
		border: 2.5px solid red; /* 선택된 이미지에 적용될 스타일 */
		z-index: 1; /* 선택될 때 다른 요소들보다 위로 올라오도록 설정 */
		transform: translateY(-5px); /* 선택될 때 약간 위로 올라가는 효과를 추가 */
	}
</style>

<div id="container" class="h-90 tall:h-3/5">
    {#each frameimg as img}
        <div class="item">
			{#each img as ele}
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
				<!-- svelte-ignore a11y-missing-attribute -->
				<img 
					src={ele.src} 
					style={ele.style}
					class:selected={$selectedImage === ele.title}
					on:click={() => handleImageClick(ele.cropp_size, ele.title, ele.cover)}
				>
			{/each}
        </div>
    {/each}
</div>
