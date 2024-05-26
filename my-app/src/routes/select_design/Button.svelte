<script>
    import { user_data } from '$lib/store'
    import { goto } from '$app/navigation';

    function BtnClick() {
        const value = $user_data.design_num;
		if (value === '') return;
		goto('/capture_imgs');
    }
</script>

<button type="button" on:click={() => BtnClick()} class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-full text-sm text-lg px-10 py-2.5 tall:text-4xl tall:px-16 tall:py-6 tall:rounded-xl focus:outline-none">Take a picture</button>
