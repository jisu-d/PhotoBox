<a href="/select_design" class="block p-10 max-w-[80vw] bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100">
    <h5 class="mb-2 text-[4vh] font-bold tracking-tight text-gray-900 ">Start taking photos</h5>
    <p class="font-normal text-gray-700 dark:text-gray-400 text-[2vh]">
        Take a photo with your friends, apply a cool frame, and print it!
    </p>
</a>

<script>
    import { user_data } from '$lib/store'
    user_data.set({
        design_num: ' ',
        capture_imgs: [],
        select_imgs_num: [],
        made_img: ' ',
        cropp_size: ' ',
        printoutNum: 1,
        cover: null,
        imgPath: ' '
    })
</script>