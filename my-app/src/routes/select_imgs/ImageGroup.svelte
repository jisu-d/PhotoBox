<script lang="ts">
  import { goto } from '$app/navigation';
  import { user_data } from '$lib/store';
  import { onDestroy, onMount } from 'svelte';
  
  let value: string[] = [];
  
  $: value = $user_data.capture_imgs;

  onMount(() => {
    if ($user_data.capture_imgs.length === 0) {
      alert('정상적인 접근이 아닙니다.');
      goto('/start_page');
    }
  });
  
  function toggleSelection(index: number) {
    user_data.update(currentData => {
      const selectedIndex = currentData.select_imgs_num.indexOf(index);
    
      // 선택된 이미지가 이미 4개인지 확인
      if (selectedIndex === -1 && currentData.select_imgs_num.length >= 4) {
        return currentData;
      }
    
      if (selectedIndex === -1) {
        return {
          ...currentData,
          select_imgs_num: [...currentData.select_imgs_num, index]
        };
      } else {
        return {
          ...currentData,
            select_imgs_num: currentData.select_imgs_num.filter(i => i !== index)
        };
      }
    });
  }
  
</script>
  
<style>
  @media (max-aspect-ratio: 1/1) {
    .dynamic-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }
  @media (min-aspect-ratio: 1/1) {
    .dynamic-grid {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }
  }
  .selected {
    filter: grayscale(30%);
  }
</style>
  
<div class="grid gap-3 dynamic-grid">
  {#each value as c, index}
    <div class="relative">
      <button
        class="w-full h-full focus:outline-none"
        on:click={() => toggleSelection(index)}
        aria-pressed={$user_data.select_imgs_num.includes(index)}
        aria-label="이미지 선택"
        class:selected={$user_data.select_imgs_num.includes(index)}
      >
        <div class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 text-8xl font-bold text-white z-10">
          {#if $user_data.select_imgs_num.includes(index)}
            {$user_data.select_imgs_num.indexOf(index) + 1}
          {/if}
        </div>
        <img src={'data:image/jpeg;base64,' + c} alt="선택 가능한 이미지" class="object-cover w-full h-full rounded-md">
      </button>
    </div>
  {/each}
</div>
  