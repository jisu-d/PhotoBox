<script lang="ts">
    import { goto } from '$app/navigation';
    import { user_data } from '$lib/store';

    function OnClick(){
        if ($user_data.select_imgs_num.length === 4){
            goto('/check_made_img', {
                replaceState: true
            })
        }
    }
</script>

<button type="button" on:click={() => OnClick()} class="text-[2vh] mt-8 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-200 rounded-xl font-medium rounded-lg px-5 pt-[0.7vh] pb-[1vh] inline-flex justify-center w-full text-center">Create photo</button>
